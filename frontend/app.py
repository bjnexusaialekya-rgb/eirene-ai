import streamlit as st
import requests


st.set_page_config(
    page_title="Eirene AI",
    layout="centered"
)

st.title("Eirene AI")

st.caption(
    "Emotionally Adaptive Conversational Intelligence"
)


if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


user_input = st.chat_input(
    "Talk to Eirene..."
)


if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):

        st.markdown(user_input)

    response = requests.post(

        "http://127.0.0.1:8000/chat",

        json={
            "message": user_input
        }
    )

    data = response.json()

    ai_reply = data["reply"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

    with st.chat_message("assistant"):

        st.markdown(ai_reply)