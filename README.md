# 📄 AI Document Summarizer & Chat Assistant

An AI-powered Streamlit web app that allows users to upload documents (PDF, DOCX, TXT), generate structured summaries, and chat with the document using Google Gemini AI.

---

## 🚀 Live Demo
👉 https://your-app-link-here.streamlit.app

---

## ✨ Features

- 📄 Upload PDF, DOCX, TXT files
- 🧠 AI-powered structured summaries
- 🔑 Key points extraction
- 📚 Important concepts breakdown
- ❓ Auto-generated exam questions
- 💬 Chat with PDF (ask questions from document)
- 📥 Download summary as text file
- ⚡ Retry mechanism for API stability

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🎈
- Google Gemini API 🤖
- python-dotenv
- PyPDF2
- python-docx

---

## 📁 Project Structure


ai-document-summarizer/
│
├── app.py
├── utils/
│ ├── summarizer.py
│ ├── pdf_reader.py
│ └── docx_reader.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-document-summarizer.git
cd ai-document-summarizer
```
2. Create virtual environment
```
python -m venv venv
```
venv\Scripts\activate   # Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Add API Key

Create a .env file:
```
GEMINI_API_KEY=your_api_key_here
```
▶️ Run the App
```
streamlit run app.py
```
🧠 How It Works

User uploads a document
Text is extracted using Python libraries
Gemini AI processes the content

App generates:

Structured summary
Q&A chat responses
User can download results or chat with document
📌 Future Improvements
🔥 Chat memory (multi-turn conversation)
📊 Highlight important lines in PDF
📄 Page-wise summarization
🌐 Multi-language support
⚡ Faster chunk-based retrieval system

👨‍💻 Author
Your shakila thasneem
GitHub: https://github.com/shakilathasnem9

⭐ If you like this project

Give it a star ⭐ and feel free to contribute!

License

This project is created for educational and portfolio purposes.
