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


account = get_general_info()
print(json.dumps(account, indent=4, ensure_ascii=False))
