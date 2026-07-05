from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

chatmodel = ChatGroq(
    model="qwen/qwen3-32b",
)

response = chatmodel.invoke("Who are you?")

print(response.content)