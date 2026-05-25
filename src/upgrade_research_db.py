import sqlite3

def upgrade_db():
    print("[+] Upgrading Cognitive DB with Research & Case Study schemas...")
    conn = sqlite3.connect('/data/data/com.termux/files/home/openrouter_manager/pedagogy_cognitive.db')
    cursor = conn.cursor()
    
    # Case Studies Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS case_studies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        summary TEXT,
        findings_blob TEXT,
        sources TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Research Queue
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS research_queue (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT,
        status TEXT DEFAULT 'PENDING',
        priority INTEGER DEFAULT 1
    )
    ''')
    
    conn.commit()
    conn.close()
    print("[+] Research schemas locked.")

if __name__ == "__main__":
    upgrade_db()
