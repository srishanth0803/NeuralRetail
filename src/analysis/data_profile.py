# pyrefly: ignore [missing-import]
from ydata_profiling import ProfileReport
import pandas as pd  


data=pd.read_csv("data/bronze/online_retail_II_bronze.csv")
data=data.dropna(subset=['Customer ID'])
data=data.dropna(subset=['Description'])

profile = ProfileReport(
    data,
    title="NeuralRetail Profiling Report"
)

profile.to_file(
    "reports/data_profile_report.html"
)

print("Report Created")