import streamlit as st

New_Chat = st.Page(page="pages/New_Chat.py", title="New chat", icon="📝", default=True)
Library = st.Page(page="pages/Library.py", title="Library", icon="📚")
Images = st.Page(page="pages/Images.py", title="Images", icon="🏙️")
Scheduled = st.Page(page="pages/Scheduled.py", title="Scheduled", icon="🕒")
Customize = st.Page(page="pages/Customize.py", title="Customize", icon="🛃")
Videos = st.Page(page="pages/Videos.py", title="Videos", icon="🎬")
New_Notebook = st.Page(page="pages/New_Notebook.py", title="New notebook", icon="➕")

pg = st.navigation(
    [New_Chat, Library, Images, Scheduled, Customize, Videos, New_Notebook],
    position="hidden",
)

with st.sidebar:
    st.title("Gemini")
    st.button("Search", icon="🔍")

    st.page_link(New_Chat)
    st.page_link(Library)
    st.page_link(Images)
    st.page_link(Scheduled)
    st.page_link(Customize)
    st.page_link(Videos)

    st.caption("Notebooks")
    st.page_link(New_Notebook)

    st.button("Settings", icon="⚙️")

pg.run()
