import subprocess
from cli_scanner.scanners.base_scanner import BaseScanner

RISKY_PORTS = {
    21: "FTP (unencrypted)",
    23: "Telnet (insecure)",
    25: "SMTP (open relay risk)",
    445: "SMB exposed"
}

class PortScanner(BaseScanner):
    name = "Port Scanner"

    def scan(self):
        findings = []
        try:
            result = subprocess.run(
                ["ss", "-tuln"],
                capture_output = True,
                text=True
            )
            
            if self.verbose:
                print("   --> Port Scan Completed, analyzing results...")
                
            for line in result.stdout.splitlines():
                for port, reason in RISKY_PORTS.items():
                    if f":{port} " in line or f":{port}\n" in line:
                        findings.append({
                            "type": "port",
                            "port": port,
                            "severity": "CRITICAL" if port in (21, 23) else "HIGH",
                            "message": f"Port {port} open - {reason}"
                        })

        except FileNotFoundError:
            findings.append({
                "type": "port",
                "severity": "LOW",
                "message": "ss command not available on this system"
            })

        if not findings:
            findings.append({
                "type": "port",
                "severity": "LOW",
                "message": "No risky open ports detected"
            })

        return findings