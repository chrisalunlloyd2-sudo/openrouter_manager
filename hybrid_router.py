import os
import requests
import json

def route_query(prompt, local_only=False):
    # Strategy: Try Local (Qwen 0.5B), if failure/complex, fallback to OpenRouter
    # Critiquing local output using OpenRouter
    
    # Placeholder for local call
    local_resp = "Local LDAP/KG Result (placeholder)" 
    
    if local_only:
        return local_resp
    
    # Critique local output
    critique_prompt = f"Critique this local KG operation for LDAP optimization: {local_resp}. Suggest LoRA update."
    
    # Fallback/Critique call to OpenRouter
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}"},
            json={"model": "qwen/qwen-2-7b-instruct", "messages": [{"role": "user", "content": critique_prompt}]}
        )
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return local_resp # Fail safe
