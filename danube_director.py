import os
import sys
import subprocess
import time
import hashlib
import sqlite3

# ==============================================================================
# DANUBE DIRECTOR (NODE 1)
# Infinite Access Loop, Headless Routing, and GitHub Syphon
# ==============================================================================

def check_cache(prompt_hash):
    """Sub-DB check to save OpenRouter API tokens on identical requests."""
    conn = sqlite3.connect('/data/data/com.termux/files/home/openrouter_manager/pedagogy_cognitive.db')
    cursor = conn.cursor()
    cursor.execute("SELECT cognitive_response FROM token_efficiency_cache WHERE hash=?", (prompt_hash,))
    row = cursor.fetchone()
    if row:
        cursor.execute("UPDATE token_efficiency_cache SET hits = hits + 1 WHERE hash=?", (prompt_hash,))
        conn.commit()
        conn.close()
        return row[0]
    conn.close()
    return None

def save_cache(prompt_hash, response):
    conn = sqlite3.connect('/data/data/com.termux/files/home/openrouter_manager/pedagogy_cognitive.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO token_efficiency_cache (hash, cognitive_response) VALUES (?, ?)", (prompt_hash, response))
    conn.commit()
    conn.close()

def run_cognitive_layer(prompt):
    """Routes the sanitized prompt exclusively to Headless OpenRouter."""
    prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()
    
    cached_response = check_cache(prompt_hash)
    if cached_response:
        print("[Danube Director] High Efficiency: Exact prompt found in Sub-DB cache. Bypassing API.")
        return cached_response

    print("[OpenRouter API] Cognitive engine thinking (Headless Mode)...")
    cmd = ["/data/data/com.termux/files/usr/bin/aichat", "--role", "openrouter-manager", prompt]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        save_cache(prompt_hash, result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"[!] OpenRouter API Error: {e.stderr}")
        return ""

def main():
    # --- BOOTSTRAP CHECK (GEN 8) ---
    if not os.path.exists("/data/data/com.termux/files/home/txt.txt"):
        print("[Danube Director] Bootstrap anomaly detected: txt.txt missing.")
        print("[Danube Director] Manifesting txt.txt...")
        with open("/data/data/com.termux/files/home/txt.txt", "w") as f:
            f.write("GEN 8 H2O MATRIX BOOTSTRAP\n")
        print("[Danube Director] txt.txt stamped. Substrate verified.\n")

    print("=====================================================================")
    print(" DETERMINISTIC ARCHITECTURE ACTIVE ")
    print(" 1. Headless OpenRouter | 2. Danube Extractor | 3. GitHub Syphon ")
    print("=====================================================================\n")
    
    while True:
        try:
            # Infinite Loop Access
            user_input = input("director> ")
            if user_input.strip().lower() in ['exit', 'quit']:
                break
            if not user_input.strip():
                continue
            
            # --- PHASE 1: HEADLESS COGNITIVE ---
            plan = run_cognitive_layer(user_input)
            
            if not plan.strip():
                continue
                
            # --- PHASE 2: DETERMINISTIC EXTRACTION ---
            payload_file = ".director_payload.md"
            with open(payload_file, "w") as f:
                f.write(plan)
            
            subprocess.run(["python3", "danube_executor.py", payload_file])
            
            # --- PHASE 3: GITHUB SYPHON ---
            print("[Danube Communicator] Pushing exact state to GitHub Seed...")
            os.system("python3 github_operator.py 'autonomous: headless danube extraction' > /dev/null 2>&1")
            
            print("[Danube Communicator] Cycle Complete. Infinite Access loop continues. Standing by.\n")
            
        except KeyboardInterrupt:
            print("\n[!] Director shutting down.")
            break
        except EOFError:
            break

if __name__ == "__main__":
    main()
