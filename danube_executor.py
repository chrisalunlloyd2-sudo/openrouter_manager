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

    # Extract [FILE: path] blocks. We use split to handle nested markdown gracefully.
    parts = re.split(r'\[FILE:\s*(.+?)\]', content)
    if len(parts) > 1:
        # parts[0] is text before first [FILE]. 
        # Then it pairs: parts[1] is filename, parts[2] is content.
        for i in range(1, len(parts), 2):
            filepath = parts[i].strip()
            code_block = parts[i+1]
            
            # Strip enclosing markdown code blocks robustly
            code_lines = code_block.strip().split('\n')
            if code_lines[0].startswith('```'):
                code_lines = code_lines[1:]
            
            # Find the closing ``` that belongs to the outer block
            # (It's usually the last ``` before another [CMD] or end)
            end_idx = len(code_lines)
            for j in range(len(code_lines)-1, -1, -1):
                if code_lines[j].strip() == '```':
                    end_idx = j
                    break
            
            code = '\n'.join(code_lines[:end_idx])

            dir_path = os.path.dirname(filepath)
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
                
            with open(filepath, 'w') as f:
                f.write(code.strip() + '\n')
            print(f"  -> Created/Updated: {filepath}")

    # Extract [CMD] blocks
    cmd_parts = re.split(r'\[CMD\]', content)
    if len(cmd_parts) > 1:
        for i in range(1, len(cmd_parts)):
            cmd_block = cmd_parts[i]
            cmd_lines = cmd_block.strip().split('\n')
            if cmd_lines[0].startswith('```'):
                cmd_lines = cmd_lines[1:]
            
            end_idx = len(cmd_lines)
            for j in range(len(cmd_lines)-1, -1, -1):
                if cmd_lines[j].strip() == '```':
                    end_idx = j
                    break
            
            cmd_str = '\n'.join(cmd_lines[:end_idx]).strip()
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
