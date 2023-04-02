from product_application.model.VersionGenerator import VersionGenerator
from AppsController import create_apps_controller

def create_version(apps: list):
    apps = create_apps_controller(apps)
    vg = VersionGenerator(apps)
    vg.generate_versions()
    vg.print_versions()

def create_versions_no(apps: list, n: int=1):
    apps = create_apps_controller(apps)
    for i in range(0, n):
        vg = VersionGenerator(apps)
        vg.generate_versions()
        vg.print_versions()

