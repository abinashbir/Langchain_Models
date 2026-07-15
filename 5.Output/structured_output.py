from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated
load_dotenv()

class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review, e.g. positive, negative, or neutral"]

chatmodel = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
structured_model = chatmodel.with_structured_output(Review)

query = input("Enter the review text : ")
result = structured_model.invoke(query)

print(result['summary'])
print(result['sentiment'])