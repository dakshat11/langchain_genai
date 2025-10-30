from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatOpenAI()

parser = JsonOutputParser()
template1 = PromptTemplate(
    template= "Give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables= [],
    partial_variables= {'format_instruction' : parser.get_format_instructions()}
)

# prompt= template1.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)


# above three lines can be replaced with below line
chain = template1 | model | parser

result = chain.invoke({})

print(result)

