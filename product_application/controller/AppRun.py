import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(parent_dir)
from product_application.controller.AppsController import *


if __name__ == '__main__':
    n = len(sys.argv)
    if n >= 1:
        print(create_app_controller(sys.argv[1]).generate_version())
    else:
        raise Exception('not enough arguments')


