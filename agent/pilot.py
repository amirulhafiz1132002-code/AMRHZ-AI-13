def pilot_agent(prompt, memory):
    if "build" in prompt.lower():
        return f"[PLAN] BUILD TASK → {prompt}"
    elif "fix" in prompt.lower():
        return f"[PLAN] DEBUG TASK → {prompt}"
    else:
        return f"[PLAN] GENERAL → {prompt} | memory: {memory}"
