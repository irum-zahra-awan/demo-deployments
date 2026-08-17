import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Idea Sharpener", page_icon="🎯")

st.title("🎯 Idea Sharpener")
st.write(
    "Type your rough idea in one line. Get back a sharper problem statement "
    "and a suggestion for who to test it on first."
)

# --- API key from secrets, never hardcoded ---
api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("No API key found. Add GEMINI_API_KEY to .streamlit/secrets.toml "
              "(locally) or to the app's Secrets settings (on Streamlit Cloud).")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-3.6-flash")

PROMPT_TEMPLATE = """You are a sharp startup mentor helping a builder at a bootcamp
turn a rough one-line idea into something they can test with a real person this week.

Rough idea: "{idea}"

Respond in exactly this format, nothing else:

Problem statement: <one clear sentence naming the specific person and the specific
problem they have, not a description of the solution>

First test user: <one concrete suggestion for who to show this to in the next 48
hours — be specific about where to find them, not a vague persona>
"""

idea = st.text_input("Your rough idea", placeholder="e.g. an app that helps students find study partners")

if st.button("Sharpen it", type="primary") and idea.strip():
    with st.spinner("Thinking..."):
        response = model.generate_content(PROMPT_TEMPLATE.format(idea=idea))
        st.markdown("---")
        st.markdown(response.text)

st.markdown("---")
st.caption("Built live at League of Launchers — Ship It session, 19 Aug 2026")
