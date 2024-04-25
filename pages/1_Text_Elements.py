import streamlit as st

st.title('Streamlit 맛보기')
st.header('1. 텍스트요소', divider='rainbow')
st.subheader('텍스트요소를 작성하기 위한 API', divider=False)

st.write('Hello _stereamlit_')
st.write('''st.title()  
st.header()

st.subheader()
''')

st.subheader('1.2 텍스트 _본문_ 을 구성하는 :red[API]')

# emoji site
# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

st.write('''
- st.caption()  
- st.text()  
- st.code()  
- st.markdown()
- st.latex
''')

st.text('This is some text')
st.caption('This is a caption')

st.markdown('''한 줄 끝에 입력한 두 칸의 공백(space)는  
다음 줄로 사용(soft return)
            
한 행에 두 개 이상의 newline은 hard return이 됨
''')

sample_code = '''
def fun():
    print('Hello!!!')
'''
st.write(':blue[st.code]')
st.code(sample_code, language='python')

st.write('---')
st.write('[st.late]')
st.latex('b \over a')
st.latex('\sqrt{x^2 + y^2}')
st.divider()
st.write('Emoji : https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/')

st.divider()
with st.echo():
    st.write('This code will be printed')

st.divider()

def get_user_name():
    return 'John'

def get_punctuation():
    return '!!!'

greeting = 'Hi there,'
value = get_user_name()
punctuation = get_punctuation()

st.write(greeting, value, punctuation)