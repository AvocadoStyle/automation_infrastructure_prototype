import importlib
def print_out_version(app_name):
    app_name = app_name.lower()
    app_name = app_name.capitalize()
    app_module = importlib.import_module(f'application.{app_name}')
    app_name = app_name.upper()
    context = ''
    app_obj = getattr(app_module, app_name)(context, app_name)
    exit_code, out = app_obj.build_app()
    print(f'exitcode is: {exit_code}, out is: {out}')


print_out_version('BMW')

