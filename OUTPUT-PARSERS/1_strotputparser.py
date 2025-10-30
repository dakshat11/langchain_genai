from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.3",
    task = "text-generation",
)

model = ChatHuggingFace(llm = llm)

# 1st promp -> detailed report
template1 = PromptTemplate(
    template = " write a deatiled report on {topic}",
    input_variables= ['topic']
)

# 2nd prompt -> summary of the report
template2 = PromptTemplate(
    template = " write a five line summary on the following text. /n  {text}",
    input_variables= ['text']
)

prompt1 = template1.invoke({'topic': "black hole"})
result = model.invoke(prompt1)

promp2 = template2.invoke({'text': result.content})
result1 = model.invoke(promp2)

print(result1.content)




# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate

# load_dotenv()


# model = ChatOpenAI()


# # 1st promp -> detailed report
# template1 = PromptTemplate(
#     template = " write a deatiled report on {topic}",
#     input_variables= ['topic']
# )

# # 2nd prompt -> summary of the report
# template2 = PromptTemplate(
#     template = " write a five line summary on the following text. /n  {text}",
#     input_variables= ['text']
# )

# prompt1 = template1.invoke({'topic': 'black hole'})
# result = model.invoke(prompt1)

# promp2 = template2.invoke({'text': result.content})
# result1 = model.invoke(promp2)

# print(result1.content)

# # this code is without str ouput parser using