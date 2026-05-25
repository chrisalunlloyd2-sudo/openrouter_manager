import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        main()

if __name__ == "__main__":
    unittest.main()


# --- FOUNDRY v10.5 EVOLUTION ---
import unittest
from openrouter_manager.src.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        # Test the main function
        main()

if __name__ == "__main__":
    unittest.main()
```

[CMD]
```bash
git add openrouter_manager/tests/test_main.py
git commit -m "Updated test_main.py with unit tests"
git push origin main
