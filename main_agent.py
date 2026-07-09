from brain_engine import find_best_match
from intent_detector import detect_intent

def run_agent(user_input):
    intent = detect_intent(user_input)
    memory = find_best_match(intent)

    if memory:
        return f"[AMRHZ AI] → {memory.get('response')}"
    else:
        return "[AMRHZ AI] → No memory found. Learning..."

if __name__ == "__main__":
    while True:
        user_input = input(">> ")
        print(run_agent(user_input))