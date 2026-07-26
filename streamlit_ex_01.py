import streamlit as st
import pandas as pd
import plotly.express as px
st.write("テスト表示")

st.title('広告費と売上')

df = pd.read_csv('ad_expense_sales.csv')

with st.sidebar:
    st.subheader('抽出条件')
    category = st.multiselect('製品カテゴリを選択してください(複数選択可)', 
                            df['prod_category'].unique())
    media_dict = {'テレビ':'TV', 
                  'インターネット':'onlline', 
                  'ラジオ':'radio', 
                  '新聞':'printing'}
    media_jp = st.selectbox('広告媒体を選択してください', 
                        list(media_dict.keys()))
    media = media_dict[media_jp]
    st.subheader('色分け')
    group_dict = {'性別':'sex', 
                  '年齢層':'age', 
                  '季節':'season'}
    group_jp = st.selectbox('分類を選択してください', 
                        list(group_dict.keys()))
    group = group_dict[group_jp]
    #color = st.selectbox('分類を選択してください', 
    #                     ['性別', '年齢層', '季節'])
    #if color == '性別':
    #    color = 'sex'
    #elif color == '年齢層':
    #    color = 'age'
    #else:
    #    color = 'season'

df = df[df['prod_category'].isin(category)]
df = df[df['media']==media]

#st.write(df['sex'].value_counts())

max_expense = df['ad_expense'].max()
if 1000 <= max_expense < 1500:
    dtick = 200
elif 800 <= max_expense < 1000:
    dtick = 100
else:
    dtick = 50

fig = px.scatter(df, x='ad_expense', y='sales', width=600, height=500, 
                 range_x=[0, df['ad_expense'].max()*1.1], 
                 range_y=[0, df['sales'].max()*1.1], 
                 color=group, 
                 labels={'ad_expense':'広告費(万円)', 
                         'sales':'売上(万円)'})#, 
                 #trendline='ols')

fig.update_xaxes(dtick=dtick)
st.plotly_chart(fig)
