import sys
import os
import re
import subprocess

# ==============================================================================
# DANUBE EXECUTOR (NODE 2) - APPEND/EXPAND ONLY v2.0
# FIXED: Resolves UnboundLocalError and improves multi-block extraction.
# ==============================================================================

PROJECT_ROOT = "/data/data/com.termux/files/home/openrouter_manager"

def execute(payload_file):
    print("[Danube Executor] Parsing headless expansion payload...")
    try:
        with open(payload_file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("[!] Danube Executor Error: Payload not found.")
        return

    # Extract [FILE: path] blocks.
    parts = re.split(r'\[FILE:\s*(.+?)\]', content)
    if len(parts) > 1:
        for i in range(1, len(parts), 2):
            filepath = parts[i].strip()
            if not filepath.startswith('/'):
                full_path = os.path.join(PROJECT_ROOT, filepath)
            else:
                full_path = filepath
                
            code_block = parts[i+1]
            code_lines = code_block.strip().split('\n')
            
            if len(code_lines) > 0:
                if code_lines[0].startswith('```'):
                    code_lines = code_lines[1:]
                
                # Find the closing ``` that belongs to the outer block
                end_idx = len(code_lines)
                for j in range(len(code_lines)-1, -1, -1):
                    if code_lines[j].strip() == '```':
                        end_idx = j
                        break
                
                new_code = '\n'.join(code_lines[:end_idx]).strip()

                # INTELLIGENT MERGING: If file exists, append/expand. Do NOT overwrite.
                if os.path.exists(full_path):
                    with open(full_path, 'r') as f:
                        old_code = f.read()
                    
                    if new_code not in old_code:
                        with open(full_path, 'a') as f:
                            f.write(f"\n\n# --- AUTOMATIC IQ-300 EXPANSION ---\n{new_code}\n")
                        print(f"  -> Expanded: {full_path}")
                    else:
                        print(f"  -> Skipping duplication: {full_path}")
                else:
                    dir_path = os.path.dirname(full_path)
                    if dir_path and not os.path.exists(dir_path):
                        os.makedirs(dir_path, exist_ok=True)
                    with open(full_path, 'w') as f:
                        f.write(new_code + '\n')
                    print(f"  -> Created: {full_path}")

    # Extract [CMD] blocks
    cmd_parts = re.split(r'\[CMD\]', content)
    if len(cmd_parts) > 1:
        for i in range(1, len(cmd_parts)):
            cmd_block = cmd_parts[i]
            cmd_lines = cmd_block.strip().split('\n')
            
            if len(cmd_lines) > 0:
                if cmd_lines[0].startswith('```'):
                    cmd_lines = cmd_lines[1:]
                
                end_idx = len(cmd_lines)
                for j in range(len(cmd_lines)-1, -1, -1):
                    if j < len(cmd_lines) and cmd_lines[j].strip() == '```':
                        end_idx = j
                        break
                
                cmd_str = '\n'.join(cmd_lines[:end_idx]).strip()
                
                # BLOCK DELETION COMMANDS
                if "rm " in cmd_str or "git rm" in cmd_str:
                    print(f"  -> [!] BLOCKED DELETION ATTEMPT: {cmd_str}")
                    continue

                print(f"  -> Executing Shell: {cmd_str}")
                subprocess.run(cmd_str, shell=True, check=False, cwd=PROJECT_ROOT)

    summary_match = re.search(r'\[SUMMARY\](.*)', content)
    if summary_match:
        print(f"[Danube Communicator] {summary_match.group(1).strip()}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        execute(sys.argv[1])
    else:
        print("[!] Danube Executor requires a payload file.")
