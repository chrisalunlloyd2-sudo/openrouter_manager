import unittest
from src.double_consent import double_consent

class TestDoubleConsent(unittest.TestCase):
    def test_double_consent(self):
        input_data = "example_input"
        output_data = double_consent(input_data)
        self.assertIsNotNone(output_data)

if __name__ == "__main__":
    unittest.main()
