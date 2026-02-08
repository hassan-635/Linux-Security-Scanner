import subprocess
from cli_scanner.scanners.base_scanner import BaseScanner

# Known common SUID binaries (baseline)
COMMON_SUID = {
    "/usr/bin/passwd",
    "/usr/bin/sudo",
    "/bin/su"
}

class SUIDScanner(BaseScanner):
    name = "SUID / SGID Scanner"

    def scan(self):
        findings = []

        try:
            if self.verbose:
                print("   --> Searching for SUID/SGID files")

            result = subprocess.run(
                ["find", "/", "-perm", "/6000", "-type", "f"],
                capture_output=True,
                text=True,
                timeout=20
            )

            files = result.stdout.splitlines()

            suspicious = []
            for f in files:
                if f not in COMMON_SUID:
                    suspicious.append(f)

            if suspicious:
                findings.append({
                    "type": "suid",
                    "severity": "HIGH",
                    "message": f"{len(suspicious)} uncommon SUID/SGID files detected",
                    "examples": suspicious[:5]
                })
            else:
                findings.append({
                    "type": "suid",
                    "severity": "LOW",
                    "message": "No suspicious SUID/SGID files detected"
                })

        except subprocess.TimeoutExpired:
            findings.append({
                "type": "suid",
                "severity": "LOW",
                "message": "SUID scan timed out"
            })

        except Exception as e:
            findings.append({
                "type": "suid",
                "severity": "LOW",
                "message": f"SUID scan failed: {str(e)}"
            })

        return findings
