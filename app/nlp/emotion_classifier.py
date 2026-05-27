from transformers import pipeline


class EmotionClassifier:

    def __init__(self):

        self.classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None
        )

    def classify_emotion(self, text: str):

        result = self.classifier(text)

        return result[0]


if __name__ == "__main__":

    engine = EmotionClassifier()

    sample = "I feel anxious and emotionally exhausted."

    output = engine.classify_emotion(sample)

    print(output)