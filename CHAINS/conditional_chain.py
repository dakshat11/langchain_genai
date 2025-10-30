from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv()

# Initialize model
model = ChatOpenAI()

# Define the output schema for sentiment classification
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Give the sentiment of the feedback")

# Parser for structured output (sentiment)
parser = PydanticOutputParser(pydantic_object=Feedback)

# Prompt for classification
prompt = PromptTemplate(
    template="Classify the sentiment of the following text:\n{text}\n{format_instruction}",
    input_variables=["text"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

# Step 1: Sentiment classification chain
classifier_chain = prompt | model | parser

# Step 2: Define response prompts
prompt_positive = PromptTemplate(
    template="Write an appropriate response to this positive feedback:\n{feedback}",
    input_variables=["feedback"]
)

prompt_negative = PromptTemplate(
    template="Write an appropriate response to this negative feedback:\n{feedback}",
    input_variables=["feedback"]
)

# Simple string parser for final LLM output
text_parser = StrOutputParser()

# Step 3: Branching logic based on sentiment
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt_positive | model | text_parser),
    (lambda x: x.sentiment == "negative", prompt_negative | model | text_parser),
    RunnableLambda(lambda x: "No valid sentiment found.")
)

# Step 4: Combine both chains
chain = classifier_chain | branch_chain

# Step 5: Run the chain
result = chain.invoke({"text": "this is a bad phone"})

print(result)
