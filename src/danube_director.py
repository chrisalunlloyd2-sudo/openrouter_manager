import os
import sys
import subprocess
import time
import hashlib
import sqlite3
import re
import json
import os
import sys
import subprocess
import time
import hashlib
import sqlite3
import re
from danube_chooser import choose_model

# ==============================================================================
# RECURSIVE DANUBE DIRECTOR (NODE 1) - v11.1 JSON-Action Pipeline
# ==============================================================================

QUEUE_DIR = os.path.expanduser("~/.matrix_ide/state/action_queue")
os.makedirs(QUEUE_DIR, exist_ok=True)

def distill_tasks_to_json(ai_response):
    """Parses [ACTION: ...] blocks and serializes to JSON steps."""
    action_blocks = re.findall(r'\[ACTION:\s*(\w+)\s*\]\s*([\s\S]*?)(?=\[ACTION:|$)', ai_response)
    for i, (performative, payload) in enumerate(action_blocks):
        step_id = f"{int(time.time())}_{i:03d}"
        task = {"performative": performative.strip(), "payload": payload.strip()}
        with open(os.path.join(QUEUE_DIR, f"{step_id}.json"), "w") as f:
            json.dump(task, f)
    print(f"[+] Distilled {len(action_blocks)} actions into pipeline.")

# (Existing Danube Logic continued...)
def run_cognitive_layer(prompt, history_context=""):
    persistent_context = load_persistent_context()
    full_prompt = f"{persistent_context}\n\n=== HISTORY HASH: {history_context} ===\n\nUSER PROMPT: {prompt}. \nInstruction: Distill your response into [ACTION: PERFORM] steps."
    # ... remainder of run_cognitive_layer ...


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
