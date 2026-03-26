import os
import json
import socket
import logging
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# --- NETWORK FIXES FOR FEDORA ---
# Forces IPv4 to prevent the 10-minute timeout hang
orig_getaddrinfo = socket.getaddrinfo
def getaddrinfo_ipv4(host, port, family=0, type=0, proto=0, flags=0):
    return orig_getaddrinfo(host, port, socket.AF_INET, type, proto, flags)
socket.getaddrinfo = getaddrinfo_ipv4

# --- INITIALIZATION ---
load_dotenv() 
logging.basicConfig(level=logging.INFO)

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("❌ ERROR: google-genai not found. Run: uv pip install google-genai python-dotenv")
    exit()

app = Flask(__name__)
CORS(app)

# --- CONFIGURATION ---
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_ID = "models/gemini-2.5-flash"

client = genai.Client(
    api_key=API_KEY,
    http_options={'api_version': 'v1beta'}
)

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_text = request.json.get("text", "")
    print(f"\n[1] Analyzing: {user_text}")
    
    prompt = f"""
    Analyze the Polish text: "{user_text}". 
    Return a JSON array where each object has:
    - "text": the original word/punctuation (include the space)
    - "is_inflected": boolean
    - "case": null OR "nom", "gen", "dat", "acc", "ins", "loc", "voc"
    - "base_form": the nominative singular form
    - "explanation": a very brief grammatical reason
    """

    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.1
            )
        )
        return jsonify(json.loads(response.text))
    except Exception as e:
        print(f"!!! Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
