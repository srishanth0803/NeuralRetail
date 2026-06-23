import pandas as pd

price = float(
    input("New Price: ")
)

expected_demand = float(
    input("Expected Demand: ")
)

revenue = (

    price
    *
    expected_demand
)

print(
    "Projected Revenue:",
    revenue
)