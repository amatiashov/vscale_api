import json
import logging
import requests

from config.config_manager import ConfigManager

config = ConfigManager().get_config_by_section("VSCALE")
logger = logging.getLogger(__name__)

request_header = {"Content-Type": "application/json",
                  "X-Token": config["api_token"]}


def get_general_info():
    uri = config["base_api_uri"] + config["account"]
    response = requests.get(uri, headers=request_header)
    if response.status_code == requests.codes.ok:
        return {"status_code": response.status_code,
                "body": response.json()}
    elif response.status_code == 403:
        logger.error("get_general_info Forbidden")
        return {"status_code": response.status_code,
                "body": None}
    print(response.text)


def get_servers():
    uri = config["base_api_uri"] + config["servers"]
    response = requests.get(uri, headers=request_header)
    if response.status_code == requests.codes.ok:
        return {"status_code": response.status_code,
                "body": response.json()}
    elif response.status_code == 403:
        logger.error("get_general_info Forbidden")
        return {"status_code": response.status_code,
                "body": None}
    print(response.text)


def get_server_details(ctid):
    uri = config["base_api_uri"] + config["detail"]
    uri = uri.replace("{ctid}", str(ctid))
    payload = {"id": str(ctid)}
    response = requests.get(uri, headers=request_header, data=payload)
    if response.status_code == requests.codes.ok:
        return {"status_code": response.status_code,
                "body": response.json()}
    elif response.status_code == 403:
        logger.error("get_general_info Forbidden")
        return {"status_code": response.status_code,
                "body": None}
    print(response.text)


def restart_server(ctid):
    uri = config["base_api_uri"] + config["restart"]
    uri = uri.replace("{ctid}", str(ctid))
    response = requests.patch(uri, headers=request_header)
    if response.status_code == requests.codes.ok:
        return {"status_code": response.status_code,
                "body": response.json()}
    elif response.status_code == 403:
        logger.error("get_general_info Forbidden")
        return {"status_code": response.status_code,
                "body": None}
    print(response.text)


def stop_server(ctid):
    uri = config["base_api_uri"] + config["stop"]
    uri = uri.replace("{ctid}", str(ctid))
    response = requests.patch(uri, headers=request_header)
    if response.status_code == requests.codes.ok:
        return {"status_code": response.status_code,
                "body": response.json()}
    elif response.status_code == 403:
        logger.error("get_general_info Forbidden")
        return {"status_code": response.status_code,
                "body": None}
    print(response.text)


def start_server(ctid):
    uri = config["base_api_uri"] + config["start"]
    uri = uri.replace("{ctid}", str(ctid))
    response = requests.patch(uri, headers=request_header)
    if response.status_code == requests.codes.ok:
        return {"status_code": response.status_code,
                "body": response.json()}
    elif response.status_code == 403:
        logger.error("get_general_info Forbidden")
        return {"status_code": response.status_code,
                "body": None}
    print(response.text)


# account = get_general_info()
# servers = get_servers()
# vs01 = get_server_details(95116)
# restart = restart_server(95116)
# stop = stop_server(95116)
start = start_server(95116)


# print(json.dumps(account, indent=4, ensure_ascii=False))
# print(json.dumps(servers, indent=4, ensure_ascii=False))
# print(json.dumps(vs01, indent=4, ensure_ascii=False))
# print(json.dumps(restart, indent=4, ensure_ascii=False))
# print(json.dumps(stop, indent=4, ensure_ascii=False))
print(json.dumps(start, indent=4, ensure_ascii=False))
