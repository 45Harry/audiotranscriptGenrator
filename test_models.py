import google.generativeai as genai
import os

API_KEY = "AIzaSyCLVplTk-iBWq3YR0g7wOAt9zI7SZ-sILc"
genai.configure(api_key=API_KEY)

candidates = [
    "gemini-1.5-pro",
    "gemini-1.5-pro-002",
    "models/gemini-1.5-pro",
    "models/gemini-1.5-pro-002",
    "gemini-pro",
    "gemini-pro-latest",
    "gemini-2.0-flash-exp" # Backup
]

for model_name in candidates:
    print(f"Testing {model_name}...")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello")
        print(f"SUCCESS: {model_name}")
        break  # Found one
    except Exception as e:
        print(f"FAILED: {model_name} - {e}")
