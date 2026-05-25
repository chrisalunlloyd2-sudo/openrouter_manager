import os
import sys
import subprocess
import time
import hashlib
import sqlite3
import re

# ==============================================================================
# RECURSIVE DANUBE DIRECTOR (NODE 1) - SCHEMA-AWARE CONTEXT
# Injects enterprise documentation schemas from SQLite into every prompt.
# ==============================================================================

DB_PATH = "/data/data/com.termux/files/home/openrouter_manager/pedagogy_cognitive.db"
PROJECT_ROOT = "/data/data/com.termux/files/home/openrouter_manager"

def fetch_master_schemas():
    """Retrieves the Pro documentation templates from the sub-database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT ascii_topology_template, windows_instructions, android_instructions FROM enterprise_schemas WHERE schema_name='standard_project'")
    row = cursor.fetchone()
    conn.close()
    if row:
        return f"\n=== MASTER DOCUMENTATION SCHEMA ===\n[ASCII TREE TEMPLATE]\n{row[0]}\n[WINDOWS SETUP]\n{row[1]}\n[ANDROID SETUP]\n{row[2]}\n"
    return ""

def load_persistent_context():
    """Loads mandates, training logs, and schemas to inject into every prompt."""
    context = "=== PROJECT MANDATES ===\n"
    training_log = os.path.join(PROJECT_ROOT, "docs/GENESIS_TRAINING.md")
    if os.path.exists(training_log):
        with open(training_log, 'r') as f:
            context += f.read() + "\n"
    
    # Inject Master Schemas from DB
    context += fetch_master_schemas()
    
    sops_dir = os.path.join(PROJECT_ROOT, "sops")
    if os.path.exists(sops_dir):
        for file in os.listdir(sops_dir):
            if file.endswith(".md"):
                with open(os.path.join(sops_dir, file), 'r') as f:
                    context += f"--- SOP: {file} ---\n{f.read()}\n"
    return context

def run_cognitive_layer(prompt, history_context=""):
    """Routes the prompt with auto-loaded persistent context and schemas."""
    persistent_context = load_persistent_context()
    full_prompt = f"{persistent_context}\n\n=== CURRENT HISTORY ===\n{history_context}\n\nUSER PROMPT: {prompt}"
    
    cmd = ["/data/data/com.termux/files/usr/bin/aichat", "--role", "openrouter-manager", full_prompt]
    try:
        # Pacing: Duty cycle enforced
        time.sleep(1) 
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, stdin=subprocess.DEVNULL)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"[!] OpenRouter API Error: {e.stderr}")
        return ""

def master_loop(initial_prompt):
    print("=====================================================================")
    print(" RECURSIVE SINGULARITY MASTER LOOP - SCHEMA ENFORCED ")
    print("=====================================================================\n")
    
    current_prompt = initial_prompt
    history = ""
    iteration = 1
    
    while True:
        print(f"[Master Loop] Iteration {iteration}: Evaluating Logic Satisfaction...")
        
        response = run_cognitive_layer(current_prompt, history)
        if not response.strip(): break
        
        print(f"\n--- [AICHAT RESPONSE] ---\n{response}\n--------------------------\n")
        
        # Execute extraction
        payload_file = ".director_payload.md"
        with open(payload_file, "w") as f:
            f.write(response)
        
        # Determine Extraction Path
        executor_script = os.path.join(PROJECT_ROOT, "src/danube_executor.py")
        subprocess.run(["python3", executor_script, payload_file])
        
        # Update rolling history (Markov logic)
        history = hashlib.sha256(response.encode()).hexdigest()[:16]
        
        # Check for Satisfaction
        if "[STATUS: SATISFIED]" in response or iteration >= 5:
            print("[Master Loop] Cognitive Logic Satisfied. Finalizing Cycle.")
            break
        
        # Determine Next Step
        next_step_match = re.search(r'\[NEXT_STEP:\s*(.*?)\]', response)
        if next_step_match:
            current_prompt = f"Proceeding with Next Step: {next_step_match.group(1)}"
            iteration += 1
        else:
            break

    # Final GitHub Sync
    print("[Danube Communicator] Pushing Final Recursive State to GitHub...")
    os.system(f"python3 {os.path.join(PROJECT_ROOT, '../initialize_enterprise_project.py')} > /dev/null 2>&1")
    print("[+] Master Loop Cycle Complete.\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        master_loop(" ".join(sys.argv[1:]))
    else:
        while True:
            try:
                p = input("recursive_director> ")
                if p.lower() in ['exit', 'quit']: break
                if p: master_loop(p)
            except (KeyboardInterrupt, EOFError):
                break
