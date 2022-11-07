import os
import sys
import streamlit as st

sys.path.insert(0, './dashboard')

from multiapp import MultiApp
from applications import model, features_viz

st.set_page_config(page_title="Feature Visualization", layout="wide")

app = MultiApp()

st.sidebar.markdown("""
# features
""")

# Add all your application here
app.add_app("features_vizualization", features_viz.app)
app.add_app("Model", model.app) 

# The main app
app.run()