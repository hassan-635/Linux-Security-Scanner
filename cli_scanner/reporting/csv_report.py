import csv

def generate_csv_report(findings, output_file="scan_report.csv"):
    fieldnames = ["severity", "title", "description", "remediation"]
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in findings:
            writer.writerow(item)
    print(f"[INFO] CSV report saved to {output_file}")


def generate_summary(findings):
    summary = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for f in findings:
        sev = f.get("severity", "LOW").upper()
        if sev in summary:
            summary[sev] += 1
        else:
            summary[sev] = 1
    return summary
