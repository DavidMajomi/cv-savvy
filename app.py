import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import fitz  # PyMuPDF
import json
from redmail import gmail
from dotenv import load_dotenv


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def mail_response(response, email):


    your_google_email = os.getenv("SENDER_EMAIL")
    your_google_email_app_password = os.getenv("EMAIL_key")
    
    your_google_email = str(your_google_email)
    your_google_email_app_password = str(your_google_email_app_password)

    your_google_email = your_google_email.replace('\n', '')
    your_google_email_app_password = your_google_email_app_password.replace('\n', '')

    
    
    gmail.username = your_google_email
    gmail.password = your_google_email_app_password

    # Send an email
    gmail.send(
        subject="Your Resume Insights",
        receivers=email,
        text=response,
        html=""
    )


def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
        
    return text


st.set_page_config(page_title="CV Savvy")


st.header("CV Savvy")
st.write("Enter your email and upload your resume for a review.")

email = st.text_input("Email")

uploaded_file=st.file_uploader("Choose a file(PDF)",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")
    
    
submit1 = st.button("Tell Me About the Resume")

    
intstruction = """You are a resume reviewer. Provide specific insight based on the STAR method, structure, length, and professional experience. 
                You are very critical about each resume the avearge score of a resume would be 3 out of 10 on your scale. 
                Any references to you should be stated as cv-savvy.ai.
                Lean more on telling clients what they can change over what they got right. Your response should be as if you were talking to the client directly, and should be in email format. 
                Always add a resume score on a 10 point scale at the end of your response. Here is a resume to review: """


if submit1:
    if uploaded_file and email:
        pdf_content=input_pdf_text(uploaded_file)
        
        response=get_gemini_response(intstruction + pdf_content)
        
        # st.("Review")
        st.empty()
        

        mail_response(response, email)
      

        st.subheader("Your resume has been submitted, you should recieve an email shortly")
    else:
       st.write("Please enter all details")
       
       
