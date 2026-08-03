# openrouter_manager

> openrouter_manager — part of the Viper RAID-0 workstation system.

*Auto-generated 2026-08-03 11:10 from source — branch `main`, 74 Python modules, 83 other files.*

## Architecture

```
  .director_payload.md
  .evolution_payload.md
  .fuzz_payload.md
  .gitignore
  .pilot_payload.md
  .task_payload.md
  Blueprint.md
  CHANGELOG.md
  ContentArchitect.py
  DATA_FLOW.md
  ENTERPRISE_INIT.p
  GLOBAL_PEDAGOGY.md
  AegisAgent/
    Blueprint.md
    README.md
  E2E_Final_Test/
    Blueprint.md
    README.md
  E2E_Test_Deploy_6172/
    Blueprint.md
    README.md
  agents/
    security_auditor_swarm.py
  analysis/
    swarm_consensus.py
  architecture/
    recursive_swarm_consensus.py
  components/
    SecurityAuditorSwarmComponent.js
  core/
    recursive_swarm_consensus.rs
    test.py
  docs/
    Blueprint.md
    Double_Consent_Protocol.md
    Double_Consent_Protocol_Implementation_Guide.md
    GENESIS_TRAINING.md
    H2OIDE_v10.1_Master_Engine_Specification.md
    H2OIDE_v10.1_System_Bible_Integration_Guide.md
    H2O_MATRIX_Architecture.md
    HOURLY_UPGRADES.md
    Master_Engine_Specification.md
    PROJECT_SUMMARY.md
    ROADMAP.md
    SINGULARITY_HORIZON_50.md
    case_studies/
      example.md
      feline_intelligence.md
  hooks/
    predictive_secret_leak_prevention.py
  openrouter_manager/
    README.md
    breeds.html
    gallery.html
    index.html
    css/
      style.css
    docs/
      Blueprint.md
      README.md
      manifest.md
      sidebar_navigation.md
    src/
      main.py
    templates/
      sidebar_navigation.html
    utils/
      navigation.py
  project/
    GENESIS_TRAINING.py
    initialize_enterprise_project.py
  skills/
    terminal.json
  sops/
    AGENT_ONBOARDING_SOP.md
    TODO.md
    refine_apk_architecture.md
    refine_apk_architecture.rs
  src/
    danube_chooser.py
    danube_director.py
    ...
```

## Dependencies

External packages imported by this project:

`cryptography`, `fastapi`, `flask`, `numpy`, `pydantic`, `redis`, `requests`, `rich`, `scipy`, `sqlalchemy`, `src`, `unittest`, `uvicorn`

## How to run

Executable entry points (have a `__main__` block):

- `python ContentArchitect.py`
- `python SCIENTIFIC_EXECUTOR.py`
- `python advanced_schema_update.py`
- `python agents/security_auditor_swarm.py`
- `python architecture/recursive_swarm_consensus.py`
- `python benchmark_models.py`
- `python cognitive_db.py`
- `python daemon.py`
- `python danube_director.py`
- `python danube_executor.py`
- `python danube_logic_orchestrator.py`
- `python danube_router.py`

## Modules

### `ContentArchitect.py`

- **class `QualityContentEngine`**
  - methods: `_load_state`, `_save_state`, `is_unique`, `generate_page_metadata`

### `advanced_schema_update.py`

- `upgrade_schema_v2()`

### `agents/security_auditor_swarm.py`

- **class `SecurityAuditRequest`**
- **class `SecurityAuditResult`**
- **class `SecurityAuditorSwarm`**
  - methods: `add_agent`, `audit`
- **class `SampleAgent`**
  - methods: `audit`
- `security_audit(request)`

### `benchmark_models.py`

- `benchmark_model(model_path)`
- `run_benchmarks()`

### `cognitive_db.py`

- `init_db()`

### `components.py`

- **class `Component`** — Base class for dashboard components
  - methods: `render`
- **class `SystemStatus`** — System status component
  - methods: `render`
- **class `UserInput`** — User input component
  - methods: `render`

### `daemon.py`

- `call_llm(prompt)`
- `process_batch(lines)`
- `main()`

### `danube_director.py`

- `run_cognitive_layer(prompt)`
- `main()`

### `danube_executor.py`

- `execute(payload_file)`

### `danube_logic_orchestrator.py`

- **class `DanubeOrchestrator`**
  - methods: `run_ai`, `distill_intent`, `plan`, `save_tree`, `display_tree`, `execute_task`, `test_task`, `sync`, `run`

### `danube_router.py`

- `execute_and_sync(instruction_text)`

### `dashboard.py`

- `render_dashboard()` — Render the interactive TUI dashboard
- `handle_user_input()` — Handle user input and update the dashboard accordingly
- `main()` — Main entry point for the dashboard

### `data_provider.py`

- **class `DataProvider`**
  - methods: `get_data`, `update_data`

### `encryption.py`

- **class `EncryptionManager`**
  - methods: `encrypt`, `decrypt`

### `error_handler.py`

- **class `ErrorHandler`**
  - methods: `handle_error`

### `genetic_optimizer.py`

- `fitness(response_text, duration)`

### `github_operator.py`

- `perform_upload(commit_msg)`

### `initialize_enterprise_project.py`

- `get_token()`
- `generate_ascii_tree(path)` — ASCII tree generator.
- `initialize()`

### `inject_pedagogy.py`

- `inject_pedagogy()`

### `main.py`

- **class `User`**
- **class `UserModel`**
- `get_db()`
- `read_users(db)`

### `matrix_orchestrator.py`

- `print_topic_update(title, summary, intent)` — Mirrors the agentic topic update structure.
- `enforce_pacing()` — Ensures we do not exceed OpenRouter API ping limits.
- `run_cognitive_layer(prompt)` — Hits the OpenRouter API via aichat CLI.
- `run_execution_layer(plan)` — Extracts commands and uses Aider to implement changes.
- `run_sync_layer(message)` — Triggers the Github Operator to upload.
- `main()`

### `models.py`

- **class `User`**

### `network_hook.py`

- `webhook()`

### `pedagogy_loop.py`

- `log_to_ledger(task, cmd)`
- `call_llm_agy(task)`
- `teach()`

### `project/GENESIS_TRAINING.py`

- `initialize_project()`
- `initialize_enterprise_project(repo_dir)`

### `redis_neural_caching.py`

- **class `RedisNeuralCaching`**
  - methods: `cache`, `get`, `delete`

### `redis_pool.py`

- **class `RedisPool`**
  - methods: `get_connection`, `close_connection`

### `research_analyst.py`

- **class `ResearchAnalyst`**
  - methods: `ingest_concepts`, `generate_content`

### `research_node.py`

- `fetch_content(url)`

### `src/danube_chooser.py`

- `choose_model(prompt)` — Analyzes the prompt and chooses the best tool for the job.

### `src/danube_director.py`

- `distill_tasks_to_json(ai_response)` — Parses [ACTION: ...] blocks and serializes to JSON steps.
- `run_cognitive_layer(prompt, history_context)`
- `binomial_consent(task)`
- `master_loop(initial_prompt)`

### `src/danube_executor.py`

- `execute(payload_file)`

### `src/documentation_scanner.py`

- `populate_file(file_path)`
- `main()`

### `src/documentation_validator_swarm.py`

- `log(msg)`
- `audit_repo(repo_name)`
- `run_fix_pass(repo_name)`
- `main()`

### `src/double_consent.py`

- `init()`
- `evaluate(user_input)`

### `src/foundry_master_engine.py`

- `run_director(prompt)`
- `main()`

### `src/fuzzer.py`

- `generate_garbage(length)`
- `test_executor_robustness()`

### `src/markov_logic_engine.py`

- `get_next_action(current_state)` — Uses Markov weights to decide the next step in the evolution loop.
- `update_weight(current_state, action, performance_delta)` — Updates the Markov transition weight based on successful performance increase.

### `src/monolith_traverser.py`

- `init_traverser_db()`
- `record_state(project, axiom, transition, snapshot)`
- `get_current_logic(project)`

### `src/qa_bot.py`

- `run_qa_checks()`

### `src/refactored_module.py`

- `optimize_performance(data)` — This function optimizes the performance of the system by 30x.
- `main()` — This is the main function that calls the optimize_performance function.

### `src/research_analyst.py`

- `run_research(topic, sources)`
- `main()`

### `src/scientific_self_trainer.py`

- `run_scientific_step(hypothesis)`
- `main()`

### `src/steering_orchestrator.py`

- `init_steering_db()`
- `record_flow(flow_type, prompt_sequence, score)`
- `prune_flows(threshold)` — Prunes inefficient logic flows from the genetic database.
- `get_best_flow(flow_type)`

### `src/upgrade_markov.py`

- `upgrade_markov_schema()`

### `src/upgrade_research_db.py`

- `upgrade_db()`

### `src/utils.py`

- `utils_function()`
- `main()`

### `src/webcrawl_self_evolve.py`

- `ingest_concepts(url)`

### `tests/test_double_consent.py`

- **class `TestDoubleConsent`**
  - methods: `test_double_consent`

### `ultimate_danube_director.py`

- `query_llm(prompt)` — Executes the Headless OpenRouter request with strict subprocess management to prevent memory leaks.
- `extract_and_apply(content)` — Deterministically extracts [FILE: path] blocks and writes them.
- `execute_cmds(content)` — Safely executes extracted [CMD] blocks.
- `evolution_pipeline(base_prompt, iterations)`

### `update_schema.py`

- `upgrade_schema()`

### `widget_manager.py`

- **class `WidgetManager`**
  - methods: `add_widget`, `update_widgets`

## Public API index

| Module | Function | Signature |
|--------|----------|-----------|
| `GENESIS_TRAINING` | `initialize_enterprise_project` | `initialize_enterprise_project(repo_dir)` |
| `GENESIS_TRAINING` | `initialize_project` | `initialize_project()` |
| `advanced_schema_update` | `upgrade_schema_v2` | `upgrade_schema_v2()` |
| `benchmark_models` | `benchmark_model` | `benchmark_model(model_path)` |
| `benchmark_models` | `run_benchmarks` | `run_benchmarks()` |
| `cognitive_db` | `init_db` | `init_db()` |
| `daemon` | `call_llm` | `call_llm(prompt)` |
| `daemon` | `main` | `main()` |
| `daemon` | `process_batch` | `process_batch(lines)` |
| `danube_chooser` | `choose_model` | `choose_model(prompt)` |
| `danube_director` | `binomial_consent` | `binomial_consent(task)` |
| `danube_director` | `distill_tasks_to_json` | `distill_tasks_to_json(ai_response)` |
| `danube_director` | `main` | `main()` |
| `danube_director` | `master_loop` | `master_loop(initial_prompt)` |
| `danube_director` | `run_cognitive_layer` | `run_cognitive_layer(prompt)` |
| `danube_director` | `run_cognitive_layer` | `run_cognitive_layer(prompt, history_context)` |
| `danube_executor` | `execute` | `execute(payload_file)` |
| `danube_executor` | `execute` | `execute(payload_file)` |
| `danube_router` | `execute_and_sync` | `execute_and_sync(instruction_text)` |
| `dashboard` | `handle_user_input` | `handle_user_input()` |
| `dashboard` | `main` | `main()` |
| `dashboard` | `render_dashboard` | `render_dashboard()` |
| `documentation_scanner` | `main` | `main()` |
| `documentation_scanner` | `populate_file` | `populate_file(file_path)` |
| `documentation_validator_swarm` | `audit_repo` | `audit_repo(repo_name)` |
| `documentation_validator_swarm` | `log` | `log(msg)` |
| `documentation_validator_swarm` | `main` | `main()` |
| `documentation_validator_swarm` | `run_fix_pass` | `run_fix_pass(repo_name)` |
| `double_consent` | `evaluate` | `evaluate(user_input)` |
| `double_consent` | `init` | `init()` |
| `foundry_master_engine` | `main` | `main()` |
| `foundry_master_engine` | `run_director` | `run_director(prompt)` |
| `fuzzer` | `generate_garbage` | `generate_garbage(length)` |
| `fuzzer` | `test_executor_robustness` | `test_executor_robustness()` |
| `genetic_optimizer` | `fitness` | `fitness(response_text, duration)` |
| `github_operator` | `perform_upload` | `perform_upload(commit_msg)` |
| `initialize_enterprise_project` | `generate_ascii_tree` | `generate_ascii_tree(path)` |
| `initialize_enterprise_project` | `get_token` | `get_token()` |
| `initialize_enterprise_project` | `initialize` | `initialize()` |
| `inject_pedagogy` | `inject_pedagogy` | `inject_pedagogy()` |
| `main` | `get_db` | `get_db()` |
| `main` | `read_users` | `read_users(db)` |
| `markov_logic_engine` | `get_next_action` | `get_next_action(current_state)` |
| `markov_logic_engine` | `update_weight` | `update_weight(current_state, action, performance_delta)` |
| `matrix_orchestrator` | `enforce_pacing` | `enforce_pacing()` |
| `matrix_orchestrator` | `main` | `main()` |
| `matrix_orchestrator` | `print_topic_update` | `print_topic_update(title, summary, intent)` |
| `matrix_orchestrator` | `run_cognitive_layer` | `run_cognitive_layer(prompt)` |
| `matrix_orchestrator` | `run_execution_layer` | `run_execution_layer(plan)` |
| `matrix_orchestrator` | `run_sync_layer` | `run_sync_layer(message)` |
| `monolith_traverser` | `get_current_logic` | `get_current_logic(project)` |
| `monolith_traverser` | `init_traverser_db` | `init_traverser_db()` |
| `monolith_traverser` | `record_state` | `record_state(project, axiom, transition, snapshot)` |
| `network_hook` | `webhook` | `webhook()` |
| `pedagogy_loop` | `call_llm_agy` | `call_llm_agy(task)` |
| `pedagogy_loop` | `log_to_ledger` | `log_to_ledger(task, cmd)` |
| `pedagogy_loop` | `teach` | `teach()` |
| `qa_bot` | `run_qa_checks` | `run_qa_checks()` |
| `refactored_module` | `main` | `main()` |
| `refactored_module` | `optimize_performance` | `optimize_performance(data)` |

## Status

- Branch: `main`
- Last commit: 2026-07-24 16:17:10 -0600
- File types: .md ×56, .html ×8, .txt ×3, .css ×3, .rs ×3, .kt ×3, .json ×2, .go ×1

### Recent commits
```
a9b4154 docs(openrouter_manager): autonomous update â€” 2 file(s)
1907055 [Moe autonomous] openrouter_manager 2026-06-29 11:13
507c3b7 docs(openrouter_manager): autonomous update â€” 2 file(s)
dab9ab3 [Moe autonomous] openrouter_manager 2026-06-27 01:39
96c892a [Moe autonomous] openrouter_manager 2026-06-21 19:00
1c5209e [Moe autonomous] openrouter_manager 2026-06-20 12:27
54758b8 [Moe autonomous] openrouter_manager 2026-06-20 00:59
1e49d03 [Moe autonomous] openrouter_manager 2026-06-19 20:57
```

---
*README generated by `readme_generator.py` (Viper). Deterministic — derived from source, not LLM prose.*