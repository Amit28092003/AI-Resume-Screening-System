from flask import Flask, render_template, request
import os
from resume_parser import extract_resume_text
from model import analyze_resume

app = Flask(__name__)

# Folder to store uploaded resumes
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Resume Upload + Analysis
@app.route("/upload", methods=["POST"])
def upload_resume():

    if "resume" not in request.files:
        return "No file uploaded"

    file = request.files["resume"]

    if file.filename == "":
        return "No selected file"

    # Save resume
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Extract text from resume
    text = extract_resume_text(filepath)

    # Analyze resume using ML logic
    skills, role, score, missing, feedback, role_scores = analyze_resume(text)

    # Send results to dashboard
    return render_template(
        "result.html",
        skills=skills,
        role=role,
        score=score,
        missing=missing,
        feedback=feedback,
        role_scores=role_scores
    )


# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)