# 🧠 H2OIDE: Prompt Engineering Guide (Levels 1-9)

To elicit accurate system orchestration from the H2O Danube 3 (500M) model, use the following prompt patterns. The `agy` CLI is optimized to handle these specifically.

## 📁 Level 1-3: System Orchestration
**Strategy:** Use direct action verbs and specific filenames. Avoid "Please" or "Can you".
- **Level 1:** `create an empty file named [filename]`
- **Level 2:** `write '[content]' into file [filename]`
- **Level 3:** `mkdir [folder] and touch [folder]/[file]` (Chained intent)

## 📊 Level 4-5: Data Structures
**Strategy:** Explicitly mention the tool (`sqlite3`) or the file extension (`.sql`).
- **Level 4:** `echo 'CREATE TABLE [name] ([columns]);' > [file].sql`
- **Level 5:** `sqlite3 [db_name].db 'CREATE TABLE [name] ([columns]);'`

## 🌐 Level 6: UI/UX Manifestation
**Strategy:** Small models struggle with syntax tags. Use a "wrapped echo" approach.
- **Prompt:** `create index.html with background [color] and text '[text]'`
- **Logic:** The `agy` CLI will strip any hallucinations after the redirection `>`.

## 🔗 Level 7-9: Advanced (Architecture)
**Strategy:** Use "Expert" terminology to trigger the specialized prompt path.
- **Level 7 (Joins):** `sqlite3 [db] "SELECT [a].[col] FROM [a] JOIN [b] ON [a].[id] = [b].[id];"`
- **Level 8 (Python):** `create python script logic.py to [logic] and main.py to call it`
- **Level 9 (API):** `create flask api in api.py with route /status`

---

## ⚡ 10x Speed Cheat Sheet
- **Threads:** Always keep server at `-t 4` for 32-bit ARM.
- **Temperature:** Keep at `0.0` for commands, `0.1` for scripts.
- **Speculative Decoding:** Ensure `--spec-type ngram-mod` is enabled.
