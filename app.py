import streamlit as st
import google.generativeai as genai
st.title("🏥 AI Health care ChatBOT With Google GenAI")
f= open("D:\AIchatbot\key\key.txt")
key = f.read()

genai.configure(api_key=key)
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              system_instruction= """ you are heplful healthcare ai  Assistant.
                              Given a healthcare  topic help user by guidence proper medication .if the question is 
                              not related to health care the replay should be ,'that is beyond my knowledge'.""")
if "chat_hostory" not in st.session_state:
    st.session_state["chat_history"] = []
chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)
user_prompt = st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"] = chat.history