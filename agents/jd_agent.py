class JDBiasAgent:

    def __init__(self):

        self.bias_words = {
            "aggressive": "motivated",
            "dominant": "confident",
            "young": "energetic"
        }

    def detect_bias(self, jd_text):

        detected_words = []

        for word in self.bias_words:
            if word in jd_text.lower():
                detected_words.append(word)

        return detected_words


class ExplainableAI:

    def explain_decision(self, jd_skills, candidate_skills, score):

        matched = []
        missing = []

        for skill in jd_skills:
            if skill in candidate_skills:
                matched.append(skill)
            else:
                missing.append(skill)

        explanation = {
            "score": score,
            "matched_skills": matched,
            "missing_skills": missing,
            "reason": f"{len(matched)} required skills matched"
        }

        return explanation