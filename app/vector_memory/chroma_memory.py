import chromadb

from app.vector_memory.embedding_engine import EmbeddingEngine


class ChromaMemory:

    def __init__(self):

        self.client = chromadb.Client()

        self.collection = self.client.get_or_create_collection(

            name="eirene_memory"
        )

        self.embedding_engine = EmbeddingEngine()

    def store_memory(

        self,

        memory_id,

        text
    ):

        embedding = self.embedding_engine.create_embedding(
            text
        )

        self.collection.add(

            ids=[memory_id],

            documents=[text],

            embeddings=[embedding]
        )

    def retrieve_memories(

        self,

        query,

        top_k=3
    ):

        query_embedding = self.embedding_engine.create_embedding(
            query
        )

        results = self.collection.query(

            query_embeddings=[query_embedding],

            n_results=top_k
        )

        return results


if __name__ == "__main__":

    chroma = ChromaMemory()

    chroma.store_memory(

        memory_id="1",

        text="I feel emotionally exhausted and anxious."
    )

    result = chroma.retrieve_memories(

        "I feel stressed and overwhelmed."
    )

    print(result)
    