import sys
import subprocess
import os
import hashlib

def execute_and_sync(instruction_text):
    print("[Danube] Orchestrating execution layer...")
    
    # 1. Simulate Aider/Execution layer (in a real setup, we pipe text to aider --message)
    # For now, we write the instruction to a tracking log and execute any embedded python
    with open("execution_log.md", "a") as f:
        f.write(f"\n## Instruction\n{instruction_text}\n")
    
    # 2. Extract code blocks if any and execute (simplified simulation)
    import re
    blocks = re.findall(r'```(?:python|bash|sh)\n(.*?)\n```', instruction_text, re.DOTALL)
    for i, block in enumerate(blocks):
        with open(f"temp_exec_{i}.sh", "w") as f:
            f.write(block)
        print(f"[Danube] Executing extracted block {i}...")
        subprocess.run(["bash", f"temp_exec_{i}.sh"], check=False)
        os.remove(f"temp_exec_{i}.sh")

    # 3. GitHub Sync Pipeline
    print("[Danube] Syncing to GitHub...")
    subprocess.run(["git", "add", "."], check=False)
    # Check if there's actually anything to commit
    status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
    if status.strip():
        subprocess.run(["git", "commit", "-m", "autonomous: execution layer update"], check=False)
        # Assuming remote origin is set, we push. (User needs to add remote later if not set)
        subprocess.run(["git", "push", "origin", "main"], check=False)
    
    # 4. Hash state and return to OpenRouter
    state_hash = hashlib.sha256(status.encode()).hexdigest()[:8]
    print(f"\n[DANUBE_OUTPUT_HASH] SUCCESS_STATE_{state_hash}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        execute_and_sync(sys.argv[1])
    else:
        input_data = sys.stdin.read()
        execute_and_sync(input_data)
