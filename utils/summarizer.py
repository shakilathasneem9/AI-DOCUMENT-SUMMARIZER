from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

# Initialize Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# -----------------------------
# 1. STRUCTURED SUMMARY
# -----------------------------
def summarize_text(text, length):

    if not text:
        return "No text provided."

    text = text[:30000]

    prompt = f"""
You are an expert student assistant and document analyzer.

Create a structured, exam-ready summary of the document.

Follow this format strictly:

📌 Overview:
Give a short 2-3 line explanation.

🔑 Key Points:
- Bullet points

📚 Important Concepts:
- Simple explanations

❓ Possible Exam Questions:
- Likely exam questions

🧠 Simple Explanation:
Explain in very easy language.

Rules:
- Do NOT copy text
- Focus on understanding
- Keep it structured

Summary Length: {length}

Document:
{text}
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text

        except Exception:
            time.sleep(2)

    return "Model is busy. Please try again later."


# -----------------------------
# 2. CHAT WITH PDF
# -----------------------------
def chat_with_pdf(text, question):

    if not text or not question:
        return "Please provide both document and question."

    text = text[:30000]

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the document below.

If not found, say:
"Not found in document."

Document:
{text}

Question:
{question}

Give a clear, simple answer.
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text

        except Exception:
            time.sleep(2)

    return "Model is busy. Try again in a few seconds."