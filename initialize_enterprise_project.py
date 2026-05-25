import json
import os
import subprocess
import time
from datetime import datetime
import requests

# Path to OAuth creds
CREDS_PATH = os.path.expanduser("~/.gemini/oauth_creds.json")

def get_token():
    try:
        with open(CREDS_PATH, 'r') as f:
            data = json.load(f)
            return data.get("access_token")
    except Exception as e:
        print(f"Error loading token: {e}")
        return None

def generate_ascii_tree(path="."):
    """ASCII tree generator."""
    output = []
    ignores = ['.git', '__pycache__', 'node_modules', '.npm', '.cache', 'build_staging']
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ignores and not d.startswith('.')]
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        output.append(f"{indent}├── {os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if not f.startswith('.'):
                output.append(f"{subindent}├── {f}")
    return "\n".join(output[:150]) + "\n... (Truncated for readability)"

README_TEMPLATE = """# 🌌 PocketMatrix OS (H2O Matrix CE)

## 📜 The Mission
The PocketMatrix OS is a fully manifested, 900-step architectural Singularity. It transforms a standard 32-bit Android environment into a distributed, AI-driven Windows CE-styled agentic network. 

**The Core Mission is Gamification & Simplification.** 
By wrapping highly complex neural-symbolic loops, cross-device network protocols, and agentic orchestration inside a nostalgic, point-and-click Windows CE desktop, the cognitive load required to operate the system is drastically reduced. It provides a visual, interactive workspace where learning (pedagogy) and execution (agentic routing) happen naturally. The user is empowered to orchestrate disparate databases, APIs, and models from a single, unified command center that feels like playing an OS simulation game.

## ✨ Feature Definitions & Rationale

**1. PocketMatrix GUI (Windows CE Interface)**
* **Definition:** A web-based, high-fidelity replica of the classic Windows CE desktop environment, complete with a taskbar, Start Menu, and draggable windows.
* **Why we need it:** It replaces cryptic terminal sessions with a gamified, centralized hub. This lowers cognitive overhead, allowing seamless visual interaction with multiple AI tools, databases, and network agents simultaneously.

**2. Danube Omni-Chat (Pocket CMD)**
* **Definition:** The central nervous system interface. A chat window that routes natural language (like "note: ..." or "remind me to ...") to specific applications, or falls back to the local H2O Danube model to translate intent into raw, executable bash/Win32 commands.
* **Why we need it:** Eliminates the need to memorize complex CLI syntax. You state the intent; the semantic router handles the execution.

**3. Excel 95 (Database Viewer & CRUD Editor)**
* **Definition:** A spreadsheet-style window that allows live viewing and editing (Create, Read, Update, Delete) of any SQLite database across the entire network. Utilizes physical ROWIDs for precision saves triggered instantly 'on blur'.
* **Why we need it:** It provides absolute, visual power over internal matrices, vectors, and state data without requiring the user to write a single line of SQL.

**4. Pocket ToDo (Google Keep Hypersync)**
* **Definition:** A cross-device reminder system that securely syncs local tasks to an actual Google Keep account via the `gkeepapi`.
* **Why we need it:** Ensures that agentic intents, reminders, and daily task lists flow out of the local OS sandbox and directly onto the user's physical mobile phone widget.

**5. Pocket Mail (Live Gmail SMTP Bridge)**
* **Definition:** An email client embedded in the CE desktop that routes KQML messages and system logs directly to real-world inboxes via an encrypted Gmail SMTP bridge.
* **Why we need it:** Enables the Matrix to communicate autonomously with external human actors, sending automated reports, alerts, and state summaries.

**6. Notes CE (VIPER Link)**
* **Definition:** A dedicated markdown text editor that reads and writes directly to the `VIPER_SCRIPT_LIBRARY`.
* **Why we need it:** Facilitates real-time, on-device documentation. The user can rapidly update the system's "cognitive behavioral core" and pedagogical notes directly from the GUI.

**7. Global Explorer (My Documents)**
* **Definition:** A gamified file explorer that recursively hunts down and groups all projects, kernels, and databases across the entire network into easily clickable desktop icons.
* **Why we need it:** Provides a unified, structured view of the entire agentic network, ensuring no database or project file is ever "lost" in the deep terminal filesystem.

**8. Task Manager (Kernel View)**
* **Definition:** A live process monitor attached directly to the underlying OS (`ps` telemetry).
* **Why we need it:** Allows immediate visual confirmation that local LLMs (`llama`), orchestration loops (`agy`), and Python server bridges are functioning properly and haven't hung.

**9. Internet Explorer (Webcrawl Ingestion)**
* **Definition:** A specialized knowledge scraper that digests documentation URLs, strips HTML, and forces the Danube AI to translate the raw text into structured "Ask Logic" rules.
* **Why we need it:** Automates the ingestion of external data. The AI teaches itself by reading FAQs and autonomously forming its own algorithmic instructions.

**10. Dynamic Fault Injector**
* **Definition:** A pedagogical sandbox tool that deliberately simulates severe OS crashes (e.g., Thread Deadlocks, Memory Corruption) within the CE environment.
* **Why we need it:** Gamified learning. By intentionally breaking the system, it forces the user to debug C/C++ in real-time, heavily assisted by the Danube AI tutor.

**11. Telemetry Parser**
* **Definition:** A memory-listening hook that pipes raw, cryptic Windows CE hex dumps and scheduler logs directly into the semantic model via regex filtering.
* **Why we need it:** Translates legacy OS crashes into plain-text English. The user learns OS internals rapidly without needing to manually decode hex addresses.

**12. Headless Accessibility Bridge**
* **Definition:** A zero-screen translation layer that converts natural language directly into low-level Win32 C/C++ API calls and executes them via serial/SSH.
* **Why we need it:** Allows complete automation and control over headless embedded devices or legacy servers without requiring any physical graphical interface.

**13. CeGCC & WCECL Integrations**
* **Definition:** The inclusion of an open-source cross-compiler (`cegcc`) and Windows CE compatibility layer (`wcecl`).
* **Why we need it:** Enables native compilation of ARM binaries directly on the Matrix substrate, breaking reliance on proprietary, legacy Microsoft toolchains.

## 📋 TOPOLOGICAL FILE TREE
```text
{tree}
```

## ⚡ CORE PERFORMATIVES
- `[PERFORMATIVE: INITIALIZE]` - Project manifestation and repository creation.
- `[PERFORMATIVE: SYNC_P2P]` - Decentralized ledger state alignment.
- `[PERFORMATIVE: BROADCAST]` - Global network intent propagation.
- `[PERFORMATIVE: RENDER]` - GL-accelerated UI / PocketMatrix GUI triggers.
- `[PERFORMATIVE: TUNE]` - Automatic hyper-parameter mutation based on fitness.
- `[PERFORMATIVE: HASH]` - Vault and network integrity verification.
- `[PERFORMATIVE: DARWIN]` - Neural-symbolic fitness scoring and selection.
- `[PERFORMATIVE: INGEST]` - Webcrawl processing and Ask Logic digestion.
- `[PERFORMATIVE: HANDOFF]` - Encrypted agentic task migration to peer nodes.
"""

def initialize():
    project_root = "/data/data/com.termux/files/home"
    os.chdir(project_root)
    project_name = "MATRIX_GEN8_HOME"
    token = get_token()
    
    if not token:
        print("[-] Missing OAuth token. Cannot proceed.")
        return

    print(f"--- 🚀 INITIALIZING ENTERPRISE PROJECT: {project_name} ---")

    # Git Setup
    if not os.path.exists(".git"):
        subprocess.run(["git", "init"], check=False)
    
    # Generate README with deep tree
    tree = generate_ascii_tree("PocketMatrix")
    with open("README.md", "w") as f:
        f.write(README_TEMPLATE.format(tree=tree))
    
    # Sync State securely via token injection
    push_url = f"https://{token}@github.com/chrisalunlloyd2-sudo/{project_name}.git"
    ce_url = f"https://{token}@github.com/chrisalunlloyd2-sudo/H2OMatrixCE.git"
    
    subprocess.run(["git", "add", "README.md", "H2OIDE/initialize_enterprise_project.py"], check=False)
    subprocess.run(["git", "commit", "-m", "Enterprise: Auto-generated gamified README with complete feature definitions."], check=False)
    subprocess.run(["git", "push", push_url, "main", "--force"], check=False)
    subprocess.run(["git", "push", ce_url, "main", "--force"], check=False)

    print("--- ✅ README GENERATED & PROJECT SYNCED TO GITHUB ---")

if __name__ == "__main__":
    initialize()
