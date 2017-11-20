import datetime
import json
from time import time

import jwt
import os

from config.config_manager import BASE_DIR

data = dict(name="Alex",
            age=21,
            exin=int(time()) + 3600,
            # exin=int(time()),
            user_id=5684658798)

with open(os.path.join(BASE_DIR, "keys", "jwtRS256.key")) as f:
    private_key = f.read()

json_web_token = jwt.encode(data, private_key, algorithm="RS256")


print("JWT: ", json_web_token)

with open(os.path.join(BASE_DIR, "keys", "jwtRS256.key.pub")) as f:
    public_key = f.read()

data = jwt.decode(json_web_token, public_key, algorithms=["RS256"])


print("DATA:")
print(json.dumps(data, indent=4))


print(datetime.datetime.fromtimestamp(data["exin"]).strftime('%Y-%m-%d %H:%M:%S'))

if data["exin"] - int(time()) < 0:
    print(data["exin"] - int(time()))
    print("Token expired!")
