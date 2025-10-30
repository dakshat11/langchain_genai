from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field



load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):
    name: str = Field(description= "Name of the person")
    age: int = Field(gt = 18, description="Age of the person")
    city: str = Field(description= "Name of the city the person belongs to")
    
parser = PydanticOutputParser(pydantic_object= Person)

template = PromptTemplate(
    template = "generate the name, age and city of a fictional {nationality} person \n {format_instruction}",
    input_variables= ['nationality'],
    partial_variables= {'format_instruction' : parser.get_format_instructions()}
)

# prompt = template.invoke({'nationality': 'indian'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = template | model | parser

result = chain.invoke({"nationality": 'indian'})

print(result)