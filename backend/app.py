# app.py
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# load env
load_dotenv()

# backend config
BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BACKEND_DIR, "..", "frontend")  # adjust if your frontend path differs

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="/")
CORS(app)

# local import - command processor
from jarvis_core import process_command, debug_gemini_call

@app.route("/", methods=["GET"])
def index():
    """
    Serve frontend index.html at root so http://127.0.0.1:5000/ loads your UI (no more Not Found).
    """
    # If frontend file exists in ../frontend/index.html, serve it.
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(index_path):
        return send_from_directory(FRONTEND_DIR, "index.html")
    return "Frontend index.html not found. Put your frontend files in ../frontend/", 404

@app.route("/api/command", methods=["POST"])
def handle_command():
    data = request.get_json(force=True, silent=True) or {}
    query = data.get("query", "").strip()
    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        reply = process_command(query)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": "Server error", "detail": str(e)}), 500

# debug route — returns model test or error trace (use while debugging)
@app.route("/debug_gemini", methods=["GET"])
def debug_gemini():
    try:
        ok, result = debug_gemini_call()
        return jsonify({"ok": ok, "result": result})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

if __name__ == "__main__":
    # Run on all interfaces if you want access from other devices: host="0.0.0.0"
    print("Starting backend on http://127.0.0.1:5000")
    app.run(port=5000, debug=True)
