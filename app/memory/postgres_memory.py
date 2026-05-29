import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime


class PostgresMemory:

    def __init__(
        self,
        host="localhost",
        database="eirene_memory",
        user="postgres",
        password="eirene123",
        port="5432"
    ):

        self.connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )

        self.cursor = self.connection.cursor(
            cursor_factory=RealDictCursor
        )

        self.create_memory_table()

    def create_memory_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS memories (

            id SERIAL PRIMARY KEY,

            user_id TEXT,

            memory_text TEXT,

            emotional_state TEXT,

            importance_score FLOAT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        self.cursor.execute(query)
        self.connection.commit()

    def store_memory(
        self,
        user_id,
        memory_text,
        emotional_state,
        importance_score
    ):

        query = """
        INSERT INTO memories (
            user_id,
            memory_text,
            emotional_state,
            importance_score
        )

        VALUES (%s, %s, %s, %s);
        """

        self.cursor.execute(
            query,
            (
                user_id,
                memory_text,
                emotional_state,
                importance_score
            )
        )

        self.connection.commit()

    def fetch_recent_memories(
        self,
        user_id,
        limit=5
    ):

        query = """
        SELECT *
        FROM memories
        WHERE user_id = %s
        ORDER BY created_at DESC
        LIMIT %s;
        """

        self.cursor.execute(
            query,
            (
                user_id,
                limit
            )
        )

        return self.cursor.fetchall()

    def close(self):

        self.cursor.close()
        self.connection.close()


if __name__ == "__main__":

    memory = PostgresMemory()

    memory.store_memory(
        user_id="user_1",
        memory_text="I feel emotionally exhausted.",
        emotional_state="sad",
        importance_score=0.85
    )

    memories = memory.fetch_recent_memories("user_1")

    print(memories)

    memory.close()