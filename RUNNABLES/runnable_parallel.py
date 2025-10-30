from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template= "generate a tweet about the topic \n {topic}",
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template= 'generate a linkedin post about the topic \n {topic}',
    input_variables = ['topic']
)

model1= ChatOpenAI()
model2= ChatOpenAI() #for different task we use diffrent outputs, i only have one paid llm so using this

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence( prompt1, model1, parser),
    'linkedin' : RunnableSequence(prompt2, model2, parser)
})

parallel_chain.invoke({'topic': 'AI'})