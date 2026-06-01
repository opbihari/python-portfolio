import os
import subprocess
import sys


def run_test(name, command, cwd=".", input_data=None, timeout=30):
    print(f"[RUNNING] {name}... ", end="", flush=True)
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            input=input_data,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        if result.returncode == 0:
            print("[PASS]")
            return True
        else:
            print("[FAIL]")
            print(f"\n--- Output of {name} ---")
            print(result.stdout)
            print(result.stderr)
            print("-" * 40)
            return False
    except subprocess.TimeoutExpired:
        print("[TIMEOUT]")
        return False
    except Exception as e:
        print(f"[ERROR] ({e})")
        return False


def main():
    print("=" * 50)
    print("PYTHON PORTFOLIO REPOSITORY HEALTH CHECKER")
    print("=" * 50)

    all_passed = True

    # 1. Cybersecurity Project Tests
    all_passed &= run_test(
        "Cybersecurity Project Unit Tests",
        ["python", "-m", "pytest", "tests/test_cybersecurity.py"],
    )

    # 2. IP Blacklist Checker Project
    all_passed &= run_test(
        "Fake IP Generator",
        ["python", "IP_Blacklist_Checker_Project/02_Fake_IP_Generator.py"],
        input_data="10\nN\n",
    )
    all_passed &= run_test(
        "Blacklist Checker (Interactive)",
        ["python", "IP_Blacklist_Checker_Project/01_Blacklist_Checker.py"],
        input_data="8.8.8.8\nexit\n",
    )

    # 3. Mini Projects
    all_passed &= run_test(
        "Contact Management System",
        ["python", "Mini_Projects/Contact_Management_System.py"],
        input_data="4\n",
    )
    all_passed &= run_test(
        "Online Bookstore System",
        ["python", "Mini_Projects/Online_Book_Store_System_V2.py"],
        input_data="5\n",
    )
    # AI Code Assistant: compile check (ensures no syntax errors without booting server)
    all_passed &= run_test(
        "AI Code Assistant (Syntax Check)",
        ["python", "-m", "py_compile", "Mini_Projects/AI_Code_Assistant_API.py"],
    )

    # 4. Web Scraping Project
    all_passed &= run_test(
        "Web Scraper", ["python", "Web_Scraping_Project/01_Web_Scraper.py"]
    )

    # 5. Python Course Materials
    all_passed &= run_test(
        "Jupyter Notebooks Check", ["python", "check_notebooks.py"], timeout=180
    )

    print("=" * 50)
    if all_passed:
        print("ALL CHECKS PASSED! The repository is healthy.")
        sys.exit(0)
    else:
        print("SOME CHECKS FAILED. Please review the output above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
