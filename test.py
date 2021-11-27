# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
from PIL import Image

st.title('あなたが飲みたいコーヒーは？')
st.write('私はコーヒーマスターです。あなたが好きなコーヒーを探し出します')

kaori = st.selectbox(
    'あなたが好きなコーヒーの香りは？',
    list(['甘い香り','芳しい香り'])
    )
sanmi = st.selectbox(
    'コーヒーに求める酸味はなんですか？',
    list(['爽やか','適度','華やか'])
    )
nigami = st.selectbox(
    'コーヒーの苦味の好みはなんですか？',
    list(['ソフトな苦み','強い苦み'])
    )

st.write('あなたが選択したのは', kaori,'で' ,sanmi ,'な', nigami,'のあるコーヒーです')

st.write('そんなコーヒーを探しているあなたに私がオススメするのは...')

if st.button('結果を表示'):
    img = Image.open('monster_Twitter_logo_400x400.jpg')
    st.image(img, caption='引用：Monster Energy Japan', 
             use_column_width=200)

    

    
