import csv
import os
import re
import sys

# Reconfigure stdout to use UTF-8 so emojis print correctly on Windows terminal without UnicodeEncodeError
sys.stdout.reconfigure(encoding="utf-8")

IP_PATTERN = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

def is_valid_ip(ip_str: str) -> bool:
    return bool(re.match(IP_PATTERN, ip_str.strip()))

def check_ip_reputation(target_ip: str) -> str:
    target_ip = target_ip.strip()
    if not is_valid_ip(target_ip):
        return f"[!] '{target_ip}' is not a valid IPv4 address format."

    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, "threat_feed.csv")
    if not os.path.isfile(csv_file):
        return "[!] Error: threat_feed.csv database file not found!"

    try:
        print(f"Scanning database for {target_ip}...")
        with open(csv_file, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                if not row or len(row) < 3:
                    continue 
                ip_in_feed = row[0].strip()

                if ip_in_feed == target_ip:
                    threat_type = row[1]
                    risk_level = row[2]
                    return f"🚨 CRITICAL ALERT! IP {target_ip} is blacklisted.\nThreat Level: {threat_type}\nPrevious Blocks: {risk_level}"

            # If the loop finishes the whole file and finds nothing:
            return (
                f"✅ Safe. IP {target_ip} is not on the blacklist. Connection allowed."
            )

    except FileNotFoundError:
        return "Error: threat_feed.csv not found! Make sure you ran the generator script first."


# The Interactive Loop
while True:
    print("\n--- Firewall Security Scanner ---")
    user_input = input("Enter an IP to check (or type 'exit' to quit): ").strip()

    if user_input.lower() == "exit":
        print("Shutting down scanner.")
        break

    result = check_ip_reputation(user_input)
    print("\n" + result)
