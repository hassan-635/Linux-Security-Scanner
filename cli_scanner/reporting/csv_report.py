import csv
from pathlib import Path

def generate_csv_report(findings, output_file="scan_report.csv"):
    report_path = Path(output_file)
    with report_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["severity","title","description","remediation"])
        writer.writeheader()
        for item in findings:
            writer.writerow(item)
    print(f"[INFO] CSV report saved to {report_path.resolve()}")
