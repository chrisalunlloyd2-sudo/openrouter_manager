import sys
import os
import re
import subprocess

# ==============================================================================
# DANUBE EXECUTOR (NODE 2) - PATH-AWARE REFACTOR
# Deterministic Headless Extraction Engine
# ==============================================================================

PROJECT_ROOT = "/data/data/com.termux/files/home/openrouter_manager"

def execute(payload_file):
    print("[Danube Executor] Parsing headless payload...")
    try:
        with open(payload_file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("[!] Danube Executor Error: Payload not found.")
        return

    # Extract [FILE: path] blocks.
    # We use a pattern that handles optional whitespace and robustly grabs filenames.
    parts = re.split(r'\[FILE:\s*(.+?)\]', content)
    if len(parts) > 1:
        for i in range(1, len(parts), 2):
            filepath = parts[i].strip()
            
            # Ensure filepath is relative to PROJECT_ROOT or absolute within it
            if not filepath.startswith('/'):
                full_path = os.path.join(PROJECT_ROOT, filepath)
            else:
                full_path = filepath
                
            code_block = parts[i+1]
            
            # Strip enclosing markdown code blocks robustly
            code_lines = code_block.strip().split('\n')
            if len(code_lines) > 0 and code_lines[0].startswith('```'):
                code_lines = code_lines[1:]
            
            # Find the closing ``` that belongs to the outer block
            end_idx = len(code_lines)
            for j in range(len(code_lines)-1, -1, -1):
                if code_lines[j].strip() == '```':
                    end_idx = j
                    break
            
            code = '\n'.join(code_lines[:end_idx])

            dir_path = os.path.dirname(full_path)
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
                
            with open(full_path, 'w') as f:
                f.write(code.strip() + '\n')
            print(f"  -> Created/Updated: {full_path}")

    # Extract [CMD] blocks
    cmd_parts = re.split(r'\[CMD\]', content)
    if len(cmd_parts) > 1:
        for i in range(1, len(cmd_parts)):
            cmd_block = cmd_parts[i]
            cmd_lines = cmd_block.strip().split('\n')
            if len(cmd_lines) > 0 and cmd_lines[0].startswith('```'):
                cmd_lines = cmd_lines[1:]
            
            end_idx = len(cmd_lines)
            for j in range(len(cmd_lines)-1, -1, -1):
                if cmd_lines[j].strip() == '```':
                    end_idx = j
                    break
            
            cmd_str = '\n'.join(cmd_lines[:end_idx]).strip()
            
            # Fix common model errors like 'git add.'
            cmd_str = cmd_str.replace('git add.', 'git add .')
            
            print(f"  -> Executing Shell (Root): {cmd_str}")
            try:
                subprocess.run(cmd_str, shell=True, check=False, cwd=PROJECT_ROOT)
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
