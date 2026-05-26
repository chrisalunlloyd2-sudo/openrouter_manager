import hashlib
import json
import os

class QualityContentEngine:
    def __init__(self):
        self.seen_hashes = set()
        self.state_file = os.path.expanduser("~/.matrix_ide/state/content_hashes.json")
        self._load_state()

    def _load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                self.seen_hashes = set(json.load(f))

    def _save_state(self):
        os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
        with open(self.state_file, 'w') as f:
            json.dump(list(self.seen_hashes), f)

    def is_unique(self, content):
        c_hash = hashlib.sha256(content.encode()).hexdigest()
        if c_hash in self.seen_hashes:
            return False
        self.seen_hashes.add(c_hash)
        self._save_state()
        return True

    def generate_page_metadata(self, count=10):
        topics = ["Evolution", "Genetics", "Domestication", "Anatomy", "Senses", 
                  "Communication", "Social Structure", "Hunting", "Nutrition", "Longevity"]
        return [{"id": i, "topic": topics[i]} for i in range(count)]

if __name__ == "__main__":
    engine = QualityContentEngine()
    print(f"[ContentArchitect] Initialized with {len(engine.seen_hashes)} unique states.")
