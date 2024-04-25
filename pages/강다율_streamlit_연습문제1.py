import pandas as pd
import streamlit as st
from collections import Counter
import matplotlib.pyplot as plt

# 1. 데이터프레임
st.header('1. 뉴스데이터를 dataframe으로 표시하기')
st.subheader('뉴스 목록')

article = pd.read_excel('data/kor_news_240326.xlsx')

st.dataframe(article)

st.divider()

# 2. url 링크
st.header('2. 뉴스데이터의 url 컬럼을 실제 뉴스 기사 페이지로 이동하도록 적절한 column configuration 사용')
st.subheader('뉴스 목록 & 기사 연결')

st.data_editor(article,
               column_config={
                   'URL': st.column_config.LinkColumn(
                       help='기사 링크',
                       max_chars=100,
                       display_text='기사 본문 이동',
                   )
               })

st.divider()

# 3. BAR CHART
st.header('3. 분류 컬럼 중 대분류 컬럼에 대한 빈도를 bar chart로 그리기')
st.subheader('뉴스 카테고리 빈도')

article['분류리스트'] = article.분류.str.split('>')
article['대분류'] = article['분류리스트'].str[0]
article['중분류'] = article['분류리스트'].str[1]
article['소분류'] = article['분류리스트'].str[2]

df = pd.DataFrame(article.대분류.value_counts())
st.bar_chart(df)

st.divider()

# 4.
st.header('4. 제목 컬럼에 대하여 텍스트 전처리를 진행한 결과를 토대로'
          '경제, 사회 분야의 빈도가 많은 주요 키워드 20위를 bar chart로 그리기')
# st.subheader('주요 키워드 20위')

import re

pattern = re.compile(r'\b(?![\[\]])(\w{2,})\b')
def preprocess_head(head):
    words = pattern.findall(head)
    words = [word.lower() for word in words]
    return words

keywords = []
for title in article['제목']:
    keyword = preprocess_head(title)
    keywords.extend(keyword)

econ_keywords = [keyword for keyword in keywords if '경제' in keyword]
soc_keywords = [keyword for keyword in keywords if '사회' in keyword]

econ_keyword_counts = Counter(econ_keywords)
soc_keyword_counts = Counter(soc_keywords)

econ_keywords_20 = dict(sorted(econ_keyword_counts.items(), key=lambda x: x[1], reverse=True)[:20])
soc_keywords_20 = dict(sorted(soc_keyword_counts.items(), key=lambda x: x[1], reverse=True)[:20])

st.subheader('경제 분야 주요 키워드 TOP20')
st.bar_chart(econ_keywords_20, color='#ff0000')

st.divider()

st.subheader('사회 분야 주요 키워드 TOP20')
st.bar_chart(soc_keywords_20)

st.divider()

# 5.
# st.header('5. 경제, 사회 분야 주요 키워드 20위를 WordCloud로 그리기')
#
# from wordcloud import WordCloud
#
# econ_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(econ_keywords_20)
# soc_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(soc_keywords_20)
#
# econ_wc = plt.imshow(econ_wordcloud, interpolation='bilinear')
# soc_wc = plt.imshow(soc_wordcloud, interpolation='bilinear')
#
# st.pyplot(econ_wc)