import sqlite3
import random

# ==============================================================================
# MARKOV LOGIC ENGINE v1.0
# Calculates state transition probabilities for autonomous self-improvement.
# ==============================================================================

DB_PATH = "/data/data/com.termux/files/home/openrouter_manager/pedagogy_cognitive.db"

def get_next_action(current_state):
    """Uses Markov weights to decide the next step in the evolution loop."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT next_action, success_weight FROM markov_transitions WHERE current_state=?", (current_state,))
    options = cursor.fetchall()
    conn.close()
    
    if not options:
        return "INITIAL"
    
    # Weighted random selection
    total_weight = sum(opt[1] for opt in options)
    r = random.uniform(0, total_weight)
    upto = 0
    for action, weight in options:
        if upto + weight >= r:
            return action
        upto += weight
    return options[0][0]

def update_weight(current_state, action, performance_delta):
    """Updates the Markov transition weight based on successful performance increase."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Adjust weight: performance_delta is expected to be positive for improvement
    cursor.execute('''
        UPDATE markov_transitions 
        SET success_weight = MAX(0.1, success_weight + ?),
            usage_count = usage_count + 1
        WHERE current_state=? AND next_action=?
    ''', (performance_delta, current_state, action))
    
    conn.commit()
    conn.close()
    print(f"[Markov Engine] Weight adjusted for {current_state} -> {action} by {performance_delta:.4f}")

if __name__ == "__main__":
    # Test
    print(f"Decided Next Action from INITIAL: {get_next_action('INITIAL')}")
