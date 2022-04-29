from utils.read_env import read_env
from utils.helper import is_image
from secrets import choice
from discord_webhook.discord_webhook import DiscordWebhook
import config
import requests
from data.data import get_closings, get_uwu_gif
from datetime import datetime
import os


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

    webhook.add_embed(
        {
            "title": f"Happy Mensiversary sayaangg <3",
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
