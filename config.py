import json
import os

import utils

class Config:
    def __init__(self,discord_token,guild_id):
        self.discord_token = discord_token
        self.guild_id = guild_id

    def get_discord_token(self):
        return self.discord_token

    def get_guild_id(self):
        return self.guild_id

    def to_json(self):
        return {
            "discord_token": self.discord_token,
            "guild_id": self.guild_id
        }

def get_default_config():
    return Config("REPLACE_ME","REPLACE_ME")

def load_config():
    if not os.path.exists(utils.get_config_file()):
        default_config = get_default_config()
        with open(utils.get_config_file(), "w") as f:
            json.dump(default_config.to_json(), f, indent=4)
        return default_config

    try:
        with open(utils.get_config_file(), "r") as f:
            data = json.load(f)
            return Config(data["discord_token"], data["guild_id"])
    except:
        return get_default_config()