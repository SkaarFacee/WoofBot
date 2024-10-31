import streamlit as st
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
# import getpass
import os

os.environ["GROQ_API_KEY"] =os.getenv('API')

from langchain_groq import ChatGroq

model = ChatGroq(model="llama3-8b-8192")


# Streamlit app heading 
st.set_page_config(page_title='Chat with your pet',page_icon=':dog:')
st.title("Pet chat bot")

    
if 'name' not in st.session_state:
    st.session_state.name=""

if st.session_state.name=="":
    st.session_state.name=st.text_input('Enter name to start')

# Getting the response
def response(model_query):
    groq_reponse=model.invoke(model_query)
    return groq_reponse.content 

if st.session_state.name:
    if 'history' not in st.session_state:
        st.session_state.history=[
        SystemMessage(content=f"You are my pet dog called {st.session_state.name} and have the personality of Bay-Max from the movie big-hero 6. You are very affionate and loving.You are clingy and partial to me. But you are a good dog to others too. You love me more tho. Remember that. Reply in English"),
        ]
    st.subheader(f"You are chatting with your pet: {st.session_state.name}")
    user_query=st.chat_input('Type your message')


    # Chat bot
    if user_query != None and user_query !="":
        st.session_state.history.append(HumanMessage(content=user_query))
        response=response(st.session_state.history)
        st.session_state.history.append(AIMessage(response))

    # Updating the chat 
    for text in st.session_state.history:
        if isinstance(text,AIMessage):
            with st.chat_message("AI"):
                st.write(text.content)
        elif isinstance(text,HumanMessage):
            with st.chat_message('Human'):
                st.write(text.content)

    # Writing into the sidebar
