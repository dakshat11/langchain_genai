from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions= 32)

docs = ["Delhi is the capital of india", "Paris is the capital of France", "Tokyo is the capital of Japan"]

result = embeddings.embed_documents(docs)

print(str(result))
