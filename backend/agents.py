def pilot(prompt):
    return f"[PILOT] planning → {prompt}"

def builder(prompt):
    return f"[BUILDER] executing → {prompt}"

def debugger(prompt):
    return f"[DEBUGGER] checking → {prompt}"

def run_agents(prompt, context):
    p = pilot(prompt)
    b = builder(prompt + context)
    d = debugger(b)
    return f"{p}\n{b}\n{d}"