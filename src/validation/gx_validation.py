# src/validation/gx_validation.py

from anyio.lowlevel import checkpoint
from src.alerts.slack_alert import send_slack_alert

try:

    validation_result = checkpoint.run()

    if not validation_result["success"]:

        send_slack_alert(
            "🚨 NeuralRetail DQ Validation Failed"
        )

except Exception as e:

    send_slack_alert(
        f"🚨 GX Error: {e}"
    )

    raise