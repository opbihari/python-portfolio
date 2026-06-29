"""
Fake IP / Threat Feed Generator
Generates a CSV file (threat_feed.csv) populated with randomised fake IP
addresses, threat levels, and block counts for use with the IP Blacklist
Checker project.

Run:
    python 02_Fake_IP_Generator.py
"""

import csv
import os
import random

# Output file
# Resolve path relative to script directory to avoid permission/write issues in virtual drive roots (like G:\)
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, "threat_feed.csv")
threat_levels = ["Low", "Medium", "High", "Critical"]


def generate_threat_feed(num_ips: int) -> None:
    """Create the threat_feed.csv with `num_ips` fake entries."""
    print(f"Generating {num_ips} fake threat signatures...")

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP_Address", "Threat_Level", "Times_Blocked"])  # Header

        for _ in range(num_ips):
            # Generate a fake IP like "192.168.x.x"
            fake_ip = f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}"
            level = random.choice(threat_levels)
            blocks = random.randint(0, 100)
            writer.writerow([fake_ip, level, blocks])

    print(f"Success! {csv_file} has been created.")


def viewing() -> None:
    """Print every entry in the threat_feed.csv to the console."""
    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for index, row_data in enumerate(reader, start=1):
            print(
                f"{index}.. IP Address: {row_data[0]}, "
                f"Threat Level: {row_data[1]}, "
                f"Times Blocked: {row_data[2]}"
            )


if __name__ == "__main__":
    # Ask how many IPs to generate and run the generator
    generate_threat_feed(int(input("Enter the number of IPs to generate: ")))

    choice_to_view = input(
        "Do you want to view the threat feed? Y for Yes, N for No: "
    ).upper()

    if choice_to_view == "Y":
        viewing()
    elif choice_to_view == "N":
        print("GoodBye")
    else:
        print("Invalid choice")
