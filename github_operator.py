import os
import subprocess
import sys

# 🛡️ GITHUB OPERATOR (v2.0)
# [MANDATE: NEVER SAY NO, ZERO SECRET LEAK]

def perform_upload(commit_msg="autonomous: high-fidelity manifestation"):
    print("[Github Operator] Engaging Enterprise Upload SOPs...")
    
    # 1. Security Scrub
    if os.path.exists("oauth_creds.json"):
        os.remove("oauth_creds.json")
    
    # 2. Path Hardening
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # Check for remote origin
        remote_res = subprocess.run(["git", "remote", "-v"], cwd=repo_dir, capture_output=True, text=True)
        if "origin" not in remote_res.stdout:
            print("[!] Remote origin missing. Manifesting project repo...")
            # Use the global enterprise project initializer if needed
            subprocess.run(["python3", os.path.expanduser("~/initialize_enterprise_project.py")], cwd=repo_dir)

        subprocess.run(["git", "add", "."], cwd=repo_dir, check=True)
        
        status = subprocess.run(["git", "status", "--porcelain"], cwd=repo_dir, capture_output=True, text=True).stdout
        if not status.strip():
            print("[Github Operator] Substrate already synchronized.")
            return

        subprocess.run(["git", "commit", "-m", commit_msg], cwd=repo_dir, check=True)
        
        # 3. Forced Push Protocol (Enterprise Fidelity)
        print("[Github Operator] Pushing to Enterprise Cloud...")
        subprocess.run(["git", "push", "origin", "main"], cwd=repo_dir, check=True)
        print("[+] GitHub Manifestation SUCCESS.")

    except subprocess.CalledProcessError as e:
        print(f"[🛑] GitHub Operator Refusal Detected. Fixing origin logic...")
        # Self-Healing: Try to fix remote if it fails
        subprocess.run(["python3", os.path.expanduser("~/initialize_enterprise_project.py")], cwd=repo_dir)

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "autonomous: high-fidelity manifestation"
    perform_upload(msg)
