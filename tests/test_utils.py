import unittest
from src.utils import utils_function

class TestUtils(unittest.TestCase):
    def test_utils_function(self):
        utils_function()

if __name__ == "__main__":
    unittest.main()
```

[CMD]
```bash
git add src/main.py
git add src/double_consent.py
git add src/utils.py
git add tests/test_main.py
git add tests/test_double_consent.py
git add tests/test_utils.py
git commit -m "Updated source code and tests"
git push origin main
