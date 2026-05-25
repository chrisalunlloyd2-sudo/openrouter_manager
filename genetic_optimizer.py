import urllib.request
import json
import time

url = "http://localhost:8080/completions"

prompts = [
    # 5: Force code block
    "<|prompt|>Task: create an empty file called txt.txt in downloads. Provide ONLY the bash command.</s><|answer|>```bash\n",
    # 6: Force code block with specific start
    "<|prompt|>Task: create an empty file called txt.txt in downloads.</s><|answer|>\nTo do this, run the following bash command:\n```bash\n",
    # 7: Command: prefix
    "User: create an empty file called txt.txt in downloads\nBash Command: ",
    # 8: Direct Bash execution
    "#!/bin/bash\n# Task: create an empty file called txt.txt in downloads\n",
    # 9: ChatML format
    "<|im_start|>user\nWrite a bash command: create an empty file called txt.txt in downloads<|im_end|>\n<|im_start|>assistant\n```bash\n"
]

def fitness(response_text, duration):
    # We want exactly "touch ~/downloads/txt.txt" or "touch downloads/txt.txt"
    # The shorter the response, the better. If it contains explanations, bad.
    response_text = response_text.strip()
    length_penalty = len(response_text)
    
    # Check for correct command
    correctness = 0
    if "touch " in response_text and "txt.txt" in response_text:
        correctness = 1000
    if "mkdir" in response_text:
        correctness -= 500 # It tried to make a dir instead of a file
        
    score = correctness - length_penalty - (duration * 10)
    return score, response_text

best_score = -99999
best_prompt_idx = -1
best_text = ""

for i, p in enumerate(prompts):
    data = json.dumps({
        "prompt": p,
        "n_predict": 32,
        "temperature": 0.1,
        "stop": ["</s>", "```"]
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    start = time.time()
    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read()
            res_json = json.loads(res_body)
            text = res_json['content'] if 'content' in res_json else res_json['choices'][0]['text']
    except Exception as e:
        text = str(e)
    duration = time.time() - start
    
    score, clean_text = fitness(text, duration)
    print(f"Gen {i} | Time: {duration:.2f}s | Score: {score:.1f} | Output: {clean_text}")
    
    if score > best_score:
        best_score = score
        best_prompt_idx = i
        best_text = clean_text

print(f"\n[WINNER] Gen {best_prompt_idx} with score {best_score:.1f}: {best_text}")
