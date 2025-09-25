from feast.feast_object import ALL_RESOURCE_TYPES
from feast.permissions.action import READ, AuthzedAction, ALL_ACTIONS
from feast.permissions.permission import Permission
from feast.permissions.policy import NamespaceBasedPolicy

# 1. for DS groups/namespaces for read only 
ds_permissions = Permission(
    name="ds_permissions",
    types=ALL_RESOURCE_TYPES,
    policy=NamespaceBasedPolicy(namespaces=["nkathole"]),
    actions=[AuthzedAction.DESCRIBE] + READ
)

# 2. MLOps groups/namespaces for read/write
mlops_permissions = Permission(
    name="mlops_permissions",
    types=ALL_RESOURCE_TYPES,
    policy=NamespaceBasedPolicy(namespaces=["feast-eap"]),
    actions=ALL_ACTIONS
)
