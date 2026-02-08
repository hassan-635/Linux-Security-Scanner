# CLI Linux Security Scanner 🛡️

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

A lightweight **command-line Linux security scanner** that audits your system for **open ports, file permissions, SUID/SGID files, and user accounts**.  
Generates clean reports in **Terminal, CSV, JSON, and HTML** formats.  

---

## Features ✨

- 🔹 **Port Scanner:** Detect risky open ports.  
- 🔹 **File Permission Scanner:** Identify world-writable files.  
- 🔹 **SUID/SGID Scanner:** Find uncommon SUID/SGID files.  
- 🔹 **User Account Scanner:** Audit users and login shells.  
- 🔹 **Multiple Report Formats:** Terminal, CSV, JSON, HTML.  
- 🔹 **Verbose Mode:** Step-by-step scan output.  

---

## Installation ⚙️

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/cli_scanner.git
cd cli_scanner
pip install -r requirements.txt
```

> Make sure `pip` is installed:  
> ```bash
> sudo apt update
> sudo apt install python3-pip
> ```

---

## Usage 💻

Run a basic scan:

```bash
python3 cli_scanner.py
```

Run with verbose output:

```bash
python3 cli_scanner.py --verbose
```

Reports will be generated automatically:

| Format | File |
|--------|------|
| JSON   | `scan_report.json` |
| CSV    | `scan_report.csv` |
| HTML   | `scan_report.html` |

---

## Example Output 🖥️

**Terminal Scan Summary:**

```
CRITICAL: 0  HIGH: 2  MEDIUM: 0  LOW: 4
Security Findings:
Severity   Title                         Description
LOW        No risky open ports detected  No risky open ports detected
HIGH       /etc/shadow permissions      /etc/shadow permissions are too open
...
```

---

## Contributing 🤝

Contributions, bug reports, and feature requests are welcome!  
Please fork the repository and open a pull request.  

---

