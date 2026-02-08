import argparse
from cli_scanner.core.runner import ScanRunner
from cli_scanner.scanners.port_scanner import PortScanner
from cli_scanner.scanners.file_perm_scanner import FilePermissionsScanner
from cli_scanner.scanners.suid_scanner import SUIDScanner
from cli_scanner.scanners.user_scanner import UserScanner



def main():
    parser = argparse.ArgumentParser(description = "CLI Linux Security Scanner")
    parser.add_argument("--verbose", action = "store_true")
    args = parser.parse_args()

    scanners = [PortScanner(verbose = args.verbose), 
                FilePermissionsScanner(verbose=args.verbose),
                SUIDScanner(verbose= args.verbose),
                UserScanner(verbose=args.verbose)]
    
    runner = ScanRunner(scanners, verbose = args.verbose)

    results = runner.run()

    print("\nScan Resuts: ")

    for r in results:
        print(f"[{r['severity']}] {r['message']}")

if __name__ == "__main__":
    main()