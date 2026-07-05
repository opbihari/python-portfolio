import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Get script directory for absolute path resolution using pathlib
SCRIPT_DIR = Path(__file__).parent.resolve()
LOG_FILE_PATH = SCRIPT_DIR / "server_logs.txt"


def initialize_log_file() -> str:
    """Initializes the server log file with sample log entries.

    Returns:
        str: Status message indicating the result.
    """
    try:
        with LOG_FILE_PATH.open("w", encoding="utf-8") as log_file:
            log_file.write("Server Log Initialized\n")
            log_file.write("Server log initiated.\n")
            log_file.write(
                '10.0.0.5 - - [19/Apr/2026:13:45:27] "GET /index.html HTTP/1.1" 200\n'
            )
            log_file.write(
                '192.168.1.99 - - [19/Apr/2026:13:45:28] "POST /login.php HTTP/1.1" 401\n'
            )
            log_file.write(
                '10.0.0.5 - - [19/Apr/2026:13:45:28] "GET /images/logo.png HTTP/1.1" 200\n'
            )
            log_file.write(
                '10.0.0.5 - - [19/Apr/2026:13:45:29] "GET /admin.php HTTP/1.1" 403\n'
            )
            log_file.write(
                '172.16.0.2 - - [19/Apr/2026:13:45:30] "GET /index.html HTTP/1.1" 200\n'
            )
            log_file.write(
                '192.168.1.99 - - [19/Apr/2026:13:45:31] "POST /login.php HTTP/1.1" 401\n'
            )
        return "Log file initialized with sample entries."
    except Exception as e:
        logging.error(f"Failed to initialize log file: {e}")
        return "Failed to initialize log file."


def log_entry(input_string: str) -> str:
    """Appends a custom log entry to the server log file.

    Args:
        input_string (str): The log entry to append.

    Returns:
        str: Status message indicating the result.
    """
    try:
        with LOG_FILE_PATH.open("a", encoding="utf-8") as log_file:
            log_file.write(input_string + "\n")
        return "Log entry added."
    except Exception as e:
        logging.error(f"Failed to add log entry: {e}")
        return "Failed to add log entry."


def view_log_file() -> str:
    """Reads and returns the contents of the server log file.

    Returns:
        str: The content of the log file.
    """
    if not LOG_FILE_PATH.exists():
        return "Log file does not exist yet."
    try:
        with LOG_FILE_PATH.open("r", encoding="utf-8") as log_file:
            logs = log_file.read()
        return logs
    except Exception as e:
        logging.error(f"Failed to view log file: {e}")
        return "Failed to view log file."


def main() -> None:
    """Main interactive loop for the log entry generator."""
    print(initialize_log_file())
    print(view_log_file())

    to_add_or_not = (
        input("Do you want to add a custom log entry? (yes/no): ").strip().lower()
    )
    if to_add_or_not == "yes":
        while True:
            custom_entry = input(
                'Enter the log entry you want to add (or type "exit" to stop): '
            ).strip()
            if custom_entry.lower() == "exit":
                break
            if custom_entry:
                print(log_entry(custom_entry))
        print(view_log_file())


if __name__ == "__main__":
    main()
