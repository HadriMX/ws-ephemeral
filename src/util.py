import logging
import os
from pathlib import Path


def write_output_file(new_value):
    logger = logging.getLogger("main.util")
    file_path = Path(os.getenv("OUTPUT_FILE_PATH", ""))
    key_to_update = os.getenv("OUTPUT_FILE_KEY", "")

    # Read the file content into a dictionary
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Convert the content to a dictionary
    config_dict = {}
    for line in lines:
        key, value = line.strip().split('=')
        config_dict[key] = value

    # Update the value for the specified key
    if key_to_update in config_dict:
        config_dict[key_to_update] = new_value
    else:
        print(f"Key '{key_to_update}' not found in the file.")

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        for key, value in config_dict.items():
            file.write(f"{key}={value}\n")

    logger.debug(f"Write to {file_path} completed.")
