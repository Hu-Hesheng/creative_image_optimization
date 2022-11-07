import streamlit as st
import pandas as pd
import os
import sys


def app():

    st.title("Features Analysis")

    df_cleaned = pd.read_csv('data/cleaned_df.csv')
    

    st.header("Object populations")
    st.subheader("most objects in an asset")
    st.bar_chart(df_cleaned['all_objects_count'])

    st.header("Object populations")
    st.subheader("most objects in an asset")
    st.heat_map(df_cleaned['all_objects_count'])

    

    st.header("Feature Importance")
    st.image('data/feature.png')