from flask import Flask
import threading
import requests
import time

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyD3FsgJlJ4JFlnWj1monbRWC5E6ALeyM_g"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

pending_prompt = None
pending_response = None

@app.route("/ask/<path:prompt>")
def ask(prompt):
    global pending_response
    body = {"contents":[{"parts":[{"text": prompt}]}]}
    r = requests.post(GEMINI_URL, json=body)
    text = r.json()["candidates"][0]["content"]["parts"][0]["text"]
    return text

@app.route("/")
def home():
    return "CatWeb AI Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
