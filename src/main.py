from testrail import *
from functions import *


def main():
    projects = getProjects()
    statuses = getStatuses()
    for project in projects:
        id = project["id"]
        print(getProject(id))
        runs = getRuns(id)
        plans = getPlans(id)
        for plan in plans:
          plan = getPlan(plan["id"])
          entries = plan["entries"]
          run1 = entries[0]["runs"]
          run2 = entries[1]["runs"]
          for run in run1:
              tests = getTests(run["id"])
              for test in tests:
                  results = getResults(test['id'])
                  pass
              pass
          pass
        reports = getReports(id)
        suites = getSuites(id)
        # for suite in suites:
        #     cases = getCases(id, suite['id'])
        #     for case in cases:
        #        case = getCase(case['id'])
        pass
    pass


if __name__ == '__main__':
    main()

