from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('sample.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 10,
    separator= ' '
)

# text = """LangChain is a framework for developing applications powered by language models. It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more."""

result = splitter.split_documents(docs)

print(result[0].page_content)