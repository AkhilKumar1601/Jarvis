import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def ask_gpt(prompt):
  try:
    response = client.models.generate_content(
      model = "gemini-2.5-flash",
      contents=prompt
    )

    return response.text

  except Exception as e:
    return f"Error while contacting Gemini: {e}"