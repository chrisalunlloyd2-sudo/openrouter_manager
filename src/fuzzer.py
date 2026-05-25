import random
import string
import os

# ==============================================================================
# DATA INJECTION FUZZER v1.0
# Tests the robustness of the Danube Executor against high-entropy payloads.
# ==============================================================================

def generate_garbage(length=1000):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def test_executor_robustness():
    print("[Fuzzer] Testing Danube Executor with high-entropy payloads...")
    
    payload = f"""
    [FILE: fuzzed_file.txt]
    ```text
    {generate_garbage(5000)}
    ```
    
    [CMD]
    ```bash
    echo "Fuzzing complete"
    ```
    """
    
    with open(".fuzz_payload.md", "w") as f:
        f.write(payload)
        
    print("[Fuzzer] Injecting high-entropy payload...")
    res = os.system("python3 /data/data/com.termux/files/home/openrouter_manager/src/danube_executor.py .fuzz_payload.md")
    
    if res == 0:
        print("[Fuzzer] [+] Executor survived high-entropy injection.")
    else:
        print("[Fuzzer] [!] Executor CRASHED during injection.")

if __name__ == "__main__":
    test_executor_robustness()
