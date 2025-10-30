# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# from dotenv import load_dotenv
# load_dotenv()
# llm = HuggingFaceEndpoint(
#     repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task = 'text-generation'
    
# )

# model = ChatHuggingFace(llm = llm)

# result = model.invoke("What is the capital of India")

# print(result.content)






# from langchain_huggingface import HuggingFaceEndpoint # Only need HuggingFaceEndpoint

# from dotenv import load_dotenv
# load_dotenv()

# # Use the HuggingFaceEndpoint directly as a standard LLM
# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task='text-generation'
# )

# # Use the standard 'invoke' method on the LLM, not the ChatModel
# # You pass the prompt string directly to the LLM.
# result = llm.invoke("What is the capital of India") 

# print(result) # The result from invoke on an LLM is the generated text (string)

# # OR, if you want a LangChain output object:
# # result_object = llm.invoke("What is the capital of India")
# # print(result_object)




from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()  # loads token if present in .env file
# or directly set here:
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your_token_here"

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=200,
    repetition_penalty=1.1
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")
print(result.content)
