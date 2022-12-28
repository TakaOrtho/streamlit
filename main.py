import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title("Streamlit intro")

st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('sample.png')
    st.image(img, caption='image showing', use_column_width=True)

option = st.selectbox(
    'what is your favorite number?',
    list(range(1,11))
)

'Your favorite number is ', option, '.'

text = st.text_input('What is your hobby?')
'Your hobby is ', text

condition = st.slider('What is your current condition?', 0 , 100, 50)
'Your current status is ', condition