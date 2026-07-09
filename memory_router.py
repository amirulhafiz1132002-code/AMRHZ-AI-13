def route_memory(intent):
    if intent == "build_system":
        return "builder_module"
    elif intent == "debug":
        return "debug_module"
    else:
        return "general_module"