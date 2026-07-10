def builder_agent(plan):
    if "BUILD" in plan:
        return f"[BUILDER] Creating system..."
    return f"[BUILDER] Executing: {plan}"
