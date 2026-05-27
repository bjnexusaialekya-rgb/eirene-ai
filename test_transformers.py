from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("Eirene AI understands emotions")

print(result)