import json
from pathlib import Path

def generate_json_report(findings, output_file="scan_report.json"):
    report_path = Path(output_file)
    with report_path.open("w") as f:
        json.dump(findings, f, indent=4)
    print(f"[INFO] JSON report saved to {report_path.resolve()}")
