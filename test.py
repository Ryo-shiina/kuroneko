# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
from PIL import Image

st.title('あなたが飲みたいコーヒーは？')
st.write('私のコーヒーマスターです。あなたが好きなコーヒーを探し出します')
kaori = st.selectbox(
    'あなたが好きなコーヒーの香りは？',
    list(['甘い香り','芳しい香り'])
    )
sanmi = st.selectbox(
    'コーヒーの酸味は好きですか？')
st.write('あなたが選択したのは、 ',kaori,'です')




left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
img = Image.open('S__28573763.jpg')
st.image(img, caption='側転練習中の私です', use_column_width=True)    
    