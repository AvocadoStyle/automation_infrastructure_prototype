import importlib
from pathlib import Path
import os
def create_app(app_name: str):
    app_name = app_name.upper()
    module_name = f'product_application.model.applications.{app_name.lower().capitalize()}Class'
    app_module = importlib.import_module(module_name,)
    app_class = getattr(app_module, app_name)
    app_obj = app_class('')
    return app_obj