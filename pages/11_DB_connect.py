import streamlit as st

# mysql 연결(접속)
conn = st.connection('shopDB',
                     type='sql',
                     url='mysql://streamlit:1234@localhost:3306/shopDB') # mysql username, password

# 질의 수행
df = conn.query('select * from customer;', ttl=600)

st.write(df)

# for row in df.itertuples():
#     st.write(f'{row.customer_name}이 {row.phone}을 가짐')
#
# sql = '''insert into customer (customer_id, customer_name, phone, birthday) values
#  (:id, :name,:phone, :birth);'''
#
# with conn.session as s:
#     s.execute(sql, {'id':6, 'name':"홍길동", 'phone':"010-1111-1111", 'birht':"2000-01-30"})
#     s.commit()
#################################################




# df = conn.query('select * from customer;', ttl=600)
# st.write(df)