# System Context & Repository Overview

You are an AI coding assistant helping the user develop their Python portfolio. The user has recently undergone a major refactor to organize and test their repository. Below is the complete context of what has been accomplished, the exact directory structure, and how to verify the repository's health. Use this context to answer the user's questions or help them build new features.

## 1. Repository Structure
The repository is structured into distinct project folders. (Virtual environments and cached files are omitted for clarity).

```text
/
├── Cybersecurity_Project/
│   ├── detector.py             # DDoS detector logic
│   ├── firewall_server.py      # FastAPI server
│   ├── log_generator.py        # Dummy log generator for testing
│   └── index.html              # Frontend Dashboard
├── IP_Blacklist_Checker_Project/
│   ├── 01_Blacklist_Checker.py # Interactive CLI app
│   └── 02_Fake_IP_Generator.py # Generates fake IP threat feed CSV
├── Mini_Projects/
│   ├── AI_Code_Assistant_API.py
│   ├── Contact_Management_System.py
│   └── Online_Book_Store_System_V2.py
├── Python_Course_Materials/
│   ├── (Contains 10 introductory Jupyter notebooks with intentional pedagogical errors)
├── Web_Scraping_Project/
│   └── 01_Web_Scraper.py
├── tests/
│   ├── __init__.py
│   └── test_cybersecurity.py   # Pytest suite for the Cybersecurity Project
├── check_notebooks.py          # Executes and validates all Jupyter notebooks
├── check_repo.py               # Unified Black-Box Health Checker for the whole repo
├── requirements.txt
└── README.md
```

## 2. Recent Actions & Decisions
* **Consolidation**: The user requested that we merge `DDoS_Detector_Project` and `FastAPI_Web_Application_Firewall` into a single, cohesive directory called `Cybersecurity_Project`. This directory now serves as a unified Web Application Firewall project.
* **Code Preservation**: The user specifically requested that we *do not modify* the original source code files in the `IP_Blacklist_Checker_Project` or `Mini_Projects`. Those files are interactive CLI applications using infinite `while True` loops and custom `input()` calls.
* **Unit Testing**: A `tests/` directory was added specifically for the `Cybersecurity_Project` using `pytest` to validate that the DDoS detection logic correctly identifies blocked IPs.

## 3. Repository Health Checker (`check_repo.py`)
To test the whole repository without modifying the original interactive CLI codes, a master script `check_repo.py` was created.
* **How it works**: It uses Python's `subprocess` module to spin up each script in the background and pipe predefined inputs (e.g., `"10\nN\n"`, `"8.8.8.8\nexit\n"`, or `"5\n"`) into them to navigate and exit their interactive menus gracefully. 
* **Current Status**: All projects pass successfully.
* **Command to run**:
  ```bash
  python check_repo.py
  ```

## 4. How to assist the User
* If the user wants to add new features to existing interactive scripts (`Mini_Projects` or `IP_Blacklist_Checker`), remember to update `check_repo.py` if you change the menu exit options!
* Suggest using `pytest` for any new backend logic you write.
* Keep your code clean, modular, and use type hints where applicable.
