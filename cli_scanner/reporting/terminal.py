from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

SEVERITY_COLORS = {
    "CRITICAL": "bold red",
    "HIGH": "red",
    "MEDIUM": "yellow",
    "LOW": "green"
}

def print_summary(summary):
    text = Text()

    for sev, count in summary.items():
        color = SEVERITY_COLORS.get(sev, "white")
        text.append(f"{sev}: {count}  ", style=color)

    console.print(
        Panel(
            text,
            title="Scan Summary",
            border_style="cyan"
        )
    )

def print_findings(findings):
    table = Table(title="Security Findings", show_lines=True)

    table.add_column("Severity", style="bold")
    table.add_column("Title")
    table.add_column("Description")
    table.add_column("Remediation")

    for f in findings:
        sev = f.get("severity", "LOW")
        color = SEVERITY_COLORS.get(sev, "white")

        table.add_row(
            sev,
            f.get("title", "-"),
            f.get("description", "-"),
            f.get("remediation", "-"),
            style=color
        )

    console.print(table)

def generate_terminal_report(findings, summary):
    print_summary(summary)
    print_findings(findings)
