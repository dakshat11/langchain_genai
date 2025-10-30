from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX2F5QT?pd_rd_w=nV5xQ&content-id=amzn1.sym.a324903e-1f30-4243-bf0d-6da5ebc52115&pf_rd_p=a324903e-1f30-4243-bf0d-6da5ebc52115&pf_rd_r=JRQDSYQ25FDWPBMN66V9&pd_rd_wg=zPNQn&pd_rd_r=44207e88-d8c3-431d-adf7-e1f85af30be5&pd_rd_i=B0CHX2F5QT&ref_=pd_hp_d_btf_unk_B0CHX2F5QT&th=1'
loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))