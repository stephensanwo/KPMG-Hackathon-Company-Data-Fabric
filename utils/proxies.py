import yaml

# Get the config definitions
with open("../proxies.yaml") as metadata:
    loader = yaml.load(metadata, Loader=yaml.FullLoader)
    proxy_list = loader['proxy_list']

print(proxy_list)
