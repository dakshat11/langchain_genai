from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-4-turbo")

result = model.invoke("best fort in maharashtra")

print(result)


# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI(model='gpt-3.5-turbo')

# result = model.invoke("what is the capital of USA")

# print(result.content)