import pandas as pd
import numpy as np
import time
import streamlit as st

st.header('Data Column Config')
st.subheader('1. Column')
df = pd.DataFrame(
    [{'command': 'st.write', 'rating': 4, 'is_widget': False},
     {'command': 'st.dataframe', 'rating': 5, 'is_widget': True},
     {'command': 'st.time_input', 'rating': 3, 'is_widget': True},
     {'command': 'st.metric', 'rating': 4, 'is_widget': True}]
)

st.dataframe(df)
st.markdown('column_config(label=, help=, width=)')
st.dataframe(df,
             column_config={
                 'command' : st.column_config.Column(
                     label='Streamlit Command',
                     help='Streamlit **widget** commands',
                     width='medium'
                 )
             })

st.markdown('column_config(label=, help=, width=, disabled=)')
st.dataframe(df,
             column_config={
                 'command' : st.column_config.Column(
                     label='Streamlit Command',
                     help='Streamlit **widget** commands',
                     width='medium',
                     disabled=True,
                 )
             })

st.header('2. Text Column')
st.dataframe(df)
st.markdown('text_column(default=)')
st.data_editor(df,
               column_config={
                   'command': st.column_config.TextColumn(
                       label='Streamlit Commands',
                       help='Streamlit **widget** commands',
                       default='st.',
                   )
               },
               num_rows='dynamic'
               )

st.markdown('text_column(validate=)')
st.data_editor(df,
               column_config={
                   'command': st.column_config.TextColumn(
                       label='Streamlit Commands',
                       help='Streamlit **widget** commands',
                       default='st.',
                       max_chars=20,
                       validate='^st.\.[a-z]+$'
                   )
               },
               num_rows='dynamic'
               )

st.subheader('3. Number Column')
st.data_editor(df,
               column_config={
                   'rating':st.column_config.NumberColumn(
                       label='좋아요',
                       help='한 달 동안 좋아요 수',
                       min_value=0,
                       max_value=10,
                       step=0.5,
                       format='%f'
                   )
               })

st.subheader('4. Checkbox Column')
st.data_editor(df,
               column_config={
                   'is_widget':st.column_config.CheckboxColumn(
                       label='위젯인가?',
                       default=False,
                   ),
                    'command': st.column_config.TextColumn(
                       label='Streamlit Commands',
                       help='Streamlit **widget** commands',
                       default='st.',
                       max_chars=20,
                       validate='^st.\.[a-z]+$'
                   )
               },
               num_rows='dynamic')

st.subheader('5. Selectbox Column')
df2 = pd.DataFrame(
    {
        "category": [
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "📊 Data Exploration",
        ],
    }
)

st.data_editor(df2)

st.data_editor(
    df2,
    column_config={
        "category": st.column_config.SelectboxColumn(
            label="App Category",
            help="The category of the app",
            width="medium",
            options=[
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            ],
            required=True,
        )
    },
    hide_index=True,
)

from datetime import datetime, date, time

st.subheader('6. Datetime Column')
df3 = pd.DataFrame(
    {'meeting_date':
     [datetime(year=2024, month=2, day=5, hour=12, minute=30),
      datetime(year=2024, month=2, day=5, hour=12, minute=30),
      datetime(year=2024, month=2, day=5, hour=12, minute=30),
      datetime(year=2024, month=2, day=5, hour=12, minute=30),
      datetime(year=2024, month=2, day=5, hour=12, minute=30)
      ]}
)

st.data_editor(df3,
               column_config={
                   'meeting_date': st.column_config.DatetimeColumn(
                       min_value=datetime(year=2024, month=1, day=1),
                       max_value=datetime(year=2024, month=4, day=10),
                       format='D MMM YYYY, h:mm a'
                   )
               })

st.subheader('7. Date Column')
df4 = pd.DataFrame(
    {'meeting_date':
     [datetime(year=2024, month=2, day=5),
      datetime(year=2024, month=2, day=5),
      datetime(year=2024, month=2, day=5),
      datetime(year=2024, month=2, day=5),
      datetime(year=2024, month=2, day=5)
      ]}
)
st.dataframe(df4)
st.data_editor(df4,
               column_config={
                   'meeting_date' : st.column_config.DatetimeColumn(
                       min_value=date(year=2023, month=1, day=1),
                       max_value=date(year=2025, month=12, day=31),
                       format='YYYY/MM/DD'
                   )
               }
               )

st.subheader('8. Time Column')
df5 = pd.DataFrame(
    {'meeting_date':
     [time(hour=12, minute=30),
      time(hour=2, minute=30),
      time(hour=10, minute=00),
      time(hour=11, minute=00),
      time(hour=10, minute=30)
     ]}
)

st.data_editor(df5,
               column_config={
                   'meeting_time' : st.column_config.TimeColumn(
                       min_value=time(hour=9, minute=0, second=0),
                       max_value=time(hour=18, minute=0, second=0),
                       format='hh:mm a'
                   )
               })

st.subheader('9. List Column')
df6 = pd.DataFrame(
    {
        'score' : [[0,4,60,80,100],
                   [80,30,80,50,70],
                   [90,30,60,80,100]
        ],
    }
)

st.dataframe(df6)
st.dataframe(df6,
             column_config={
                 'score' : st.column_config.ListColumn(
                     width='medium'
                 )
             })
st.table(df6)

st.subheader('10. Link Column')
df7 = pd.DataFrame(
    {
        'site' : ['naver', 'daum', 'google'],
        'url' : ['https://www.naver.com',
                 'https://www.daum.net',
                 'https://www.google.com']
    }
)

st.data_editor(df7,
             column_config={
                 'url' : st.column_config.LinkColumn(
                     help='Search portal site!',
                     max_chars=100,
                     validate='^https://www\.[a-z]+[a-z]+',
                     display_text='Search site'
                 )
             })

df6 = pd.DataFrame(
    {
        'score' : [[0,4,60,80,100],
                   [80,30,80,50,70],
                   [90,30,60,80,100]
        ],
        'score2' : [[0,4,60,80,100],
                   [80,30,80,50,70],
                   [90,30,60,80,100]
        ],
        'score3' : [[0,4,60,80,100],
                   [80,30,80,50,70],
                   [90,30,60,80,100]
        ]
    }
)

st.dataframe(df,
             column_config={
                 'score2': st.column_config.LineChartColumn(
                     y_min=0, y_max=100
                 ),
                 'score3': st.column_config.AreaChartColumn(
                     y_min=0, y_max=100
                 ),
                 'score': st.column_config.BarChartColumn(
                     y_min=0, y_max=100
                 )
             })

st.subheader('12. Image Column')
df9 = pd.DataFrame({
    'image':[
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
        ],
    'png_image':[
        'img/apple.png',
        'img/banana.png',
        'img/mango.png',
        'img/Fubao.png',
    ]
    }
)

st.dataframe(df9,
             column_config={
                 'image': st.column_config.ImageColumn(),
                 'png_image': st.column_config.ImageColumn()
             })

st.subheader('13. Progress Column')
df10 = pd.DataFrame({'sales': [100, 50, 60, 70]})

st.data_editor(df10,
               column_config={
                   'sales': st.column_config.ProgressColumn(
                       min_value=0, max_value=150,
                       format='%f원'
                   )
               })