import pandas as pd

def test_quantity_column_exists():
    data = pd.read_csv("data/raw/online_retail_II.csv")
    assert "Quantity" in data.columns

def test_invoice_column_exists():
    data = pd.read_csv("data/raw/online_retail_II.csv")
    assert "Invoice" in data.columns
