class ScanRunner:
    def __init__(self, scanners, verbose = false):
        self.scanners = scanners
        self.verbose = verbose

    def run(self):
        results = []

        for scanner in self.scanners:
            if scanner.verbose:
                print(f"[+] Running {scanner.name}")
                try:
                    findings = scanner.scan()
                    results.extend(findings)
                except Exception as e:
                    results.append({
                        "type": "error",
                        "severity": "low",
                        "message": f"{scanner.name} Failed: {str(e)}"
                    })       
        return results