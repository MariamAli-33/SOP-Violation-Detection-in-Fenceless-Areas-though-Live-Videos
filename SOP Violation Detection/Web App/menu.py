import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit.components.v1 as components
import streamlit as st
import subprocess
import sys
# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
class Menu:
    def streamlit_menu(self,example):
        if example == 2:
            # st.title("DETEXIVE")
            st.markdown("""
                <style>
                    .css-18e3th9 {
                            padding-top: 0rem;
                            padding-bottom: 0rem;
                            padding-left: 5rem;
                            padding-right: 5rem;
                        }
                    .css-1d391kg {
                            padding-top: 0rem;
                            padding-right: 1rem;
                            padding-bottom: 0rem;
                            padding-left: 1rem;
                        }
                </style>
                """, unsafe_allow_html=True)
            hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
            st.markdown(hide_streamlit_style, unsafe_allow_html=True)
            col1,col2=st.columns((1,3))
            with col1:
                # st.subheader("Detexie", style)
                components.html("""
                <style>
                
                h1{
                    font-family: 'Cookie', cursive;
                    margin-top: -15px;
                    font-size: 50px;

                }
                </style>
                <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cookie&display=swap" rel="stylesheet"> 
                <h1>Detexive</h1>
                """)
            
            with col2:
                selected = option_menu(
                    menu_title=None,  # required
                    options=["Home", "Services","News","Tools", "Contact","Detect"],  # required
                    icons=["house", "bi bi-aspect-ratio-fill","bi bi-book-half", "bi bi-stack","bi bi-telephone-fill", "bi bi-webcam-fill"],  # optional
                    menu_icon="cast",  # optional
                    default_index=0,  # optional
                    orientation="horizontal",
                    styles={
                    "container": {"padding": "0!important", "background-color": "#fafafa",},
                    "icon": {"color": "black", "font-size": "10px"},
                    "nav-link": {
                        "font-size": "12px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#fff",
                    },
                    "nav-link-selected": {"background-color": "#2e4c7d","border":"2px solid #2e4c7d"}
            },
                )
        return selected



          
