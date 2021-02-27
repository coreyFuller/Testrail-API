from testrail import *
from json import loads

creds = open("config.json").read()
config = loads(creds)
client = APIClient(config["server"])
client.user = config["user"]
client.password = config["password"]

def getProjects():
    return client.send_get("get_projects/")

def getProject(projectID = None):
    return client.send_get("get_project/" + str(projectID))