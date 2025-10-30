from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model = "gpt-4-turbo")

st.header("Reasearch Tool")

paper_input = st.selectbox(" Select the research paper Name", ["Select ...", " Attention is all you need",
" BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
" GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select the explanation style", ["Beginner-Friendly", "Technical", "Code-oriented", 
                                            "Mathematical"])

length_input = st.selectbox("Select the length of explanation", ["Concise (3-5 lines)", "Detailed (10-15 lines)",
                                                                 "Extensive (15-20 lines)"])

template = load_prompt('template.json') 

# fill the template with user inputs


if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({"paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input})

    st.write(result.content)