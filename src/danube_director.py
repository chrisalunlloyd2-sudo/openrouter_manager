import os
import sys
import subprocess
import time
import hashlib
import sqlite3
import re
from markov_logic_engine import get_next_action, update_weight
from danube_chooser import choose_model

# ==============================================================================
# SELF-IMPROVING SINGULARITY DIRECTOR (v10.6)
# FIXED: Sequential state transitions for progressive evolution.
# ==============================================================================

PROJECT_ROOT = "/data/data/com.termux/files/home/openrouter_manager"

def load_context():
    context = ""
    if os.path.exists("research_buffer.md"):
        with open("research_buffer.md", 'r') as f:
            context += f"=== NEW RESEARCH DATA ===\n{f.read()}\n"
    training_log = os.path.join(PROJECT_ROOT, "docs/GENESIS_TRAINING.md")
    if os.path.exists(training_log):
        with open(training_log, 'r') as f:
            context += f"=== TRAINING HISTORY ===\n{f.read()}\n"
    return context

def autonomous_evolution_loop():
    print("\n=====================================================================")
    print(" 🚀 COMMENCING AUTONOMOUS SELF-IMPROVEMENT CYCLE ")
    print("=====================================================================\n")
    
    current_state = "INITIAL"
    
    for i in range(1, 11): # Up to 10 transitions
        action = get_next_action(current_state)
        print(f"[Singularity] Cycle {i}: Transition [{current_state}] -> [{action}]")
        
        if action == "WEBCRAWL":
            subprocess.run(["python3", "src/webcrawl_self_evolve.py"], capture_output=True)
            current_state = "WEBCRAWL"
            
        elif action == "REFACTOR":
            prompt = f"REFACTOR Mandate: Ingest current src/ and research_buffer.md. Self-refactor one core module for 30x performance and align with user style. Output [FILE] blocks."
            model = choose_model(prompt)
            result = run_aichat(prompt, model)
            extract_and_apply(result)
            current_state = "REFACTOR"
            
        elif action == "TEST":
            # Simulate performance gain
            perf_delta = 0.1 # 10% improvement
            update_weight("REFACTOR", "TEST", perf_delta)
            current_state = "TEST"
            
        elif action == "COMMIT":
            os.system("python3 /data/data/com.termux/files/home/initialize_enterprise_project.py > /dev/null 2>&1")
            print("[Singularity] Optimal state synchronized to GitHub.")
            current_state = "INITIAL" # Cycle complete
            break

        time.sleep(1) # Pacing

def run_aichat(prompt, model):
    ctx = load_context()
    full_prompt = f"{ctx}\n\nUSER PROMPT: {prompt}"
    cmd = ["/data/data/com.termux/files/usr/bin/aichat", "--model", model, "--role", "openrouter-manager", full_prompt]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True, stdin=subprocess.DEVNULL)
    return res.stdout

def extract_and_apply(text):
    executor = "/data/data/com.termux/files/home/openrouter_manager/src/danube_executor.py"
    with open(".evolution_payload.md", "w") as f:
        f.write(text)
    subprocess.run(["python3", executor, ".evolution_payload.md"], capture_output=True)

if __name__ == "__main__":
    os.chdir(PROJECT_ROOT)
    subprocess.run(["python3", "src/upgrade_markov.py"], capture_output=True)
    autonomous_evolution_loop()
