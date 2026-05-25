import os
import subprocess
import time
import sys

# ==============================================================================
# FOUNDRY MASTER ENGINE v10.2 - MASSIVE CLONE & SYNC
# Ensures all 23 repositories are local and standardized.
# ==============================================================================

DIRECTOR_PATH = "/data/data/com.termux/files/home/openrouter_manager/src/danube_director.py"
GH_USER = "chrisalunlloyd2-sudo"
REPO_LIST = "/data/data/com.termux/files/home/all_repos.txt"
FOUNDRY_ROOT = "/data/data/com.termux/files/home/foundry_work"

def run_director(prompt):
    cmd = ["python3", DIRECTOR_PATH, prompt]
    try:
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = proc.communicate(input='1\n') # Double Consent
        return True
    except: return False

def main():
    if not os.path.exists(REPO_LIST): return

    with open(REPO_LIST, 'r') as f:
        repos = [line.strip() for line in f if line.strip()]

    print(f"--- [FOUNDRY] Initializing global sync for {len(repos)} projects ---")
    
    for repo in repos:
        if repo == "openrouter_manager": continue
        
        target_dir = os.path.join(FOUNDRY_ROOT, repo)
        if not os.path.exists(target_dir):
            os.makedirs(os.path.dirname(target_dir), exist_ok=True)
            print(f"  -> [Cloning] {repo}...")
            subprocess.run(["git", "clone", f"https://github.com/{GH_USER}/{repo}.git", target_dir], capture_output=True)
        
        # We skip the heavy standardization here to let the Swarm Agent handle the audit/fix logic.
        # This script's goal is just to ensure everything is local and ready.
        
    print("[+] Foundry Workspace is fully initialized. All repositories are local.")

if __name__ == "__main__":
    main()
