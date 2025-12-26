# # # from flask import Flask, request, jsonify
# # # from flask_cors import CORS
# # # from jarvis_core import process_command

# # # app = Flask(__name__)
# # # CORS(app)  # allows frontend JS to call API

# # # @app.route("/api/command", methods=["POST"])
# # # def handle_command():
# # #     data = request.get_json()
# # #     query = data.get("query", "")
# # #     reply = process_command(query)
# # #     return jsonify({"reply": reply})

# # # if __name__ == "__main__":
# # #     app.run(debug=True)


# # from flask import Flask, request, jsonify, send_from_directory
# # from flask_cors import CORS
# # from jarvis_core import process_command
# # import os

# # app = Flask(__name__, static_folder="../frontend")
# # CORS(app)  # Allow JS frontend to call backend

# # # Serve frontend files
# # @app.route('/')
# # def home():
# #     return send_from_directory(app.static_folder, "index.html")

# # @app.route('/<path:path>')
# # def serve_files(path):
# #     """Serve other frontend files (JS, CSS)"""
# #     return send_from_directory(app.static_folder, path)

# # # API to handle Jarvis commands
# # @app.route("/api/command", methods=["POST"])
# # def handle_command():
# #     data = request.get_json()
# #     query = data.get("query", "")
# #     reply = process_command(query)
# #     return jsonify({"reply": reply})

# # if __name__ == "__main__":
# #     print("🚀 Jarvis backend running...")
# #     print("Open http://127.0.0.1:5000/ in your browser to use the assistant.")
# #     app.run(debug=True)

# # app.py
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from dotenv import load_dotenv
# import os

# # load env first
# load_dotenv()

# from jarvis_core import process_command  # local module

# app = Flask(__name__)
# CORS(app)

# @app.route("/api/command", methods=["POST"])
# def handle_command():
#     data = request.get_json(force=True)
#     query = data.get("query", "")
#     if not query:
#         return jsonify({"error": "No query provided"}), 400

#     # process the command (this may open a website locally if command asks)
#     reply = process_command(query)
#     return jsonify({"reply": reply})

# if __name__ == "__main__":
#     # set host=0.0.0.0 if you want it reachable from other devices on the LAN
#     app.run(port=5000, debug=True)


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
