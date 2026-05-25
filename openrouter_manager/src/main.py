import os
import sys

def main():
    # Initialize the router manager
    router_manager = RouterManager()

    # Start the configuration interface
    router_manager.start_interface()

if __name__ == "__main__":
    main()
```

[CMD]
```bash
git add .
git commit -m "Initial commit of Open Router Manager"
git push origin main
