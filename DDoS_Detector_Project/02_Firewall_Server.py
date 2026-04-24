from fastapi import FastAPI
from fastapi.responses import FileResponse  # We need this to send files!

app = FastAPI()

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