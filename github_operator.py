import os
import subprocess
import sys

# [ADVANCE 4 & 5] Github Operator & Network Bridge
# Manages Github uploads adhering to SOPs and bridges OneDrive paths.

def get_onedrive_path():
    # Bridge to the user's cross-device network
    path = "/data/data/com.termux/files/home/storage/shared/OneDrive"
    if os.path.exists(path):
        return path
    return "ONEDRIVE_NOT_MOUNTED"

def perform_upload(commit_msg="autonomous: engineered update"):
    print("[Github Operator] Engaging Upload SOPs...")
    
    # Ensure no credentials are in workspace
    if os.path.exists("oauth_creds.json"):
        print("[!] Security Violation: Credentials found in workspace. Purging.")
        os.remove("oauth_creds.json")

    try:
        subprocess.run(["git", "add", "."], check=True)
        # Check if changes exist
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
        if not status.strip():
            print("[Github Operator] No changes detected.")
            return

        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[+] Github Upload Complete.")
        
        # Bridge notification to OneDrive (cross-device signaling)
        od_path = get_onedrive_path()
        if od_path != "ONEDRIVE_NOT_MOUNTED":
            signal_file = os.path.join(od_path, "MATRIX_SIGNAL.txt")
            try:
                with open(signal_file, "a") as f:
                    f.write(f"Updated Github at {subprocess.check_output(['date']).decode('utf-8')}")
                print("[+] Signal routed to Desktop via OneDrive bridge.")
            except Exception:
                pass

    except subprocess.CalledProcessError as e:
        print(f"[!] Github Operator Failed: {e}")

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "autonomous: agentic pipeline update"
    perform_upload(msg)
