from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import spacy

app = FastAPI()

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# -----------------------------
# SKILL DATASET
# -----------------------------

SKILLS = [
"python","java","c","c++","javascript","typescript","go","rust",
"html","css","react","angular","vue","node","express","fastapi",
"flask","django","sql","mysql","postgresql","mongodb","redis",
"data science","data analysis","statistics","pandas","numpy",
"matplotlib","seaborn","machine learning","deep learning",
"tensorflow","pytorch","keras","scikit-learn","xgboost",
"nlp","natural language processing","bert","transformers",
"computer vision","opencv","image processing",
"hadoop","spark","pyspark","kafka",
"aws","azure","gcp","docker","kubernetes",
"git","github","gitlab","ci/cd",
"android","flutter","react native",
"excel","tableau","power bi","linux","bash"
]

# -----------------------------
# REQUIRED SKILLS
# -----------------------------

REQUIRED_SKILLS = [
"python",
"machine learning",
"deep learning",
"tensorflow",
"pytorch",
"sql",
"docker",
"fastapi",
"nlp",
"data science"
]

# -----------------------------
# JOB DESCRIPTIONS
# -----------------------------

JOB_DESCRIPTIONS = {

"Machine Learning Engineer":
"Develop machine learning models using Python, TensorFlow, PyTorch and deploy them.",

"Data Scientist":
"Analyze datasets using Python, statistics, SQL and machine learning.",

"AI Engineer":
"Build intelligent AI systems using deep learning and NLP.",

"NLP Engineer":
"Develop natural language processing systems using transformers.",

"Computer Vision Engineer":
"Build image recognition and object detection models.",

"Backend Developer":
"Develop scalable APIs using Python, FastAPI and databases.",

"Full Stack Developer":
"Build frontend and backend applications using React and Node.",

"Data Analyst":
"Analyze business data using SQL, Excel and Python.",

"Cloud Engineer":
"Design scalable systems using AWS, Azure or GCP.",

"DevOps Engineer":
"Automate deployment pipelines using Docker and CI/CD."
}

# -----------------------------
# ROOT
# -----------------------------

@app.get("/")
def root():
    return {"message": "AI Resume Analyzer backend is running"}

# -----------------------------
# RESUME ANALYSIS
# -----------------------------

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    try:

        text = ""

        # Extract text from PDF
        with pdfplumber.open(file.file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        text_lower = text.lower()
        # -----------------------------
# RESUME SECTION DETECTION
# -----------------------------

        sections_found = []

        if "project" in text_lower or "projects" in text_lower:
                        sections_found.append("projects")

        if "experience" in text_lower or "work experience" in text_lower:
                         sections_found.append("experience")

        if "education" in text_lower:
                        sections_found.append("education")

        if "certification" in text_lower or "certifications" in text_lower:
                        sections_found.append("certifications")

        if "skills" in text_lower:
                        sections_found.append("skills")

        # -----------------------------
        # SKILL DETECTION
        # -----------------------------

        detected_skills = []

        for skill in SKILLS:
            if skill in text_lower:
                detected_skills.append(skill)

        # -----------------------------
        # MISSING SKILLS
        # -----------------------------

        missing_skills = []

        for skill in REQUIRED_SKILLS:
            if skill not in detected_skills:
                missing_skills.append(skill)

        # -----------------------------
        # RESUME SCORE
        # -----------------------------

        score = int((len(detected_skills) / len(REQUIRED_SKILLS)) * 100)

        # -----------------------------
        # JOB MATCHING
        # -----------------------------

        job_matches = []

        for job, description in JOB_DESCRIPTIONS.items():

            job_text = description.lower()

            match_count = 0

            for skill in detected_skills:
                if skill in job_text:
                    match_count += 1

            job_score = int((match_count / len(REQUIRED_SKILLS)) * 100)

            job_matches.append({
                "job_role": job,
                "match_score": job_score
            })

        job_matches = sorted(job_matches, key=lambda x: x["match_score"], reverse=True)

        # -----------------------------
        # SUGGESTIONS
        # -----------------------------

        suggestions = []

        for skill in missing_skills:

            if skill == "docker":
                suggestions.append("Learn Docker and containerization for deploying applications.")

            elif skill == "fastapi":
                suggestions.append("Build backend APIs using FastAPI or Flask.")

            elif skill == "tensorflow":
                suggestions.append("Practice deep learning models using TensorFlow.")

            elif skill == "pytorch":
                suggestions.append("Implement machine learning models using PyTorch.")

            elif skill == "nlp":
                suggestions.append("Work on NLP projects such as chatbots or text classification.")

            elif skill == "deep learning":
                suggestions.append("Add deep learning projects such as CNNs or neural networks.")

            else:
                suggestions.append(f"Consider gaining experience with {skill}.")

        # general resume suggestions

        suggestions.append("Add measurable achievements in your projects (example: improved accuracy by 20%).")
        suggestions.append("Include GitHub repository links for your projects.")
        suggestions.append("Add machine learning deployment experience using APIs.")
        suggestions.append("Highlight real-world AI or ML projects.")
        suggestions.append("Use strong action verbs like built, developed, implemented.")
        suggestions.append("Add internships or industry experience if available.")
        suggestions.append("Mention tools like Git, Docker, or cloud platforms.")
        suggestions.append("Add a professional summary at the top of your resume.")
        suggestions.append("Keep resume length within 1–2 pages.")
        suggestions.append("Highlight teamwork, leadership, and problem-solving skills.")
        suggestions.append("Include certifications related to AI, ML, or cloud.")
        suggestions.append("Create a portfolio website showcasing your projects.")
        suggestions.append("Contribute to open-source projects on GitHub.")
        suggestions.append("Add projects related to computer vision or NLP.")
        suggestions.append("Include real datasets and problem-solving case studies.")
        # suggestions for missing resume sections

        if "projects" not in sections_found:
              suggestions.append("Add a Projects section describing your AI or software projects.")

        if "experience" not in sections_found:
             suggestions.append("Include a Work Experience or Internship section.")

        if "education" not in sections_found:
             suggestions.append("Add your Education details such as degree and university.")

        if "certifications" not in sections_found:
             suggestions.append("Add certifications related to AI, ML, or cloud technologies.")

        if "skills" not in sections_found:
            suggestions.append("Add a dedicated Skills section listing your technical skills.")

        suggestions = suggestions[:10]

        return {

            "resume_score": score,

            "skills_detected": detected_skills,

            "missing_skills": missing_skills,

            "job_matches": job_matches[:5],

            "suggestions": suggestions,
            "sections_found": sections_found

        }

    except Exception as e:

        return {
            "error": "Invalid PDF file",
            "details": str(e)
        }