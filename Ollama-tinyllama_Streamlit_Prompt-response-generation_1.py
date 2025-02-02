# (tensorflowvenv) E:\PYTHONCLASSTF
# cd PrakashSenapati\2024_12_26_Llama_Ollama\Chatbot_with_Llama_Streamlit
# streamlit run app_corrected_self.py

import streamlit as st
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

# Initialize the Ollama model
model = Ollama(model="tinyllama")

# Define a simple prompt template
prompt_template = PromptTemplate(
    input_variables=["input_text"],
    template="You are a helpful assistant. Respond to the following input: {input_text}"
)

# Streamlit application layout
st.title("Ollama tinyllama Model with LangChain")
st.write("Enter your text below and get a response from the model.")

# Text input for user
user_input = st.text_area("Input Text", "")

if st.button("Get Response"):
    if user_input:
        # Create the prompt
        prompt = prompt_template.format(input_text=user_input)
        
        # Get the response from the model
        response = model(prompt)
        
        # Display the response
        st.write("Model Response:")
        st.write(response)
    else:
        st.warning("Please enter some text to get a response.")
