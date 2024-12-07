import os
from dotenv import load_dotenv
import pprint
import json
import re

from mastodon import Mastodon

def mastodon_client():
    """Returns a usable Mastodon instance based on the environment variables MASTODON_TOKEN and MASTODON_BASE_URL"""
    environment = envs()
    MASTODON_TOKEN = environment["MASTODON_TOKEN"]
    MASTODON_BASE_URL = environment["MASTODON_BASE_URL"]

    print("using token " + MASTODON_TOKEN)
    print("using base URL " + MASTODON_BASE_URL)

    mastodon_instance = Mastodon(
        access_token=MASTODON_TOKEN,
        api_base_url=MASTODON_BASE_URL
    )


    return mastodon_instance


def mastodon_client_multiple(token, base_url):
    MASTODON_TOKEN = token
    MASTODON_BASE_URL = base_url

    mastodon_instance = Mastodon(
        access_token=MASTODON_TOKEN,
        api_base_url=MASTODON_BASE_URL
    )

    return mastodon_instance

def envs():
    load_dotenv()
    return os.environ