from testrail import *
from functions import *


def main():
    projects = getProjects()
    for project in projects:
        id = project["id"]
        print(getProject(id))
        acive_runs = getActiveRuns(id)
        reports = getReports(id)
        cases = getCases(id)
        pass
    pass


if __name__ == '__main__':
    main()

