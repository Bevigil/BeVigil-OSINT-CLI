import os

import click

from .settings import BEVIGIL_CONFIG_DIR


def getAPIKey():
    bevigil_dir = os.path.expanduser(BEVIGIL_CONFIG_DIR)
    api_key_file = bevigil_dir + "/api_key"

    # Check if the file exists
    if not os.path.exists(api_key_file):
        raise click.ClickException("Please configure an API key first")

    with open(api_key_file, "r") as file_obj:
        return file_obj.read().strip()
