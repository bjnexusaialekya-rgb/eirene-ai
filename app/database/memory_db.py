import sqlite3
from datetime import datetime


class MemoryDatabase:

    def __init__(self):

        self.connection = sqlite3.connect(

            "eirene_memory.db",

            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS conversation_memory (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            user_message TEXT,

            ai_reply TEXT,

            sentiment TEXT,

            emotion TEXT,

            tone TEXT

        )

        """)

        self.connection.commit()

    def store_memory(

        self,

        user_message,

        ai_reply,

        sentiment,

        emotion,

        tone
    ):

        timestamp = str(datetime.now())

        self.cursor.execute("""

        INSERT INTO conversation_memory (

            timestamp,

            user_message,

            ai_reply,

            sentiment,

            emotion,

            tone

        )

        VALUES (?, ?, ?, ?, ?, ?)

        """, (

            timestamp,

            user_message,

            ai_reply,

            sentiment,

            emotion,

            tone
        ))

        self.connection.commit()

    def fetch_memories(self):

        self.cursor.execute("""

        SELECT

            timestamp,

            user_message,

            ai_reply,

            sentiment,

            emotion,

            tone

        FROM conversation_memory

        """)

        rows = self.cursor.fetchall()

        memories = []

        for row in rows:

            memories.append({

                "timestamp": row[0],

                "user_message": row[1],

                "ai_reply": row[2],

                "sentiment": row[3],

                "emotion": row[4],

                "tone": row[5]
            })

        return memories


if __name__ == "__main__":

    db = MemoryDatabase()

    db.store_memory(

        user_message="I feel anxious.",

        ai_reply="I'm here with you.",

        sentiment="NEGATIVE",

        emotion="fear",

        tone="supportive"
    )

    print(db.fetch_memories())