import requests
from bs4 import BeautifulSoup
import csv

# 1. The Target: Where are we getting the data from?
url = "http://quotes.toscrape.com/"

# 2. The Request: Ask the website to give us its HTML code
print("Connecting to the website...")
response = requests.get(url)

# Check if the connection was successful (Status code 200 means OK)
if response.status_code == 200:
    print("Connection successful! Extracting data...\n")
    print("-" * 40)
    
    # 3. The Soup: Parse the messy HTML into a readable format
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 4. The Hunt: Find all the "blocks" on the page that hold our data
    # (On this site, each quote is inside a <div> with the class "quote")
    data_blocks = soup.find_all("div", class_="quote")
    
    # Open a CSV file in write mode to store our extracted data
    with open("quotes_data.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write our column headers
        writer.writerow(["Author", "Quote"])
        
        # 5. The Extraction: Loop through each block and pull out the specific text
        for block in data_blocks:
            # Find the text of the quote
            text = block.find("span", class_="text").text
            # Find the author's name
            author = block.find("small", class_="author").text
        
            # Write the row to our CSV file
            writer.writerow([author, text])
            
            # Print the cleaned-up data to your terminal
            print(f"Author: {author}")
            print(f"Data: {text}")
        
            print("-" * 40)
            
        print("Scraping complete! Data successfully saved to quotes_data.csv")

else:
    print(f"Failed to connect. Status code: {response.status_code}")

def search_for_quote(author_name):
    with open("quotes_data.csv", mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row[0].lower() == author_name.lower():
                print(f"Author: {row[0]}")
                print(f"Quote: {row[1]}")
                print("-" * 40)