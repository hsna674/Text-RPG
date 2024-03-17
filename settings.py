import json

with open("settings.json", "r") as f:
    data = json.load(f)
TEXT_SPEED = data["textSpeed"]
APP_NAME = data["appName"]