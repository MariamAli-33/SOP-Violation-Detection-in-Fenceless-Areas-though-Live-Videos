
import os
import streamlit as st
# st.set_page_config(layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage
from pages import redundant, face_mask_detection, social_distance, sop_both_violations


app = MultiPage()


col1, col2 = st.columns(2)

app.add_page("Dashboard",dashboard.app)
app.add_page("Face Mask Detection", face_mask_detection.main)
app.add_page("Social Distancing Detection",social_distance.main)
app.add_page("SOPs Detection (Both)", sop_both_violations.main)

# The main app
app.run()