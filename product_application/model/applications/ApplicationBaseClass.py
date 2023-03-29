class AppBaseClass:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.generate_version()

    def generate_version(self):
            # implementation for generating version
            return f"{self.name}-v{self.version}"

