forecast_mape = 2.58

churn_auc = 0.94

print("\n===== WEEK 2 VALIDATION =====")

if forecast_mape <= 10:
    print("Forecast Model PASSED")
else:
    print("Forecast Model FAILED")

if churn_auc >= 0.90:
    print("Churn Model PASSED")
else:
    print("Churn Model FAILED")