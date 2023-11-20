import pathlib
import sys

import requests
import click

NOTIFY_URL = "http://assist.home.nitori.org/api/services/notify/notify"


@click.command()
@click.argument("title")
def main(title):
    send_notification(title, sys.stdin.read())


def send_notification(title, message):
    auth = pathlib.Path("/mnt/docker-data/homeassist/api_key").read_text().strip()
    headers = {
        "Authorization": f"Bearer {auth}",
        "content-type": "application/json",
    }
    response = requests.post(
        NOTIFY_URL,
        headers=headers,
        json={
            "message": message,
            "title": title,
        },
    )
    response.raise_for_status()
