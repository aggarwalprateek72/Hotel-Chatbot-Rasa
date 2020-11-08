# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from datetime import datetime

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_relative"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        now = datetime.now()
        hrs= (int(now.strftime("%H"))+5)%24
        min= (int(now.strftime("%M"))+30)%60
        offset=int(tracker.get_slot("number_of_hours"))
        final_time=hrs+offset
        time=final_time+":"+min
        print("Sure, I have scheduled a cleaning at "+time)
        dispatcher.utter_message(text="Sure, I have scheduled a cleaning at "+time)

        return []
