import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import json
import folium
from streamlit_folium import st_folium

st.title('연습문제2')

tab1, tab2, tab3 = st.tabs(['IRIS','KOR_NEWS','POPULATION'])

with tab1:
    # iris 데이터셋 로드
    iris = sns.load_dataset('iris')

    # iris 데이터셋을 데이터프레임으로 출력
    st.header('1. Iris 데이터셋')
    st.subheader("Iris 데이터셋 데이터프레임")
    st.dataframe(iris)

    st.divider()

    st.header('2. 품종 선택 후, 선택 품종 정보를 데이터프레임으로 출력')
    # 품종 선택
    choose_species = st.multiselect('품종을 선택해주세요',
                                    options=['setosa', 'versicolor', 'virginica'],
                                    placeholder='품종 선택'
                                    )

    # 선택 품종 데이터프레임으로 출력
    if choose_species:
        selected = iris[iris['species'].isin(choose_species)]
        st.subheader("선택한 품종 데이터")
        st.dataframe(selected)

    st.divider()

    st.header('3. radio 요소를 사용하여 컬럼 선택하고, 히스토그램 그리기')
    st.subheader('컬럼 선택')
    # 품종을 제외한 4가지 컬럼을 radio 요소를 사용하여 선택
    size = st.radio(
        "어떤 정보가 필요하세요?",
        ["꽃잎 길이", "꽃잎 너비", "꽃받침 길이", "꽃받침 너비"],
        captions=["Petal Length", "Petal Width", "Sepal Length", "Sepal Width"],
        horizontal=True)

    mapping = {
        "꽃잎 길이": "petal_length",
        "꽃잎 너비": "petal_width",
        "꽃받침 길이": "sepal_length",
        "꽃받침 너비": "sepal_width"
    }

    size2 = mapping[size]

    if size2:
        fig, ax = plt.subplots()
        ax.hist(iris[size2])
        ax.set_title('IRIS DATA')
        ax.set_xlabel(size2)
        st.pyplot(fig)


with tab2:
    st.header('kor_news 데이터셋')
    st.subheader('대분류 기준 해당 분야 주요 키워드 20위')

    st.divider()

    article = pd.read_excel('data/kor_news_240326.xlsx')

    article['분류리스트'] = article.분류.str.split('>')
    article['대분류'] = article['분류리스트'].str[0]
    main_category = [main for main in article['대분류'].unique()]

    def ranking(df, category):
        category_df = df[df['대분류'] == category]
        # 키워드 카운트
        keywords = []
        for title in category_df['제목']:
            keywords.extend(title.split())
        keyword_counts = pd.Series(keywords).value_counts()
        top20 = keyword_counts[:20]
        return top20

    choose_category = st.radio('카테고리를 선택하세요🔽',
                               main_category,
                               horizontal=True)

    top20 = ranking(article, choose_category)

    st.bar_chart(top20)

with tab3:
    st.header('3. 경기도 인구데이터')
    st.subheader('연도별 인구수에 대한 지도시각화: \n\n 2007년, 2015년, 2017년 연도를 탭으로 제시')

    with open('data/경기도행정구역경계.json', encoding='utf-8') as f:
        geo_gg = json.loads(f.read())

    df_gg = pd.read_excel('data/경기도인구데이터.xlsx', index_col='구분')

    tab1, tab2, tab3 = st.tabs(['2007년', '2015년', '2017년'])

    with tab1:
        map_2007 = folium.Map(location=[37.566, 126.9782], zoom_start=8)
        folium.GeoJson(geo_gg).add_to(map_2007)
        folium.Choropleth(geo_data=geo_gg,
                          data=df_gg[2007],
                          columns=[df_gg.index, df_gg[2007]],
                          key_on='feature.properties.name').add_to(map_2007)
        st_folium(map_2007, width=600, height=400, key=2007)

    with tab2:
        map_2015 = folium.Map(location=[37.566, 126.9782], zoom_start=8)
        folium.GeoJson(geo_gg).add_to(map_2015)
        folium.Choropleth(geo_data=geo_gg,
                          data=df_gg[2015],
                          columns=[df_gg.index, df_gg[2007]],
                          key_on='feature.properties.name').add_to(map_2015)
        st_folium(map_2015, width=600, height=400, key=2015)

    with tab3:
        map_2017 = folium.Map(location=[37.566, 126.9782], zoom_start=8)
        folium.GeoJson(geo_gg).add_to(map_2017)
        folium.Choropleth(geo_data=geo_gg,
                          data=df_gg[2017],
                          columns=[df_gg.index, df_gg[2007]],
                          key_on='feature.properties.name').add_to(map_2017)
        st_folium(map_2017, width=600, height=400, key=2017)