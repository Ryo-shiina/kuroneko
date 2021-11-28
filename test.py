# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

st.title('あなたが飲みたいコーヒーは？')
st.write('私はコーヒーマスターです。あなたが好きなコーヒーを探し出します')

kaori = st.selectbox(
    'あなたが好きなコーヒーの香りは？',
    list(['――','甘い香り','芳しい香り','コーヒー飲めないです'])
    )
if kaori==('甘い香り'):
    sanmi = st.selectbox(
        'コーヒーの酸味は好きですか？',
        list(['――','好き','普通','嫌い'])
    )
    if sanmi==('好き'):
        st.write('グアテマラコーヒーをオススメします')
    if sanmi==('普通'):
        nigami = st.selectbox(
            'コーヒーの苦味の好みは？',
            list(['――','苦い方が好き','普通','柔らかめな苦味が好き'])
        )
        if nigami==('苦い方が好き'):
            st.write('ベトナムコーヒーをオススメします')
        if nigami==('普通'):
            st.write('グアテマラコーヒーをオススメします')
        if nigami==('柔らかめな苦味が好き'):
            st.write('ブルーマウンテンをオススメします')
    if sanmi==('嫌い'):
        nigami = st.selectbox(
            'コーヒーの苦味の好みは？',
            list(['――','苦い方が好き','普通','柔らかめな苦味が好き'])
        )
        if nigami==('苦い方が好き'):
            st.write('ケニアコーヒーをオススメします')
        if nigami==('普通'):
            st.write('カロシ・トラジャをオススメします')
        if nigami==('柔らかめな苦味が好き'):
            st.write('モカシダモG4をオススメします')
if kaori==('芳しい香り'):
    nigami = st.selectbox(
        'コーヒーの苦味の好みは？',
        list(['――','苦い方が好き','普通','柔らかめな苦味が好き'])
    )
    if nigami==('苦い方が好き'):
        st.write('ゴールデンマンデリンをオススメします')
    if nigami==('普通'):
        st.write('カロシ・トラジャをオススメします')
    if nigami==('柔らかめな苦味が好き'):
        st.write('ドミニカバラオナをオススメします')
if kaori==('コーヒー飲めないです'):
    if st.button('そんなあなたに'):
        st.title('Monster Energy')
        st.write('良いモンエナライフを！！')
   


    

    
