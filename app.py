import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

chatbot = pipeline("text-generation",model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "would you like to schedule appoinment with the Doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly.If you have concerns,consult your Doctor."
    else:
        response=chatbot(user_input,max_length=500,num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input =st.text_input("How can I help you?")
    if st.button("Submit"):
        if user_input:
            st.write("User :", user_input)
            with st.spinner("processing your query ,Please wait..."):
                response=healthcare_chatbot(user_input)
            st.write("Healthcare Assistant:",response)
            print(response)
        else:
            st.write("Please enter a message to get a response.")
    

if __name__=="__main__":
    main()