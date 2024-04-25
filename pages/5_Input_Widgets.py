import streamlit as st

st.title('Input Widgets!')
st.header('1. Button Elements')
st.subheader('Button')
st.button('초기화', type='primary')
if st.button('안녕'):
    st.write('반가워 :smile:')
else:
    st.write('잘가! :raising_hand:')


st.subheader('Link Button')
st.link_button('google', 'http://www.google.com')


st.subheader('Page Link')
st.page_link('My_apps.py', label='Home', icon='🏠' )
st.page_link('pages/1_Text_Elements.py', label='Text_Elements')
st.page_link('pages/2_Data_Elements.py', label='Data_Elements')
st.page_link('pages/3_Data_Column_Configure.py', label='Data_Column_Elements')
st.page_link('pages/4_Chart_Elements.py', label='Chart_Elements')
st.page_link('pages/5_Input_Widgets.py', label='Input_Widget')
st.page_link('pages/6_Layout-Containers.py', label='Layout&Containers')
st.page_link('pages/강다율_streamlit_연습문제1.py', label='Exercise', disabled=True)
st.page_link('https://docs.streamlit.io/develop/api-reference', label='Streamlit Docs', icon='🌐')
st.page_link('https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/', label='Emoji', icon='😄')


st.subheader('Form Submit Button', divider=True)

with st.form(key='form1'):
    id = st.text_input('Id')
    pw = st.text_input('Password', type='password')
    submitted = st.form_submit_button()
    if submitted:
        st.write('id:', id, 'password:', pw)


form = st.form(key='form2')
title = form.text_input('제목')
contents = form.text_area(('질문 입력'))
submit = form.form_submit_button('작성')
if submit:
    st.write('제목 : ', title)

st.divider()


st.header('2. Selection Elements')
st.subheader('Checkbox')


agree = st.checkbox('찬성', value=True, label_visibility='visible') #label_visibility='collapsed'/'hidden'
if agree:
    st.write('GOOD!')


st.subheader('Toggle')
on = st.toggle('선택')
if on:
    st.write('on')


st.subheader('Radio')
fruit = st.radio(
    label='좋아하는 과일은?',
    options=['바나나:banana:','사과:apple:','멜론:melon:','딸기:strawberry:','망고:mango:'],
    captions=['웃어요','달콤해요','시원해요','상큼해요','즙이 많아요'],
    horizontal=True, # True=가로 나열, False=세로 나열
    index=2 # 기본 선택값
)
if fruit == '바나나':
    st.write('바나나를 선택했어요!:banana:')
else:
    st.write('바나나가 아니네:unamused:')


st.subheader('Selectbox')
fruit = st.selectbox('과일을 선택하세요',
                     ['바나나','사과','멜론','딸기','망고'],
                     index=None,
                     placeholder='과일을 골라주세요',
                     label_visibility='hidden' # '과일을 선택하세요' 문구 출력 여부
                     )
st.write(f'당신이 선택한 과일은!!!:drum_with_drumsticks::drum_with_drumsticks::drum_with_drumsticks:'
         f'\n\n {fruit}입니다!:yum:')

st.divider()

# Streamlit Sample
# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

st.divider()

st.subheader('Multiselect')
colours = st.multiselect('당신이 좋아하는 컬러는?:purple_heart:',
                         options=['red', 'green','orange','yellow','navy'],
                         default=['green','orange']
                         )
st.write('선택한 컬러는 ', colours)

st.subheader('Selectslider')
colours = st.select_slider('당신이 좋아하는 컬러는',
                    options=['red','green','orange','yellow',
                             'navy','violet','indigo','mint'],
                    value='navy')

colours_st, colours_end = st.select_slider('당신이 좋아하는 컬러는',
                        options=['red','green','orange','yellow',
                                 'navy', 'violet','indigo','mint'],
                        value=('navy', 'indigo'))

st.write('당신이 좋아하는 컬러는', colours_st, colours_end)


st.subheader('colour picker')
colour = st.color_picker('Pick A Colour', '#00f900')
st.write('The current colour is', colour)


st.header('3. Number Input Elements')
st.subheader('Number Input')

num = st.number_input('숫자입력')
st.write(num)

num = st.number_input('숫자입력',
                      min_value=-10,
                      max_value=10,
                      step=2)
st.write(f'현재숫자: {num}')

num = st.number_input('숫자입력',
                      min_value=-10.0,
                      max_value=10.0,
                      step=0.5,
                      format='%.2f')
st.write(f'현재숫자: {num:.2f}')


st.subheader('Slider')
age = st.slider('나이',
                min_value=0,
                max_value=100,
                value=20,
                step=2
                )
st.write(age)

scores = st.slider('점수대',
                min_value=0.0,
                max_value=100.0,
                value=(25.0, 50.0)
                )
st.write(scores)


st.header('4. Text Input Elements')
st.subheader('Text Input')

id = st.text_input('ID', value='Login ID')
pw = st.text_input('PASSWORD', placeholder='Login Password', type='password')
st.write(f'ID: {id} \n\n PASSWORD: {pw}')


st.subheader('Text Area')
text = st.text_area('질문을 입력하세요')
st.write(text)
st.write(f'총 문자 길이는 {len(text)} 입니다.')


st.header('5. Date&Time Input Elements')
st.subheader('Date Input')

from datetime import datetime, date, time, timedelta


date = st.date_input('일자 선택', value=date(year=2024, month=3, day=1),
                     min_value=date(year=2023, month=1, day=1),
                     max_value=date(year=2024, month=12, day=31),
                     format='DD.MM.YYYY')
st.write(date)

st.subheader('Time Input')
time = st.time_input('시간입력',
                     value=time(hour=6, minute=30),
                     step=timedelta(minutes=10)
                     )
st.write(time)
