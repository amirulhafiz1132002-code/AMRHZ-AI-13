import csv
from typing import Dict, List
from datetime import datetime

BRAIN_FILE = "data/brain_v2.csv"
HISTORY_FILE = "data/autopilot_history.csv"

class AutoPilot:
    def __init__(self, max_iterations=3, confidence_threshold=0.6):
        self.max_iterations = max_iterations
        self.confidence_threshold = confidence_threshold
        self.iteration_log = []
    
    def score_memory(self, row: Dict, intent: str, context_history: List) -> float:
        """Enhanced scoring with history context"""
        score = 0.0
        
        # Intent match (weight: 3.0)
        if row.get("intent") == intent:
            score += 3.0
        
        # Priority boost (weight: 2.0)
        if row.get("priority") == "high":
            score += 2.0
        
        # Auto-learned context (weight: 1.0)
        if row.get("context_tag") == "auto":
            score += 1.0
        
        # Historical success rate (weight: 2.0)
        if context_history:
            success_rate = self._calculate_success_rate(row, context_history)
            score += success_rate * 2.0
        
        return score
    
    def _calculate_success_rate(self, row: Dict, history: List) -> float:
        """Calculate success rate based on past use"""
        if not history:
            return 0.0
        
        memory_id = row.get("id")
        uses = sum(1 for h in history if h.get("memory_id") == memory_id)
        successes = sum(1 for h in history if h.get("memory_id") == memory_id and h.get("success") == "true")
        
        return successes / uses if uses > 0 else 0.0
    
    def find_top_matches(self, intent: str, context_history: List, top_n=3) -> List:
        """Get top N candidates for iterative refinement"""
        brain = self._load_brain()
        scored = []
        
        for row in brain:
            score = self.score_memory(row, intent, context_history)
            scored.append((row, score))
        
        # Sort by score descending
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_n]
    
    def autopilot_loop(self, prompt: str, user_feedback_fn=None) -> Dict:
        """
        Iterative improvement loop:
        1. Generate initial candidate responses
        2. Evaluate quality/confidence
        3. Refine or select best match
        4. Learn from feedback
        """
        intent = self._detect_intent(prompt)
        context_history = self._load_history()
        
        best_result = None
        best_confidence = 0.0
        iteration = 0
        
        for iteration in range(self.max_iterations):
            print(f"\n[AUTOPILOT] Iteration {iteration + 1}/{self.max_iterations}")
            
            # Step 1: Get top candidates
            candidates = self.find_top_matches(intent, context_history, top_n=3)
            
            if not candidates:
                return {
                    "success": False,
                    "message": "No candidates found",
                    "iterations": iteration,
                    "learning": {"new_intent": intent}
                }
            
            # Step 2: Evaluate and rank
            best_candidate, confidence = self._evaluate_candidate(
                candidates[0], prompt, iteration
            )
            
            print(f"  → Candidate: {best_candidate[0].get('response')}")
            print(f"  → Confidence: {confidence:.2%}")
            
            # Step 3: Check if confident enough
            if confidence >= self.confidence_threshold:
                best_result = best_candidate
                best_confidence = confidence
                print(f"  ✓ Confidence threshold met!")
                break
            
            # Step 4: Refine for next iteration (if not final)
            if iteration < self.max_iterations - 1:
                prompt = self._refine_prompt(prompt, candidates[:2], iteration)
                print(f"  → Refined prompt: {prompt}")
            else:
                best_result = best_candidate
                best_confidence = confidence
        
        # Step 5: Learn from result
        result = {
            "success": best_confidence >= self.confidence_threshold,
            "response": best_result[0].get("response"),
            "confidence": best_confidence,
            "iterations": iteration + 1,
            "memory_id": best_result[0].get("id"),
            "intent": intent
        }
        
        # Optional: Get user feedback
        if user_feedback_fn:
            user_feedback = user_feedback_fn(result["response"])
            result["user_feedback"] = user_feedback
            self._update_learning(best_result[0], user_feedback)
        
        self._log_autopilot_run(result)
        return result
    
    def _detect_intent(self, prompt: str) -> str:
        """Simple intent detection"""
        lower = prompt.lower()
        if "build" in lower:
            return "build_system"
        elif "fix" in lower or "debug" in lower:
            return "debug"
        elif "status" in lower:
            return "check_status"
        return "general"
    
    def _evaluate_candidate(self, candidate_tuple: tuple, prompt: str, iteration: int) -> tuple:
        """
        Evaluate candidate quality
        Returns: (candidate, confidence_score)
        """
        row, score = candidate_tuple
        
        # Base confidence from scoring
        confidence = min(score / 6.0, 1.0)  # Normalize to 0-1
        
        # Boost if response matches prompt keywords
        response = row.get("response", "").lower()
        prompt_lower = prompt.lower()
        
        keyword_matches = sum(1 for word in prompt_lower.split() 
                             if len(word) > 3 and word in response)
        confidence += (keyword_matches * 0.1)
        confidence = min(confidence, 1.0)
        
        return (row, score), confidence
    
    def _refine_prompt(self, prompt: str, candidates: List, iteration: int) -> str:
        """Refine prompt based on candidate feedback for next iteration"""
        # Extract key terms from top candidates
        top_terms = set()
        for candidate, _ in candidates:
            response = candidate.get("response", "").lower().split()
            top_terms.update(response[:3])
        
        # Reconstruct prompt with refined focus
        refined = f"{prompt} [REFINED: focus on {', '.join(list(top_terms)[:2])}]"
        return refined
    
    def _update_learning(self, memory_row: Dict, feedback: str) -> None:
        """Update learning based on user feedback"""
        if feedback.lower() in ["yes", "correct", "good", "helpful"]:
            # Increment success count
            priority = memory_row.get("priority")
            if priority == "low":
                memory_row["priority"] = "medium"
            elif priority == "medium":
                memory_row["priority"] = "high"
        
        self._save_brain()
    
    def _load_brain(self) -> List[Dict]:
        """Load memory from CSV"""
        data = []
        try:
            with open(BRAIN_FILE, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print("[ERROR] Brain file not found.")
        return data
    
    def _load_history(self) -> List[Dict]:
        """Load execution history"""
        history = []
        try:
            with open(HISTORY_FILE, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    history.append(row)
        except FileNotFoundError:
            pass
        return history
    
    def _save_brain(self) -> None:
        """Persist brain updates"""
        # Implementation: save updated brain to CSV
        pass
    
    def _log_autopilot_run(self, result: Dict) -> None:
        """Log autopilot execution for analysis"""
        try:
            with open(HISTORY_FILE, "a", newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=[
                    "timestamp", "memory_id", "intent", "confidence", 
                    "iterations", "success", "user_feedback"
                ])
                writer.writerow({
                    "timestamp": datetime.now().isoformat(),
                    "memory_id": result.get("memory_id"),
                    "intent": result.get("intent"),
                    "confidence": result.get("confidence"),
                    "iterations": result.get("iterations"),
                    "success": result.get("success"),
                    "user_feedback": result.get("user_feedback", "")
                })
        except Exception as e:
            print(f"[ERROR] Failed to log autopilot run: {e}")
