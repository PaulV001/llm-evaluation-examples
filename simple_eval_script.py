# Tiny illustrative scoring script

responses = {
    "Explain gravity": "Gravity pulls things down...",
}

rubric = {
    "accuracy": 4,
    "clarity": 5,
    "tone": 5
}

print("Sample LLM Evaluation Scores:")
for category, score in rubric.items():
    print(f"{category.capitalize()}: {score}/5")
