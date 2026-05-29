from datetime import datetime


class MemoryDecayEngine:

    def calculate_decay(

        self,

        created_at
    ):

        now = datetime.utcnow()

        delta = now - created_at

        days_old = delta.days

        decay_score = max(
            0.1,
            1 - (days_old * 0.02)
        )

        return round(decay_score, 2)