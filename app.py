from fastapi import FastAPI, UploadFile, File, Form

from parser import extract_text_from_pdf
from matcher import calculate_similarity_score
from skills import extract_skills

app = FastAPI(
    title="Smart Resume Screening System"
)


@app.post("/match")
async def match_resume(
    job_description: str = Form(...),
    resume: UploadFile = File(...)
):

    # Extract Resume Text
    resume_text = extract_text_from_pdf(
        resume.file
    )

    # Extract Skills
    jd_skills = extract_skills(job_description)
    resume_skills = extract_skills(resume_text)

    # Matched Skills
    matched_skills = list(
        set(jd_skills) &
        set(resume_skills)
    )

    # Missing Skills
    missing_skills = list(
        set(jd_skills) -
        set(resume_skills)
    )

    # Skill Match Score
    if len(jd_skills) > 0:
        skill_match_score = round(
            (len(matched_skills) / len(jd_skills)) * 100,
            2
        )
    else:
        skill_match_score = 0

    # TF-IDF Similarity Score
    similarity_score = calculate_similarity_score(
        job_description,
        resume_text
    )

    # Candidate Status
    if skill_match_score >= 80:
        status = "Excellent Match"
    elif skill_match_score >= 60:
        status = "Good Match"
    elif skill_match_score >= 40:
        status = "Average Match"
    else:
        status = "Poor Match"

    # Explanation
    if missing_skills:
        explanation = (
            f"Resume matched {skill_match_score}% of the required skills. "
            f"Text similarity score is {similarity_score}%. "
            f"Missing skills: {', '.join(missing_skills)}."
        )
    else:
        explanation = (
            f"Resume matched 100% of the required skills. "
            f"Text similarity score is {similarity_score}%. "
            f"All required skills are present in the resume."
        )

    return {
        "status": status,
        "skill_match_score": skill_match_score,
        "semantic_similarity_score": similarity_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "explanation": explanation
    }