from sentence_transformers import SentenceTransformer


class EmbeddingEngine:

    def __init__(self):

        self.model = SentenceTransformer(

            "all-MiniLM-L6-v2"
        )

    def create_embedding(
        self,
        text
    ):

        embedding = self.model.encode(
            text
        )

        return embedding.tolist()


if __name__ == "__main__":

    engine = EmbeddingEngine()

    result = engine.create_embedding(

        "I feel emotionally exhausted."
    )

    print(result[:10])