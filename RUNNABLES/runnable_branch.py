from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template= 'generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= 'summarize the given text \n {text}',
    input_variables= ['text']
)

report_gen_chain = RunnableSequence(prompt1, model, parser)

bracnh_chain = RunnableBranch(
    (lambda x: len(x.split()) > 200 , RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
) 

final_chain = RunnableSequence( report_gen_chain, bracnh_chain)

result = final_chain.invoke({'topic' : 'russia vs ukraine'})

print(result)

# final_chain.get_graph().print_ascii()