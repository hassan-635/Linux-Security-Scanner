from pathlib import Path
from cli_scanner.scanners.base_scanner import BaseScanner

class UserScanner(BaseScanner):
    name = "User Account Scanner"

    def scan(self):
        findings = []

        passwd_file = Path("/etc/passwd")

        if not passwd_file.exists():
            findings.append({
                "type": "user",
                "severity": "LOW",
                "message": "/etc/passwd not found"
            })
            return findings

        uid0_users = []
        login_users = []

        for line in passwd_file.read_text().splitlines():
            parts = line.split(":")
            if len(parts) < 7:
                continue

            username, _, uid, _, _, _, shell = parts
            uid = int(uid)

            if uid == 0:
                uid0_users.append(username)

            if shell not in ("/sbin/nologin", "/bin/false"):
                login_users.append(username)

        # --- Findings ---

        if len(uid0_users) > 1:
            findings.append({
                "type": "user",
                "severity": "CRITICAL",
                "message": f"Multiple UID 0 users detected: {', '.join(uid0_users)}"
            })
        else:
            findings.append({
                "type": "user",
                "severity": "LOW",
                "message": "Only one UID 0 user present"
            })

        findings.append({
            "type": "user",
            "severity": "LOW",
            "message": f"{len(login_users)} users have login shells",
            "examples": login_users[:5]
        })

        shadow = Path("/etc/shadow")
        if shadow.exists() and shadow.stat().st_mode & 0o077:
            findings.append({
                "type": "user",
                "severity": "HIGH",
                "message": "/etc/shadow permissions are too open"
            })
        else:
            findings.append({
                "type": "user",
                "severity": "LOW",
                "message": "/etc/shadow permissions appear secure or not accessible"
            })

        return findings
