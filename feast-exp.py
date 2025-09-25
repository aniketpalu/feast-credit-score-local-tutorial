import os
from feast import FeatureStore

repo_path = os.getenv("FEAST_REPO_PATH", "./feature_repo/")

store = FeatureStore(repo_path=repo_path)

print(store.list_projects())