import sys
import os
import pyfiglet
from loghawk.scanner import LogHawk

def main():
    ascii_banner = pyfiglet.figlet_format("LogHawk")
    print(ascii_banner)
    print("Your Log Analysis Tool\n")

    if len(sys.argv) != 2:
        print("Usage: loghawk <logfile_or_directory>")
        sys.exit(1)

    target = sys.argv[1]

    if os.path.isdir(target):
        LogHawk.scan_directory(target)
    elif os.path.isfile(target):
        alerts, summary = LogHawk.analyze_logs(target)
        if alerts:
            print(f"[+] Suspicious events found in: {target}")
            for alert in alerts:
                print(f"[{alert['Category']}] {alert['Timestamp']} - Line {alert['Line Number']}: {alert['Log Entry']}")

        else:
            print("No suspicious events detected.")
    else:
        print("[-] Invalid path. Please provide a log file or directory.")
        
if __name__ == "__main__":

    main()
