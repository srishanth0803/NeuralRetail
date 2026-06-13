import requests

import os

WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_alert(message):

    payload={
        "text":message
    }

    requests.post(
        SLACK_WEBHOOK,json=payload
    )

