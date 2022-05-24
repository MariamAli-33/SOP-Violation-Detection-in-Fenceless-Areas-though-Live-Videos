
# Import necessary libraries 
import streamlit as st
from PIL import Image
class MultiPage: 
    def __init__(self) -> None:
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.pages = []
    
    def add_page(self, title, func) -> None: 

        self.pages.append(
            {
                "title": title, 
                "function": func
            }
        )

    def run(self):
        # Drodown to select the page to run
        
        st.sidebar.header("Select Activity")
        
        page = st.sidebar.selectbox(
            'Navigate App', 
            self.pages, 
            format_func=lambda page: page['title']
        )

        # run the app function 
        page['function']()
        
        # with st.sidebar:
        #     container = st.container()
        #     with container:
        #         st.write("eee")
        # with st.sidebar.container():
        #     col1,col2,col3=st.columns(1)
        #     with col1:
        #         st.text("")
        #     with col2:
        #         st.text("")
        #     with col2:
        #         image = Image.open('image.jpg')
        #         st.image(image, width= 100,use_column_width=True) 

        
        #  st.markdown("""
        #         <style>
        #             .css-18e3th9 {
        #                     padding-top: 3rem;
        #                     padding-bottom: 0rem;
        #                     padding-left: 5rem;
        #                     padding-right: 5rem;
        #                 }
        #             .css-1d391kg {
        #                     padding-top: 5rem;
        #                     padding-right: 1rem;
        #                     padding-bottom: 3.5rem;
        #                     padding-left: 1rem;
        #                 }
        #         </style>
        #         """, unsafe_allow_html=True)
        # hide_streamlit_style = """
        #         <style>
        #         #MainMenu {visibility: hidden;}
        #         footer {visibility: hidden;}
        #         </style>
        #         """
        # st.markdown(hide_streamlit_style, unsafe_allow_html=True) 