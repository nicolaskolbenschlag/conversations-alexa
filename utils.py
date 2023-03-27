import string
import random
import requests

VOICEFLOW_API_KEY = "<YOUR-API-KEY-HERE>"


def generate_session_id(length: int = 32) -> str:
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def handle_conversation_voiceflow(session_id: str, payload: str) -> str:
    body = {"action": {"type": "text", "payload": payload}}
    response = requests.post(
        f"https://general-runtime.voiceflow.com/state/user/{session_id}/interact",
        json=body,
        headers={"Authorization": VOICEFLOW_API_KEY}
    )

    payload = [r for r in response.json() if r["type"] == "text"]
    if len(payload) < 1:
        return None
    payload = payload[0]["payload"]["message"]
    return payload
