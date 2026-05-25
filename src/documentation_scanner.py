import os
import subprocess
import time

# ==============================================================================
# EXHAUSTIVE DOCUMENTATION SCANNING BOT
# Crawls the project and populates every empty or 'sad' documentation file.
# ==============================================================================

DIRECTOR_PATH = "/data/data/com.termux/files/home/openrouter_manager/src/danube_director.py"
PROJECT_ROOT = "/data/data/com.termux/files/home/openrouter_manager"

def populate_file(file_path):
    print(f"\n[Scanning Bot] Target Identified: {file_path}")
    
    # Construct a high-fidelity population prompt
    prompt = f"""
    The file at '{file_path}' is currently empty or incomplete.
    You MUST exhaustively populate this file based on its name and our project context (OpenRouter Manager).
    Apply the SCARY SMART standard.
    Use the MASTER DOCUMENTATION SCHEMA (Visual Badges, ASCII Trees, etc.) if it is a README or SOP.
    Output only the [FILE: {file_path}] block with the content.
    """
    
    cmd = ["python3", DIRECTOR_PATH, prompt]
    try:
        # Run through the Master Loop for genetic refinement
        subprocess.run(cmd, capture_output=True, text=True, timeout=300, stdin=subprocess.DEVNULL)
        print(f"[Scanning Bot] SUCCESS: {file_path} populated.")
        return True
    except Exception as e:
        print(f"[Scanning Bot] ERROR populating {file_path}: {str(e)}")
        return False

def main():
    print("=========================================================================")
    print(" INITIATING EXHAUSTIVE DOCUMENTATION SCANNING BOT ")
    print(f" Root: {PROJECT_ROOT} ")
    print("=========================================================================")
    
    md_files = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        if '.git' in dirs: dirs.remove('.git')
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.relpath(os.path.join(root, file), PROJECT_ROOT)
                # Check if file is empty or too small (< 100 bytes)
                full_path = os.path.join(root, file)
                if os.path.getsize(full_path) < 100:
                    md_files.append(file_path)

    if not md_files:
        print("[Scanning Bot] All documentation files are currently populated. Standing by.")
        return

    print(f"[Scanning Bot] Found {len(md_files)} files requiring population.")
    
    for f in md_files:
        populate_file(f)
        time.sleep(2) # Duty cycle pacing

    print("\n=========================================================================")
    print(" SCANNING CYCLE COMPLETE: PROJECT FULLY POPULATED ")
    print("=========================================================================")

if __name__ == "__main__":
    main()
