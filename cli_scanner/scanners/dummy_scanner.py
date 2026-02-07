from cli_scanner.scanners.base_scanner import BaseScanner

class DummyScanner(BaseScanner):
    name = "Dummy Scanner"

    def __init__(self, verbose=False):
        super().__init__(verbose)

    def scan(self):
        if self.verbose:
            print("-> Dummy Scan Running...")
        return [{
            "type": "test",
            "severity": "LOW",
            "message": "Scanner working"
        }]