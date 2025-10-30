from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

result = model.invoke('write a poem on cricket.')

# we will save the result to a text file
with open('poem.txt', 'w') as f:
    f.write(result.content)

print(result.content)