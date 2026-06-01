import csv
import os
import re
import sys

# Reconfigure stdout to use UTF-8 so emojis print correctly on Windows terminal without UnicodeEncodeError
sys.stdout.reconfigure(encoding='utf-8')

def check_ip_reputation(target_ip):
    target_ip = target_ip.strip()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, "threat_feed.csv")
    
    try:
        print(f"Scanning database for {target_ip}...")
        with open(csv_file, mode="r") as file:
            reader = csv.reader(file)
            next(reader) # Skip the header row
            
            for row in reader:
                # row[0] is the IP, row[1] is Threat Level, row[2] is Times Blocked
                if row[0] == target_ip:
                    return f"🚨 CRITICAL ALERT! IP {target_ip} is blacklisted.\nThreat Level: {row[1]}\nPrevious Blocks: {row[2]}"
            
            # If the loop finishes the whole file and finds nothing:
            return f"✅ Safe. IP {target_ip} is not on the blacklist. Connection allowed."
            
    except FileNotFoundError:
        return "Error: threat_feed.csv not found! Make sure you ran the generator script first."

# The Interactive Loop
while True:
    print("\n--- Firewall Security Scanner ---")
    user_input = input("Enter an IP to check (or type 'exit' to quit): ").strip()
    
    if user_input.lower() == 'exit':
        print("Shutting down scanner.")
        break
        
    result = check_ip_reputation(user_input)
    print("\n" + result)