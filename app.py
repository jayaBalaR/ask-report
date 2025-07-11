import streamlit as st
from docx import Document
import os

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(page_title="📘 DOCX Page Flip App", layout="centered")
st.title("📄 Page Flip Viewer (from report1.docx)")

# -----------------------------
# Resolve path to the .docx file
# -----------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
docx_path = os.path.join(current_dir, "report1.docx")

# -----------------------------
# Function to extract non-empty paragraphs
# -----------------------------
def extract_pages_from_docx(path):
    doc = Document(path)
    return [para.text.strip() for para in doc.paragraphs if para.text.strip()]

# -----------------------------
# Try reading the document
# -----------------------------
try:
    pages = extract_pages_from_docx(docx_path)

    if not pages:
        st.warning("The document is empty or contains only whitespace.")
    else:
        # Initialize session state
        if "page_number" not in st.session_state:
            st.session_state.page_number = 0

        # Navigation buttons
        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            if st.button("⬅️ Previous") and st.session_state.page_number > 0:
                st.session_state.page_number -= 1

        with col3:
            if st.button("Next ➡️") and st.session_state.page_number < len(pages) - 1:
                st.session_state.page_number += 1

        # Display the current page
        current_page = pages[st.session_state.page_number]
        st.markdown(f"### Page {st.session_state.page_number + 1}")
        st.text_area("Content", current_page, height=300)

        # Show page number indicator
        st.markdown(
            f"<p style='text-align:center;color:grey;'>Page {st.session_state.page_number + 1} of {len(pages)}</p>",
            unsafe_allow_html=True,
        )

except Exception as e:
    st.error(f"❌ Could not load 'report1.docx': {e}")
