from transformers import pipeline


class SentimentEngine:

    def __init__(self):

        self.classifier = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def analyze_sentiment(self, text: str):

        result = self.classifier(text)

        return {
            "label": result[0]["label"],
            "score": result[0]["score"]
        }

    def detect_emotion(self, text: str):

        sentiment = self.analyze_sentiment(text)

        label = sentiment["label"]

        if label == "NEGATIVE":
            return "sad"

        if label == "POSITIVE":
            return "happy"

        return "neutral"


if __name__ == "__main__":

    engine = SentimentEngine()

    sample = "I feel stressed and emotionally overwhelmed."

    output = engine.detect_emotion(sample)

    print(output)