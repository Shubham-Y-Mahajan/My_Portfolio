import streamlit as st
import pandas #pandas is used to read csv data
                # pandas gets already installed due to streamlit
st.set_page_config(layout="wide")

col1,col2=st.columns(2)  #.columns(n) will create n column objects

with col1: #opens the column space
    st.image("images/shubham.png")

with col2:
    st.title("Shubham Mahajan")
    content = """ Hello, I am Shubham Mahajan from Thane West (Maharashtra) a 2nd year BTech student of IIT Bhilai, 
    pursuing Computer Science and Engineering .
    \n I am proficient in Python programming, my skills include-\n 
    Django ,Django REST framework, Flask and streamlit for web development.\n
    PyQt6 , PySimpleGui - Desktop App development\n
    Basic Cloud Computing\n
    SQLite,MySQL- Database Management.\n
    Basic Machine Learning ,Natural Language processing and image processing(opencv)\n
    
    I have also worked on PHP projects.
    
    
     """
    st.info(content)

st.info("Below you can find some of the python projects I have worked on - " )

col3,empty_col, col4 =st.columns([1.5,0.5,1.5]) #if you provide a list it will the ratio
                                                # of column sizes


df=pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:6].iterrows(): #df[:10] on conisders first 10 rows
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"]) # images directory me hasi isliye add kiya
        #st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[6:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])  # images directory me hasi isliye add kiya
        #st.write(f"[Source Code]({row['url']})")