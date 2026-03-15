from skills import job_roles

def analyze_resume(text):

    text = text.lower()

    detected_skills = []
    role_scores = {}

    for role in job_roles:

        required_skills = job_roles[role]
        matched = 0

        for skill in required_skills:

            if skill in text:
                matched += 1
                detected_skills.append(skill)

        percentage = round((matched / len(required_skills)) * 100, 2)

        role_scores[role] = percentage

    detected_skills = list(set(detected_skills))

    predicted_role = max(role_scores, key=role_scores.get)

    resume_score = role_scores[predicted_role]

    missing_skills = []

    for skill in job_roles[predicted_role]:

        if skill not in text:
            missing_skills.append(skill)

    feedback = generate_feedback(resume_score)

    return detected_skills, predicted_role, resume_score, missing_skills, feedback, role_scores


def generate_feedback(score):

    if score >= 80:
        return "Excellent resume. Strong match for this role."

    elif score >= 60:
        return "Good resume but adding more relevant skills will improve it."

    elif score >= 40:
        return "Average resume. Improve your technical skills."

    else:
        return "Weak match for this role. Consider learning more relevant skills."