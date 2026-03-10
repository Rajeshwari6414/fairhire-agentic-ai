from agents.fairness_agent import FairnessAgent

agent = FairnessAgent()

scores = [0.8,0.75,0.6,0.9]

result = agent.evaluate(scores)

print(result)