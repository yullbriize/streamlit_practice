import streamlit as st
import numpy as np

st.title('Tab')

tab1, tab2, tab3 = st.tabs(['Cat','Dog','Owl'])

with tab1:
    st.subheader('CAT')
    st.image('https://static.streamlit.io/examples/cat.jpg',
             width=200)

with tab2:
    st.subheader('DOG')
    st.image('https://static.streamlit.io/examples/dog.jpg',
             width=200)

with tab3:
    st.subheader('OWL')
    st.image('https://static.streamlit.io/examples/owl.jpg',
             width=200)

data = np.random.randn(30,3)
tab1, tab2 = st.tabs(['data', 'chart'])
tab1.subheader('DataFrame')
tab1.write(data)

tab2.subheader('Area Chart')
tab2.area_chart(data)