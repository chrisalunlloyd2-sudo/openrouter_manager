import os
import time
import subprocess
import json

MODELS_DIR = "/sdcard/MatrixVault/GGUF/"
LLAMA_CLI = os.path.expanduser("~/llama.cpp/build/bin/llama-cli")
PROMPT = "Explain how to make a simple HTML page in one sentence."

def benchmark_model(model_path):
    print(f"\n[Benchmarking] {os.path.basename(model_path)}")
    cmd = [
        LLAMA_CLI,
        "-m", model_path,
        "-p", PROMPT,
        "-n", "100",
        "--threads", "4"
    ]
    
    start_time = time.time()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        end_time = time.time()
        
        # Thermal Throttling Gap (4s)
        time.sleep(4)
        
        duration = end_time - start_time
        output = result.stdout.strip()
        
        print(f"  Duration: {duration:.2f}s")
        print(f"  Output: {output[:100]}...")
        
        return {
            "model": os.path.basename(model_path),
            "duration": duration,
            "output": output
        }
    except Exception as e:
        print(f"  Error: {e}")
        return None

def run_benchmarks():
    results = []
    models = [f for f in os.listdir(MODELS_DIR) if f.endswith(".gguf")]
    
    for model in sorted(models):
        model_path = os.path.join(MODELS_DIR, model)
        # Skip if too big for immediate benchmark (> 2GB)
        if os.path.getsize(model_path) > 2 * 1024 * 1024 * 1024:
            print(f"Skipping {model} (Too large for quick benchmark)")
            continue
            
        res = benchmark_model(model_path)
        if res:
            results.append(res)
            
    with open("benchmark_results.json", "w") as f:
        json.dump(results, f, indent=4)
    
    print("\n" + "="*40)
    print(" BENCHMARK COMPLETE")
    print("="*40)
    for res in sorted(results, key=lambda x: x['duration']):
        print(f"{res['model']:30} | {res['duration']:.2f}s")

if __name__ == "__main__":
    run_benchmarks()
