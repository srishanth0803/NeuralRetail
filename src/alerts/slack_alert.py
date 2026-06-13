import requests

from dotenv import load_dotenv
import os

load_dotenv()

WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_alert(message):

    payload={
        "text":message
    }

    requests.post(
        SLACK_WEBHOOK,json=payload
    )

