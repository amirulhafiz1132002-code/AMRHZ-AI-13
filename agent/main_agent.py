from core.brain_engine import find_best_match
from core.intent_detector import detect_intent
from agent.autopilot import AutoPilot

# Initialize autopilot with configuration
autopilot = AutoPilot(max_iterations=3, confidence_threshold=0.7)

def run_agent(user_input, use_autopilot=True):
    """
    Run agent with optional autopilot enhancement
    
    Args:
        user_input: User's input prompt
        use_autopilot: If True, uses iterative autopilot loop; if False, uses simple mode
    
    Returns:
        Response string or full result dict (if autopilot enabled)
    """
    if use_autopilot:
        # Use enhanced autopilot loop for iterative improvement
        result = autopilot.autopilot_loop(user_input)
        return result
    else:
        # Legacy: simple single-pass mode
        intent = detect_intent(user_input)
        memory = find_best_match(intent)
        
        if memory:
            return f"[AMRHZ AI] → {memory.get('response')}"
        else:
            return "[AMRHZ AI] → No memory found. Learning..."


def run_agent_with_feedback(user_input):
    """
    Run agent with user feedback for continuous learning
    """
    def get_feedback(response):
        feedback = input(f"\nResponse: {response}\nWas this helpful? (yes/no): ")
        return feedback
    
    result = autopilot.autopilot_loop(user_input, user_feedback_fn=get_feedback)
    return result


if __name__ == "__main__":
    print("[AMRHZ AI] - Enhanced Agent with AutoPilot Loop")
    print("=" * 50)
    
    mode = input("Select mode (1=autopilot, 2=simple, 3=with_feedback): ").strip()
    
    while True:
        user_input = input("\n>> ")
        
        if mode == "1":
            result = run_agent(user_input, use_autopilot=True)
            print(f"\n[RESULT] {result['response']}")
            print(f"[CONFIDENCE] {result['confidence']:.1%}")
            print(f"[ITERATIONS] {result['iterations']}")
        
        elif mode == "2":
            response = run_agent(user_input, use_autopilot=False)
            print(response)
        
        elif mode == "3":
            result = run_agent_with_feedback(user_input)
            print(f"\n[RESULT] {result['response']}")
            print(f"[CONFIDENCE] {result['confidence']:.1%}")
            print(f"[LEARNING] Feedback: {result.get('user_feedback', 'N/A')}")
