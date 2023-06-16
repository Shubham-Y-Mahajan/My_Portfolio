import streamlit as st

st.set_page_config(layout="wide")

col1,col2=st.columns(2)  #.columns(n) will create n column objects

with col1: #opens the column space
    st.image("images/photo.png")

with col2:
    st.title("Shubham Mahajan")
    content = """ Hello I am shubham mahajan creating a portfolio website"""
    st.info(content)