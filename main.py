import streamlit as st
import pandas #pandas is used to read csv data
                # pandas gets already installed due to streamlit
st.set_page_config(layout="wide")

col1,col2=st.columns(2)  #.columns(n) will create n column objects

with col1: #opens the column space
    st.image("images/coco_and_shubham.jpg")

with col2:
    st.title("Shubham Mahajan")
    content = """ Hello I am shubham mahajan creating a portfolio website"""
    st.info(content)

st.write("Below you can find some of the python apps i created " )

col3,empty_col, col4 =st.columns([1.5,0.5,1.5]) #if you provide a list it will the ratio
                                                # of column sizes


df=pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows(): #df[:10] on conisders first 10 rows
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"]) # images directory me hasi isliye add kiya
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])  # images directory me hasi isliye add kiya
        st.write(f"[Source Code]({row['url']})")