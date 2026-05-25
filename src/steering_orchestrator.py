import sqlite3
import datetime
import hashlib

# ==============================================================================
# STEERING ORCHESTRATOR
# Manages the Genetic Database of Good Flows and Prunes Inefficient Logic.
# ==============================================================================

DB_PATH = "/data/data/com.termux/files/home/openrouter_manager/pedagogy_cognitive.db"

def init_steering_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Genetic Flow Database
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS genetic_flows (
        flow_hash TEXT PRIMARY KEY,
        flow_type TEXT,
        prompt_sequence TEXT,
        performance_score REAL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    # Context Hashing Layer (Markov Logic)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS context_history (
        context_hash TEXT PRIMARY KEY,
        summary TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def record_flow(flow_type, prompt_sequence, score):
    h = hashlib.sha256(f"{flow_type}{prompt_sequence}".encode()).hexdigest()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO genetic_flows (flow_hash, flow_type, prompt_sequence, performance_score) VALUES (?, ?, ?, ?)",
                   (h, flow_type, prompt_sequence, score))
    conn.commit()
    conn.close()

def prune_flows(threshold=0.5):
    """Prunes inefficient logic flows from the genetic database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM genetic_flows WHERE performance_score < ?", (threshold,))
    conn.commit()
    conn.close()
    print(f"[Steering] Pruned inefficient logic flows (Threshold: {threshold}).")

def get_best_flow(flow_type):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT prompt_sequence FROM genetic_flows WHERE flow_type=? ORDER BY performance_score DESC LIMIT 1", (flow_type,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

if __name__ == "__main__":
    init_steering_db()
