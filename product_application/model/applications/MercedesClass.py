from .ApplicationBaseClass import AppBaseClass

class MERCEDES(AppBaseClass):
    def __init__(self, version):
        super().__init__("Mercedes", version)

    def generate_version(self):
        # implementation for generating version for Mercedes
        self.version = f"{self.name} version {self.version}"