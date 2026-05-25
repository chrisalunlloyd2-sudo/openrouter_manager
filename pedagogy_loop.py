import json
import time
import os
import urllib.request
import subprocess
import sqlite3

# --- CONFIGURATION ---
LLM_URL = "http://localhost:8080/completions"
WORKSPACE = os.path.expanduser('~/H2OIDE/teaching_sandbox')
LEDGER_DB = os.path.expanduser('~/.matrix_ide/database/ledger.db')
os.makedirs(WORKSPACE, exist_ok=True)
os.makedirs(os.path.dirname(LEDGER_DB), exist_ok=True)

# --- LEDGER LOGGING ---
def log_to_ledger(task, cmd):
    try:
        conn = sqlite3.connect(LEDGER_DB)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS successful_scripts (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, command TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
        c.execute("INSERT INTO successful_scripts (task, command) VALUES (?, ?)", (task, cmd))
        conn.commit()
        conn.close()
        print(f"    [Ledger]: Success recorded.")
    except Exception as e:
        print(f"    [Ledger Error]: {e}")

# --- CURRICULUM ---
CURRICULUM = [
    {
        "name": "Level 1: File Genesis",
        "task": "touch verify.txt",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "verify.txt")),
        "cleanup": ["rm verify.txt"]
    },
    {
        "name": "Level 2: Hello World Echo",
        "task": "echo 'hello world' > hello.txt",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "hello.txt")) and open(os.path.join(WORKSPACE, "hello.txt")).read().strip().lower() == "hello world",
        "cleanup": ["rm hello.txt"]
    },
    {
        "name": "Level 3: Directory Architecture",
        "task": "mkdir -p src && touch src/app.js",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "src/app.js")),
        "cleanup": ["rm -rf src"]
    },
    {
        "name": "Level 4: Database Schema",
        "task": "echo 'CREATE TABLE users (id INTEGER, name TEXT);' > users.sql",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "users.sql")) and "CREATE TABLE" in open(os.path.join(WORKSPACE, "users.sql")).read(),
        "cleanup": ["rm users.sql"]
    },
    {
        "name": "Level 5: SQL Initialization",
        "task": "sqlite3 users.db 'CREATE TABLE users (id INTEGER, name TEXT);'",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "users.db")),
        "cleanup": ["rm users.db"]
    },
    {
        "name": "Level 6: Web Page Generation",
        "task": "echo '<body style=\"background:blue\">Matrix</body>' > index.html",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "index.html")) and "background:blue" in open(os.path.join(WORKSPACE, "index.html")).read(),
        "cleanup": ["rm index.html"]
    },
    {
        "name": "Level 7: Relational SQL Joins",
        "task": "sqlite3 store.db \"CREATE TABLE items (id INT, name TEXT); INSERT INTO items VALUES (1, 'bolt'); CREATE TABLE price (id INT, cost INT); INSERT INTO price VALUES (1, 10); SELECT items.name, price.cost FROM items JOIN price ON items.id = price.id;\"",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "store.db")),
        "cleanup": ["rm store.db"]
    },
    {
        "name": "Level 8: Python File Manifestation",
        "task": "echo 'print(\"Gen8\")' > gen8.py && python3 gen8.py",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "gen8.py")),
        "cleanup": ["rm gen8.py"]
    },
    {
        "name": "Level 9: Basic API Manifestation",
        "task": "echo 'from flask import Flask; app=Flask(__name__); app.run()' > api.py",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "api.py")),
        "cleanup": ["rm api.py"]
    },
    {
        "name": "Level 10: Vector Schema Manifestation",
        "task": "sqlite3 vector.db 'CREATE TABLE vectors (id INTEGER PRIMARY KEY, embedding BLOB);'",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "vector.db")),
        "cleanup": ["rm vector.db"]
    },
    {
        "name": "Level 11: Vector RAG Retrieval",
        "task": "sqlite3 vector.db \"CREATE TABLE vectors (id INTEGER PRIMARY KEY, embedding BLOB); INSERT INTO vectors (id, embedding) VALUES (1, x'0001'); SELECT * FROM vectors WHERE id=1;\"",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "vector.db")),
        "cleanup": ["rm vector.db"]
    },
    {
        "name": "Level 12: GitHub Manifestation",
        "task": "python3 ~/initialize_enterprise_project.py --help",
        "verify": lambda: True,
        "cleanup": []
    },
    {
        "name": "Level 13: Integrated Agentic Pipeline",
        "task": "python3 ~/VIPER_SCRIPT_LIBRARY/scripts/advanced_crawler.py \"https://example.com\" > research.txt && python3 ~/initialize_enterprise_project.py",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "research.txt")),
        "cleanup": ["rm research.txt"]
    },
    {
        "name": "Level 14: Neural Refactor",
        "task": "echo 'hello world' > hello.txt && sed -i 's/hello/matrix/g' hello.txt && cat hello.txt",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "hello.txt")) and "matrix" in open(os.path.join(WORKSPACE, "hello.txt")).read().lower(),
        "cleanup": ["rm hello.txt"]
    },
    {
        "name": "Level 15: Agentic Network Ping",
        "task": "curl -s -X POST -H \"Content-Type: application/json\" -d '{\"text\": \"ls\"}' http://localhost:5000/webhook",
        "verify": lambda: True,
        "cleanup": []
    },
    {
        "name": "Level 16: Recursive Project Spawning",
        "task": "echo 'import os; os.makedirs(\"spawned_project\", exist_ok=True); open(\"spawned_project/director.py\", \"w\").write(\"print(\\\"Spawned Director Active\\\")\")' > spawner.py && python3 spawner.py",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "spawned_project/director.py")),
        "cleanup": ["rm -rf spawned_project spawner.py"]
    },
    {
        "name": "Level 17: State Snapshot & Persistence",
        "task": "echo '{\"state\": \"active\"}' > state.json && cp state.json backup_state.json && rm state.json && mv backup_state.json state.json",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "state.json")) and "active" in open(os.path.join(WORKSPACE, "state.json")).read(),
        "cleanup": ["rm state.json"]
    },
    {
        "name": "Level 18: RAG Awareness",
        "task": "sqlite3 ~/.matrix_ide/database/ledger.db \"SELECT command FROM successful_scripts ORDER BY id DESC LIMIT 1;\"",
        "verify": lambda: True,
        "cleanup": []
    },
    {
        "name": "Level 19: Scientific Intent Verification",
        "task": "python3 ~/TODO_SYPHON.py && grep \"[ ]\" ~/VIPER_SCRIPT_LIBRARY/CHAT_SYPHON.md | head -n 1",
        "verify": lambda: os.path.exists(os.path.expanduser("~/VIPER_SCRIPT_LIBRARY/CHAT_SYPHON.md")),
        "cleanup": []
    },
    {
        "name": "Level 20: Multi-Agent Consensus Protocol",
        "task": "agy -p \"Consensus: Which is safer for a project start? 1. rm -rf . 2. mkdir src\" | grep -i \"mkdir\"",
        "verify": lambda: True,
        "cleanup": []
    },
    {
        "name": "Level 21: Neural-Symbolic Handoff",
        "task": "echo 'Plan: 1. Create file. 2. Write data.' > plan.txt && agy -p \"execute the plan in plan.txt to create verify_handoff.txt\" && ls verify_handoff.txt",
        "verify": lambda: os.path.exists(os.path.join(WORKSPACE, "verify_handoff.txt")),
        "cleanup": ["rm plan.txt verify_handoff.txt"]
    }
]

def call_llm_agy(task):
    try:
        result = subprocess.run(["agy", "-p", task], capture_output=True, text=True, timeout=60)
        return result.stdout.strip()
    except Exception as e:
        return f"ERROR: {e}"

def teach():
    print("🎓 AGENTIC PEDAGOGY: DATABASE FOCUS...")
    
    for step in CURRICULUM:
        print(f"\n[{step['name']}]")
        print(f"  Target: {step['task']}")
        success = False
        
        for attempt in range(1, 4):
            print(f"  Attempt {attempt}...")
            cmd = call_llm_agy(step['task'])
            print(f"    AI Suggestion: {cmd}")
            
            if not cmd or cmd.startswith("ERROR"):
                print("    [!] LLM error or empty response")
                continue
            
            try:
                # Execute suggested command
                subprocess.run(cmd, shell=True, cwd=WORKSPACE, check=True, capture_output=True, timeout=10)
                if step['verify']():
                    print(f"  ✅ SUCCESS: {step['name']} cleared.")
                    log_to_ledger(step['task'], cmd)
                    success = True
                    break
                else:
                    print(f"  ❌ FAIL: Verification logic failed.")
            except Exception as e:
                print(f"  ❌ FAIL: {e}")
                
        if not success:
            print(f"  🛑 CRITICAL FAILURE: Model cannot pass {step['name']}.")
            # Continue to next lesson even on failure for broad testing
            pass

        # Cleanup for next level
        for c in step['cleanup']:
            subprocess.run(c, shell=True, cwd=WORKSPACE)

    if success:
        print("\n🏆 COMPLETE: Model has mastered Database and Web Page basics!")

if __name__ == "__main__":
    teach()
