import json
import requests

d={"valA":111, "valB":14}

r = requests.post("https://n1x3kgq78d.execute-api.us-east-1.amazonaws.com/prod/MikiTestFunction", data=json.dumps(d))
print(r.status_code, r.reason)
print(r.text[:300] + '...')
