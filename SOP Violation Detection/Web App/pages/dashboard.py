from turtle import width
from matplotlib import container
import streamlit as st
with open('pages/dashboard.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
import numpy as np
import pandas as pd
from pages import utils
import os
import time
import plotly.figure_factory as ff
from PIL import Image
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
def app():
  st.title("SOP VIOLATION DETECTION")
  st.write("The Intelligent System based on Deep Learning and Computer Vision techniques has eased the manual effort of realization of SOPs i.e., Face Masking and Social Distancing. The application is developed using famous detection tools and technologies Python, YOLO, OpenCV, and Streamlit. The developers have trained the model using a personalized dataset that was collected from various regions of Pakistan. The application shows efficient results in less favorable environments i.e., processes low-resolution CCTV footage of different public places. ")
  st.markdown("---")
  st.subheader("Applications")
  components.html("""
  	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<div class="card-deck">
  <div class="card text-white bg-info">
    <div class="card-body">
      <h5 class="card-title">Detection of Face Mask</h5>
      <p class="card-text">The system is enabled to detect the wearing of Face Mask with mAP (mean Average Precision) of 87% on images, videos, and Live Stream.</p>
    </div>
  </div>
  <div class="card text-white bg-secondary">
    <div class="card-body">
      <h5 class="card-title">Detection of Social Distancing</h5>
      <p class="card-text">Based on the pre-trained model of the Yolov4 system ensures the abiding of safe distance between two persons in a public place. </p>
    </div>
  </div>
  <div class="card text-white bg-success">
    <div class="card-body">
      <h5 class="card-title">Applicable Areas</h5>
      <p class="card-text">Medical Units like child nurseries, Operation theaters, ICUs, and wards for patients with chronic respiratory problems.
<br>Public places for COVID-19 SOPs
<br>Chemical Industries.
<br>Medical Research Laboratories. 
</p>
    </div>
  </div>
</div>
  """, height=270, )
  st.subheader("Privacy")
  components.html("""
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <div class="list-group">
  <a  class="list-group-item list-group-item-action flex-column align-items-start rounded border-info bg-light">
    <p class="mb-1">The data collected for training purposes to improve the algorithm’s accuracy has been obtained after the consent of a panel of representatives and whose record is saved with the company in hard form </p>
  </a>
  <a  class="list-group-item list-group-item-action flex-column align-items-start rounded border-success bg-light">
    <p class="mb-1">The system uses personal information of individuals like physical appearance to identify faces, objects,and movements. No data is being stored on backend servers for unauthorized use.</p>
    
  </a>
  <a class="list-group-item list-group-item-action flex-column align-items-start rounded border-primary bg-light">
    <p class="mb-1">The application is designed as an initial version for a highly efficient intelligent system that can be customized based on the needs and requirements of the client. The system will not be used by any third party for identification purposes.</p>
  </a>
  </a>
  <a class="list-group-item list-group-item-action flex-column align-items-start rounded border-secondary bg-light">
    <p class="mb-1">Appropriate tools and technologies such as Python, OpenCV, YOLO and Streamlit were selected for development after performing extensive research to address the problem effectively.</p>
  </a>
</div>

  """, height=350)



