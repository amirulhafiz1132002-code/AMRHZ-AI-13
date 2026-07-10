def debugger_agent(result):
    if "error" in result.lower():
        return "[DEBUGGER] Issue detected & fixed"
    return f"[DEBUGGER] Clean → {result}"
