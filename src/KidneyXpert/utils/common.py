import os
from pathlib import Path

from box.exceptions import BoxValueError
import yaml
from KidneyXpert import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
import base64


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read config from yaml file
    :param path_to_yaml: path to yaml file
    :return: data of file
    """
    while True:
        try:
            with open(path_to_yaml) as yaml_file:
                content = yaml.safe_load(yaml_file)
                logger.info(f"yaml file: {path_to_yaml} loaded successfully")
                return ConfigBox(content)
        except BoxValueError:
            raise ValueError("yaml file is empty")
        except FileNotFoundError:
            path_to_yaml = Path("../") / path_to_yaml
        except Exception as e:
            raise e


def create_directories(path_to_directories: list, verbose=True) -> None:
    """
    Create a list of directories
    :param path_to_directories: List of directories to create
    :param verbose: Ignore logs
    :return: None
    """
    for path in path_to_directories:
        os.makedirs(Path("../") / path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


def save_json(path: Path, data: dict) -> None:
    """
    Save data to json file
    :param path: Path to json file
    :param data: Data to be saved in the json file
    :return: None
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"Data saved at: {path}")


@ensure_annotations
def save_bins(path: Path, data: Any):
    """
    Save data to a binary file
    :param path: Path to binary file
    :param data: Data to be saved in the file
    """
    joblib.dump(value=data, filename=path)


@ensure_annotations
def load_bins(path: Path) -> Any:
    """
    Load binary data from file
    :param path: Path to binary file
    :return: Loaded data
    """
    data = joblib.load(path)
    logger.info(f"Loaded binary data from file: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in Kb
    :param path: Path of the file
    :return: size in KB
    """
    return f"` {round(os.path.getsize(path) / 1024)} KB"


def decode_image(img_string, file_name):
    """
    Decode an image into base64 and write to file
    :param img_string: Image to be saved
    :param file_name: Path of the file to save
    :return:
    """
    imgdata = base64.b64decode(img_string)
    with open(file_name, "wb") as f:
        f.write(imgdata)
        f.close()


def encode_image_into_base64(cropped_img_path):
    """
    Read binary from file Encode into image
    :param cropped_img_path: Path of binary file
    :return:
    """
    with open(cropped_img_path, "rb") as f:
        return base64.b64encode(f.read())
