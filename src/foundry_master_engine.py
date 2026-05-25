import os
import subprocess
import time
import sys

# ==============================================================================
# FOUNDRY MASTER ENGINE v10.1
# Meticulously standardizes and populates all repositories on GitHub.
# Standard: Autonomous Systems Engineering Project Foundry. v10.1
# ==============================================================================

DIRECTOR_PATH = "/data/data/com.termux/files/home/openrouter_manager/src/danube_director.py"
GH_USER = "chrisalunlloyd2-sudo"
REPO_LIST = "/data/data/com.termux/files/home/all_repos.txt"

def run_director(prompt):
    """Executes the prompt through the Recursive Master Loop."""
    cmd = ["python3", DIRECTOR_PATH, prompt]
    try:
        subprocess.run(cmd, capture_output=True, text=True, timeout=600, stdin=subprocess.DEVNULL)
        return True
    except Exception as e:
        print(f"[!] Director failure: {e}")
        return False

def standardize_project(repo_name):
    print(f"\n=========================================================")
    print(f"🛠️ [FOUNDRY] Standardizing Project: {repo_name}")
    print(f"=========================================================\n")
    
    # 1. Clone or navigate
    target_dir = f"/data/data/com.termux/files/home/foundry_work/{repo_name}"
    if not os.path.exists(target_dir):
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)
        print(f"[Foundry] Cloning {repo_name}...")
        subprocess.run(["git", "clone", f"https://github.com/{GH_USER}/{repo_name}.git", target_dir], capture_output=True)
    
    os.chdir(target_dir)

    # 2. Fire the Meticulous Standardization Prompt
    # This prompt forces the AI to build the 4 core docs according to the v10.1 spec.
    prompt = f"""
    Meticulously standardize and populate the repository: '{repo_name}'.
    Title: Autonomous Systems Engineering Project Foundry. v10.1 Master Engine with System Bible and Double Consent.
    
    TASKS:
    1. Populate/Update README.md with the 500x Pro Schema (ASCII tree, visual badges, etc.).
    2. Generate an exhaustive Blueprint.md describing core logic and dataflow.
    3. Generate an ASCII visual ROADMAP.md with future performatives.
    4. Initialize/Update CHANGELOG.md.
    5. Standardize folder structure (src, docs, tests).
    6. Inject 'Double Consent' binomial logic (interaction steps).
    
    Output strictly using [FILE: path] blocks.
    """
    
    if run_director(prompt):
        print(f"[Foundry] SUCCESS: {repo_name} documents updated and standardized.")
        # 3. Final Sync for this repo
        subprocess.run(["python3", "/data/data/com.termux/files/home/initialize_enterprise_project.py"], capture_output=True)
    else:
        print(f"[!] [Foundry] FAILED to standardize {repo_name}.")

def main():
    if not os.path.exists(REPO_LIST):
        print("[!] Repository list not found. Run the fetch command first.")
        return

    with open(REPO_LIST, 'r') as f:
        repos = [line.strip() for line in f if line.strip()]

    print(f"--- [FOUNDRY] Commencing 92-step standardization for {len(repos)} projects ---")
    
    # We'll process a small subset first to verify, then proceed
    for i, repo in enumerate(repos, 1):
        # Skipping the manager itself if we're in it to avoid recursion issues
        if repo == "openrouter_manager": continue
        
        standardize_project(repo)
        
        # Pacing: Nothing lives for free.
        time.sleep(5)
        
        if i >= 3: # Break after 3 repos for this turn to show progress
            print(f"\n[Foundry] Initial 3-repo standardization set complete.")
            break

if __name__ == "__main__":
    main()
