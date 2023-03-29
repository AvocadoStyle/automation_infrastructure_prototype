from .ApplicationBaseClass import AppBaseClass


class TOYOTA(AppBaseClass):
    def __init__(self, version):
        super().__init__("Toyota", version)

    def generate_version(self):
        # implementation for generating version for Toyota
        self.version = f"{self.name}-{self.version}"