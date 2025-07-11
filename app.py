import streamlit as st
from docx import Document

# --------------------------
# Config and Title
# --------------------------
st.set_page_config(page_title="📘 Page Flip from DOCX", layout="centered")
st.title("📄 Page Flip Viewer - report1.docx")

# --------------------------
# Load and read docx content
# --------------------------
def read_docx_as_pages(filepath):
    doc = Document(filepath)
    return [para.text.strip() for para in doc.paragraphs if para.text.strip()]

# Read the file directly
pages = read_docx_as_pages("./report1.docx")  # Make sure it's in the same folder

# --------------------------
# Initialize session state
# --------------------------
if "page_number" not in st.session_state:
    st.session_state.page_number = 0

# --------------------------
# Navigation
# --------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous") and st.session_state.page_number > 0:
        st.session_state.page_number -= 1

with col3:
    if st.button("Next ➡️") and st.session_state.page_number < len(pages) - 1:
        st.session_state.page_number += 1

# --------------------------
# Show current page content
# --------------------------
current_page = st.session_state.page_number
st.markdown(f"### Page {current_page + 1}")
st.text_area("Page Content", pages[current_page], height=300)

# --------------------------
# Page count footer
# --------------------------
st.markdown(
    f"<p style='text-align:center;color:grey;'>Page {current_page + 1} of {len(pages)}</p>",
    unsafe_allow_html=True,
)
