# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:16:50 2023

@author: DELL
"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import time
path = 'test.xlsx'
st.set_page_config(page_title='Dashboard',
                   page_icon=':bar_chart:',
                   layout='wide')
@st.cache_data
def load(path):
    df = pd.read_excel(path)
    #df=df.style.background_gradient(axis=0)
    return df
df = load(path)
#df = pd.read_excel('test.xlsx' )
#print(df)
#a = df.columns



#st.dataframe(df)

#%%
st.sidebar.header('aaa')
tram = st.sidebar.multiselect(
    'Select trạm:', 
     options= df['TramNM'].unique()
     )
df_select = df.query("TramNM == @tram")
ngan = st.sidebar.multiselect(
     'Select ngăn:', 
      options= df_select['Ngan'].unique())
#%%
df_select = df.query("TramNM == @tram & Ngan == @ngan ")
df_select = df_select.reset_index(drop=True)
st.dataframe(df_select)
#%%
st.title(":bar_chart: Sales")
st.markdown("##")
backgroundColor = "#00172B"
#%%
left,mid,right = st.columns(3)
with left:
    st.subheader("left")
    linechart = df_select.loc[0, ['0 H', '1 H', '2 H', '3 H', '4 H', '5 H', '6 H', '7 H', '8 H', '9 H', '10 H', '11 H', '12 H', '13 H', '14 H', '15 H', '16 H', '17 H', '18 H', '19 H', '20 H', '21 H', '22 H', '23 H']]
    fig = px.line(linechart,height=500,width=1000,template='gridon')
    st.plotly_chart(fig,use_container_width=True)
with mid:
    st.subheader("mid")
with right:
    st.subheader("right")
 