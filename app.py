import streamlit as st
from docx import Document
import os

st.set_page_config(page_title="📘 DOCX Page Flip App", layout="centered")
st.title("📄 Page Flip Viewer (from report1.docx)")

# --- Resolve path ---
current_dir = os.path.dirname(os.path.abspath(__file__))
filename = "report1.docx"
docx_path = os.path.join(current_dir, filename)

# --- Check if file exists ---
if not os.path.exists(docx_path):
    st.error(f"❌ File '{filename}' not found at: {docx_path}")
    st.stop()

# --- Function to read document ---
def extract_pages_from_docx(path):
    doc = Document(path)
    return [para.text.strip() for para in doc.paragraphs if para.text.strip()]

# --- Read and display ---
pages = extract_pages_from_docx(docx_path)

if "page_number" not in st.session_state:
    st.session_state.page_number = 0

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous") and st.session_state.page_number > 0:
        st.session_state.page_number -= 1

with col3:
    if st.button("Next ➡️") and st.session_state.page_number < len(pages) - 1:
        st.session_state.page_number += 1

current_page = pages[st.session_state.page_number]
st.markdown(f"### Page {st.session_state.page_number + 1}")
st.text_area("Content", current_page, height=300)

st.markdown(
    f"<p style='text-align:center;color:grey;'>Page {st.session_state.page_number + 1} of {len(pages)}</p>",
    unsafe_allow_html=True,
)
