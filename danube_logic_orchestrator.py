import os
import sys
import subprocess
import json
import time
import re

# ==============================================================================
# DANUBE LOGIC ORCHESTRATOR (v4.0)
# [MANDATE: LOGIC TREE, SID, BENCHMARK ORCHESTRATION, SLOPPY INPUT HANDLING]
# ==============================================================================

class DanubeOrchestrator:
    def __init__(self, goal):
        self.raw_goal = goal
        self.scientific_intent = ""
        self.tree_file = "logic_tree.json"
        self.tree = {"goal": goal, "scientific_intent": "", "tasks": [], "current_index": 0}
        self.role = "openrouter-manager-v2"
        self.real_aichat = "/data/data/com.termux/files/usr/bin/aichat"

    def run_ai(self, prompt, system_instruction=""):
        """Calls OpenRouter via aichat."""
        full_prompt = f"{system_instruction}\n\nTask: {prompt}"
        cmd = [self.real_aichat, "--role", self.role, full_prompt]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"[!] OpenRouter API Error: {e.stderr}")
            return ""

    def distill_intent(self):
        """Phase 0: Scientific Intent Distillation (SID).
        Handles sloppy verbage and extracts strict technical performatives.
        """
        print(f"[SID] Distilling scientific intent from: '{self.raw_goal}'")
        instruction = (
            "You are a Scientific Intent Distiller. The user might provide 'sloppy' input with typos or informal language. "
            "Your job is to ignore the mess and extract the STRICT TECHNICAL INTENT. "
            "Output format: [INTENT: ...][REQUIREMENTS: list...][CONSTRAINTS: list...]. "
            "ZERO PROSE."
        )
        response = self.run_ai(self.raw_goal, instruction)
        self.scientific_intent = response.strip()
        self.tree["scientific_intent"] = self.scientific_intent
        print(f"[SID] Manifested Intent:\n{self.scientific_intent}\n")

    def plan(self):
        """Phase 1: Generate Logic Tree based on SID."""
        if not self.scientific_intent:
            self.distill_intent()
            
        print(f"[Planner] Generating Logic Tree for distilled intent...")
        instruction = (
            "You are a Project Architect. Break the Scientific Intent into sequential tasks. "
            "Output MUST be a valid JSON array of objects with keys: 'name', 'description'. "
            "ZERO PROSE. ONLY JSON."
        )
        response = self.run_ai(self.scientific_intent, instruction)
        
        try:
            start = response.find('[')
            end = response.rfind(']') + 1
            if start != -1 and end != 0:
                json_str = response[start:end]
                tasks = json.loads(json_str)
                self.tree["tasks"] = tasks
                for task in self.tree["tasks"]:
                    task["status"] = "pending"
                    task["attempts"] = 0
                self.save_tree()
                print("[Planner] Logic Tree Manifested.")
            else:
                print(f"[!] Failed to parse JSON: {response}")
        except Exception as e:
            print(f"[!] Planning Error: {e}")

    def save_tree(self):
        with open(self.tree_file, "w") as f:
            json.dump(self.tree, f, indent=4)

    def display_tree(self):
        print("\n" + "="*40)
        print(f" LOGIC TREE: {self.tree['goal']}")
        print("="*40)
        for i, task in enumerate(self.tree["tasks"]):
            status_char = " "
            if task["status"] == "done": status_char = "x"
            elif task["status"] == "working": status_char = ">"
            elif task["status"] == "failed": status_char = "!"
            
            print(f"[{status_char}] {i+1}. {task['name']}")
        print("="*40 + "\n")

    def execute_task(self, task):
        """Phase 2: Implementation (Director + Executor)."""
        print(f"[Director] Attacking Task: {task['name']} (Attempt {task['attempts']+1})")
        # Mirroring Gemini CLI: Research -> Strategy -> Execution
        instruction = (
            "Follow the Gemini CLI Benchmark: Research context, devise a Strategy, then Execute. "
            "Generate the code to complete the task. "
            "Format: [FILE: path]...code...[CMD]...shell command...[SUMMARY]...text. "
            "ZERO PROSE."
        )
        payload = self.run_ai(f"Project Intent: {self.scientific_intent}\nTask: {task['name']}\nDescription: {task['description']}", instruction)
        
        if not payload.strip(): return False

        with open(".task_payload.md", "w") as f:
            f.write(payload)
        
        subprocess.run(["python3", "danube_executor.py", ".task_payload.md"])
        return True

    def test_task(self, task):
        """Phase 3: Validation (Tester)."""
        print(f"[Tester] Verifying Task: {task['name']}")
        instruction = (
            "You are a Quality Assurance Engineer. "
            "Generate a single python script named 'test_task.py' that verifies the task was completed successfully. "
            "The script should exit with code 0 on success, and non-zero on failure. "
            "ONLY output the python code. ZERO PROSE."
        )
        test_code = self.run_ai(f"Project Intent: {self.scientific_intent}\nTask: {task['name']}\nDescription: {task['description']}\nGenerate a test for this.", instruction)
        
        test_code = re.sub(r'```python\n|```', '', test_code)
        
        with open("test_task.py", "w") as f:
            f.write(test_code.strip())
        
        try:
            result = subprocess.run(["python3", "test_task.py"], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"[Tester] Task Verified: {task['name']}")
                return True
            else:
                print(f"[Tester] Verification Failed: {result.stderr or result.stdout}")
                return False
        except Exception as e:
            print(f"[Tester] Test Execution Error: {e}")
            return False

    def sync(self, task_name):
        """Phase 4: Synchronization (Synchronizer)."""
        print("[Synchronizer] Syphoning state to GitHub...")
        subprocess.run(["python3", "github_operator.py", f"autonomous: completed {task_name}"])

    def run(self):
        if not self.tree["tasks"]:
            self.plan()
        
        while self.tree["current_index"] < len(self.tree["tasks"]):
            index = self.tree["current_index"]
            task = self.tree["tasks"][index]
            
            self.display_tree()
            task["status"] = "working"
            task["attempts"] += 1
            self.save_tree()
            
            success = self.execute_task(task)
            if success:
                verified = self.test_task(task)
                if verified:
                    task["status"] = "done"
                    self.sync(task["name"])
                    self.tree["current_index"] += 1
                else:
                    task["status"] = "failed"
                    if task["attempts"] >= 3:
                        print(f"[!] Task {task['name']} failed after 3 attempts. Stopping.")
                        break
                    print(f"[!] Retrying task (Attempt {task['attempts']+1}/3)...")
            else:
                task["status"] = "failed"
                break
            
            self.save_tree()
            time.sleep(2)

        self.display_tree()
        if self.tree["current_index"] == len(self.tree["tasks"]):
            print("[Danube] All subjects manifested. Project Complete.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        goal = " ".join(sys.argv[1:])
        orchestrator = DanubeOrchestrator(goal)
        orchestrator.run()
    else:
        print("Usage: python3 danube_logic_orchestrator.py \"Your project goal\"")
