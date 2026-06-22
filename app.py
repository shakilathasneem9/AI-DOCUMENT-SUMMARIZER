import streamlit as st
from utils.pdf_reader import read_pdf
from utils.docx_reader import read_docx
from utils.summarizer import summarize_text, chat_with_pdf

st.set_page_config(
    page_title="AI Document Summarizer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Document Summarizer")
st.write("Upload a PDF, DOCX, or TXT file and interact with it using AI.")

# -------------------------
# CHAT SECTION (ALWAYS VISIBLE)
# -------------------------
st.markdown("---")
st.subheader("💬 Chat with Document")

question = st.text_input(
    "Ask a question from the document",
    placeholder="Upload a document and ask questions..."
)

# -------------------------
# FILE UPLOAD
# -------------------------
uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf", "docx", "txt"]
)

summary_length = st.selectbox(
    "Choose Summary Length",
    ["Short", "Medium", "Long"]
)

# Store extracted text
text = ""

if uploaded_file:

    st.success(f"File Uploaded: {uploaded_file.name}")

    try:
        # -------------------------
        # TEXT EXTRACTION
        # -------------------------
        if uploaded_file.name.endswith(".pdf"):
            text = read_pdf(uploaded_file)

        elif uploaded_file.name.endswith(".docx"):
            text = read_docx(uploaded_file)

        elif uploaded_file.name.endswith(".txt"):
            text = uploaded_file.read().decode("utf-8")

        # -------------------------
        # METRICS
        # -------------------------
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Words", len(text.split()))

        with col2:
            st.metric("Characters", len(text))

        # -------------------------
        # PREVIEW TEXT
        # -------------------------
        st.subheader("📄 Extracted Text")

        st.text_area(
            "Document Content",
            text[:1000],
            height=300
        )

        # -------------------------
        # SUMMARY SECTION
        # -------------------------
        if st.button("✨ Generate Summary"):

            with st.spinner("Generating Summary..."):

                summary = summarize_text(
                    text,
                    summary_length
                )

            st.subheader("📝 Summary")
            st.write(summary)

            st.success("Summary generated successfully!")

            clean_name = uploaded_file.name
            clean_name = (
                clean_name
                .replace(".pdf", "")
                .replace(".docx", "")
                .replace(".txt", "")
            )

            st.download_button(
                label="📥 Download Summary",
                data=summary,
                file_name=f"{clean_name}_summary.txt",
                mime="text/plain"
            )

    except Exception as e:
        st.error(f"Error: {e}")

# -------------------------
# CHAT LOGIC
# -------------------------
if question:

    if uploaded_file and text:

        with st.spinner("Thinking..."):
            answer = chat_with_pdf(text, question)

        st.markdown("### 🤖 Answer")
        st.write(answer)

    else:
        st.warning("Please upload a document first.")