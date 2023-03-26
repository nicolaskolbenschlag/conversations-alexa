import string
import random
from dotenv import load_dotenv
load_dotenv()
import requests
import os


def generate_session_id(length: int = 32) -> str:
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def handle_conversation_voiceflow(session_id: str, payload: str) -> str:
    body = {"action": {"type": "text", "payload": payload}}
    response = requests.post(
        f"https://general-runtime.voiceflow.com/state/user/{session_id}/interact",
        json=body,
        headers={"Authorization": os.getenv("VOICEFLOW_API_KEY")},
    )

    return response.json()[-1]["payload"]["message"]


if __name__ == "__main__":
    response = handle_conversation_voiceflow("4", "Nicolas")
    print(response)
