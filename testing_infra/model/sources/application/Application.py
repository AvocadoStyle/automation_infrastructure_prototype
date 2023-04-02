from testing_infra.model.utilities import utilities
testing_infra.data.configuration
class ApplicationClass():
    def __init__(self, context, name):
        self.__context = context
        self.__name = name
        self.__command = ['python',
            'C:\\study\\projects\\automation_infrastructure_prototype\\product_application\\controller\\AppRun.py',
                          self.__name]

    def build_app(self):
        cmd =
    def run_app_process(self, cmd: str, timeout=1200):
        try:
            exit_code, out = utilities.run_process(cmd=cmd, timeout=timeout)
        except Exception as e:
            print(f'error {e}')
            raise e

