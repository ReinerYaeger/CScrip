import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


def custom_gemini(prompt):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
