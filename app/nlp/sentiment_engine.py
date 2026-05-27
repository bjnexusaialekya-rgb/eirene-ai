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


if __name__ == "__main__":

    engine = SentimentEngine()

    sample = "I feel stressed and emotionally overwhelmed."

    output = engine.analyze_sentiment(sample)

    print(output)