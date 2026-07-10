@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("message")

    memory = load_memory(prompt)

    plan = pilot_agent(prompt, memory if memory else "no memory")

    for _ in range(3):
        result = builder_agent(plan)
        result = debugger_agent(result)

        if "clean" in result.lower():
            break

        plan = result

    save_memory(prompt, result)

    return {"response": result}
