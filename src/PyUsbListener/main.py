import pyudev
import os
import json
from src.PyUsbListener import config
import importlib.resources as pkg_resources


def start():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')

    # Initializing config folder path
    config_folder_path = "/.config/PyUsbListener"

    # Getting config folder path
    user_config_folder_path = os.path.expanduser("~") + config_folder_path

    # Getting config file path
    user_config_file_path = user_config_folder_path + "/config.json"

    # Check if the config file exists
    if not os.path.exists(user_config_file_path):
        # Create the file if the config file does not exist
        os.mkdir(user_config_folder_path)
        config_json = pkg_resources.read_text(config, "config.json")
        with open(user_config_file_path, 'w+') as file:
            file.write(config_json)

    # Parsing from json to Object
    with open(user_config_file_path, 'r') as file:
        json_data = json.load(file)

    for device in iter(monitor.poll, None):
        if device.action == 'add':
            for usb_device in json_data:
                if device.get('ID_MODEL') == usb_device['name']:
                    os.system(usb_device['command'])
