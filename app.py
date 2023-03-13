import streamlit as st

with st.container():
    st.markdown("<h1 style='text-align: center; color: black;'>Who\'s this ?</h1>", unsafe_allow_html=True)

with st.container():
    st.empty()

with st.container():
    st.empty()
with st.container():
    st.empty()
with st.container():
    st.empty()

audio = st.file_uploader('**Please upload an audio file** (.wav) :notes:',type=['wav'],
                accept_multiple_files=False,)

if audio:
    st.audio(audio)
