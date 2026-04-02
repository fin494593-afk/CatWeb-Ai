from flask import Flask
import requests

app = Flask(__name__)

import os
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={GEMINI_API_KEY}"

@app.route("/ask/<path:prompt>")
def ask(prompt):
    body = {"contents":[{"parts":[{"text": prompt}]}]}
    r = requests.post(GEMINI_URL, json=body)
    data = r.json()
    if "candidates" not in data:
        return str(data)
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    return text

@app.route("/")
def home():
    return "CatWeb AI Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
