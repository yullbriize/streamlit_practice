import pandas as pd
import numpy as np
import streamlit as st

st.title('Data elements 둘러보기')
st.header('1. Dataframe', divider=True)

df = pd.DataFrame({'Col1' : [1, 2, 3, 4],
                   'Col2' : [10, 20, 30, 40]})

st.write(df)

st.dataframe(df)
with st.echo():
    st.dataframe(df, use_container_width=True)

df1 = pd.DataFrame(
    np.random.randn(5, 10),
    columns=['col_%d'% (i+1) for i in range(10)]
)
st.dataframe(df1)
st.dataframe(df1, width=400, height=150)
st.dataframe(df1, width=400, height=150, use_container_width=True)

st.dataframe(df, column_order=('Col2', 'Col1'))

st.dataframe(df1.style.highlight_max(axis=0))
st.dataframe(df1.style.highlight_max(axis=1))

st.dataframe(df1.style.highlight_min(axis=0))
st.dataframe(df1.style.highlight_min(axis=1))

st.divider()

df2 = pd.DataFrame(
    [{'command': 'st.write', 'rating': 4, 'is_widget': False},
     {'command': 'st.dataframe', 'rating': 5, 'is_widget': True},
     {'command': 'st.time_input', 'rating': 3, 'is_widget': True},
     {'command': 'st.metric', 'rating': 4, 'is_widget': True}]
)
st.write(df2)
st.dataframe(df2, use_container_width=True)

df3 = pd.read_excel('data/kor_news_240326.xlsx')
df3_part = df3.iloc[:100]
st.dataframe(df3_part, hide_index=True)

st.subheader('add_rows()')
df3_part1 = df3.iloc[:10]
df3_part2 = df3.iloc[20:30]

out_df = st.dataframe(df3_part1)
out_df.add_rows(df3_part2)

st.header('2. data editor')
edited_df = st.data_editor(df2)
fav_com = edited_df.loc[edited_df['rating'].idxmax()]['command']
st.markdown(f'가장 높은 점수의 위젯은?  :red[{fav_com}] :+1:')

edited_df3 = st.data_editor(df3_part)

st.markdown('num_rows=True')
st.data_editor(df3_part1, num_rows='dynamic')

st.markdown('disabled=(col, ...')
st.data_editor(df2, disabled=['command', 'is_widget'])




st.header('3. table : st.table()')
st.table(df3_part.iloc[:3])

out_table = st.table(df3_part1)
out_table.add_rows(df3_part2)