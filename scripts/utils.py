"""This module implements utility functions for other modules."""
import logging
from pathlib import Path
import yaml


def parse_config(config_file):
    """
    This function parses the config yaml file
    Args:
        config_file [str]: path to the config yaml file
    Returns:
        config [dict]
    """
    with open(config_file, "rb") as file:
        config = yaml.safe_load(file)
    return config


def set_logger(log_path):
    """
    This function configure a logger
    Args:
        log_path [str]: eg: "../log/etl.log"
    Returns:
        logger [logging object]
    """
    log_path = Path(log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_path, mode='w')
    formatter = logging.Formatter(
        "%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.info("Finished logger configuration!")
    return logger
