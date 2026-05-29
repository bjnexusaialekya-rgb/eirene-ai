class EpisodicCluster:

    def cluster_memories(

        self,

        memories
    ):

        clusters = {

            "work": [],

            "relationships": [],

            "family": [],

            "burnout": [],

            "loneliness": [],

            "anxiety": []
        }

        for memory in memories:

            text = memory["memory_text"].lower()

            if "work" in text or "job" in text:

                clusters["work"].append(text)

            if "relationship" in text or "partner" in text:

                clusters["relationships"].append(text)

            if "family" in text or "parents" in text:

                clusters["family"].append(text)

            if "burnout" in text or "exhausted" in text:

                clusters["burnout"].append(text)

            if "alone" in text or "lonely" in text:

                clusters["loneliness"].append(text)

            if "anxious" in text or "anxiety" in text:

                clusters["anxiety"].append(text)

        return {

            key: value

            for key, value in clusters.items()

            if value
        }