from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests


class ActionEireneResponse(Action):

    def name(self) -> Text:
        return "action_eirene_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        try:

            user_message = tracker.latest_message.get("text")

            print(f"[DEBUG] User message: {user_message}")

            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={
                    "message": user_message
                },
                timeout=60
            )

            print(f"[DEBUG] Status code: {response.status_code}")

            print(f"[DEBUG] Raw response: {response.text}")

            data = response.json()

            bot_reply = data.get(
                "response",
                "I'm here with you."
            )

            dispatcher.utter_message(
                text=bot_reply
            )

        except Exception as e:

            print(f"[ACTION ERROR] {e}")

            dispatcher.utter_message(
                text="I’m here with you, but something went wrong internally."
            )

        return []