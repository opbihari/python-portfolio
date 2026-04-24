import csv

def analyze_logs():
    ip_counts = {} 
    
    print("Reading server_logs.txt...")
    
    try:
        # 1. Read the messy text file
        with open("server_logs.txt", mode="r") as file:
            for line in file:
                # Make sure the line isn't completely empty
                if line.strip(): 
                    
                    parts = line.split(" ")
                    ip = parts[0] 

                    # --- THE DATA SANITIZER ---
                    if "." in ip and ip[0].isdigit(): # Checks if it has a dot AND starts with a number
              
                    # ------------------------------
                    
                    # Count the IP
                         if ip in ip_counts:
                          ip_counts[ip] += 1
                         else:
                          ip_counts[ip] = 1
                        
        # 2. Save the results to a clean CSV
        print("Analysis complete. Saving to ddos_report.csv...\n")
        with open("ddos_report.csv", mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["IP_Address", "Request_Count", "Action_Required"])
            
            for ip, count in ip_counts.items():
                # If an IP makes 3 or more requests, flag it!
                action = "BLOCK" if count >= 3 else "ALLOW"
                
                writer.writerow([ip, count, action])
                
                # Print a color-coded alert to the terminal
                if action == "BLOCK":
                    print(f"🚨 ALERT! IP {ip} exceeded rate limit ({count} requests) -> ACTION: {action}")
                else:
                    print(f"✅ IP {ip} is within normal limits ({count} requests) -> ACTION: {action}")
                    
    except FileNotFoundError:
        print("Error: Could not find 'server_logs.txt'.")

# Run the analyzer
analyze_logs()