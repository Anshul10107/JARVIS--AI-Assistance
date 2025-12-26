# jarvis_core.py
import os
import webbrowser
import re
from dotenv import load_dotenv

load_dotenv()

# Load API key from .env
API_KEY = os.getenv("GEMINI_API_KEY")

# Try to import and configure google.generativeai
have_genai = False
genai = None
if API_KEY:
    try:
        import google.generativeai as genai_lib
        genai_lib.configure(api_key=API_KEY)
        genai = genai_lib
        have_genai = True
    except Exception as e:
        # leave have_genai False and print useful message for local debugging
        print("google.generativeai import/config error:", e)

# Choose a model that exists in your account (from list_models_debug output)
# You can change this to any other model string you saw in your list (e.g. "models/gemini-flash-latest")
MODEL_NAME = "models/gemini-2.5-flash"

# site shortcuts
SITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "github": "https://github.com",
    "wikipedia": "https://en.wikipedia.org",
    "reddit": "https://www.reddit.com",
    "stackoverflow": "https://stackoverflow.com",
}

def is_url(text):
    return bool(re.search(r"(https?://|www\.)", text))

def open_site_by_keyword(keyword):
    keyword = keyword.lower().strip()
    for k, url in SITES.items():
        if k in keyword:
            webbrowser.open(url)
            return f"Opened {k} in your browser."
    # fallback: treat as raw url
    if is_url(keyword):
        url = keyword if keyword.startswith("http") else "https://" + keyword
        webbrowser.open(url)
        return f"Opened {url}"
    return None

def call_gemini(prompt: str) -> str:
    """
    Tries generate_content first (generateContent). If that fails,
    falls back to chat completions if supported by the SDK/model.
    Returns a user-visible string with the reply or an error message.
    """
    if not have_genai:
        return "Generative model not available. Check GEMINI_API_KEY and installed package."

    try:
        # initialize model object with the exact model id (as returned by list_models)
        model = genai.GenerativeModel(MODEL_NAME)

        # Primary approach: generate_content (maps to generateContent)
        try:
            resp = model.generate_content(prompt)
            if hasattr(resp, "text") and resp.text:
                return resp.text
            if getattr(resp, "candidates", None):
                return resp.candidates[0].output
            # fallback: stringify the response object
            return str(resp)
        except Exception as e_gen:
            # Fallback: try chat completions (some SDKs/models expect this)
            try:
                chat_resp = genai.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[{"role": "user", "content": prompt}]
                )
                # Common shapes: chat_resp.choices[0].message.content or chat_resp.choices[0].text
                if hasattr(chat_resp, "choices") and len(chat_resp.choices) > 0:
                    choice = chat_resp.choices[0]
                    # if message is dict or object
                    msg = None
                    if getattr(choice, "message", None):
                        # message may be dict-like or object-like
                        m = choice.message
                        if isinstance(m, dict):
                            msg = m.get("content") or m.get("content", None)
                        else:
                            # object-like: try attribute access
                            msg = getattr(m, "get", None) and m.get("content") or getattr(m, "content", None)
                    if not msg and getattr(choice, "text", None):
                        msg = choice.text
                    if msg:
                        return msg
                return str(chat_resp)
            except Exception as e_chat:
                # return combined errors to help debugging on frontend
                return f"generate_content failed: {e_gen}  |  chat fallback failed: {e_chat}"
    except Exception as e:
        return f"API call failed (model init): {e}"

def process_command(query: str) -> str:
    q = query.strip()
    low = q.lower()

    # small control words
    if any(word in low for word in ["exit", "quit", "stop", "goodbye"]):
        return "Goodbye!"

    # open commands
    if low.startswith("open ") or low.startswith("go to ") or low.startswith("visit "):
        target = re.sub(r"^(open|go to|visit)\s+", "", low, flags=re.I).strip()
        if not target:
            return "Which site should I open?"
        result = open_site_by_keyword(target)
        if result:
            return result
        # try raw url
        url = target if target.startswith("http") else "https://" + target
        try:
            webbrowser.open(url)
            return f"Opened {url}"
        except Exception as e:
            return f"Failed to open {url}: {e}"

    # URL anywhere in query
    if is_url(q):
        m = re.search(r"(https?://[^\s]+|www\.[^\s]+)", q)
        if m:
            url = m.group(0)
            url = url if url.startswith("http") else "https://" + url
            try:
                webbrowser.open(url)
                return f"Opened {url}"
            except Exception as e:
                return f"Failed to open {url}: {e}"

    # fallback to generative model
    if not API_KEY:
        return "No GEMINI_API_KEY configured. Please add your key in backend/.env"

    return call_gemini(q)

def debug_gemini_call():
    """
    Returns (ok, result) to help debug from app.py /debug_gemini route.
    ok=True => result is reply text
    ok=False => result is error message
    """
    if not have_genai:
        return False, "google.generativeai not available or API key missing."
    try:
        # Use the same robust call used by call_gemini
        reply = call_gemini("Hello from debug test. Reply briefly.")
        # if reply starts with 'API call failed' or contains 'failed', consider it an error for debug
        if isinstance(reply, str) and ("failed" in reply.lower() or "error" in reply.lower()):
            return False, reply
        return True, reply
    except Exception as e:
        return False, str(e)
