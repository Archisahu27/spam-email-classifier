# app.py

import streamlit as st
from predict import predict_spam

# Page title
st.title("📩 Spam Email Classifier")

st.write("Enter a message to check whether it is Spam or Not Spam")

# Input box
user_input = st.text_area("Enter your message:")

# Button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message")
    else:
        result = predict_spam(user_input)

        if result == "spam":
            st.error("🚫 This is SPAM")
        else:
            st.success("✅ This is NOT SPAM")