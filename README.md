# Python Scripting & Cybersecurity Portfolio

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests: PASS](https://img.shields.io/badge/tests-PASS-success.svg)](#-repository-health-checker)

Welcome to my Python portfolio! I am an incoming Bachelor of Computer Applications (BCA) student with a strong focus on Python scripting, backend development, and cybersecurity. 

**I am currently actively seeking a part-time online internship** where I can apply my skills in building APIs, parsing data, and creating security tools.

---

## 🚀 Featured Projects

### 1. AI Code Assistant API
A Flask-based REST API server that routes code-explanation, snippet-generation, and refactoring requests to configurable AI back-ends.
- **Highlights:** Successfully consumes and integrates external LLM APIs (Google Gemini, OpenAI, Anthropic), handles JSON payloads, and demonstrates robust backend architecture.
- **Tech Stack:** Python, Flask, Flask-CORS, External APIs
- 📁 **[View Project Folder →](./Mini_Projects)** (See `AI_Code_Assistant_API.py`)

### 2. Python Web Application Firewall (WAF)
A lightweight, full-stack security tool to parse server logs, detect DDoS patterns, and dynamically block malicious IP addresses.
- **Highlights:** Reads and sanitizes unstructured server logs to detect rate-limit anomalies and dynamically checks incoming connections against a CSV threat feed.
- **Tech Stack:** Python, FastAPI, Uvicorn, HTML5, CSS3, JavaScript (Fetch API)
- 📁 **[View Project Folder →](./Cybersecurity_Project)**

---

## 📂 Repository Structure

* **`Cybersecurity_Project/`**: Consolidated Web Application Firewall (WAF) featuring log generation, DDoS detection, and a FastAPI server dashboard.
* **`IP_Blacklist_Checker_Project/`**: Cybersecurity tools for generating fake IP threat feeds and verifying IPs against blacklists via an interactive CLI.
* **`Web_Scraping_Project/`**: Data extraction tools built using `requests` and `BeautifulSoup` to parse HTML DOMs and save structured data to CSV.
* **`Mini_Projects/`**: Includes the AI Code Assistant API, a CLI Contact Management System, and an Online Bookstore System.
* **`Frontend_Assets/`**: Organized UI components and templates for full-stack integration.
* **`Python_Course_Materials/` & `phthon_practice/`**: Foundational Jupyter notebooks demonstrating proficiency in data structures, algorithms, and iterative logic.

---

## 🛡️ Repository Health Checker

To ensure code stability across all interactive CLI programs and projects without manual testing, I built a custom automated health checker:
- **`check_repo.py`**: A master script that uses Python's `subprocess` to spin up each interactive app and feed it predefined inputs, verifying everything exits cleanly.
- **`tests/`**: A suite of `pytest` unit tests validating the core logic of the Cybersecurity Project.

You can run the full diagnostic check with:
```bash
python check_repo.py
```

---

## 💻 Getting Started

1. Clone this repository: 
   ```bash
   git clone https://github.com/opbihari/python-portfolio.git
   ```
2. Install the required dependencies: 
   ```bash
   pip install -r requirements.txt
   ```
3. Run the automated tests to verify the environment:
   ```bash
   python check_repo.py
   ```
4. Run any of the interactive CLI scripts or start the local API servers!
