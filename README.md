# AI Resume Analyzer & Job Matcher

An intelligent web application that analyzes resumes using Natural Language Processing (NLP) and provides insights such as skill detection, resume scoring, job role matching, and personalized improvement suggestions.

This project helps job seekers understand how well their resume fits industry expectations and how they can improve it to increase their chances of getting hired.

---

## Features

### Resume Analysis

* Upload a PDF resume
* Extracts text from the resume
* Detects technical skills automatically

### Resume Scoring

* Calculates a resume score based on required skills
* Identifies missing skills needed for AI/ML roles

### Job Matching

* Suggests suitable job roles based on detected skills
* Provides match score for each job

### Resume Improvement Suggestions

* Suggests missing skills to learn
* Suggests resume improvements
* Detects missing resume sections such as:

  * Projects
  * Experience
  * Certifications
  * Skills

### Modern Interactive UI

* Drag and drop resume upload
* Glassmorphism design
* Animated background
* Skill tags and job cards
* Loading animation during analysis

---

## Tech Stack

### Frontend

* React.js
* CSS (Glassmorphism UI)
* Axios

### Backend

* FastAPI
* Python

### AI / NLP

* spaCy
* Rule-based skill detection

### Libraries

* pdfplumber
* python-multipart
* CORS middleware

---

## Project Architecture

User Uploads Resume
↓
React Frontend
↓
FastAPI Backend
↓
Resume Text Extraction
↓
Skill Detection
↓
Resume Score Calculation
↓
Job Role Matching
↓
AI Resume Suggestions
↓
Results Displayed on Dashboard

---

## Installation

### 1 Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-analyzer.git
cd ai-resume-analyzer
```

---

### 2 Backend Setup

```bash
pip install fastapi uvicorn pdfplumber spacy python-multipart
python -m spacy download en_core_web_sm
```

Run backend:

```bash
python -m uvicorn main:app --reload --port 9000
```

---

### 3 Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

Backend runs at:

```
http://127.0.0.1:9000
```

---

## Example Output

```
Resume Score: 72%

Skills Detected:
Python, Machine Learning, SQL

Missing Skills:
Docker, NLP

Recommended Jobs:
Machine Learning Engineer – 82%
Data Scientist – 74%

Suggestions:
• Add Docker experience
• Include measurable achievements
• Add ML deployment projects
```

---

## Future Improvements

* AI semantic job matching using BERT embeddings
* Resume ATS compatibility scoring
* Keyword density analysis
* Multiple job role matching
* Resume improvement AI chatbot

---

## Author

Shreesha Rai
Computer Science Engineering Student
Passionate about Artificial Intelligence, Machine Learning, and intelligent sys

This project is open-source and available for learning and educational purposes.
