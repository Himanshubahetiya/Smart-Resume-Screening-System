# Smart Resume Screening System

## Overview

Smart Resume Screening System is an AI-powered application that compares a candidate's resume with a Job Description (JD) and calculates a relevance score.

The system extracts skills from both the resume and the job description, identifies matched and missing skills, and provides a final match score with a short explanation.

---

## Features

* Resume PDF Parsing
* Skill Extraction
* Skill Matching
* Missing Skill Detection
* Resume Relevance Score
* FastAPI REST API
* Streamlit User Interface

---

## Project Structure

smart_resume_screening/

├── app.py

├── parser.py

├── matcher.py

├── skills.py

├── resume_ui.py

├── requirements.txt

└── README.md

---

## Approach

### 1. Resume Parsing

The uploaded PDF resume is parsed using PDFPlumber.

The extracted text is converted into plain text format for further processing.

### 2. Skill Extraction

A predefined skill database is used to identify technical skills present in:

* Job Description
* Resume

### 3. Matching Logic

TF-IDF Vectorization is used to convert text into numerical vectors.

Cosine Similarity is used to calculate semantic similarity between:

* Job Description
* Resume Content

### 4. Scoring

The final score is calculated using:

Final Score = (Skill Match × 90%) + (Semantic Similarity × 10%)

### 5. Output

The system returns:

* Match Score (0-100)
* Matched Skills
* Missing Skills
* Candidate Status
* Short Explanation

---

## API Endpoint

### POST /match

Request:

Form Data

* job_description (Text)
* resume (PDF File)

Response:

{
"status": "Strong Match",
"final_score": 83.67,
"matched_skills": [],
"missing_skills": [],
"explanation": ""
}

---

## Installation

### Clone Repository

git clone <repository-url>

cd smart_resume_screening

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux / Mac:

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

---

## Run FastAPI

uvicorn app:app --reload

API Documentation:

http://127.0.0.1:8000/docs

---

## Run Streamlit UI

streamlit run resume_ui.py

---

## Future Improvements

* Experience Extraction
* Education Matching
* Resume Ranking for Multiple Candidates
* Embedding-Based Similarity Models
* Advanced ATS Scoring

---

## Timeline

Development Time: Approximately 1 Day

1. Resume Parsing
2. Skill Extraction
3. Matching Logic
4. FastAPI Endpoint
5. Streamlit UI
6. Testing and Documentation
