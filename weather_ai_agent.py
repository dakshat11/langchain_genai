# app.py
import streamlit as st
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchResults  # example tool
from langchain_openai import ChatOpenAI
from langchain import hub
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# --- Streamlit Page Config ---
st.set_page_config(page_title="Weather AI Agent", page_icon="🌦️", layout="centered")

st.title("🌤️ Weather AI Agent")
st.markdown("Ask about the weather anywhere in the world — powered by LangChain ReAct Agent!")

# --- Initialize Agent ---
@st.cache_resource
def initialize_agent():
    # Use your preferred LLM
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    # Example: using DuckDuckGo search tool for weather lookup
    tools = [DuckDuckGoSearchResults(name="weather_search")]

    # Load a ReAct-style prompt from LangChain hub (you can customize it too)
    prompt = hub.pull("hwchase17/react")

    # Create the ReAct agent
    agent = create_react_agent(llm, tools, prompt)

    # Create the agent executor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor

agent_executor = initialize_agent()

# --- User Input ---
query = st.text_input("🌍 Your weather question:", placeholder="e.g., What's the weather in Goa right now?")

if st.button("Get Weather"):
    if query.strip():
        with st.spinner("Thinking..."):
            try:
                response = agent_executor.invoke({"input": query})
                st.success(response["output"])
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("Please type a question.")

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ using LangChain + Streamlit (ReAct Agent)")
