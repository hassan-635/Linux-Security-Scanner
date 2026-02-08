from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def generate_html_report(findings, output_file="scan_report.html"):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")
    html_content = template.render(findings=findings)
    
    report_path = Path(output_file)
    report_path.write_text(html_content)
    print(f"[INFO] HTML report saved to {report_path.resolve()}")
