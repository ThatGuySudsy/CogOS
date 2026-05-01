import json

def loadSetting(username, settingName):
    with open("Files/users/" + username + "/data/settings.json", "r") as f:
        return json.load(f).get(settingName)