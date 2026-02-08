class ScanRunner:
    def __init__(self, scanners, verbose=False):
        self.scanners = scanners
        self.verbose = verbose

    def run(self):
        all_results = []

        for scanner in self.scanners:
            if self.verbose:
                print(f"[+] Running {scanner.name}")

            try:
                findings = scanner.scan()
                if findings:
                    all_results.extend(findings)

            except Exception as e:
                all_results.append({
                    "severity": "LOW",
                    "title": f"{scanner.name} failed",
                    "description": str(e),
                    "remediation": "Check scanner implementation or permissions"
                })

        return all_results
