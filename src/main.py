from testrail import *
from functions import *

projects = getProjects()
for project in projects:
    id = project["id"]
    print(getProject(id))

pass


