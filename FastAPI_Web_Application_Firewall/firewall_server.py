from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import csv
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# The Main Page (Your UI)
@app.get("/")
def home():
    # This sends the actual HTML web page to the browser
    return FileResponse("index.html")

# The Data Page (Your API)
@app.get("/api/status")
def status():
    # We can keep your JSON data safely on a separate route!
    return {
        "status": "Firewall Active",
        "message": "Monitoring incoming traffic...",
        "security_level": "High"
    }

@app.get("/api/threats")
def threats():
    threats_data = []
    if os.path.exists("ddos_report.csv"):
        with open("ddos_report.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("Action_Required") == "BLOCK":
                    threats_data.append({
                        "ip": row.get("IP_Address"),
                        "count": row.get("Request_Count")
                    })
    return threats_data