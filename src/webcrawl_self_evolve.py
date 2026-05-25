import os
import subprocess
import time
import sys

# ==============================================================================
# WEBCRAWL SELF-EVOLVE
# Ingests advanced engineering concepts to fuel the AI's self-improvement.
# ==============================================================================

CRAWLER_PATH = "/data/data/com.termux/files/home/VIPER_SCRIPT_LIBRARY/scripts/advanced_crawler.py"

def ingest_concepts(url):
    print(f"[Self-Evolve] Crawling for advanced concepts at: {url}")
    
    cmd = ["python3", CRAWLER_PATH, url]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        content = res.stdout
        
        # Save to a temporary research buffer for the Director to analyze
        with open("research_buffer.md", "w") as f:
            f.write(f"SOURCE: {url}\n\n=== INGESTED CONTENT ===\n{content}")
        
        print("[+] Concepts ingested and buffered for Markov analysis.")
        return True
    except Exception as e:
        print(f"[!] Crawl failed: {e}")
        return False

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "https://arxiv.org/list/cs.AI/recent"
    ingest_concepts(target)
