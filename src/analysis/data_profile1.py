# src/analysis/data_profile.py

import pandas as pd
# pyrefly: ignore [missing-import]
from ydata_profiling import ProfileReport

df = pd.read_parquet(
    "data/feature_store/retail_features.parquet"
)

profile = ProfileReport(
    df,
    title="NeuralRetail Data Profiling Report",
    explorative=True
)

profile.to_file(
    "reports/data_profile.html"
)

print("Report generated")