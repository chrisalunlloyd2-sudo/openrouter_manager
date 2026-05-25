import sqlite3
import json
import datetime

# [ADVANCE 1 & 2] Cognitive Pedagogy Database
# Stores user preferences, network topology, and execution success patterns.

def init_db():
    conn = sqlite3.connect('pedagogy_cognitive.db')
    cursor = conn.cursor()
    
    # Core Identity & Network Topology
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS identity_matrix (
        key TEXT PRIMARY KEY,
        value TEXT,
        updated_at TEXT
    )
    ''')
    
    # Execution Memory (The Learning Layer)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS execution_memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prompt_hash TEXT,
        action_taken TEXT,
        code_injected TEXT,
        success_score REAL,
        timestamp TEXT
    )
    ''')
    
    # Seed Initial Identity Data
    topology = {
        "github_username": "chrisalunlloyd2-sudo",
        "onedrive_path": "/data/data/com.termux/files/home/storage/shared/OneDrive",
        "desktop_bridge": "active",
        "agentic_network": "danube_orchestrator, aider_injection, openrouter_cognitive",
        "auth_sops": "Environment variables strictly. NEVER hardcode OAuth or Tokens."
    }
    
    for k, v in topology.items():
        cursor.execute('INSERT OR REPLACE INTO identity_matrix (key, value, updated_at) VALUES (?, ?, ?)',
                      (k, v, datetime.datetime.now().isoformat()))
    
    conn.commit()
    conn.close()
    print("[+] Pedagogy DB Initialized: Identity Matrix Seeded.")

if __name__ == "__main__":
    init_db()
