import streamlit as st
import pandas as pd
import os
import sys
import sklearn


def app():

    st.title("Features Analysis")

    df_cleaned = pd.read_csv('data/cleaned_df.csv')
    

    st.header("Object populations")
    st.subheader("most objects in an asset")
    st.line_chart(df_cleaned['all_objects_count'])


    st.header("Creatives with the widest CTA buttons")
    st.subheader("Wide CTAs")
    st.bar_chart(df_cleaned['cta_width'])
    

    st.header("Feature Importance")
    st.image('data/CTR_dist.png')

    st.header("Feature Importance")
    st.image('data/feature.png')