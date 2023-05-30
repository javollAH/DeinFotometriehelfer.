# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:26:20 2023

@author: einew
"""

import streamlit as st
import pandas as pd

st.write("""
         *BMLD 2022 Informatik*
         # Streamlit Project
         *Mock-up*
         """)
         
# Cache the dataframe so it's only loaded once
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )

df = load_data()

st.write("""
         Table one
         """)

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=True)

st.write("""
         Table two
         """)

st.dataframe(df, use_container_width=True)
