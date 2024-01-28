import functools
import logging
import os
from pathlib import Path

import schedule

logger = logging.getLogger("main.util")


def catch_exceptions(cancel_on_failure=False):
    """
    This decorator allow to capture the error in the schedule run and provide option
    if job cancellation require.
    """

    def catch_exceptions_decorator(job_func):
        @functools.wraps(job_func)
        def wrapper(*args, **kwargs):
            try:
                return job_func(*args, **kwargs)
            except Exception:
                import traceback

                logging.error(traceback.format_exc())
                if cancel_on_failure:
                    return schedule.CancelJob

        return wrapper

    return catch_exceptions_decorator


def write_output_file(new_value):
    output_dir = os.getenv("OUTPUT_DIR", "")
    output_file = os.getenv("OUTPUT_FILE", ".env")
    file_path = Path(output_dir) / output_file
    key_to_update = os.getenv("OUTPUT_FILE_KEY", "WINDSCRIBE_EPHEMERAL_PORT")

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

    logger.info(f"Write to {file_path} completed.")
