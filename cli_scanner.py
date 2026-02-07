import argparse
from cli_scanner.core.runner import ScanRunner
from cli_scanner.scanners.dummy_scanner import DummyScanner

def main():
    parser = argparse.ArgumentParser(description = "CLI Linux Security Scanner")
    parser.add_argument("--verbose", action = "store_true")
    args = parser.parse_args()

    scanners = [DummyScanner()]
    runner = ScanRunner(scanners, verbose = args.verbose)

    results = runner.run()

    print("\nScan Resuts: ")

    for r in results:
        print(f"[{r['severity']}] {r['message']}")

if __name__ == "__main__":
    main()