from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnableLambda, RunnablePassthrough

load_dotenv()

prompt = PromptTemplate(
    template= "generate a joke about the topic \n {topic}",
    input_variables= ['topic']
)


model= ChatOpenAI()
parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model , parser)

def word_count(text):
    return len(text.split())

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(word_count)
    
})

final_chain = RunnableSequence( joke_gen_chain, parallel_chain)
result = final_chain.invoke({'topic': ' cricket'})

print(result)