from kubernetes import client, config

config.load_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_namespaced_service(namespace="default")

for i in ret.items:
    print(i.metadata.name)
    break