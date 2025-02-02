# Ensure ollama application is running in background on windows and 'tinyllama' model is installed on C:\Users\RAJEEV\.ollama\models\blobs
# (tensorflowvenv) E:\PYTHONCLASSTF>cd PrakashSenapati\2024_12_26_Llama_Ollama\Llama_405b_with_Langchain
# streamlit run app_self.py

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st

# Set up the Streamlit interface
st.title("Langchain-Tinyllama App")

# Define the template for the model
template = """Question: {question}

Answer: Let's think step by step."""

# Create the prompt using Langchain's ChatPromptTemplate
prompt = ChatPromptTemplate.from_template(template)

# Initialize the OllamaLLM model with the correct version (ensure llama3.1 is supported)
model = OllamaLLM(model="tinyllama")
#model = OllamaLLM(model="llama3")


# Chain the prompt with the model
chain = prompt | model

# Streamlit chat input for user questions
question = st.chat_input("Enter your question here")
if question:
    # Pass the question to the LangChain-Ollama pipeline and display the response
    response = chain.invoke({"question": question})
    st.write(response)
