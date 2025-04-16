import re
import os
import json
from collections import defaultdict

class LogHawk:
    """Log analysis tool for detecting suspicious activities."""
    
    patterns = {
        "Failed Logins": re.compile(r"Failed login|authentication failure", re.IGNORECASE),
        "Lateral Movement": re.compile(r"(RDP|SMB) connection from .*", re.IGNORECASE),
        "Encoded PowerShell": re.compile(r"powershell.*-e\s+[A-Za-z0-9+/=]+", re.IGNORECASE),
        "Suspicious Execution": re.compile(r"cmd\.exe|wscript|cscript|rundll32|regsvr32", re.IGNORECASE),
        "Privilege Escalation": re.compile(r"(SeDebugPrivilege|SeAssignPrimaryTokenPrivilege)", re.IGNORECASE),
        "Unusual Network Activity": re.compile(r"(nc.exe|nmap|mimikatz|Powershell Invoke-WebRequest)", re.IGNORECASE)
    }

    timestamp_pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")

    @classmethod
    def analyze_logs(cls, log_file):
        """Scans a log file for suspicious patterns."""
        alerts = []
        event_summary = defaultdict(int)

        with open(log_file, "r", encoding="utf-8", errors="ignore") as file:
            for line_number, line in enumerate(file, start=1):
                for category, pattern in cls.patterns.items():
                    if pattern.search(line):
                        timestamp_match = cls.timestamp_pattern.search(line)
                        timestamp = timestamp_match.group(1) if timestamp_match else "No Timestamp"
                        alert_message = {
                            "Category": category,
                            "Timestamp": timestamp,
                            "Line Number": line_number,
                            "Log Entry": line.strip()
                        }
                        alerts.append(alert_message)
                        event_summary[category] += 1

        return alerts, event_summary

    @classmethod
    def scan_directory(cls, log_dir, output_file="loghawk_report.txt"):
        """Scans all log files in a directory and saves results."""
        all_alerts = []
        total_summary = defaultdict(int)

        with open(output_file, "w", encoding="utf-8") as report:
            report.write("=== LogHawk Security Report ===\n")

            for root, _, files in os.walk(log_dir):
                for file in files:
                    if file.endswith(".log"):
                        log_path = os.path.join(root, file)
                        print(f"\nScanning {log_path}...")
                        alerts, summary = cls.analyze_logs(log_path)

                        if alerts:
                            report.write(f"\n[+] Suspicious events found in: {log_path}\n")
                            for alert in alerts:
                                report.write(json.dumps(alert, indent=2) + "\n")

                        for category, count in summary.items():
                            total_summary[category] += count

                        all_alerts.extend(alerts)

            report.write("\n=== Summary of Detected Events ===\n")
            for category, count in total_summary.items():
                report.write(f"{category}: {count} occurrences\n")

        print("\n=== Log Analysis Completed ===")
        for category, count in total_summary.items():
            print(f"{category}: {count} occurrences")

        print(f"\n[+] Detailed report saved to: {output_file}")
