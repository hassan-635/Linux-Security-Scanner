def normalize_findings(findings):
    normalized = []
    for f in findings:
        normalized.append({
            "severity": f.get("severity", "LOW").upper(),
            "title": f.get("title", f.get("message", "-")),
            "description": f.get("description", f.get("message", "-")),
            "remediation": f.get("remediation", "-")
        })
    return normalized


def generate_summary(findings):
    summary = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for f in findings:
        sev = f.get("severity", "LOW").upper()
        if sev in summary:
            summary[sev] += 1
        else:
            summary[sev] = 1
    return summary
