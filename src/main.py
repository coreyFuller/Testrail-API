from testrail import *
from functions import *


def main():
    projects = getProjects()
    for project in projects:
        id = project["id"]
        print(getProject(id))
    pass


if __name__ == '__main__':
    main()

