import streamlit as st
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='shopDB',
    user='streamlit',
    password='1234'
)

if conn.is_connected():
    db_info=conn.get_server_info()
    st.write('server_version:', db_info)
# 여기까지하고 브라우저에서 잘 연결되었는지 확인하기
# 잘 연결되었다면 "server_version: 8.0.36" 이렇게 뜸

cur = conn.cursor()
cur.execute('select * from customer;')

# record = cur.fetchone()
# st.write('connected to DB: ', record)

records = cur.fetchall()
# st.write(records)

# @st.cache_data # 함수를 캐시로 저장하면 쉽게 가져올 수 있음
def make_df():
    cur.execute('select * from customer;')
    records = cur.fetchall()
    st.write(pd.DataFrame(records, # 여기까지만 하면 컬럼명이 생기지 않음. (숫자로 표기)
                        columns = ['id', 'name', 'phone', 'birth']))
                        # 컬럼을 명시해주어야 컬럼명으로 리스트 요소가 들어감
make_df()

with st.form(key='input_form'):
    id = st.number_input('고객번호', min_value=1)
    name = st.text_input('고객이름')
    phone = st.text_input('전화번호')
    birth = st.date_input('생년월일', format='YYYY-MM-DD', value=None)
    submitted = st.form_submit_button('입력')

if submitted:
    sql = 'insert into customer (customer_id, customer_name, phone, birthday) values (' \
        + str(id) + ', \"' + name + '\" , \"' + phone + '\" , \"' + str(birth) + '\");'
    cur.execute(sql)
    conn.commit()
    make_df()
