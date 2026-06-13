from feast import FeatureStore

store = FeatureStore(repo_path=".")

print(store.list_feature_views())