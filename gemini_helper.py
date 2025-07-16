from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def summarize_answer(question: str, answer_snippets: str) -> str:
    # Try different model names in order of preference
    model_names = ["models/gemini-2.0-flash"]
    
    for model_name in model_names:
        try:
            model = genai.GenerativeModel(model_name)
            prompt = f"""
You are a helpful AI assistant. A developer asked this question:

{question}

You found the following answers on StackOverflow:

{answer_snippets}

Summarize the likely solution in clear, simple terms.
"""
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Model {model_name} failed: {e}")
            continue
    
    # If all models fail, return the raw results
    return f"❌ Failed to generate summary with any available model.\n\nHere are the raw results:\n{answer_snippets}"
