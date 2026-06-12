"""
Master execution script for Mutual Fund Analytics Project
"""

import subprocess

scripts = [
    "etl/data_cleaning.py",
    "etl/load_to_sqlite.py",
    "analytics/performance_analysis.py",
    "analytics/advanced_analytics.py"
]

for script in scripts:
    print(f"\nRunning: {script}")
    subprocess.run(["python", script], check=True)

print("\nProject execution completed successfully!")