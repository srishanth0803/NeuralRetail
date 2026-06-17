from sklearn.isotonic import IsotonicRegression

import numpy as np

predicted_quantiles = np.array(
    [0.1,0.2,0.4,0.6,0.8]
)

actual = np.array(
    [0,0,1,1,1]
)

iso = IsotonicRegression()

iso.fit(
    predicted_quantiles,
    actual
)

calibrated = iso.predict(
    predicted_quantiles
)

print("\nCalibrated Probabilities")

print(calibrated)

