import os
import subprocess
import time
import sys

# ==============================================================================
# DOCUMENTATION VALIDATOR SWARM AGENT v1.1
# FIXED: Unicode resilience and aggressive audit heuristics.
# ==============================================================================

DIRECTOR_PATH = "/data/data/com.termux/files/home/openrouter_manager/src/danube_director.py"
REPO_LIST = "/data/data/com.termux/files/home/all_repos.txt"
FOUNDRY_ROOT = "/data/data/com.termux/files/home/foundry_work"

def log(msg): print(f"[Swarm Agent] {msg}")

def audit_repo(repo_name):
    target_dir = os.path.join(FOUNDRY_ROOT, repo_name)
    if not os.path.exists(target_dir): return False

    os.chdir(target_dir)
    issues = []
    
    # Audit README.md with Unicode resilience
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        issues.append("MISSING_README")
    else:
        try:
            with open(readme_path, 'r', errors='ignore') as f:
                content = f.read()
                if len(content) < 800:
                    issues.append(f"SAD_README ({len(content)} bytes)")
                if "+---" not in content and "|" not in content:
                    issues.append("MISSING_ASCII_CHART")
        except: issues.append("READ_ERROR")

    if issues:
        log(f"Audit FAILED: {repo_name} | {', '.join(issues)}")
        return True
    return False

def run_fix_pass(repo_name):
    log(f"Fixing {repo_name}...")
    prompt = f"""
    MANDATORY REPAIR: Repository '{repo_name}' failed documentation audit.
    You MUST output a MASSIVE (20+ lines) HIGH-FIDELITY ASCII DATA FLOW CHART.
    You MUST output an EXHAUSTIVE technical bible (3000+ words).
    NEVER DELETE. APPEND ONLY.
    Output [FILE: README.md] and [FILE: Blueprint.md].
    """
    cmd = ["python3", DIRECTOR_PATH, prompt]
    try:
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        proc.communicate(input='1\n')
        return True
    except: return False

def main():
    if not os.path.exists(REPO_LIST): return
    with open(REPO_LIST, 'r') as f:
        repos = [line.strip() for line in f if line.strip()]

    log("Commencing Global Audit v1.1...")
    needs_fix = [r for r in repos if r != "openrouter_manager" and audit_repo(r)]
    
    log(f"Found {len(needs_fix)} repos requiring repair.")
    
    for repo in needs_fix[:5]: # Process 5 at a time for stability
        run_fix_pass(repo)
        time.sleep(3)

if __name__ == "__main__":
    main()
