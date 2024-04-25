import streamlit as st
import time
with st.spinner('Wait for it...'):
    time.sleep(5)
st.balloons()
st.success('Done!')

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.button("Rerun")