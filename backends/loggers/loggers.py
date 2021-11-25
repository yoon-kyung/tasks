import logging
import logging.config
import json


def basic_logger(name: str = None, log_path: str = None):

    config = json.load(open("backend/loggers/logger.json"))
    logging.config.dictConfig(config)

    return logging.getLogger(name)
