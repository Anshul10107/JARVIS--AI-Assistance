# # # # import datetime
# # # # import webbrowser
# # # # import os
# # # # import pyttsx3

# # # # engine = pyttsx3.init()
# # # # engine.setProperty('rate', 175)
# # # # engine.setProperty('volume', 1.0)

# # # # def say(text):
# # # #     print(f"🤖 Jarvis: {text}")
# # # #     engine.say(text)
# # # #     engine.runAndWait()

# # # # def process_command(query):
# # # #     """Process the user command and return Jarvis's reply."""
# # # #     query = query.lower().strip()

# # # #     # Exit
# # # #     if any(word in query for word in ["exit", "stop", "quit", "goodbye"]):
# # # #         say("Goodbye! Have a great day.")
# # # #         return "Goodbye!"

# # # #     # Sites
# # # #     sites = {
# # # #         "youtube": "https://www.youtube.com",
# # # #         "google": "https://www.google.com",
# # # #         "instagram": "https://www.instagram.com",
# # # #         "facebook": "https://www.facebook.com",
# # # #         "wikipedia": "https://www.wikipedia.com",
# # # #         "hotstar": "https://www.hotstar.com"
# # # #     }
# # # #     for site in sites:
# # # #         if f"open {site}" in query:
# # # #             webbrowser.open(sites[site])
# # # #             say(f"Opening {site}")
# # # #             return f"Opening {site}"

# # # #     # Music
# # # #     if "play music" in query:
# # # #         musicpath = r"C:\Users\MY\Downloads\RADHA KRISHNA FLUTE MUSIC  RELAXING MUSIC SLEEP MUSIC.mp3"
# # # #         if os.path.exists(musicpath):
# # # #             os.startfile(musicpath)
# # # #             say("Playing music now...")
# # # #             return "Playing music now..."
# # # #         else:
# # # #             return "Music file not found."

# # # #     # Time
# # # #     if "time" in query:
# # # #         current_time = datetime.datetime.now().strftime("%I:%M %p")
# # # #         say(f"The current time is {current_time}")
# # # #         return f"The current time is {current_time}"

# # # #     # Date
# # # #     if "date" in query or "today" in query:
# # # #         current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
# # # #         say(f"Today's date is {current_date}")
# # # #         return f"Today's date is {current_date}"

# # # #     say("Sorry, I didn’t understand that command.")
# # # #     return "Sorry, I didn’t understand that command."


# # # import datetime
# # # import webbrowser
# # # import os
# # # import pyttsx3
# # # import google.generativeai as genai   # <-- Added

# # # # Configure Gemini API key
# # # genai.configure(api_key="AIzaSyCllYoD1Md9QJGZ2OytSklqGTpFcW-ZTms")   # <-- Your key

# # # engine = pyttsx3.init()
# # # engine.setProperty('rate', 175)
# # # engine.setProperty('volume', 1.0)

# # # def say(text):
# # #     print(f"🤖 Jarvis: {text}")
# # #     engine.say(text)
# # #     engine.runAndWait()

# # # def process_command(query):
# # #     """Process the user command and return Jarvis's reply."""
# # #     query = query.lower().strip()

# # #     # Exit
# # #     if any(word in query for word in ["exit", "stop", "quit", "goodbye"]):
# # #         say("Goodbye! Have a great day.")
# # #         return "Goodbye!"

# # #     # Sites
# # #     sites = {
# # #         "youtube": "https://www.youtube.com",
# # #         "google": "https://www.google.com",
# # #         "instagram": "https://www.instagram.com",
# # #         "facebook": "https://www.facebook.com",
# # #         "wikipedia": "https://www.wikipedia.com",
# # #         "hotstar": "https://www.hotstar.com"
# # #     }
# # #     for site in sites:
# # #         if f"open {site}" in query:
# # #             webbrowser.open(sites[site])
# # #             say(f"Opening {site}")
# # #             return f"Opening {site}"

# # #     # Music
# # #     if "play music" in query:
# # #         musicpath = r"C:\Users\MY\Downloads\RADHA KRISHNA FLUTE MUSIC  RELAXING MUSIC SLEEP MUSIC.mp3"
# # #         if os.path.exists(musicpath):
# # #             os.startfile(musicpath)
# # #             say("Playing music now...")
# # #             return "Playing music now..."
# # #         else:
# # #             return "Music file not found."

# # #     # Time
# # #     if "time" in query:
# # #         current_time = datetime.datetime.now().strftime("%I:%M %p")
# # #         say(f"The current time is {current_time}")
# # #         return f"The current time is {current_time}"

# # #     # Date
# # #     if "date" in query or "today" in query:
# # #         current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
# # #         say(f"Today's date is {current_date}")
# # #         return f"Today's date is {current_date}"

# # #     # --- AI Search (Gemini) ---
# # #     try:
# # #         model = genai.GenerativeModel("gemini-1.5-flash")
# # #         response = model.generate_content(query)
# # #         answer = response.text

# # #         say(answer)
# # #         return answer

# # #     except Exception as e:
# # #         err = f"AI error: {e}"
# # #         say(err)
# # #         return err

# # #     # Default fallback
# # #     say("Sorry, I didn’t understand that command.")
# # #     return "Sorry, I didn’t understand that command."

# # # jarvis_core.py
# # import os
# # import webbrowser
# # import re
# # from dotenv import load_dotenv
# # load_dotenv()

# # # Optional: text-to-speech (commented out - enable if you have pyttsx3)
# # # import pyttsx3
# # # engine = pyttsx3.init()
# # # engine.setProperty('rate', 175)
# # # engine.setProperty('volume', 1.0)
# # # def say(text):
# # #     print("Jarvis:", text)
# # #     engine.say(text)
# # #     engine.runAndWait()

# # def say(text):
# #     # simple console output (replace with TTS if you want)
# #     print("Jarvis:", text)

# # # ---- Google Gemini setup (google-generativeai) ----
# # # Install: pip install google-generativeai
# # API_KEY = os.getenv("GEMINI_API_KEY")  # put new key in .env
# # if not API_KEY:
# #     say("Warning: GEMINI_API_KEY not found in environment. Generative responses will fail.")
# # else:
# #     try:
# #         import google.generativeai as genai
# #         genai.configure(api_key=API_KEY)
# #         have_genai = True
# #     except Exception as e:
# #         have_genai = False
# #         say(f"google.generativeai import failed: {e}")

# # # Common site shortcuts
# # SITES = {
# #     "youtube": "https://www.youtube.com",
# #     "google": "https://www.google.com",
# #     "instagram": "https://www.instagram.com",
# #     "facebook": "https://www.facebook.com",
# #     "github": "https://github.com",
# #     "wikipedia": "https://en.wikipedia.org",
# #     "reddit": "https://www.reddit.com",
# #     # add more as needed
# # }

# # def is_url(text):
# #     # very simple url detection
# #     return bool(re.search(r"(https?://|www\.)", text))

# # def open_site_by_keyword(keyword):
# #     keyword = keyword.lower().strip()
# #     # if someone types "open stack overflow" -> detect 'stack' or 'stackoverflow'
# #     for k, url in SITES.items():
# #         if k in keyword:
# #             webbrowser.open(url)
# #             return f"Opened {k} in your browser."
# #     # fallback: treat keyword as raw url (add http if missing)
# #     if is_url(keyword):
# #         url = keyword if keyword.startswith("http") else "https://" + keyword
# #         webbrowser.open(url)
# #         return f"Opened {url} in your browser."
# #     # if no match
# #     return None

# # def call_gemini(prompt):
# #     if not globals().get("have_genai", False):
# #         return "Generative model not available. Check GEMINI_API_KEY and installed package."

# #     try:
# #         model = genai.GenerativeModel("gemini-1.5-flash-001")
# #         response = model.generate_content(prompt)
# #         # two common shapes returned by different SDK versions:
# #         if hasattr(response, "text") and response.text:
# #             return response.text
# #         if getattr(response, "candidates", None):
# #             return response.candidates[0].output
# #         # fallback: str(response)
# #         return str(response)
# #     except Exception as e:
# #         return f"API call failed: {e}"

# # def process_command(query: str) -> str:
# #     """
# #     - Opens websites if query says 'open' or 'go to'.
# #     - If query contains a URL, open it.
# #     - Otherwise, send the query to Gemini and return the reply.
# #     """
# #     q = query.strip()
# #     low = q.lower()

# #     # exit words
# #     if any(word in low for word in ["exit", "quit", "stop", "goodbye"]):
# #         say("Goodbye!")
# #         return "Goodbye!"

# #     # direct 'open' command
# #     if low.startswith("open ") or low.startswith("go to ") or low.startswith("visit "):
# #         # remove the verb
# #         # e.g. "open youtube" -> target = "youtube"
# #         target = re.sub(r"^(open|go to|visit)\s+", "", low, flags=re.I).strip()
# #         if not target:
# #             return "Which site should I open?"
# #         result = open_site_by_keyword(target)
# #         if result:
# #             say(result)
# #             return result
# #         # otherwise attempt to open as url
# #         url = target if target.startswith("http") else ("https://" + target)
# #         try:
# #             webbrowser.open(url)
# #             msg = f"Opened {url}"
# #             say(msg)
# #             return msg
# #         except Exception as e:
# #             err = f"Failed to open {url}: {e}"
# #             say(err)
# #             return err

# #     # if the user gave a URL anywhere
# #     if is_url(q):
# #         # try to extract the url
# #         m = re.search(r"(https?://[^\s]+|www\.[^\s]+)", q)
# #         if m:
# #             url = m.group(0)
# #             url = url if url.startswith("http") else "https://" + url
# #             try:
# #                 webbrowser.open(url)
# #                 msg = f"Opened {url}"
# #                 say(msg)
# #                 return msg
# #             except Exception as e:
# #                 err = f"Failed to open {url}: {e}"
# #                 say(err)
# #                 return err

# #     # otherwise use Gemini for a conversational reply
# #     say(f"Sending to Gemini: {q}")
# #     reply = call_gemini(q)
# #     say(reply)
# #     return reply




# # jarvis_core.py
# import os
# import webbrowser
# import re
# from dotenv import load_dotenv

# load_dotenv()

# # Load API key from .env
# API_KEY = os.getenv("GEMINI_API_KEY")

# # Try to import and configure google.generativeai
# have_genai = False
# genai = None
# if API_KEY:
#     try:
#         import google.generativeai as genai_lib
#         genai_lib.configure(api_key=API_KEY)
#         genai = genai_lib
#         have_genai = True
#     except Exception as e:
#         # leave have_genai False and return useful messages later
#         print("google.generativeai import/config error:", e)

# # site shortcuts
# SITES = {
#     "youtube": "https://www.youtube.com",
#     "google": "https://www.google.com",
#     "instagram": "https://www.instagram.com",
#     "facebook": "https://www.facebook.com",
#     "github": "https://github.com",
#     "wikipedia": "https://en.wikipedia.org",
#     "reddit": "https://www.reddit.com",
#     "stackoverflow": "https://stackoverflow.com",
# }

# def is_url(text):
#     return bool(re.search(r"(https?://|www\.)", text))

# def open_site_by_keyword(keyword):
#     keyword = keyword.lower().strip()
#     for k, url in SITES.items():
#         if k in keyword:
#             webbrowser.open(url)
#             return f"Opened {k} in your browser."
#     # fallback: treat as raw url
#     if is_url(keyword):
#         url = keyword if keyword.startswith("http") else "https://" + keyword
#         webbrowser.open(url)
#         return f"Opened {url}"
#     return None

# def call_gemini(prompt):
#     if not have_genai:
#         return "Generative model not available. Check GEMINI_API_KEY and installed package."

#     try:
#         # NOTE: use the updated model name (gemini-1.5-flash-001)
#         model = genai.GenerativeModel("gemini-1.5-flash-001")
#         resp = model.generate_content(prompt)
#         # robust extraction across SDK versions:
#         if hasattr(resp, "text") and resp.text:
#             return resp.text
#         if getattr(resp, "candidates", None):
#             # typical structure: candidates[0].output
#             return resp.candidates[0].output
#         return str(resp)
#     except Exception as e:
#         # return message so frontend can display error
#         return f"API call failed: {e}"

# def process_command(query: str) -> str:
#     q = query.strip()
#     low = q.lower()

#     # small control words
#     if any(word in low for word in ["exit", "quit", "stop", "goodbye"]):
#         return "Goodbye!"

#     # open commands
#     if low.startswith("open ") or low.startswith("go to ") or low.startswith("visit "):
#         target = re.sub(r"^(open|go to|visit)\s+", "", low, flags=re.I).strip()
#         if not target:
#             return "Which site should I open?"
#         result = open_site_by_keyword(target)
#         if result:
#             return result
#         # try raw url
#         url = target if target.startswith("http") else "https://" + target
#         try:
#             webbrowser.open(url)
#             return f"Opened {url}"
#         except Exception as e:
#             return f"Failed to open {url}: {e}"

#     # URL anywhere in query
#     if is_url(q):
#         m = re.search(r"(https?://[^\s]+|www\.[^\s]+)", q)
#         if m:
#             url = m.group(0)
#             url = url if url.startswith("http") else "https://" + url
#             try:
#                 webbrowser.open(url)
#                 return f"Opened {url}"
#             except Exception as e:
#                 return f"Failed to open {url}: {e}"

#     # fallback to generative model
#     if not API_KEY:
#         return "No GEMINI_API_KEY configured. Please add your key in backend/.env"

#     return call_gemini(q)

# def debug_gemini_call():
#     """
#     Returns (ok, result) to help debug from app.py /debug_gemini route.
#     """
#     if not have_genai:
#         return False, "google.generativeai not available or API key missing."
#     try:
#         model = genai.GenerativeModel("gemini-1.5-flash-001")
#         resp = model.generate_content("Hello from debug test. Reply briefly.")
#         if hasattr(resp, "text") and resp.text:
#             return True, resp.text
#         if getattr(resp, "candidates", None):
#             return True, resp.candidates[0].output
#         return True, str(resp)
#     except Exception as e:
#         return False, str(e)




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
