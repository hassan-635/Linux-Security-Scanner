from cli_scanner.scanners.base_scanner import BaseScanner

class DummyScanner(BaseScanner):
    name = "Dummy Scanner"

    def scan(self):
        return [{
            "type": "test",
            "severity": "LOW",
            "message": "Scanner working"
        }]