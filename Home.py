import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide",
)

st.write("# Welcome to the Real Estate Scraper App!")
st.write(
    """
    This app allows you to scrape real estate data from various websites. 
    You can choose the website you want to scrape from the sidebar.
    """
)
st.sidebar.success("Select a website to scrape from the sidebar.")