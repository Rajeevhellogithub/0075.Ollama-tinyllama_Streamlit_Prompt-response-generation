# Please note that before running codes:
# First open ollama application on windows: start - ollama
# In cmd check the model 'tinyllama' is installed or downloaded- C:\Users\RAJEEV>ollama list
# E:\PYTHONCLASSTF>.\tensorflowvenv\Scripts\activate
# (tensorflowvenv) E:\PYTHONCLASSTF>cd PrakashSenapati\2024_12_26_Llama_Ollama\Chatbot_with_Llama_Streamlit
# streamlit run code_self.py


from langchain_ollama import OllamaLLM
import streamlit as st

llm = OllamaLLM(model="tinyllama")

st.title("Chatbot using Tinyllama")

prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            st.write(llm.stream(prompt, stop=['<|eot_id|>']))