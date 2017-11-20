import os
import logging
from configparser import ConfigParser
from . import __file__ as source_path


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(source_path)))
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")


LOG_FOLDER = os.path.join(BASE_DIR, "logs")

if not os.path.exists(os.path.join(BASE_DIR, LOG_FOLDER)):
    os.makedirs(LOG_FOLDER)

LOG_FILE_NAME = "log.txt"


logging.basicConfig(format=u'%(filename)s\t[LINE:%(lineno)d]# %(levelname)-8s\t [%(asctime)s]  %(message)s',
                    level=logging.DEBUG,
                    filename=os.path.join(LOG_FOLDER, LOG_FILE_NAME))


class ConfigManager(object):
    _config = None

    def __init__(self):
        self._config = ConfigParser()
        self._config.read(os.path.join(BASE_DIR, "config", "config.ini"))

    def get_config_by_section(self, section_name):
        if section_name not in self._config.keys():
            return None
        return self._config[section_name]
