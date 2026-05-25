import unittest
from openrouter_manager.dashboard import Dashboard

class TestDashboard(unittest.TestCase):
    def test_render(self):
        dashboard = Dashboard()
        dashboard.render()

    def test_update(self):
        dashboard = Dashboard()
        dashboard.update("Test data")

if __name__ == "__main__":
    unittest.main()
```

# 🧬 SYNC STATE ACROSS DEVICES
To sync the state of the dashboard across devices, I will use OneDrive to store the dashboard's configuration and data.
[CMD]
```bash
onedrive --sync openrouter_manager
