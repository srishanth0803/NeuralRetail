from sklearn.isotonic import IsotonicRegression
import pandas as pd 

iso = IsotonicRegression()

iso.fit(
    # pyrefly: ignore [unknown-name]
    predicted_q50,
    # pyrefly: ignore [unknown-name]
    actual
)

calibrated = iso.predict(
    # pyrefly: ignore [unknown-name]
    predicted_q50
)
pd.DataFrame({
    # pyrefly: ignore [unknown-name]
    "actual": actual,
    "calibrated": calibrated
}).to_csv(
    "outputs/calibrated_forecast.csv",
    index=False
)

