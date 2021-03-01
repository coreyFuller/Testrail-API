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

def getPlans(projectID = None):
    return client.send_get("get_plans/" + str(projectID) + "&is_completed=0")

def getPlan(planID=None):
    return client.send_get("get_plan/" + str(planID))

def getReports(projectID = None):
    return client.send_get("get_reports/" + str(projectID))

def getCases(projectID=None, suiteID=None):
    return client.send_get(f"get_cases/{projectID}&suite_id={suiteID}")

def getSuites(projectID=None):
    return client.send_get("get_suites/" + str(projectID))

def getCase(caseID=None):
    return client.send_get("get_case/%s" % str(caseID))

def getStatuses():
    return client.send_get("get_statuses")

def getResults(testID=None):
    return client.send_get('get_results/' + str(testID))
    pass

def getResultsForCase(runID=None, caseID=None):
    return client.send_get("get_results_for_case/" + str(runID) + '/' + str(caseID))
    pass

def getRuns(projectID=None):
    return client.send_get("get_runs/" + str(projectID))

def getTests(runID=None):
    return client.send_get("get_tests/" + str(runID))
