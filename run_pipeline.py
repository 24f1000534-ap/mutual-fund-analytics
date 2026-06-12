"""
Master execution script for Mutual Fund Analytics Project
"""

import subprocess

scripts = [
    "data_ingestion.py",
    "clean_nav_history.py",
    "clean_transactions.py",
    "clean_performance.py",
    "clean_remaining_datasets.py",
    "load_sqlite.py"
]

for script in scripts:
    print(f"\nRunning: {script}")

    result = subprocess.run(
        ["python", script],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print(f"\nERROR in {script}")
        print(result.stderr)
        break

print("\nPipeline execution completed.")