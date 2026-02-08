def generate_summary(findings):
    summary = {
        "CRITICAL": 0,
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0
    }

    for f in findings:
        sev = f.get("severity", "").upper()
        if sev in summary:
            summary[sev] += 1

    return summary
