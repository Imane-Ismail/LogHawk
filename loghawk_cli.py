import argparse
from loghawk.scanner import LogHawk

def main():
    parser = argparse.ArgumentParser(description="LogHawk - Logs Analysis Tool")
    parser.add_argument("log_directory", help="Directory containing log files to analyze")
    parser.add_argument("-o", "--output", default="loghawk_report.txt", help="Output file for results")
   
    args = parser.parse_args()
  
    LogHawk.scan_directory(args.log_directory, args.output)

if __name__ == "__main__":

    main()
