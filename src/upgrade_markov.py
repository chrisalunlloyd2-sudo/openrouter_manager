import sqlite3

def upgrade_markov_schema():
    print("[+] Upgrading Pedagogy DB for Markov Transition Logic...")
    conn = sqlite3.connect('/data/data/com.termux/files/home/openrouter_manager/pedagogy_cognitive.db')
    cursor = conn.cursor()
    
    # Markov Transition Matrix Table
    # Stores the probability/weight of moving from one architectural state to another
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS markov_transitions (
        current_state TEXT,
        next_action TEXT,
        success_weight REAL DEFAULT 1.0,
        usage_count INTEGER DEFAULT 0,
        PRIMARY KEY (current_state, next_action)
    )
    ''')
    
    # Seed initial Markov states
    states = [
        ('INITIAL', 'WEBCRAWL'),
        ('INITIAL', 'REFACTOR'),
        ('WEBCRAWL', 'ANALYZE'),
        ('ANALYZE', 'REFACTOR'),
        ('REFACTOR', 'TEST'),
        ('TEST', 'COMMIT'),
        ('TEST', 'ROLLBACK')
    ]
    
    for current, action in states:
        cursor.execute("INSERT OR IGNORE INTO markov_transitions (current_state, next_action) VALUES (?, ?)", (current, action))

    conn.commit()
    conn.close()
    print("[+] Markov Logic Schema locked and seeded.")

if __name__ == "__main__":
    upgrade_markov_schema()
