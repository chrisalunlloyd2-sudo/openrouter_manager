import os
import sys
import subprocess
import time
import hashlib
import sqlite3
import re
from danube_chooser import choose_model

# ==============================================================================
# RECURSIVE DANUBE DIRECTOR (NODE 1) - v11.1 CONTEXT-EFFICIENT
# Optimized context loading to prevent token overflow/budget crashes.
# ==============================================================================

PROJECT_ROOT = "/data/data/com.termux/files/home/openrouter_manager"

def load_persistent_context():
    """Loads a truncated, efficient context snapshot."""
    context = "=== PROJECT MANDATES (TRUNCATED) ===\n"
    
    # 1. Training Log Snippet
    training_log = os.path.join(PROJECT_ROOT, "docs/GENESIS_TRAINING.md")
    if os.path.exists(training_log):
        with open(training_log, 'r') as f:
            # Only take the first 1k chars of training log
            context += f.read()[:1000] + "\n"
    
    # 2. SOP Snippet (Avoiding huge TODO.md)
    sops_dir = os.path.join(PROJECT_ROOT, "sops")
    if os.path.exists(sops_dir):
        for file in os.listdir(sops_dir):
            if file.endswith(".md"):
                file_path = os.path.join(sops_dir, file)
                # If it's TODO.md, only take the LAST 1k chars (most recent tasks)
                if file == "TODO.md":
                    with open(file_path, 'r') as f:
                        f.seek(max(0, os.path.getsize(file_path) - 1000))
                        context += f"--- RECENT SOP: {file} ---\n... {f.read()}\n"
                else:
                    with open(file_path, 'r') as f:
                        context += f"--- SOP: {file} ---\n{f.read()[:500]}\n"
    return context

def run_cognitive_layer(prompt, history_context=""):
    persistent_context = load_persistent_context()
    full_prompt = f"{persistent_context}\n\n=== HISTORY HASH: {history_context} ===\n\nUSER PROMPT: {prompt}"
    
    model = choose_model(prompt)
    cmd = ["/data/data/com.termux/files/usr/bin/aichat", "--model", model, "--role", "openrouter-manager", full_prompt]
    try:
        time.sleep(2) 
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, stdin=subprocess.DEVNULL)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"[!] OpenRouter API Error: {e.stderr}")
        return ""

def binomial_consent(task):
    print(f"\n[⚠️  SYSTEM BIBLE] Massive Task Detected: {task}")
    print("[1] PROCEED | [2] ABORT")
    if sys.stdin.isatty():
        return input("Select [1/2]: ") == "1"
    return True # Auto-consent in non-interactive batch mode

def master_loop(initial_prompt):
    print("=====================================================================")
    print(" 🌀 RECURSIVE DATA CIRCLE - CONTEXT OPTIMIZED ")
    print("=====================================================================\n")
    
    if "operating system" in initial_prompt.lower() or len(initial_prompt) > 200:
        if not binomial_consent(initial_prompt): return

    current_prompt = initial_prompt
    history = ""
    iteration = 1
    
    while iteration <= 5:
        print(f"[Master Loop] Iteration {iteration}...")
        response = run_cognitive_layer(current_prompt, history)
        if not response.strip(): break
        
        print(f"\n--- [AI PILOT RESPONSE] ---\n{response[:300]}...\n")
        
        payload_file = ".pilot_payload.md"
        with open(payload_file, "w") as f:
            f.write(response)
        
        executor_script = os.path.join(PROJECT_ROOT, "src/danube_executor.py")
        subprocess.run(["python3", executor_script, payload_file])
        
        history = hashlib.sha256(response.encode()).hexdigest()[:16]
        
        if "[STATUS: SATISFIED]" in response: break
        
        next_step_match = re.search(r'\[NEXT_STEP:\s*(.*?)\]', response)
        if next_step_match:
            current_prompt = f"Proceed with Next Step: {next_step_match.group(1)}"
            iteration += 1
        else: break

    os.system(f"python3 {os.path.join(PROJECT_ROOT, '../initialize_enterprise_project.py')} > /dev/null 2>&1")
    print("[+] Cycle Complete.\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        master_loop(" ".join(sys.argv[1:]))
    else:
        while True:
            try:
                p = input("data_circle_pilot> ")
                if p.lower() in ['exit', 'quit']: break
                if p: master_loop(p)
            except (KeyboardInterrupt, EOFError): break
