import re


class ResumeAgent:

    def anonymize(self, resume_text):

        resume_text = re.sub(r'\S+@\S+', 'email_removed', resume_text)
        resume_text = re.sub(r'\d{10}', 'phone_removed', resume_text)

        return resume_text


    def extract_skills(self, resume_text):

        skill_db = [
            "python",
            "machine learning",
            "sql",
            "deep learning",
            "data science"
        ]

        found_skills = []

        for skill in skill_db:
            if skill in resume_text.lower():
                found_skills.append(skill)

        return found_skills


class SkillGapAnalyzer:

    def analyze(self, jd_skills, candidate_skills):

        missing_skills = []

        for skill in jd_skills:
            if skill not in candidate_skills:
                missing_skills.append(skill)

        return missing_skills