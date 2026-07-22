from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatmodel = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

while True:
    question=input("Enter your query : ")
    response = chatmodel.invoke(question)
    print("AI : ",response.content)