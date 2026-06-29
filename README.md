# Python Portfolio — @opbihari

[![CI — Python Tests](https://github.com/opbihari/python-portfolio/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/opbihari/python-portfolio/actions/workflows/python-package-conda.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

> Incoming BCA student | Python · FastAPI · Cybersecurity · Data Engineering  
> Actively seeking a **part-time online internship** in backend development or security tooling.

---

## Repository Structure

```
python-portfolio/
├── Security/                  — Cybersecurity & network tools
│   ├── Cybersecurity_Project/ — Consolidated WAF (canonical version)
│   ├── DDoS_Detector/         — Standalone DDoS detection pipeline
│   ├── FastAPI_WAF/           — FastAPI WAF reference implementation
│   └── IP_Blacklist_Checker/  — IP threat feed validator
├── Mini_Projects/             — Standalone Python applications
├── Web_Scraping/              — Data extraction tools
├── Python_PRACTICE/           — Foundations: notebooks + scripts
├── LeetCode_Solutions/        — DSA practice organized by pattern
├── Frontend_Assets/           — UI components for full-stack demos
└── tests/                     — pytest unit tests
```

---

## Featured Projects

### Security Domain

| Project | Description | Tech Stack | Status |
|---------|-------------|-----------|--------|
| [Cybersecurity Project](./Security/Cybersecurity_Project/) | Full-stack WAF: log ingestion → DDoS detection → FastAPI dashboard | Python · FastAPI · Uvicorn · HTML/CSS/JS | Active |
| [DDoS Detector](./Security/DDoS_Detector/) | Standalone pipeline: log generation, IP rate-limit analysis, CSV reporting | Python · CSV | Archive |
| [FastAPI WAF](./Security/FastAPI_WAF/) | Early WAF prototype with FastAPI REST endpoints | Python · FastAPI | Reference |
| [IP Blacklist Checker](./Security/IP_Blacklist_Checker/) | Generates fake threat feeds and verifies IPs via interactive CLI | Python · CSV | Active |

### Applications

| Project | Description | Tech Stack | Status |
|---------|-------------|-----------|--------|
| [AI Code Assistant API](./Mini_Projects/ai_code_assistant_api.py) | Flask REST API routing code tasks to Gemini / OpenAI / Anthropic backends | Python · Flask · External APIs | Active |
| [Contact Management System](./Mini_Projects/contact_management_system.py) | Full CRUD CLI app persisting contacts to CSV | Python | Active |
| [Online Book Store v2](./Mini_Projects/online_book_store_system_v2.py) | OOP-based bookstore system with inventory management | Python | Active |

### Data Engineering

| Project | Description | Tech Stack | Status |
|---------|-------------|-----------|--------|
| [Web Scraper](./Web_Scraping/web_scraper.py) | Scrapes quotes from the web and saves structured data to CSV | Python · requests · BeautifulSoup | Active |

---

## LeetCode Solutions

Organized by algorithmic pattern following the [NeetCode Roadmap](https://neetcode.io/roadmap).

| Pattern | Problems | Folder |
|---------|----------|--------|
| Arrays & Hashing | — | [View →](./LeetCode_Solutions/Arrays_and_Hashing/) |
| Two Pointers | — | [View →](./LeetCode_Solutions/Two_Pointers/) |
| Sliding Window | — | [View →](./LeetCode_Solutions/Sliding_Window/) |
| Binary Search | — | [View →](./LeetCode_Solutions/Binary_Search/) |
| Trees & Graphs | — | [View →](./LeetCode_Solutions/Trees_and_Graphs/) |
| Dynamic Programming | — | [View →](./LeetCode_Solutions/Dynamic_Programming/) |
| SQL 50 | — | [View →](./LeetCode_Solutions/SQL_50/) |

---

## Python Practice

Foundational notebooks and scripts covering Python core concepts:

| Module | Topic | Format |
|--------|-------|--------|
| 01A | Variables & Data Types | Jupyter Notebook |
| 01B | Input / Output | Jupyter Notebook |
| 02A | Functions — Basics | Jupyter Notebook |
| 02B | Conditionals — Advanced | Jupyter Notebook |
| 03 | Loops & Algorithms | Jupyter Notebook |
| 04A | Lists & Tuples | Jupyter Notebook |
| 04B | Sets & Dictionaries | Jupyter Notebook |
| 05A | File I/O (Text) | Jupyter Notebook |
| 05B | File I/O (CSV) | Jupyter Notebook |
| 06A | Lambda Functions | Python Script |
| 06B | Lambda + Filter | Python Script |
| 06C | Object & CLASS | Python Script |
| 07A | Encapsulation | Python Script |

---

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/opbihari/python-portfolio.git
cd python-portfolio

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the test suite
pytest tests/

# 4. Launch the Cybersecurity WAF dashboard (example)
cd Security/Cybersecurity_Project
python log_generator.py   # generate sample logs
python detector.py        # run DDoS analysis
python firewall_server.py # start FastAPI server at http://127.0.0.1:8000
```

---

## CI / CD

This repository uses **GitHub Actions** for automated testing on every push.

- Linting: `flake8` (syntax errors + undefined names)
- Tests: `pytest` against the `tests/` suite

[![CI Status](https://github.com/opbihari/python-portfolio/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/opbihari/python-portfolio/actions/workflows/python-package-conda.yml)

---

## Roadmap

| Domain | Status |
|--------|--------|
| DevSecOps tools | Coming soon |
| AWS / Azure automation scripts | Coming soon |
| LeetCode solutions (pattern-by-pattern) | In progress |

---

## License

[MIT](./LICENSE) © opbihari
