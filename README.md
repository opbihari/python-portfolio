# Python Web Application Firewall (WAF) & Backend Portfolio

Welcome to my Python backend portfolio! I specialize in building APIs, parsing data, and creating full-stack security tools. I am currently pursuing my BCA in Cybersecurity at Galgotias University.

## 🚀 Featured Project: Python Web Application Firewall

A lightweight, full-stack security tool built with FastAPI to parse server logs, detect DDoS patterns, and dynamically block malicious IP addresses.

📁 **[View Project Folder →](./FastAPI_Web_Application_Firewall)**

### 🛠️ Tech Stack
* **Backend:** Python 3, FastAPI, Uvicorn
* **Frontend:** HTML5, CSS3 (Neon UI), JavaScript (Fetch API)
* **Data:** CSV, File I/O streaming

### ✨ Core Features
* **Log Parsing:** Reads and sanitizes unstructured server logs to detect rate-limit anomalies.
* **Threat Intelligence:** Dynamically checks incoming connections against a CSV threat feed.
* **REST API:** Exposes endpoints (`/api/status`, `/api/threats`) to serve real-time JSON data.
* **Live Dashboard:** Neon-styled frontend that auto-refreshes every 5 seconds via the Fetch API.

### 💻 How to Run Locally
1. Clone this repository and navigate to the `FastAPI_Web_Application_Firewall` folder.
2. Install dependencies: `pip install fastapi uvicorn`
3. Start the server: `uvicorn firewall_server:app --reload`
4. Open your browser to `http://127.0.0.1:8000`

---

## 📚 Additional Foundations & Mini-Projects
* **Web Scraping Data Extractor:** Built using `requests` and `BeautifulSoup` to parse HTML DOMs and save structured data to CSV.
* **LLM Code Generator API:** A Flask-based backend API that integrates with Gemini/OpenAI to generate Python scripts.
* **Data Structures & Algorithms:** A collection of Jupyter notebooks demonstrating proficiency in dictionary comprehensions, tuple unpacking, and iterative logic.
