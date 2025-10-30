from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

loader = PyPDFLoader('pdf_file.pdf')

docs = loader.load()

print(docs[0].page_content)
