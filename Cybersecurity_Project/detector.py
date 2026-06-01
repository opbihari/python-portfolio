import csv
import logging
from pathlib import Path
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def analyze_logs(log_file_path: Path, report_file_path: Path) -> None:
    """Analyzes a server log file to detect potential DDoS attacks.

    Reads IP addresses from the log file, counts the number of requests per IP,
    and flags any IP with 3 or more requests as 'BLOCK' in the output CSV report.

    Args:
        log_file_path (Path): Path to the input server logs text file.
        report_file_path (Path): Path to the output CSV report file.
    """
    ip_counts: Dict[str, int] = {}

    logging.info(f"Reading {log_file_path.name}...")

    if not log_file_path.exists():
        logging.error(f"Could not find '{log_file_path.name}'. Please generate logs first.")
        return

    try:
        # 1. Read the messy text file
        with log_file_path.open(mode="r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(" ")
                    if not parts:
                        continue
                        
                    ip = parts[0]

                    # --- THE DATA SANITIZER ---
                    # Checks if it has a dot AND starts with a number
                    if "." in ip and ip[0].isdigit():
                        # Count the IP
                        ip_counts[ip] = ip_counts.get(ip, 0) + 1

        # 2. Save the results to a clean CSV
        logging.info(f"Analysis complete. Saving to {report_file_path.name}...\n")
        
        with report_file_path.open(mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["IP_Address", "Request_Count", "Action_Required"])

            for ip, count in ip_counts.items():
                # If an IP makes 3 or more requests, flag it!
                action = "BLOCK" if count >= 3 else "ALLOW"

                writer.writerow([ip, count, action])

                # Log alert to the terminal
                if action == "BLOCK":
                    logging.warning(f"🚨 ALERT! IP {ip} exceeded rate limit ({count} requests) -> ACTION: {action}")
                else:
                    logging.info(f"✅ IP {ip} is within normal limits ({count} requests) -> ACTION: {action}")

    except Exception as e:
        logging.error(f"An error occurred while analyzing logs: {e}")

if __name__ == "__main__":
    current_dir = Path(__file__).parent
    analyze_logs(
        log_file_path=current_dir / "server_logs.txt",
        report_file_path=current_dir / "ddos_report.csv"
    )
