import streamlit as st

st.header('Expander')
st.bar_chart({'data':[10,30,15,25,20]})

with st.expander('참고 설명'): #('참고 설명', expanded=True) 이렇게 적으면 탭이 열려있는 게 기본값
    st.write('''위 차트는 점심식사 선호도를 조사한 결과로서, ...''')
    st.image('https://static.streamlit.io/examples/owl.jpg')

expander = st.expander('expander 사용 시 주의점')
expander.write('expander 내에 다른 expander를 둘 수 없다')