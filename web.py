import streamlit as st
from predict_page import predict_page
from visual_page import visual_page

if __name__ == '__main__':
    st.set_page_config(
        page_title="Developer's Salary Prediction",
        page_icon=":desktop_computer:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    page = st.sidebar.selectbox("Explore or Predict", ("Explore", "Predict"))

    if page == "Predict":
        predict_page()
    else:
        visual_page()
        