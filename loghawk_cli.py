import sys
import os
import pyfiglet
import argparse
from loghawk.scanner import LogHawk

def main():
    ascii_banner = pyfiglet.figlet_format("LogHawk")
    print(ascii_banner)
    print("Your Log Analysis Tool\n")

    parser = argparse.ArgumentParser(description="LogHawk - Scan log files for suspicious activity.")
    parser.add_argument("--input", type=str, help="Path to the log file or directory", required=True)
    args = parser.parse_args()

    if os.path.isdir(args.input):
        LogHawk.scan_directory(args.input)
    elif os.path.isfile(args.input):
        alerts, summary = LogHawk.analyze_logs(args.input)
        if alerts:
            print(f"\n[+] Suspicious events found in: {args.input}\n")
            for alert in alerts:
                print(f"[{alert['Category']}] {alert['Timestamp']} - Line {alert['Line Number']}: {alert['Log Entry']}")
            print("\n=== Summary of Detected Events ===")
            for category, count in summary.items():
                print(f"{category}: {count} event(s)")
        else:
            print("[-] No suspicious events detected.")
    else:
        print("❌ Invalid path. Please provide a valid log file or directory.")

if __name__ == "__main__":
    main()
