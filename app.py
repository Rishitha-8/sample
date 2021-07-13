# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 09:00:15 2021

@author: NiruSai
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 

st.set_page_config(page_title='welcome')
st.header('hello')
st.subheader('world')

volume = st.text_input("volume","Type Here")
Open = st.text_input("open","Type Here")
High = st.text_input("high","Type Here")
Low = st.text_input("low","Type Here")
