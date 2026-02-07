class BaseScanner:
    name = "Base Scanner"

    def __init__(self, verbose = False):
        self.verbose = verbose

    def scan(self):
        raise NotImplementedError