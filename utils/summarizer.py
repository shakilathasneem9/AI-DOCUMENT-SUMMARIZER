from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def summarize_text(text, length):

    if not text:
        return "No text provided."

    text = text[:30000]

    prompt = f"""
You are an expert student assistant.

Create a structured summary.

Summary Length: {length}

Document:
{text}
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            return response.text

        except Exception as e:
            if "503" in str(e):
                time.sleep(3)
                continue
            return f"Gemini Error: {str(e)}"

    return "Gemini is busy."


def chat_with_pdf(text, question):

    if not text or not question:
        return "Please provide both."

    text = text[:30000]

    prompt = f"""
Answer using document only.

Document:
{text}

Question:
{question}
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            return response.text

        except Exception as e:
            if "503" in str(e):
                time.sleep(3)
                continue
            return f"Gemini Error: {str(e)}"

    return "Gemini is busy."