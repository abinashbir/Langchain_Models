from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

chatmodel = ChatGroq(
    model="qwen/qwen3-32b",
)

st.header("Research Tool")

user_input=st.text_input("Enter your prompt")

if st.button('Summurise'):
    response = chatmodel.invoke(user_input)
    st.write(response.content)