import streamlit as st
from docx import Document
import os

# -------------------------------
# App Setup
# -------------------------------
st.set_page_config(page_title="📘 DOCX Page Flip App", layout="centered")
st.title("📄 Multi-DOCX Page Flip Viewer")

# -------------------------------
# Function to read all docx files
# -------------------------------
def load_all_docx_files(folder_path):
    pages = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.lower().endswith(".docx"):
            file_path = os.path.join(folder_path, filename)
            try:
                doc = Document(file_path)
                content = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
                if not content:
                    content = "[Empty document]"
            except Exception as e:
                content = f"[Error reading '{filename}': {e}]"
            pages.append((filename, content))
    return pages

# -------------------------------
# Load documents
# -------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
pages = load_all_docx_files(script_dir)

if not pages:
    st.error("❌ No .docx files found in the current folder.")
    st.stop()

# -------------------------------
# Session state initialization
# -------------------------------
if "page_number" not in st.session_state:
    st.session_state.page_number = 0

# -------------------------------
# Navigation controls
# -------------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous") and st.session_state.page_number > 0:
        st.session_state.page_number -= 1

with col3:
    if st.button("Next ➡️") and st.session_state.page_number < len(pages) - 1:
        st.session_state.page_number += 1

# -------------------------------
# Display current page (read-only)
# -------------------------------
pg = st.session_state.page_number
filename, content = pages[pg]

st.markdown(f"### 📘 {filename} (Page {pg + 1})")
st.code(content, language="text")

st.markdown(
    f"<p style='text-align:center;color:grey;'>Page {pg + 1} of {len(pages)}</p>",
    unsafe_allow_html=True,
)
