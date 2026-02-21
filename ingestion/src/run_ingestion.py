import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

def run(module: str) -> None:
    p = subprocess.run([sys.executable, str(HERE / module)], check=True)
    return None

if __name__ == "__main__":
    run("fetch_apps.py")
    run("fetch_reviews.py")
    print("Ingestion completed.")
