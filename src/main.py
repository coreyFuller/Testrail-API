from testrail import *
from json import loads

creds = open("../config.json").read()
config = loads(creds)
print(config)
client = APIClient(config["server"])
client.user = config["user"]
client.password = config["password"]

