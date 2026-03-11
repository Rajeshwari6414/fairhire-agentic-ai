from agents.jd_agent import JDBiasAgent, ExplainableAI
from agents.resume_agent import ResumeAgent, SkillGapAnalyzer
from agents.scoring_agent import ScoringAgent, InterviewQuestionAgent
from agents.fairness_agent import FairnessAgent


class HiringController:

    def __init__(self):

        self.jd_agent = JDBiasAgent()
        self.resume_agent = ResumeAgent()
        self.scoring_agent = ScoringAgent()
        self.fairness_agent = FairnessAgent()

        self.explain = ExplainableAI()
        self.skill_gap = SkillGapAnalyzer()
        self.questions = InterviewQuestionAgent()


    def run(self, jd_text, resumes):

        jd_skills = ["python","machine learning","sql"]

        scores = []

        for resume in resumes:

            clean = self.resume_agent.anonymize(resume)

            skills = self.resume_agent.extract_skills(clean)

            score = self.scoring_agent.calculate_score(jd_skills,skills)

            explanation = self.explain.explain_decision(jd_skills,skills,score)

            gap = self.skill_gap.analyze(jd_skills,skills)

            questions = self.questions.generate_questions(skills)

            print("\nCandidate Skills:",skills)
            print("Score:",score)
            print("Explanation:",explanation)
            print("Skill Gap:",gap)
            print("Interview Questions:",questions)

            scores.append(score)

        fairness = self.fairness_agent.evaluate(scores)

        print("\nFairness Result:",fairness)
        print("\nFairness Result:",fairness)
