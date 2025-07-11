import streamlit as st

# --- Page config ---
st.set_page_config(page_title="Page Flip App", layout="centered")

# --- Define content pages ---
pages = [
    {
        "title": "Welcome",
        "content": "📖 **Welcome to the Page Flip App!**\n\nUse the navigation buttons below to flip through the book."
    },
    {
        "title": "About",
        "content": "💡 **What is this app?**\n\nIt simulates a book or slide viewer using Streamlit."
    },
    {
        "title": "Yoga Wisdom",
        "content": "🧘‍♀️ **Yoga is the journey of the self, through the self, to the self.**"
    },
    {
        "title": "Thank You",
        "content": "🙏 **Thank you for flipping through!**\n\nFeel free to customize this book."
    }
]

# --- Safely initialize or get page number ---
page_number = st.session_state.get("page_number", 0)

# --- Navigation buttons ---
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous"):
        page_number = max(0, page_number - 1)

with col3:
    if st.button("Next ➡️"):
        page_number = min(len(pages) - 1, page_number + 1)

# --- Save updated page number ---
st.session_state["page_number"] = page_number

# --- Display current page ---
current = pages[page_number]
st.markdown(f"### {current['title']}")
st.markdown(current['content'])

# --- Page count display ---
st.markdown(
    f"<p style='text-align:center;color:grey;'>Page {page_number + 1} of {len(pages)}</p>",
    unsafe_allow_html=True
)
