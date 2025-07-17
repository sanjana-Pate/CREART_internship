# app.py

import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyC7w0XO41rZ-pNG4OT1ytJncVl4N-RHM54")  

model = genai.GenerativeModel("models/gemini-1.5-flash")

def get_study_material(topic):
    prompt = f"Explain the topic '{topic}' for students with examples."
    return model.generate_content(prompt).text

def get_quiz(topic):
    prompt = f"Create a 5-question multiple-choice quiz on the topic '{topic}'. Include correct answers."
    return model.generate_content(prompt).text

def get_summary(topic):
    prompt = f"Summarize the topic '{topic}' in simple student-friendly language."
    return model.generate_content(prompt).text

st.set_page_config(page_title="EduBot - AI Study Assistant", layout="centered")
st.title("EduBot - AI Study Assistant 📚🤖")
st.write("Enter a topic and choose what you'd like to generate:")

# Input
topic = st.text_input("Enter the topic")
choice = st.radio("Choose an option:", ("Study Material", "Quiz", "Summary"))

if st.button("Generate"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating content..."):
            if choice == "Study Material":
                result = get_study_material(topic)
            elif choice == "Quiz":
                result = get_quiz(topic)
            else:
                result = get_summary(topic)

            st.markdown("### ✨ Result:")
            st.write(result)
