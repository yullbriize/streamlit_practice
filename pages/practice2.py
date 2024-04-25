import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from konlpy.tag import Okt
from collections import Counter
import json
import folium
from streamlit_folium import st_folium

# 2. kor_news 데이터셋을 이용
st.header('2. kor_news 데이터')
news = pd.read_excel('data/kor_news_240326.xlsx')
news_df = pd.DataFrame(news)

# 2-1) 분류의 대분류기준을 선택하면 해당 분야의 주요 키워드 20위에 대한 barchart표시
st.subheader('1.대분류를 선택하여 주요 키워드 20위에 대한 Barchart 표시')

news_df['대분류'] = news_df.분류.str.split('>').str[0]

news_list = [i for i in news_df['대분류'].unique()]

col3, col4 = st.columns([1,2])

with col3:
    news_options = st.radio('대분류를 선택하시오👇',news_list)
with col4:
    okt = Okt()
    def pick_tag_tokens(gobun_name, tag_name='Noun', word_len=1):
        temp_list = []
        for sentence in news_df.제목[news_df.대분류 == gobun_name]:
            s_list = okt.pos(sentence)
            for word, tag in s_list:
                if tag == tag_name and len(word) >= word_len:
                    temp_list.append(word)
        return temp_list


    def counter(pick):
        verb_cnt = Counter(pick)
        verb_df = pd.DataFrame(pd.Series(verb_cnt), columns=['freq'])
        sorted_verb_df = verb_df.sort_values(by='freq', ascending=False)
        return sorted_verb_df

    pick1 = pick_tag_tokens(news_options, tag_name='Noun', word_len=2)
    df2 = counter(pick1)
    df2 = df2.iloc[:20]
    st.bar_chart(df2)