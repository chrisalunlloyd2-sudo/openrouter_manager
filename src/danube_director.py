import os
import sys
import subprocess
import time
import re
from danube_chooser import choose_model

# ==============================================================================
# DATA CIRCLE SUBSTRATE (v11.0)
# The AI-Driven steering engine. The AI Pilot controls the loop, not the script.
# ==============================================================================

PROJECT_ROOT = "/data/data/com.termux/files/home/openrouter_manager"

def run_cognitive_layer(prompt, model):
    """Routes the prompt to the AI Pilot with full project context."""
    # Aggressive context loading
    training_log = os.path.join(PROJECT_ROOT, "docs/GENESIS_TRAINING.md")
    sops_log = os.path.join(PROJECT_ROOT, "sops/TODO.md")
    
    context = "=== DATA CIRCLE PILOT CONTEXT ===\n"
    if os.path.exists(training_log):
        context += open(training_log).read() + "\n"
    if os.path.exists(sops_log):
        context += open(sops_log).read() + "\n"
        
    full_prompt = f"{context}\n\nUSER PROMPT: {prompt}"
    
    cmd = ["/data/data/com.termux/files/usr/bin/aichat", "--model", model, "--role", "openrouter-manager", full_prompt]
    try:
        time.sleep(2) # Duty Cycle
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, stdin=subprocess.DEVNULL)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"[!] Substrate API Error: {e.stderr}")
        return ""

def pilot_steering_loop(initial_prompt):
    print("=====================================================================")
    print(" 🌀 RECURSIVE DATA CIRCLE ACTIVE | PILOT AT THE HELM ")
    print("=====================================================================\n")
    
    current_prompt = initial_prompt
    iteration = 1
    
    while True:
        model = choose_model(current_prompt)
        print(f"[Substrate] Epoch {iteration}: AI Pilot is steering logic...")
        
        response = run_cognitive_layer(current_prompt, model)
        if not response.strip(): break
        
        # Display AI's actual behavior
        print(f"\n--- [AI PILOT RESPONSE] ---\n{response}\n--------------------------\n")
        
        # --- 1. DATA INJECTION ---
        payload_file = ".pilot_payload.md"
        with open(payload_file, "w") as f:
            f.write(response)
        
        executor_script = os.path.join(PROJECT_ROOT, "src/danube_executor.py")
        subprocess.run(["python3", executor_script, payload_file])
        
        # --- 2. STEERING ANALYSIS ---
        if "[STEER: SYPHON]" in response:
            print("[Substrate] AI Pilot has commanded: SYPHON. Pushing to GitHub.")
            os.system(f"python3 {os.path.join(PROJECT_ROOT, '../initialize_enterprise_project.py')} > /dev/null 2>&1")
            break
            
        elif "[STEER: MUTATE]" in response:
            print("[Substrate] AI Pilot has commanded: MUTATE. Initiating architectural evolution.")
            current_prompt = f"Previous Epoch Response: {response[:1000]}\n\nDIRECTIVE: Implement the architectural mutation you proposed. Expand the System Bible. Ensure 30x performance gain."
            
        elif "[STEER: REFINE]" in response or iteration < 3: # Default minimal loops
            print("[Substrate] AI Pilot has commanded: REFINE. Proceeding to next genetic pass.")
            current_prompt = f"Previous Epoch Response: {response[:1000]}\n\nDIRECTIVE: Self-critique and refactor. Improve articulation and documentation fidelity. Fix any mistakes."
            
        else:
            # Fallback
            print("[Substrate] No steering signal detected. Defaulting to SYPHON.")
            os.system(f"python3 {os.path.join(PROJECT_ROOT, '../initialize_enterprise_project.py')} > /dev/null 2>&1")
            break
            
        iteration += 1
        if iteration > 10: # Safety guard
            print("[Substrate] Cycle limit reached. Forcing SYPHON.")
            os.system(f"python3 {os.path.join(PROJECT_ROOT, '../initialize_enterprise_project.py')} > /dev/null 2>&1")
            break

    print("\n[+] Data Circle Cycle Complete. AI Pilot has finalized the epoch.\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pilot_steering_loop(" ".join(sys.argv[1:]))
    else:
        while True:
            try:
                p = input("data_circle_pilot> ")
                if p.lower() in ['exit', 'quit']: break
                if p: pilot_steering_loop(p)
            except (KeyboardInterrupt, EOFError):
                break
