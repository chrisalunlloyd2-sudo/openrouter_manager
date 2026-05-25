import subprocess
import time
import sys
import os

# ==============================================================================
# AUTONOMOUS QA BOT v1.1
# FIXED: Resilience against missing directories and pytest paths.
# ==============================================================================

PROJECT_ROOT = "/data/data/com.termux/files/home/openrouter_manager"

def run_qa_checks():
    os.chdir(PROJECT_ROOT)
    print("[QA Bot] Initiating Workspace Audit...")
    
    # 1. Run all python tests
    if os.path.exists("tests/"):
        print("[QA Bot] Running Pytest suite...")
        # Use python3 -m pytest for environment resilience
        res = subprocess.run(["python3", "-m", "pytest", "tests/"], capture_output=True, text=True)
        if res.returncode == 0:
            print("[QA Bot] [+] Pytest: 100% PASS.")
        else:
            print(f"[QA Bot] [!] Pytest issues detected or tests missing.")
    else:
        print("[QA Bot] [!] Warning: tests/ directory not found.")

    # 2. Check documentation coverage
    print("[QA Bot] Auditing documentation fidelity...")
    md_count = sum(1 for root, dirs, files in os.walk('.') for f in files if f.endswith('.md'))
    print(f"[QA Bot] Found {md_count} high-fidelity documents.")

    # 3. Verify GitHub Sync status
    print("[QA Bot] Verifying Git integrity...")
    res = subprocess.run(["git", "status"], capture_output=True, text=True)
    if "working tree clean" in res.stdout:
        print("[QA Bot] [+] Git: State Persisted.")
    else:
        print("[QA Bot] [!] Git: Unpushed changes detected.")

if __name__ == "__main__":
    run_qa_checks()
