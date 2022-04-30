import os
import sys
from datetime import datetime
from secrets import choice

import requests

import config
from data.data import events, get_closings, get_uwu_gif
from discord_webhook.discord_webhook import DiscordWebhook
from utils.helper import is_image
from utils.read_env import read_env


def main():
    read_env()
    is_ci = os.getenv("CI", "") == "true"

    webhook_url: str = os.getenv("WEBHOOK_URL_DEV" if is_ci else "WEBHOOK_URL", "")
    if is_ci and not webhook_url:
        webhook_url = os.getenv("WEBHOOK_URL", "")

    webhook = DiscordWebhook(
        url=webhook_url,
        username=config.USERNAME,
        avatar_url=config.AVATAR_URL,
    )

    res = requests.get("http://herapi.ronz.workers.dev/")
    message = res.json()["message"]

    event = None if len(sys.argv) < 2 else events.get(sys.argv[1])

    webhook.add_embed(
        {
            "title": event.get("title") if event else "Happy Mensiversary sayaangg <3",
            "description": message,
            "color": 0x631313,
            "image": {
                "url": get_uwu_gif(),
            },
            "timestamp": datetime.now().isoformat(),
            "thumbnail": {
                "url": get_uwu_gif(),
            },
            "footer": {
                "text": get_closings(),
                "icon_url": "https://www.freeiconspng.com/uploads/love-png-5.png",
            },
        }
    )

    webhook.execute()


if __name__ == "__main__":
    main()
