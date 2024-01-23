#!/usr/bin/python3
import requests

image = requests.get("https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon.png",)

with open("images/icon.png", "wb") as f:

    f.write(image.content)
