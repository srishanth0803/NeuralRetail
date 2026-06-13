from feast import Entity, FeatureView, FileSource, Field
from feast.types import Float64, Int64

customer_source = FileSource(
    path="data/customer_rfm.parquet",
    timestamp_field="event_timestamp"
)

product_source = FileSource(
    path="data/demand_features.parquet",
    timestamp_field="event_timestamp"
)

customer = Entity(
    name="customer",
    join_keys=["Customer ID"]
)

product = Entity(
    name="product",
    join_keys=["StockCode"]
)

customer_feature = FeatureView(
    name="customer_feature",
    entities=[customer],
    ttl=None,
    schema=[
        Field(name="Recency", dtype=Int64),
        Field(name="Frequency", dtype=Int64),
        Field(name="Monetary", dtype=Float64),
    ],
    source=customer_source,
)

product_feature = FeatureView(
    name="product_feature",
    entities=[product],
    ttl=None,
    schema=[
        Field(name="lag_1", dtype=Float64),
        Field(name="lag_7", dtype=Float64),
        Field(name="lag_14", dtype=Float64),

        Field(name="rolling_mean_7", dtype=Float64),
        Field(name="rolling_mean_14", dtype=Float64),
        Field(name="rolling_mean_30", dtype=Float64),

        Field(name="rolling_std_7", dtype=Float64),
        Field(name="rolling_std_14", dtype=Float64),
        Field(name="rolling_std_30", dtype=Float64),
    ],
    source=product_source,
)