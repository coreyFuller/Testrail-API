from testrail import *
from functions import *



def main():
    status_list = {}
    test_results = {}
    projects = getProjects()
    statuses = getStatuses()
    for status in statuses:
        status_list[status['id']] = status['name']
    status_list[None] = "comment"
    for project in projects:
        id = project["id"]
        runs = getRuns(id)
        plans = getPlans(id)
        for plan in plans:
          plan = getPlan(plan["id"])
          entries = plan["entries"]
          for entry in entries:
              runs = entry["runs"]
              for run in runs:
                print(".",end="")
                tests = getTests(run["id"])
                for test in tests:
                  results = getResults(test['id'])
                  for result in results:
                    test_results[result['test_id']] = status_list[result['status_id']]
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

