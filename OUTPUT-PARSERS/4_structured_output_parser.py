from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


load_dotenv()

model = ChatOpenAI()

schema = [
    ResponseSchema(name= "fact_1", description = "fact 1 about the topic"),
    ResponseSchema(name= "fact_2", description = "fact 2 about the topic"),
    ResponseSchema(name= "fact_3", description = "fact 3 about the topic")
]
# the diffrence is a structured schema is created first and then passed to the parser
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = "give 3 facts about {topic} \n  {format_instructions}",
    input_variables= ["topic"],
    partial_variables = {'format_instructions' : parser.get_format_instructions() }
)

prompt = template.invoke({"topic" : "black hole"})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)
