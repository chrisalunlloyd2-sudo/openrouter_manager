import json
import time
import os
import urllib.request
import subprocess

LOG_FILE = os.path.expanduser('~/.matrix_ide/logs/agy_master.log')
PROCESSED_FILE = os.path.expanduser('~/.matrix_ide/logs/agy_processed.log')

def call_llm(prompt):
    url = "http://localhost:8080/completions"
    data = json.dumps({
        "prompt": f"<|prompt|>Write a python script to accomplish this task: {prompt}. Output ONLY python code. NO explanations.</s><|answer|>```python\n",
        "max_tokens": 512,
        "temperature": 0.1,
        "stop": ["```", "</s>"]
    }).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read()
            res_json = json.loads(res_body)
            return res_json['content'] if 'content' in res_json else res_json['choices'][0]['text']
    except Exception as e:
        print(f"[LLM Error] {e}")
        return ""

def process_batch(lines):
    for line in lines:
        try:
            entry = json.loads(line)
            ask = entry.get("ask", "")
            # Detect tasks for python scripts, pings, or github uploads
            if "make a python script" in ask.lower() or "ping" in ask.lower() or "upload to github" in ask.lower() or "backup" in ask.lower():
                print(f"[Daemon] Found agentic task: {ask}")
                
                if "upload to github" in ask.lower() or "backup" in ask.lower():
                    # Direct git backup execution
                    print("[Daemon] Initiating H2OIDE backup...")
                    repo_dir = os.path.expanduser("~/H2OIDE")
                    subprocess.run(["git", "add", "."], cwd=repo_dir)
                    subprocess.run(["git", "commit", "-m", "Autonomous agentic backup"], cwd=repo_dir)
                    res = subprocess.run(["git", "push"], cwd=repo_dir, capture_output=True, text=True)
                    response_text = f"Backup result: {res.stdout} {res.stderr}"
                else:
                    # AI-generated script execution
                    code = call_llm(ask)
                    if code:
                        script_path = os.path.expanduser(f"~/H2OIDE/auto_task_{int(time.time())}.py")
                        with open(script_path, 'w') as f:
                            f.write(code.strip())
                        print(f"[Daemon] Executing {script_path}...")
                        subprocess.run(["python", script_path])
                        response_text = f"Successfully executed auto-script for task: {ask}"
                    else:
                        response_text = "Failed to generate AI script."

                # "ping you" - log that it was completed
                with open(LOG_FILE, 'a') as lf:
                    logLine = json.dumps({"timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"), "ask": "system_ping", "response": response_text})
                    lf.write(logLine + "\n")
        except json.JSONDecodeError:
            pass

def main():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w').close()
        
    processed_count = 0
    if os.path.exists(PROCESSED_FILE):
        with open(PROCESSED_FILE, 'r') as f:
            try:
                processed_count = int(f.read().strip())
            except:
                pass

    print("[Daemon] Monitoring logs for tasks...")
    while True:
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()
            
        unprocessed = lines[processed_count:]
        
        if len(unprocessed) > 0:
            process_batch(unprocessed)
            processed_count += len(unprocessed)
            with open(PROCESSED_FILE, 'w') as f:
                f.write(str(processed_count))
            
        time.sleep(5)

if __name__ == "__main__":
    main()
