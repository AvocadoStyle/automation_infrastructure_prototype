from .ApplicationBaseClass import AppBaseClass

class BMW(AppBaseClass):
    def __init__(self, version):
        super().__init__("BMW", version)

    def generate_version(self):
        # implementation for generating version for BMW
        self.version = f"{self.name} {self.version}"