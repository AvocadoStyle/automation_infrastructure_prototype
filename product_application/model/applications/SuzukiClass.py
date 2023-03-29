from .ApplicationBaseClass import AppBaseClass

class SUZUKI(AppBaseClass):
    def __init__(self, version):
        super().__init__("Suzuki", version)

    def generate_version(self):
        # implementation for generating version for Suzuki
        self.version = f"{self.name}({self.version})"