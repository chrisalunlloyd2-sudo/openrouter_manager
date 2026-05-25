import os
import sys

# ==============================================================================
# DANUBE CHOOSER v1.0
# Dynamically selects the optimal OpenRouter model based on prompt complexity.
# ==============================================================================

# Model Tier Hierarchy
TIERS = {
    "ULTRA": "openrouter:meta-llama/llama-3.3-70b-instruct", # High complexity, deep logic
    "PRIME": "openrouter:meta-llama/llama-3.3-70b-instruct", # Balanced, fast, articulate
    "CORE": "openrouter:meta-llama/llama-3.1-8b-instruct"  # Fast, low-latency tasks
}

def choose_model(prompt):
    """Analyzes the prompt and chooses the best tool for the job."""
    p_lower = prompt.lower()
    
    # Tier 1: Ultra Complexity (OS, APK, Complex Merges, 500x Documentation)
    if any(x in p_lower for x in ["operating system", "apk", "merge", "exhaustive", "master"]):
        print("[Danube Chooser] High Complexity Detected. Routing to ULTRA Tier (Llama 3.3).")
        return TIERS["ULTRA"]
    
    # Tier 2: Standard Logic (Websites, Database Schemas, Refactoring)
    if any(x in p_lower for x in ["website", "database", "schema", "optimize", "refactor"]):
        print("[Danube Chooser] Moderate Complexity Detected. Routing to PRIME Tier (Llama 3.3).")
        return TIERS["PRIME"]
    
    # Default: Core Tier
    print("[Danube Chooser] Standard Task Detected. Routing to CORE Tier (Llama 3.1).")
    return TIERS["CORE"]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(choose_model(" ".join(sys.argv[1:])))
    else:
        print(TIERS["PRIME"])
