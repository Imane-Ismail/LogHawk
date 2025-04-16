import sys
import os
import pyfiglet
from loghawk.scanner import LogHawk

def main():
    # Create banner with tool name
    ascii_banner = pyfiglet.figlet_format("LogHawk")
    print(ascii_banner)

    # Add author and usage instructions
    print("🔍 LogHawk - A log analysis tool by Imane Ismail")
    print("📦 GitHub: https://github.com/Imane-Ismail/LogHawk\n")
    print("📘 Usage:")
    print("   loghawk <path_to_log_file>       → Scan a single .log file")
    print("   loghawk <path_to_directory>      → Scan all .log files in a folder\n")

    # Validate arguments
    if len(sys.argv) != 2:
        print("❌ Error: Missing path to log file or directory.\n")
        print("Example: loghawk /var/log/auth.log")
        sys.exit(1)

    target = sys.argv[1]

    if os.path.isdir(target):
        LogHawk.scan_directory(target)
    elif os.path.isfile(target):
        alerts, summary = LogHawk.analyze_logs(target)
        if alerts:
            print(f"\n[+] Suspicious events found in: {target}")
            for alert in alerts:
                print(alert)
        else:
            print("[-] No suspicious events detected.")
    else:
        print("❌ Invalid path. Please provide a valid log file or directory.")
