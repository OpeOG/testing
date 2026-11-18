import streamlit as st

col1, col2 = st.columns(2)
with col1:
    st.button("Get app", icon="⬇️")
with col2:
    st.button("Upgrade", icon="✨")

st.title("Where should we start?", anchor=False)

with st.container():
    st.chat_input("Ask Gemini")

st.button("Design a phone wallpaper for me")
st.button("Help me make a big life decision")
st.button("Build a weekly checklist from my routine")
