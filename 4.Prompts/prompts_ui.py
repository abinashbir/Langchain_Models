from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
chatmodel = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
st.header("Research Tool")
user_input=st.text_input("Enter your prompt")
if st.button('Ask'):
    response = chatmodel.invoke(user_input)
    st.write(response.content)