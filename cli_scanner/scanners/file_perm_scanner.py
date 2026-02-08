import subprocess
from cli_scanner.scanners.base_scanner import BaseScanner

SCAN_PATHS = ["/tmp", "/var", "/home"]

class FilePermissionsScanner(BaseScanner):
    name = "File Permission Scanner"

    def scan(self):
        findings = []
        for path in SCAN_PATHS:
            try:
                if self.verbose:
                    print(f"   --> Scanning {path} for world-writable files")
                    result = subprocess.run([
                        "find", path, "-type", "f", "-perm", "002"
                    ],
                    capture_output=True,
                    text=True,
                    timeout=15)
                    
                    files = result.stdout.splitlines()

                    if files:
                        findings.append({
                            "type": "file_permission",
                            "severity": "HIGH",
                            "message": f"{len(files)} world-writable files found in {path}",
                            "examples": files[:5]
                        })

            except subprocess.TimeoutExpired:
                findings.append({
                    "type": "file_permission",
                    "severity": "LOW",
                    "message": f"Scan timed out for {path}"
                })

            except Exception as e:
                findings.append({
                   "type": "file_permission",
                    "severity": "LOW",
                    "message": f"Failed Scanning {path}: {str(e)}" 
                })

        if not findings:
            findings.append({
                "type": "file_permission",
                "severity": "LOW",
                "message": f"No world-writable files detected"
            })

        return findings    