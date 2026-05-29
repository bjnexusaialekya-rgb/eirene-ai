class RelationshipGraph:

    def map_relationship(
        self,
        trust_score,
        attachment
    ):

        return {

            "trust_score": trust_score,

            "attachment_style": attachment,

            "relationship_depth": "developing"
        }
