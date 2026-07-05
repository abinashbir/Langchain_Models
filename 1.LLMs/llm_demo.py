from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatmodel = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

response = chatmodel.invoke("What are you?")
print(response.content)