# list_models_debug.py
from dotenv import load_dotenv
import os, traceback, json

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
print("GEMINI_API_KEY loaded:", bool(API_KEY))

try:
    import google.generativeai as genai
except Exception as e:
    print("ERROR importing google.generativeai:", e)
    raise

genai.configure(api_key=API_KEY)

print("\nCalling list_models() to show available models and methods...\n")
try:
    # call the list models endpoint
    models = genai.list_models()  # most SDKs expose this; if this fails we catch and print
    # models might be a list or a dict-like object
    try:
        # try to iterate
        for m in models:
            try:
                # print id and any 'methods' property (SDKs vary)
                mid = getattr(m, "name", None) or getattr(m, "id", None) or str(m)
                methods = getattr(m, "methods", None) or (m.get("methods") if isinstance(m, dict) else None)
                print("MODEL:", mid)
                print("  raw object:", m)
                print("  methods:", methods)
                print("-" * 40)
            except Exception:
                print("MODEL (raw):", m)
                print("-" * 40)
    except TypeError:
        # if it's a mapping
        print("models (repr):", repr(models))
        print(json.dumps(models, default=str, indent=2))
except Exception:
    print("ERROR calling list_models():")
    traceback.print_exc()

# Try to find a model that supports generate or chat and do a quick test:
print("\nAttempting to find a usable model automatically...")
usable = None
try:
    # if 'models' above exists and is iterable, inspect it
    for m in (models if 'models' in locals() else []):
        mid = getattr(m, "name", None) or getattr(m, "id", None) or (m.get("name") if isinstance(m, dict) else None)
        methods = getattr(m, "methods", None) or (m.get("methods") if isinstance(m, dict) else [])
        if not mid:
            continue
        # check for common method names
        if methods:
            # method list might be strings or objects; normalize to strings
            meths = [ (x if isinstance(x, str) else (x.get("name") if isinstance(x, dict) else str(x))) for x in methods ]
            if any("generate" in s.lower() or "chat" in s.lower() for s in meths):
                usable = mid
                print("Selecting usable model:", usable, "with methods:", meths)
                break
    if not usable:
        print("No model with explicit 'generate'/'chat' found in the list above.")
    else:
        # attempt a small call using generate_content (if available) and fallback to a chat call
        try:
            print("\nTrying generate_content on", usable)
            model = genai.GenerativeModel(usable)
            resp = model.generate_content("Say hello in one short sentence.")
            if hasattr(resp, "text") and resp.text:
                print("RESP.text:", resp.text)
            elif getattr(resp, "candidates", None):
                print("RESP.candidate:", resp.candidates[0].output)
            else:
                print("RESP (raw):", resp)
        except Exception as e:
            print("generate_content failed:", e)
            print("Trying chat completion fallback (if supported)...")
            try:
                # many SDKs support a chat endpoint; try safe fallback
                chat_resp = genai.chat.completions.create(model=usable, messages=[{"role":"user","content":"Say hello in one short sentence."}])
                print("Chat response object:", chat_resp)
                # show common fields
                if hasattr(chat_resp, "choices"):
                    print("Chat text:", getattr(chat_resp.choices[0], "message", getattr(chat_resp.choices[0], "text", None)))
            except Exception:
                print("Chat fallback also failed:")
                traceback.print_exc()
except Exception:
    traceback.print_exc()
