import urllib.request
import urllib.error
import sys
import re

# [ADVANCE 3] Autonomous Research Node
# Allows the AI to crawl web pages and ingest documentation into context.

def fetch_content(url):
    try:
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={'User-Agent': 'Mozilla/5.0 (Agentic Research Node)'}
        )
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            # Extremely basic HTML stripping for context digestion
            text = re.sub('<[^<]+?>', ' ', html)
            text = re.sub(r'\s+', ' ', text).strip()
            return text[:5000] # Return first 5k chars to save token context
    except Exception as e:
        return f"[!] Research failed for {url}: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1]
        print(f"[Research Node] Ingesting: {query}")
        result = fetch_content(query)
        print("\n--- INGESTED CONTENT ---\n")
        print(result)
    else:
        print("Usage: python3 research_node.py <URL>")
