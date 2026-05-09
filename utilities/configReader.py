import json
import os


def load_config():
    # Gets the path to the root directory
    root_path = os.path.dirname(__file__)
    config_path = os.path.join(root_path, "config.json")

    with open(config_path, "r") as file:
        return json.load(file)


# Create a global config object to import easily
config = load_config()