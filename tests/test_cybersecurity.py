import pytest
from pathlib import Path
import csv
import sys
import os

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Cybersecurity_Project.detector import analyze_logs


def test_analyze_logs(tmp_path: Path):
    """Test that analyze_logs correctly identifies blocked IPs based on request count."""
    log_file = tmp_path / "test_logs.txt"
    report_file = tmp_path / "test_report.csv"

    # Create sample logs
    # IP 10.0.0.1 has 3 requests (should be blocked)
    # IP 10.0.0.2 has 1 request (should be allowed)
    log_content = """10.0.0.1 - - [19/Apr/2026:13:45:27] "GET /" 200
10.0.0.1 - - [19/Apr/2026:13:45:28] "GET /" 200
10.0.0.1 - - [19/Apr/2026:13:45:29] "GET /" 200
10.0.0.2 - - [19/Apr/2026:13:45:30] "GET /" 200
"""
    log_file.write_text(log_content)

    # Run the analyzer
    analyze_logs(log_file, report_file)

    assert report_file.exists(), "Report CSV was not created"

    # Verify report contents
    results = {}
    with report_file.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            results[row["IP_Address"]] = row["Action_Required"]

    assert "10.0.0.1" in results
    assert results["10.0.0.1"] == "BLOCK"

    assert "10.0.0.2" in results
    assert results["10.0.0.2"] == "ALLOW"
