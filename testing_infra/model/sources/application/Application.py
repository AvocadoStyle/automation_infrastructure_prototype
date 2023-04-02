import os

from testing_infra.model.utilities import utilities
from testing_infra.model.utilities.utilities import read_json_file, read_json_for_specific_platform
class ApplicationClass():
    CONFIG_FILE = r'C:\study\projects\automation_infrastructure_prototype\testing_infra\data\configuration\application_config.json'
    def __init__(self, context, name):
        self.__context = context
        self.__name = name
        self.execute_path = None
        self.initialize_apps()
        self.__command = ['python', self.execute_path, self.__name]
    def initialize_apps(self):
        try:
            read_json_for_specific_platform(self.CONFIG_FILE)
            self.execute_path = os.environ.get("EXECUTE_APP_PATH")
        except Exception as e:
            raise Exception(f'couldn\'t initialize the apps {e}')

    def build_app(self):
        self.run_app_process(self.__command)

    def run_app_process(self, cmd: list, timeout=1200):
        try:
            exit_code, out = utilities.run_process(cmd=cmd, timeout=timeout)
        except Exception as e:
            print(f'error {e}')
            raise e

