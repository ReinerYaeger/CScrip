import os

import openai
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def cscrip_chatgpt(prompt):
    responses = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": prompt}]
    )
    return responses.choices[0].message.content


def chat():
    return None
