import sys
import os
import re
import subprocess

# ==============================================================================
# DANUBE EXECUTOR (NODE 2) - v10.5 HEURISTIC REFINEMENT
# Deterministic Headless Extraction Engine with Smarter Command Filtering.
# ==============================================================================

def execute(payload_file):
    project_root = os.environ.get("PROJECT_ROOT", os.getcwd())
    project_name = os.path.basename(project_root)
    print(f"[Danube Executor] Parsing payload in: {project_root}")
    
    try:
        with open(payload_file, 'r', errors='ignore') as f:
            content = f.read()
    except FileNotFoundError:
        print("[!] Danube Executor Error: Payload not found.")
        return

    # Extract [FILE: path] blocks.
    parts = re.split(r'\[FILE:\s*(.+?)\]', content)
    if len(parts) > 1:
        for i in range(1, len(parts), 2):
            filepath = parts[i].strip()
            
            # Expand ~ and relative markers
            filepath = filepath.replace('~', '/data/data/com.termux/files/home')
            
            # Strip lead project name if redundant
            if filepath.startswith(f"{project_name}/"):
                filepath = filepath[len(project_name)+1:]
            
            if not filepath.startswith('/'):
                full_path = os.path.abspath(os.path.join(project_root, filepath))
            else:
                full_path = os.path.abspath(filepath)
            
            # SECURITY: Ensure the path is within the home directory
            if not full_path.startswith('/data/data/com.termux/files/home'):
                print(f"  -> [!] BLOCKED OUT-OF-BOUNDS PATH: {full_path}")
                continue
                
            code_block = parts[i+1]
            code_lines = code_block.strip().split('\n')
            
            if len(code_lines) > 0:
                if code_lines[0].startswith('```'):
                    code_lines = code_lines[1:]
                end_idx = len(code_lines)
                for j in range(len(code_lines)-1, -1, -1):
                    if code_lines[j].strip() == '```':
                        end_idx = j
                        break
                new_code = '\n'.join(code_lines[:end_idx]).strip()

                # APPEND-ONLY MERGING
                if os.path.exists(full_path):
                    try:
                        with open(full_path, 'r', errors='ignore') as f:
                            old_code = f.read()
                        if new_code not in old_code:
                            with open(full_path, 'a') as f:
                                f.write(f"\n\n# --- FOUNDRY v10.5 EVOLUTION ---\n{new_code}\n")
                            print(f"  -> Expanded: {full_path}")
                        else:
                            print(f"  -> Skipping duplication: {full_path}")
                    except Exception as e:
                        print(f"  -> [!] Merging failed for {full_path}: {e}")
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
                if cmd_lines[0].startswith('```'): cmd_lines = cmd_lines[1:]
                end_idx = len(cmd_lines)
                for j in range(len(code_lines)-1, -1, -1):
                    if j < len(cmd_lines) and cmd_lines[j].strip() == '```':
                        end_idx = j
                        break
                cmd_str = '\n'.join(cmd_lines[:end_idx]).strip()
                
                # IMPROVED BLOCKING: Use regex word boundaries (\b) to avoid matching inside "swarm"
                if re.search(r'\brm\b|\bgit\s+rm\b|\bmv\b', cmd_str) and "mkdir" not in cmd_str:
                    print(f"  -> [!] BLOCKED DELETION/MOVE ATTEMPT: {cmd_str}")
                    continue
                
                print(f"  -> Executing Shell: {cmd_str}")
                subprocess.run(cmd_str, shell=True, check=False, cwd=project_root)

    summary_match = re.search(r'\[SUMMARY\](.*)', content)
    if summary_match:
        print(f"[Danube Communicator] {summary_match.group(1).strip()}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        execute(sys.argv[1])
    else:
        print("[!] Danube Executor requires a payload file.")
