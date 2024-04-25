import streamlit as st

with st.sidebar:
    st.radio('학년', ('1학년','2학년'))

choice = st.sidebar.selectbox('학년', ('1학년','2학년'))
st.write(choice)

with st.sidebar:
    st.page_link('pages/1_Text_Elements.py', label='Text')
    st.page_link('https://google.com', label='google')
    st.page_link('https://naver.com', label='naver')