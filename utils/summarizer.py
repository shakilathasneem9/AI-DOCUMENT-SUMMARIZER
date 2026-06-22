from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

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

Summary Length: {length}

Document:
{text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"


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

If the answer is not present, reply:
Not found in document.

Document:
{text}

Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"