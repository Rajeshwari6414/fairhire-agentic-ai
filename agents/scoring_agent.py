class ScoringAgent:

    def calculate_score(self, jd_skills, candidate_skills):

        match = 0

        for skill in candidate_skills:
            if skill in jd_skills:
                match += 1

        if len(jd_skills) == 0:
            return 0

        score = match / len(jd_skills)

        return round(score,2)


class InterviewQuestionAgent:

    def generate_questions(self, skills):

        question_bank = {
            "python": "Explain the difference between list and tuple.",
            "machine learning": "What is overfitting in ML?",
            "sql": "What is a JOIN in SQL?",
            "deep learning": "What is a neural network?"
        }

        questions = []

        for skill in skills:
            if skill in question_bank:
                questions.append(question_bank[skill])

        return questions