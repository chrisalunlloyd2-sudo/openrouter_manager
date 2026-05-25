import os
import sys
import subprocess
import time
import hashlib
import sqlite3
import re
from monolith_traverser import record_state, get_current_logic

# ==============================================================================
# RECURSIVE DANUBE DIRECTOR (NODE 1) - v10.1 MASTER ENGINE
# Implements Double Consent, Monolith Traversal, and Recursive Evolution.
# ==============================================================================

PROJECT_ROOT = "/data/data/com.termux/files/home/openrouter_manager"

def binomial_consent(task_description):
    """Enforces Double Consent (Binomial Presentation) for massive tasks."""
    print(f"\n[⚠️ SYSTEM BIBLE ALERT] Massive Task Detected: {task_description}")
    print("[1] PROCEED WITH STEP-BY-STEP EVOLUTION")
    print("[2] ABORT MISSION")
    choice = input("Select [1/2]: ")
    return choice == "1"

def run_cognitive_layer(prompt, context_hash=""):
    """Routes the prompt with Markov state injection."""
    full_prompt = f"MARKOV_STATE_HASH: {context_hash}\n\nUSER PROMPT: {prompt}"
    cmd = ["/data/data/com.termux/files/usr/bin/aichat", "--role", "openrouter-manager", full_prompt]
    try:
        time.sleep(2) # Duty cycle
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, stdin=subprocess.DEVNULL)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"[!] OpenRouter API Error: {e.stderr}")
        return ""

def master_loop(initial_prompt):
    print("=====================================================================")
    print(" 🛠️ FOUNDRY MASTER ENGINE v10.1 ACTIVE (DOUBLE CONSENT) ")
    print("=====================================================================\n")
    
    # 1. Detection of Mega-Tasks
    if len(initial_prompt.split()) > 10 or "operating system" in initial_prompt.lower():
        if not binomial_consent(initial_prompt):
            print("[Foundry] Task aborted by user.")
            return

    current_prompt = initial_prompt
    iteration = 1
    project_name = os.path.basename(os.getcwd())
    
    while True:
        # Get logic snapshot from Markov Traverser
        logic_snapshot = get_current_logic(project_name)
        
        print(f"[Master Engine] Iteration {iteration} | Logic State: {logic_snapshot[:20]}...")
        
        response = run_cognitive_layer(current_prompt, logic_snapshot)
        if not response.strip(): break
        
        # Display behavioral markers
        print(f"\n--- [AICHAT v10.1 RESPONSE] ---\n{response}\n--------------------------\n")
        
        # 2. Deterministic Extraction
        payload_file = ".director_payload.md"
        with open(payload_file, "w") as f:
            f.write(response)
        
        executor_script = os.path.join(PROJECT_ROOT, "src/danube_executor.py")
        subprocess.run(["python3", executor_script, payload_file])
        
        # 3. Record State Transition (Markov Logic)
        new_state_hash = record_state(project_name, f"Iter_{iteration}", "GENETIC_EVOLUTION", response[:200])
        
        # Check for Satisfaction
        if "[STATUS: SATISFIED]" in response or iteration >= 5:
            print("[Master Engine] v10.1 Logic Satisfied. Finalizing.")
            break
        
        # Determine Next Step (Axiomatic Traversal)
        next_step_match = re.search(r'\[NEXT_STEP:\s*(.*?)\]', response)
        if next_step_match:
            current_prompt = f"Proceeding with Axiom: {next_step_match.group(1)}"
            iteration += 1
        else:
            break

    # 4. Global GitHub Syphon
    print("[Danube Communicator] Pushing Final Master State to GitHub...")
    os.system(f"python3 /data/data/com.termux/files/home/initialize_enterprise_project.py > /dev/null 2>&1")
    print("[+] Foundry Cycle Complete. Project Standardized Globally.\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        master_loop(" ".join(sys.argv[1:]))
    else:
        while True:
            try:
                p = input("v10.1_engine> ")
                if p.lower() in ['exit', 'quit']: break
                if p: master_loop(p)
            except (KeyboardInterrupt, EOFError):
                break
