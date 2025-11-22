
# Resume Ranker — ATS-Based Resume Scoring System

Resume Ranker is an AI-powered application that evaluates and ranks resumes against a given job description using Natural Language Processing (NLP), Machine Learning, and Large Language Models.  
It generates a percentage match score, identifies resume issues, and provides improvement suggestions, making it useful for job seekers, recruiters, and hiring platforms.

---

## Features

- Upload resume in PDF or DOC format
- Automatic text extraction from resume
- AI-based resume analysis using Gemini 2.5 Flash
- Percentage match scoring (0–100)
- Identification of missing skills and gaps
- ATS-oriented evaluation
- Detailed improvement recommendations
- Downloadable ranked report
- Fast API processing via FastAPI and Flask backend
- Streamlit-based user interface
- Deployed on Heroku

---

## Tech Stack

### Backend
- Python 3.9.13
- FastAPI / Flask
- Gemini 2.5 Flash API

### Frontend
- Streamlit

### Core Libraries
- scikit-learn
- nltk / spacy
- PyPDF / docx2txt
- requests
- pydantic

### Deployment
- Heroku
- Git CLI
- Conda environment

---

## Software and Tools Requirements

1. [GitHub Account](https://github.com)  
2. [Heroku Account](https://heroku.com)  
3. [VS Code IDE](https://code.visualstudio.com/)  
4. [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)  
5. [Conda](https://docs.conda.io/en/latest/)

---

# Installation and Setup

### Create a new environment:-

- conda create -p venv python=3.9.13 -y

### Activate the environment:-

- conda activate venv/

### Install dependencies:-

- pip install -r requirements.txt

### Run the backend:-

- uvicorn app.main:app --reload

### Launch the Streamlit interface:-

- streamlit run app.py

 
---

## Deployment on Heroku

- Login to Heroku.
- Create a new application.
- Deploy the project.
- git push heroku main.
- Scale dynos.
- heroku ps.
- scale web=1


---

## API Endpoints

| Method | Endpoint       | Description                     |
|--------|----------------|---------------------------------|
| POST   | /upload        | Upload resume for processing    |
| POST   | /rank          | Generate match score and insights |
| GET    | /report/{id}   | Download ranked report          |

---

## Core Capabilities

### Percentage Match
- Job description relevance scoring
- Skill and keyword matching
- Resume-to-role alignment

### Resume Insights
- Missing important keywords
- Weak or unmatched experience
- Structural and ATS-related issues

### Tell Me About the Resume
- Summary of strengths
- Fitment assessment
- Actionable improvement suggestions

---

## Requirements

- Python 3.9.13
- Conda 22.9.0
- requirements.txt included

---

## Status

This project is completed and production-ready.

---

## Contribution

Contributions are welcome.  
You may submit feature requests, report issues, or open pull requests.

---

## License

This project is licensed under the Apache License 2.0.

---

## Support

If this project was helpful:
- Star the repository
- Share it with others
- Fork and enhance the project
