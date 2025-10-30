from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
load_dotenv()

model = ChatOpenAI()

template = PromptTemplate(
    template= "Write a 2 line jingle on {topic}",
    input_variables= ["topic"]
)

# template.save('template_0.json')

temp = load_prompt('template_0.json')

chain = temp | model

result = chain.invoke({"topic": "candy"})
print(result.content)
