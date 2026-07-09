def detect_intent(user_input):
    user_input = user_input.lower()

    if "build" in user_input:
        return "build_system"
    elif "fix" in user_input:
        return "debug"
    elif "status" in user_input:
        return "check_status"
    else:
        return "general"