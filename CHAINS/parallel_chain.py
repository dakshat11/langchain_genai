from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()

model2 = ChatOpenAI()

prompt1 = PromptTemplate(
    template= "generate short and simple notes from the following text \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template= "generate 5 short question answer from the following text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template= 'merge the provided notes and quiz into a single document \n notes -> {notes}, quiz -> {quiz}',
    input_variables=['notes', 'quiz' ]
)

parser = StrOutputParser()


# first we will be developing parallel chain then the merging chain

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """In machine learning, support vector machines (SVMs, also support vector networks[1]) are supervised max-margin models with associated learning algorithms that analyze data for classification and regression analysis. Developed at AT&T Bell Laboratories,[1][2] SVMs are one of the most studied models, being based on statistical learning frameworks of VC theory proposed by Vapnik (1982, 1995) and Chervonenkis (1974).

In addition to performing linear classification, SVMs can efficiently perform non-linear classification using the kernel trick, representing the data only through a set of pairwise similarity comparisons between the original data points using a kernel function, which transforms them into coordinates in a higher-dimensional feature space. Thus, SVMs use the kernel trick to implicitly map their inputs into high-dimensional feature spaces, where linear classification can be performed.[3] Being max-margin models, SVMs are resilient to noisy data (e.g., misclassified examples). SVMs can also be used for regression tasks, where the objective becomes 
ϵ
{\displaystyle \epsilon }-sensitive."""

result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()