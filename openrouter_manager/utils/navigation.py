import os

def get_pages():
    pages = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                page = {
                    "title": file.replace(".md", ""),
                    "url": file.replace(".md", ".html")
                }
                pages.append(page)
    return pages
```

[CMD]
```bash
python utils/navigation.py
