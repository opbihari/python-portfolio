import csv
import logging
from pathlib import Path
from typing import List, Dict, Any

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Get script directory for absolute path resolution using pathlib
SCRIPT_DIR = Path(__file__).parent.resolve()

app = FastAPI(title="WAF API Dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home() -> FileResponse:
    """Serves the main HTML dashboard.
    
    Returns:
        FileResponse: The index.html file.
    """
    index_path = SCRIPT_DIR / "index.html"
    return FileResponse(index_path)

@app.get("/api/status")
def status() -> Dict[str, str]:
    """Returns the current status of the firewall.
    
    Returns:
        Dict[str, str]: A JSON object with status details.
    """
    return {
        "status": "Firewall Active",
        "message": "Monitoring incoming traffic...",
        "security_level": "High"
    }

@app.get("/api/threats")
def threats() -> List[Dict[str, Any]]:
    """Retrieves a list of blocked IP threats from the report CSV.
    
    Returns:
        List[Dict[str, Any]]: A list of dictionaries representing blocked threats.
    """
    threats_data: List[Dict[str, Any]] = []
    report_path = SCRIPT_DIR / "ddos_report.csv"
    
    if report_path.exists():
        try:
            with report_path.open("r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row.get("Action_Required") == "BLOCK":
                        threats_data.append({
                            "ip": row.get("IP_Address", ""),
                            "count": row.get("Request_Count", 0)
                        })
        except Exception as e:
            logging.error(f"Error reading threats report: {e}")
            
    return threats_data

if __name__ == "__main__":
    logging.info("Starting Firewall Server at http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
