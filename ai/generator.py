import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_structure_and_content(idea: str):
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
You are an expert Python developer assistant. Based on the user's idea, generate a JSON with this structure:
{{
  "project_name": "your_project_name",
  "files": [
    {{
      "path": "main.py",
      "content": "...code here..."
    }},
    {{
      "path": "utils/helper.py",
      "content": "...more code..."
    }}
  ]
}}

Only return the JSON. The idea is: {idea}
"""

    response = model.generate_content(prompt)
    try:
        # Gemini might return markdown formatting; strip it
        text = response.text.strip().strip("```json").strip("```").strip()
        return json.loads(text)
    except Exception as e:
        print("❌ Failed to parse Gemini response:", e)
        print("Raw response:", response.text)
        return {"project_name": "failed_project", "files": []}
