import sys
from product_application.controller.VersionController import *

if __name__ == '__main__':
    n = len(sys.argv)
    apps = []
    for i in range(1, n):
        apps.append(sys.argv[i])

    create_versions_no(apps)