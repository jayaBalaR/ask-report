import streamlit as st
from docx import Document
import os

st.set_page_config(page_title="📖 DOCX Book Reader", layout="centered")
st.title("📄 Page Flip App from Local DOCX File")

# --- Path to docx file in the repo ---
DOCX_PATH = os.path.join(os.path.dirname(__file__), "report1.docx")

# --- Load paragraphs as pages ---
def extract_pages_from_docx(filepath):
    doc = Document(filepath)
    return [para.text for para in doc.paragraphs if para.text.strip() != ""]

# --- Read and prepare pages ---
pages = extract_pages_from_docx(DOCX_PATH)

# --- Initialize session state ---
if "page_number" not in st.session_state:
    st.session_state.page_number = 0

# --- Navigation buttons ---
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous") and st.session_state.page_number > 0:
        st.session_state.page_number -= 1

with col3:
    if st.button("Next ➡️") and st.session_state.page_number < len(pages) - 1:
        st.session_state.page_number += 1

# --- Display current page ---
current_page = pages[st.session_state.page_number]
st.markdown(f"### Page {st.session_state.page_number + 1}")
st.text_area("Page Content", current_page, height=300)

# --- Footer ---
st.markdown(
    f"<p style='text-align:center;color:grey;'>Page {st.session_state.page_number + 1} of {len(pages)}</p>",
    unsafe_allow_html=True,
)
