import json
import os


basedir = os.path.abspath(os.path.dirname(__file__))
config_file_json = basedir+'/config.json'

with open(config_file_json) as config_file:
    data = json.load(config_file)


def psql_settings():
    return data["psql_settings"]


# print(type(psql_settings()['user']))
# USER = data["psql_settings"]["user"]
# PSWD = data["psql_settings"]["pswd"]
# HOST = data["psql_settings"]["host"]
# PORT = data["psql_settings"]["port"]
# DB_NAME = data["psql_settings"]["db_name"]
