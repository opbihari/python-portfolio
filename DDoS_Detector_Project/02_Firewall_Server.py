from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import csv
import os

# Get script directory for absolute path resolution
script_dir = os.path.dirname(os.path.abspath(__file__))

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
    index_path = os.path.join(script_dir, "index.html")
    return FileResponse(index_path)

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
    report_path = os.path.join(script_dir, "ddos_report.csv")
    if os.path.exists(report_path):
        with open(report_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("Action_Required") == "BLOCK":
                    threats_data.append({
                        "ip": row.get("IP_Address"),
                        "count": row.get("Request_Count")
                    })
    return threats_data

if __name__ == "__main__":
    import uvicorn
    print("Starting server at http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
