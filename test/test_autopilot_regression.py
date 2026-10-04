import unittest

from agent.autopilot import AutoPilot


class TestAutoPilotStatusRegression(unittest.TestCase):
    def test_exact_intent_wins_score_tie(self):
        autopilot = AutoPilot(max_iterations=3, confidence_threshold=0.7)
        autopilot._load_brain = lambda: [
            {
                "id": "1",
                "intent": "build_system",
                "context_tag": "auto",
                "priority": "high",
                "response": "System build initialized",
            },
            {
                "id": "3",
                "intent": "check_status",
                "context_tag": "manual",
                "priority": "medium",
                "response": "System status is stable",
            },
        ]

        matches = autopilot.find_top_matches("check_status", [])

        self.assertEqual(matches[0][0]["id"], "3")
        self.assertEqual(matches[0][0]["intent"], "check_status")

    def test_status_candidate_reaches_existing_confidence_threshold(self):
        autopilot = AutoPilot(max_iterations=3, confidence_threshold=0.7)
        candidate = (
            {
                "id": "3",
                "intent": "check_status",
                "context_tag": "manual",
                "priority": "medium",
                "response": "System status is stable",
            },
            3.0,
        )

        _, confidence = autopilot._evaluate_candidate(candidate, "status", 0)

        self.assertGreaterEqual(confidence, 0.7)


if __name__ == "__main__":
    unittest.main()
