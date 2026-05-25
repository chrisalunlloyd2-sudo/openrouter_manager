import sqlite3

def upgrade_schema():
    print("[+] Upgrading Cognitive Database Schema...")
    conn = sqlite3.connect('/data/data/com.termux/files/home/openrouter_manager/pedagogy_cognitive.db')
    cursor = conn.cursor()
    
    # Enforce API boundaries at the database level
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS api_constraints (
        constraint_id TEXT PRIMARY KEY,
        rule_definition TEXT,
        enforcement_level TEXT
    )
    ''')
    cursor.execute("INSERT OR REPLACE INTO api_constraints VALUES ('NO_GEMINI', 'Strictly block openrouter:google/gemini models', 'ABSOLUTE')")
    cursor.execute("INSERT OR REPLACE INTO api_constraints VALUES ('NO_GOOGLE', 'Strictly block any Google-affiliated API endpoints', 'ABSOLUTE')")
    cursor.execute("INSERT OR REPLACE INTO api_constraints VALUES ('REQUIRE_OPENROUTER', 'All cognitive routing must pass exclusively through openrouter.ai/api', 'ABSOLUTE')")

    # Enterprise Documentation Templates
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS enterprise_schemas (
        schema_name TEXT PRIMARY KEY,
        ascii_topology_template TEXT,
        windows_instructions TEXT,
        android_instructions TEXT,
        dependency_format TEXT
    )
    ''')
    
    ascii_template = """
├── .git/
├── README.md
├── src/
│   └── main.py
└── tests/
    """
    
    win_setup = "1. Install Python 3.10+ from python.org\n2. Open PowerShell\n3. Run: pip install -r requirements.txt\n4. Execute: python src/main.py"
    and_setup = "1. Install Termux\n2. pkg install python git\n3. pip install -r requirements.txt\n4. python src/main.py"
    
    cursor.execute("INSERT OR REPLACE INTO enterprise_schemas VALUES ('standard_project', ?, ?, ?, '- {dependency}: {reason}')",
                   (ascii_template, win_setup, and_setup))

    conn.commit()
    conn.close()
    print("[+] Schema upgrade complete. Constraints locked.")

if __name__ == "__main__":
    upgrade_schema()
