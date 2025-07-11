import streamlit as st
import os

# --------------------------
# Config and Title
# --------------------------
st.set_page_config(page_title="📘 TXT Page Flip App", layout="centered")
st.title("📄 Page Flip Viewer - report1.txt")

# --------------------------
# Load and split txt file content
# --------------------------
def read_txt_as_pages(filepath, delimiter="\n\n"):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        # Split into pages using double newline as default
        return [page.strip() for page in content.split(delimiter) if page.strip()]

# --------------------------
# Get absolute path to the txt file
# --------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
txt_path = os.path.join(script_dir, "report1.txt")

# --------------------------
# Check and load
# --------------------------
if not os.path.exists(txt_path):
    st.error(f"❌ File 'report1.txt' not found at:\n{txt_path}")
    st.stop()

pages = read_txt_as_pages(txt_path)

# --------------------------
# Initialize session state
# --------------------------
if "page_number" not in st.session_state:
    st.session_state.page_number = 0

# --------------------------
# Navigation buttons
# --------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous") and st.session_state.page_number > 0:
        st.session_state.page_number -= 1

with col3:
    if st.button("Next ➡️") and st.session_state.page_number < len(pages) - 1:
        st.session_state.page_number += 1

# --------------------------
# Display current page
# --------------------------
pg = st.session_state.page_number
st.markdown(f"### Page {pg + 1}")
st.text_area("Page Content", pages[pg], height=300)

st.markdown(
    f"<p style='text-align:center;color:grey;'>Page {pg + 1} of {len(pages)}</p>",
    unsafe_allow_html=True,
)
