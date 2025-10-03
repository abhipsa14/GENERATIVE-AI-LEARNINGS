import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")
name=st.text_input("Enter your name","Type here ...")
if name:
    st.write(f"Hello, {name}")
age=st.slider("Select your age:",0,130,25)
st.write(f"Your age is {age}")
options = ["Python","Java","C++","JavaScript"]
choice=st.selectbox("Choose your favorite programming language:",options)
st.write(f"You selected:{choice}")

data={
    "Name":["Alice","Bob","Charlie","David"],
    "Age":[24,30,22,35],
    "City":["New York","Los Angeles","Chicago","Houston"]
}
df=pd.DataFrame(data)
st.write("Here is the DataFrame:")  
df.to_csv("data.csv",index=False)
st.dataframe(df)

uploaded_file=st.file_uploader("Upload a CSV file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)