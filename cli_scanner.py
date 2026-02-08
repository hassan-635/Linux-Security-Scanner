import argparse
from cli_scanner.core.runner import ScanRunner
from cli_scanner.scanners.port_scanner import PortScanner
from cli_scanner.scanners.file_perm_scanner import FilePermissionsScanner
from cli_scanner.scanners.suid_scanner import SUIDScanner
from cli_scanner.scanners.user_scanner import UserScanner
from cli_scanner.reporting.csv_report import generate_csv_report
from cli_scanner.reporting.terminal import generate_terminal_report
from cli_scanner.reporting.html_report import generate_html_report
from cli_scanner.reporting.json_report import generate_json_report
from cli_scanner.core.utils import generate_summary
from cli_scanner.core.utils import normalize_findings




def main():
    parser = argparse.ArgumentParser(description="CLI Linux Security Scanner")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    scanners = [
        PortScanner(verbose=args.verbose),
        FilePermissionsScanner(verbose=args.verbose),
        SUIDScanner(verbose=args.verbose),
        UserScanner(verbose=args.verbose)
    ]

    runner = ScanRunner(scanners, verbose=args.verbose)
    results = runner.run()
    results = normalize_findings(results)
    summary = generate_summary(results)

    print("\nScan Results:")
    generate_terminal_report(results, summary)

    generate_json_report(results, output_file="scan_report.json")
    generate_csv_report(results, output_file="scan_report.csv")
    generate_html_report(results, output_file="scan_report.html")


if __name__ == "__main__":
    main()