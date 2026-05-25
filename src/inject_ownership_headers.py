import os

# Define the ownership header
ownership_header = """
# ==========================================================================
# Copyright (c) 2024 chrisalunlloyd2-sudo
# ==========================================================================
"""

# Iterate over all files in the src/ directory
for root, dirs, files in os.walk('src/'):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'r+') as f:
            content = f.read()
            f.seek(0)
            f.write(ownership_header + content)
            f.truncate()
        # Commit the changes
        [CMD]
        ```bash
git add.
git commit -m "Injected ownership headers into $file"
