import os
import jwt
import json
import datetime
from time import time
from config.config_manager import RESOURCES_DIR

if not os.path.exists(os.path.join(RESOURCES_DIR, "keys")):
    os.mkdir(os.path.join(RESOURCES_DIR, "keys"))

list_dir = os.listdir(os.path.join(RESOURCES_DIR, "keys"))

key_name = "jwtRS256.key"
if list_dir:
    for file_name in list_dir:
        if file_name.endswith(".key"):
            key_name = file_name
            break
else:
    os.system("""ssh-keygen -t rsa -b 4096 -f %s -q -N "" """ % os.path.join(RESOURCES_DIR, "keys", key_name))
    os.system("""openssl rsa -in %s -pubout -outform PEM -out %s""" %
              (os.path.join(RESOURCES_DIR, "keys", key_name), os.path.join(RESOURCES_DIR, "keys", key_name + ".pub")))


data = dict(name="Alex",
            age=21,
            exin=int(time()) + 3600,
            # exin=int(time()),
            user_id=5684658798)

with open(os.path.join(RESOURCES_DIR, "keys", key_name)) as f:
    private_key = f.read()

json_web_token = jwt.encode(data, private_key, algorithm="RS256").decode("utf-8")


print("JWT: ", json_web_token)


with open(os.path.join(RESOURCES_DIR, "keys", key_name + ".pub")) as f:
    public_key = f.read()

print("PUBLIC KEY:")
print(public_key)

data = jwt.decode(json_web_token, public_key, algorithms=["RS256"])


print("DATA:")
print(json.dumps(data, indent=4))


print("Token will be expired in ", datetime.datetime.fromtimestamp(data["exin"]).strftime('%Y-%m-%d %H:%M:%S'))

if data["exin"] - int(time()) < 0:
    print(data["exin"] - int(time()))
    print("Token expired!")

with open(os.path.join(RESOURCES_DIR, "jwt.token"), "w") as f:
    f.write(json_web_token)
