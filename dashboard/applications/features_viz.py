import streamlit as st
import pandas as pd
import os
import sys



def app():

    st.title("Features Analysis")

    df_cleaned = pd.read_csv('data/cleaned_df.csv')
    

    st.header("Object populations")
    st.subheader("most objects in an asset")
    st.line_chart(df_cleaned['all_objects_count'])


    st.header("Creatives with the widest CTA buttons")
    st.subheader("Wide CTAs")
    st.bar_chart(df_cleaned['cta_width'])


    st.header("Logo to preview image ratio")
    st.subheader("logo ratio")
    st.bar_chart(df_cleaned['LAR'])


    

    st.header("Click through rate distribution")
    st.image('data/CTR_dist.png')

    st.header("Feature Importance")
    st.image('data/feature.png')


    st.header("Correlation matrix")
    st.image('data/download (2).png')

    st.header("Evaluation metrics")
    st.image('data/image (7).png')