from product_application.model.applications.app import *


def create_app_controller(app: str):
    return create_app(app)


def create_apps_controller(apps: list):
    applications_list = []
    for app in apps:
        applications_list.append(create_app(app))

    return applications_list

