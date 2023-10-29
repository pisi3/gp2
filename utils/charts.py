import plotly.express as px
import streamlit as st


def boxplot(df, x:str, y:str='', title: str='', p: str=''):
    if y == '':
        fig = px.box(df,x,title=title)
    else:
        fig = px.box(df,x,y,title=title)
    field = st.container()
    field.markdown(f'### {title}')
    field.plotly_chart(fig)
    field.markdown(p, unsafe_allow_html=True)