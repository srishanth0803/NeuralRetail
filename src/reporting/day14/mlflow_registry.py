# pyrefly: ignore [missing-import]
from mlflow.tracking import MlflowClient

client = MlflowClient()

client.transition_model_version_stage(

    name="Prophet_Model",

    version=1,

    stage="Production"
)

print(
    "Model promoted"
)
