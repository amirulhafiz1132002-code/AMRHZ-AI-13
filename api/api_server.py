from flask import Flask, request, jsonify
from agent.main_agent import run_agent

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    response = run_agent(data["message"])
    return jsonify({"response": response})

app.run(port=5000)