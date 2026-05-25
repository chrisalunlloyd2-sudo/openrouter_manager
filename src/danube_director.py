import os
import sys
import subprocess
import time
import hashlib
import sqlite3
import re

# ==============================================================================
# RECURSIVE DANUBE DIRECTOR (NODE 1)
# Implements Master Loop, Context Hashing, and Steering Integration.
# ==============================================================================

DB_PATH = "/data/data/com.termux/files/home/openrouter_manager/pedagogy_cognitive.db"

def hash_context(text):
    """Markov-inspired context hashing to manage long-term state."""
    return hashlib.sha256(text.encode()).hexdigest()[:16]

def save_context_summary(h, summary):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO context_history (context_hash, summary) VALUES (?, ?)", (h, summary))
    conn.commit()
    conn.close()

def run_cognitive_layer(prompt, context=""):
    """Routes the prompt to OpenRouter with recursive context injection."""
    full_prompt = f"CONTEXT SNAPSHOT: {context}\n\nUSER PROMPT: {prompt}"
    cmd = ["/data/data/com.termux/files/usr/bin/aichat", "--role", "openrouter-manager", full_prompt]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True, stdin=subprocess.DEVNULL)
        return res.stdout
    except subprocess.CalledProcessError as e:
        print(f"[!] OpenRouter API Error: {e.stderr}")
        return ""

def master_loop(initial_prompt):
    print("=====================================================================")
    print(" RECURSIVE SINGULARITY MASTER LOOP ACTIVE ")
    print("=====================================================================\n")
    
    current_prompt = initial_prompt
    context = ""
    iteration = 1
    
    while True:
        print(f"[Master Loop] Iteration {iteration}: Evaluating Logic Satisfaction...")
        
        response = run_cognitive_layer(current_prompt, context)
        if not response.strip(): break
        
        # Display AI behavior
        print(f"\n--- [AICHAT RESPONSE] ---\n{response}\n--------------------------\n")
        
        # Execute extraction
        payload_file = ".director_payload.md"
        with open(payload_file, "w") as f:
            f.write(response)
        subprocess.run(["python3", "/data/data/com.termux/files/home/openrouter_manager/src/danube_executor.py", payload_file])
        
        # Hash context for Markov memory
        ctx_hash = hash_context(response)
        save_context_summary(ctx_hash, f"Iteration {iteration} summary")
        context = ctx_hash # Update rolling context
        
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
            print("[Master Loop] No explicit next step found. Defaulting to satisfied.")
            break

    # Final GitHub Sync
    print("[Danube Communicator] Pushing Final Recursive State to GitHub...")
    os.system("python3 /data/data/com.termux/files/home/initialize_enterprise_project.py > /dev/null 2>&1")
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
