import os
import sys
import subprocess
import re
import time
import hashlib

# ==============================================================================
# PACED DANUBE ORCHESTRATOR
# Manages the flow: Danube (Pacing/Filtering) -> OpenRouter API -> Aider -> GitHub
# ==============================================================================

# Pacing: Max 15 pings per minute = 1 ping every 4 seconds minimum
MIN_PING_INTERVAL_SEC = 4.0
last_ping_time = 0.0

def print_topic_update(title, summary, intent):
    """Mirrors the agentic topic update structure."""
    print(f"\n[Danube Orchestrator: State Transition]")
    print(f"Current phase: \"{title}\"")
    print(f"Action summary: {summary}")
    print(f"Strategic Intent: {intent}\n")

def enforce_pacing():
    """Ensures we do not exceed OpenRouter API ping limits."""
    global last_ping_time
    now = time.time()
    elapsed = now - last_ping_time
    if elapsed < MIN_PING_INTERVAL_SEC:
        sleep_time = MIN_PING_INTERVAL_SEC - elapsed
        print(f"[Danube Orchestrator] Enforcing duty cycle. Pacing API request for {sleep_time:.2f}s...")
        time.sleep(sleep_time)
    last_ping_time = time.time()

def run_cognitive_layer(prompt):
    """Hits the OpenRouter API via aichat CLI."""
    enforce_pacing()
    print("[OpenRouter API] Serving cognitive request. Awaiting response...")
    # Use the injected pedagogy role
    cmd = ["aichat", "--role", "openrouter-manager-v2", prompt]
    try:
        # We capture output to prevent messy TUI overlap, we are acting as a headless backend
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"[!] OpenRouter API Error: {e.stderr}")
        return ""

def run_execution_layer(plan):
    """Extracts commands and uses Aider to implement changes."""
    print("[Danube Orchestrator] Routing generated code to Execution Layer (Aider)...")
    
    # If no code blocks are found, we can skip aider to save time, but aider handles text fine.
    # Write plan to a temporary file to pass to aider safely
    with open(".matrix_temp_plan.md", "w") as f:
        f.write(plan)
        
    cmd = ["aider", "--message-file", ".matrix_temp_plan.md", "--yes", "--no-auto-commits"]
    try:
        # Redirect stdout to devnull to keep the terminal clean, only show errors
        subprocess.run(cmd, stdout=subprocess.DEVNULL)
        print("[+] Execution Layer successfully applied code changes.")
    except Exception as e:
        print(f"[!] Execution Layer Failed. Is aider installed? Error: {e}")
    finally:
        if os.path.exists(".matrix_temp_plan.md"):
            os.remove(".matrix_temp_plan.md")

def run_sync_layer(message):
    """Triggers the Github Operator to upload."""
    print("[Danube Orchestrator] Syphoning state to GitHub...")
    cmd = ["python3", "github_operator.py", message]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("[+] GitHub Syphon Complete. State synchronized.")

def main():
    print("=====================================================================")
    print(" DANUBE ORCHESTRATOR - PACED EXECUTION ENGINE ACTIVE ")
    print(" Architecture: [Terminal] -> [Danube Filter] -> [OpenRouter API] ")
    print("               -> [Aider Execution] -> [GitHub Syphon] -> [Terminal] ")
    print(f" Pacing: Maximum 15 pings/minute ({MIN_PING_INTERVAL_SEC}s duty cycle)")
    print("=====================================================================\n")
    
    while True:
        try:
            # Danube Input Filter
            user_input = input("danube_orchestrator> ")
            if user_input.strip().lower() in ['exit', 'quit']:
                break
            if not user_input.strip():
                continue
            
            # --- 1. COGNITIVE PHASE ---
            print_topic_update(
                title="Cognitive API Processing",
                summary="Danube is pacing the request and routing the sanitized input to the OpenRouter API. OpenRouter will generate the architectural logic.",
                intent="Querying cognitive engine for code performatives."
            )
            
            plan = run_cognitive_layer(user_input)
            
            if not plan.strip():
                print("[Danube Orchestrator] Received empty response from OpenRouter API. Aborting cycle.")
                continue
                
            # Print a clean snippet of what the AI decided
            print(f"\n[OpenRouter API Output (Truncated)]\n{plan[:300]}...\n")
            
            # --- 2. EXECUTION PHASE ---
            print_topic_update(
                title="Aider Execution Routing",
                summary="Danube has received the cognitive plan and is now injecting it into the Aider headless process to surgically modify the workspace files.",
                intent="Applying AI-generated code to local filesystem."
            )
            
            run_execution_layer(plan)
            
            # --- 3. SYPHON PHASE ---
            print_topic_update(
                title="GitHub State Syphoning",
                summary="Execution complete. Danube is now triggering the GitHub Operator to commit and push changes, establishing the seed state for the next recursive cycle.",
                intent="Persisting execution state to GitHub repository."
            )
            
            commit_msg = f"autonomous: {user_input[:40]}..."
            run_sync_layer(commit_msg)
            
            print("\n[Danube Orchestrator] Recursive cycle finished. Standing by for next state hash.")
            print("---------------------------------------------------------------------\n")
            
        except KeyboardInterrupt:
            print("\n[!] Orchestrator loop interrupted by user.")
            break
        except EOFError:
            break

if __name__ == "__main__":
    main()
