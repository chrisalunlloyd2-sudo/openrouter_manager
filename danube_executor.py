import sys
import os
import re
import subprocess

# ==============================================================================
# DANUBE EXECUTOR (NODE 2)
# Deterministic Headless Extraction Engine
# ==============================================================================

def execute(payload_file):
    print("[Danube Executor] Parsing headless payload...")
    try:
        with open(payload_file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("[!] Danube Executor Error: Payload not found.")
        return

    # Extract [FILE: path] blocks
    file_pattern = re.compile(r'\[FILE:\s*(.+?)\]\n```[a-zA-Z]*\n(.*?)\n```', re.DOTALL)
    files = file_pattern.findall(content)
    
    for filepath, code in files:
        filepath = filepath.strip()
        dir_path = os.path.dirname(filepath)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
            
        with open(filepath, 'w') as f:
            f.write(code.strip() + '\n')
        print(f"  -> Created/Updated: {filepath}")

    # Extract [CMD] blocks
    cmd_pattern = re.compile(r'\[CMD\]\n```[a-zA-Z]*\n(.*?)\n```', re.DOTALL)
    cmds = cmd_pattern.findall(content)
    
    for cmd_str in cmds:
        cmd_str = cmd_str.strip()
        print(f"  -> Executing Shell: {cmd_str}")
        try:
            subprocess.run(cmd_str, shell=True, check=False)
        except Exception as e:
            print(f"  -> [!] Command failed: {e}")

    # Extract Summary
    summary_match = re.search(r'\[SUMMARY\](.*)', content)
    if summary_match:
        print(f"[Danube Communicator] {summary_match.group(1).strip()}")
    else:
        print("[Danube Communicator] Extraction cycle complete.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        execute(sys.argv[1])
    else:
        print("[!] Danube Executor requires a payload file.")
