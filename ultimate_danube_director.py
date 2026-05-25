import os
import sys
import subprocess
import re
import time

# ==============================================================================
# ULTIMATE DANUBE DIRECTOR - 10X GENETIC EVOLUTION ENGINE
# Resolves bad piping, implements 10 evolutionary passes per prompt, pushes 30x optimizations.
# ==============================================================================

def query_llm(prompt):
    """Executes the Headless OpenRouter request with strict subprocess management to prevent memory leaks."""
    cmd = ["/data/data/com.termux/files/usr/bin/aichat", "--role", "openrouter-manager", prompt]
    try:
        # stdin=subprocess.DEVNULL prevents the infinite pipe 'out of memory' crash
        res = subprocess.run(cmd, capture_output=True, text=True, check=True, stdin=subprocess.DEVNULL)
        return res.stdout
    except subprocess.CalledProcessError as e:
        print(f"[!] API Error: {e.stderr}")
        return ""

def extract_and_apply(content):
    """Deterministically extracts [FILE: path] blocks and writes them."""
    file_pattern = re.compile(r'\[FILE:\s*(.+?)\]\n```[a-zA-Z]*\n(.*?)\n```', re.DOTALL)
    files = file_pattern.findall(content)
    created = []
    
    for filepath, code in files:
        filepath = filepath.strip()
        os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(code.strip() + '\n')
        created.append(filepath)
        print(f"  -> Extracted & Written: {filepath}")
        
    return created

def execute_cmds(content):
    """Safely executes extracted [CMD] blocks."""
    cmd_pattern = re.compile(r'\[CMD\]\n```[a-zA-Z]*\n(.*?)\n```', re.DOTALL)
    cmds = cmd_pattern.findall(content)
    for cmd_str in cmds:
        cmd_str = cmd_str.strip()
        print(f"  -> Executing: {cmd_str}")
        try:
            subprocess.run(cmd_str, shell=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"  -> [!] Command failed: {e}")

def evolution_pipeline(base_prompt, iterations=10):
    print("=========================================================================")
    print(f" INITIATING AUTONOMOUS {iterations}X GENETIC EVOLUTION PIPELINE ")
    print("=========================================================================")
    
    # Evolution 1: Scaffolding and Basic Architecture
    current_prompt = f"INITIAL USER REQUEST: {base_prompt}\n\nDIRECTIVE (EVOLUTION 1): Generate the V1 architecture. Break this down into axiomatic functional components. You MUST include core code files and an exhaustive README.md with an ASCII topological tree. Output strictly using [FILE: path] blocks."
    
    for i in range(1, iterations + 1):
        print(f"\n[Danube] Running Genetic Evolution Pass {i}/{iterations}...")
        
        response = query_llm(current_prompt)
        
        if not response.strip():
            print(f"[!] Evolution {i} yielded no response. Retrying or halting.")
            continue
            
        print(f"[Danube] Analyzing Headless Payload for Pass {i}...")
        files = extract_and_apply(response)
        execute_cmds(response)
        
        if i < iterations:
            # Recursive Feedback Loop for 30X Optimization
            current_prompt = f"EVOLUTION {i} COMPLETE. You generated {len(files)} files.\n\nCRITICAL DIRECTIVE (EVOLUTION {i+1}): Analyze your previous output. Identify any inefficiencies, bad wording in comments, or lack of industry standards. Refactor the codebase for 30X performance and usability optimization. Expand the README.md to be even more articulate and exhaustive based on the new refactor. Output the improved [FILE: path] blocks."
            time.sleep(2) # Duty cycle pacing
            
    # Final Deploy Phase
    print("\n[Danube] 10X Evolution Complete. Syphoning optimal state to GitHub Seed...")
    os.system("python3 /data/data/com.termux/files/home/openrouter_manager/github_operator.py 'autonomous: 10x genetic evolution complete' > /dev/null 2>&1")
    print("\n[+] Cycle Complete. System Standing By.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        evolution_pipeline(" ".join(sys.argv[1:]))
    else:
        while True:
            try:
                p = input("director> ")
                if p.lower() in ['exit', 'quit']: break
                if p: evolution_pipeline(p)
            except (KeyboardInterrupt, EOFError):
                break
