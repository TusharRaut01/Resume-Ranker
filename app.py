from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import io
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel("models/gemini-2.5-flash")
    respose=model.generate_content([input,pdf_content[0],prompt])
    return respose.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        
        # Convert to bytes
        img_byte_arr = io. BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [{
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() # encode to base64
            }]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


#streamlit App

st.set_page_config(page_title='ATS Resume expert')
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key='input')
uploaded_file=st.file_uploader('Upload your resume(pdf)...',type=['pdf'])

if uploaded_file is not None:
    st.write('pdf Uploaded Successfully')

submit1 = st.button('Tell Me About the Resume')

submit2 = st.button('Percentage match')

submit3 = st.button('Resume Issues')


input_prompt1 ="""
You are an experienced Technical HR Manager.
Review the resume against the job description and provide a concise, structured evaluation with:

1. **Overall Fit** — Yes/No with brief justification
2. **Strengths** — Relevant skills, experience, achievements
3. **Gaps/Weaknesses** — Missing skills, experience, or concerns
4. **Final Recommendation** — Short hiring suggestion
"""


input_prompt2 = """
You are an ATS (Applicant Tracking System) with expertise in data science roles.
Evaluate the resume against the job description and provide:

1. **Match Percentage** — numeric match score
2. **Missing Keywords** — list only relevant missing skills/terms
3. **Final Assessment** — brief summary of alignment

Keep the response concise and structured.
"""

input_prompt3 = """
You are a resume quality checker.
Identify:
1. Red flags (gaps, inconsistencies, vague points)
2. Formatting issues
3. Quick fixes (bullet points)
Answer concisely.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")


else:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")