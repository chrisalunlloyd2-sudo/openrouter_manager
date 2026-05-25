import os
import json
import shutil

def merge_nova_logic():
    # Load the PROMPT_EVOLUTION_LOG.json from Nova
    with open('~/Nova/PROMPT_EVOLUTION_LOG.json', 'r') as f:
        prompt_evolution_log = json.load(f)

    # Inspect the current src/ directory
    current_src_dir = os.listdir('src/')

    # Determine the necessary files to merge from Nova
    files_to_merge = []
    for file in prompt_evolution_log:
        if file not in current_src_dir:
            files_to_merge.append(file)

    # Merge the necessary files from Nova into openrouter_manager
    for file in files_to_merge:
        shutil.copy('~/Nova/src/' + file, 'src/')

    # Update docs/GENESIS_TRAINING.md with the results
    with open('docs/GENESIS_TRAINING.md', 'a') as f:
        f.write('### Merged Nova Logic\n')
        f.write('The following files were merged from Nova:\n')
        for file in files_to_merge:
            f.write('* ' + file + '\n')

[CMD]
```bash
python3 openrouter_manager/src/merge_nova_logic.py


# --- FOUNDRY v10.2 RESTORATION & EXPANSION ---
import os
import json
import shutil

def merge_nova_logic():
    # Load the PROMPT_EVOLUTION_LOG.json from Nova
    with open('~/Nova/PROMPT_EVOLUTION_LOG.json', 'r') as f:
        prompt_evolution_log = json.load(f)

    # Inspect the current src/ directory
    src_dir = './src'
    if not os.path.exists(src_dir):
        os.makedirs(src_dir)

    # Inspect the Nova source directory
    nova_dir = '~/Nova'
    if not os.path.exists(nova_dir):
        print("Nova directory not found.")
        return

    # Merge the necessary logic or files from Nova into openrouter_manager
    build_txt_path = os.path.join(nova_dir, 'BUILD.txt')
    if os.path.exists(build_txt_path):
        # Copy the BUILD.txt file to the src/ directory
        shutil.copy(build_txt_path, src_dir)

        # Update the docs/GENESIS_TRAINING.md file
        genesis_training_md_path = './docs/GENESIS_TRAINING.md'
        with open(genesis_training_md_path, 'a') as f:
            f.write('\n## Merged Nova Logic\n')
            f.write('The `BUILD.txt` file from Nova has been merged into the `src/` directory.\n')

        print("Merged Nova logic successfully.")
    else:
        print("BUILD.txt file not found in Nova directory.")

    # Sync everything to GitHub
    # This step will be performed by the Node 3 (Syphon) in the Dual-Danube Engine

[CMD]
```bash
python3 /data/data/com.termux/files/home/initialize_enterprise_project.py
```

[ASCII TREE TEMPLATE]
```
├──.git/
├── README.md
├── docs/
│   ├── GENESIS_TRAINING.md
├── src/
│   ├── main.py
│   ├── BUILD.txt
└── tests/


# --- FOUNDRY v10.2 RESTORATION & EXPANSION ---
import os
import json
import shutil

def merge_nova_logic():
    # Load the PROMPT_EVOLUTION_LOG.json from Nova
    with open('~/Nova/PROMPT_EVOLUTION_LOG.json', 'r') as f:
        prompt_evolution_log = json.load(f)

    # Inspect the current src/ and the Nova source at ~/Nova/
    current_src = os.listdir('src/')
    nova_src = os.listdir('~/Nova/')

    # Merge the necessary logic or files from Nova into openrouter_manager
    for file in nova_src:
        if file not in current_src:
            shutil.copy('~/Nova/' + file, 'src/')

    # Update docs/GENESIS_TRAINING.md with the results
    with open('docs/GENESIS_TRAINING.md', 'a') as f:
        f.write('## Merged Nova Logic\n')
        f.write('The following files were merged from Nova:\n')
        for file in nova_src:
            if file not in current_src:
                f.write('- ' + file + '\n')

    # Sync everything to GitHub
    os.system('git add.')
    os.system('git commit -m "Merged Nova logic"')
    os.system('git push origin main')

# Call the function
merge_nova_logic()
```

[CMD]
```bash
python3 openrouter_manager/src/merge_nova_logic.py
