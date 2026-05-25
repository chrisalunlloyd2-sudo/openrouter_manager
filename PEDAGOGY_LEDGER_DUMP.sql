PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE snippets (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, content TEXT, language TEXT, tags TEXT);
INSERT INTO snippets VALUES(1,'network_socket','import socket\n\ndef create_socket(host, port):\n    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n    s.connect((host, port))\n    return s','python','network,socket');
INSERT INTO snippets VALUES(2,'file_watcher','import os\nimport time\n\ndef watch_file(path):\n    last_mtime = os.path.getmtime(path)\n    while True:\n        mtime = os.path.getmtime(path)\n        if mtime != last_mtime:\n            print(f"File {path} changed")\n            last_mtime = mtime\n        time.sleep(1)','python','fs,watcher');
INSERT INTO snippets VALUES(3,'network_socket','import socket\ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\ns.bind(("localhost", 8080))','python','network,socket');
INSERT INTO snippets VALUES(4,'file_watcher','import os\nimport time\ndef watch(path):\n    last_stat = os.stat(path).st_mtime\n    while True:\n        stat = os.stat(path).st_mtime\n        if stat != last_stat:\n            print("Changed!")\n            last_stat = stat\n        time.sleep(1)','python','fs,watcher');
CREATE TABLE state (key TEXT PRIMARY KEY, value TEXT);
INSERT INTO state VALUES('memory_map_active','1');
INSERT INTO state VALUES('fuzzy_triangulation_mode','standard');
INSERT INTO state VALUES('best_genetic_variant','7ab5ee5941f8c90eb74e2fa1247c1c88:0.9999990771864076');
CREATE TABLE formula_table (pattern_hash TEXT PRIMARY KEY, dependency_url TEXT, secret_alias TEXT, status TEXT);
INSERT INTO formula_table VALUES('hash123','http://repo.example.com/lib.zip','api_key_alias','pending');
INSERT INTO formula_table VALUES('[49, 49, 53]','http://repo.example.com/lib.zip','api_key_alias','pending');
CREATE TABLE code_patterns (sequence_id INTEGER PRIMARY KEY AUTOINCREMENT, token_sequence TEXT, frequency INTEGER, context_type TEXT);
INSERT INTO code_patterns VALUES(1,'Module,Import,Import,Import,Import,ImportFrom,Assign,Assign,FunctionDef,FunctionDef,If,alias,alias,alias,alias,alias,Name,Call,Name,Call,arguments,Assign,Assign,Expr,Assign,Expr,If,Expr,Return,arguments,Pass,Compare,If,Store,Attribute,Constant,Store,Attribute,Name,Constant,arg,Name,Call,Name,Call,Call,Name,Call,Call,Name,Assign,Assign,Expr,Return,Call,Constant,Name,Eq,Constant,BoolOp,Assign,Expr,Expr,Attribute,Load,Attribute,Load,Load,Store,Attribute,Name,Store,Attribute,Attribute,Constant,Tuple,Store,Attribute,Attribute,Load,Tuple,Name,Name,Call,Call,Constant,Name,JoinedStr,Load,And,Compare,Compare,Name,IfExp,Call,Call,Name,Load,Name,Load,Name,Load,Load,Name,Load,Name,Load,Name,Load,Name,Load,Name,Load,Name,Name,Store,Load,Store,Name,Name,Name,JoinedStr,Load,Constant,FormattedValue,Call,Gt,Constant,Subscript,Eq,Constant,Store,Compare,Subscript,Constant,Name,Name,Name,Load,Load,Load,Load,Load,Load,Load,Load,Store,Store,Load,Load,Load,Constant,FormattedValue,Constant,FormattedValue,Name,Name,Attribute,Attribute,Constant,Load,Call,Gt,Constant,Attribute,Constant,Load,Load,Load,Load,Name,Name,Load,Load,Name,Load,Name,Load,Name,Attribute,Name,Load,Load,Load,Load,Load,Load,Name,Load,Load,Load',1,'python');
INSERT INTO code_patterns VALUES(2,'Module,Import,ClassDef,If,alias,FunctionDef,FunctionDef,Compare,Expr,arguments,Assign,Assign,Assign,Assign,arguments,Expr,Expr,While,Name,Eq,Constant,Call,arg,Attribute,List,Attribute,List,Attribute,Constant,Attribute,Constant,arg,arg,Call,Call,Constant,Expr,Assign,Expr,If,Expr,Assign,If,Load,Attribute,Lambda,Name,Store,Constant,Constant,Constant,Load,Name,Store,Constant,Constant,Load,Name,Store,Name,Store,Attribute,Constant,Attribute,Constant,Call,Tuple,Call,Call,Compare,For,If,Call,Name,Call,Compare,Break,If,Name,Load,arguments,Call,Load,Load,Load,Load,Name,Load,Name,Load,Attribute,Name,Name,Store,Attribute,Attribute,Constant,Constant,JoinedStr,Attribute,Attribute,Eq,Constant,Tuple,Call,Assign,Expr,Compare,Expr,Expr,If,Attribute,Store,Attribute,Name,Eq,Call,Compare,Assign,If,Load,arg,Attribute,Name,Load,Load,Name,Load,Store,Store,Name,Load,Name,Load,Constant,FormattedValue,Constant,Name,Load,Name,Load,Name,Name,Store,Name,Attribute,Name,IfExp,Call,Attribute,Eq,Constant,Call,Call,Compare,Expr,For,Name,Load,Name,Load,Load,Name,Constant,Name,Eq,Call,Attribute,Constant,Compare,Assign,If,Call,Load,Load,Load,Load,Load,Attribute,Load,Load,Store,Store,Load,Name,Load,Store,Compare,Attribute,Attribute,Attribute,BinOp,Constant,JoinedStr,Name,Name,Load,Attribute,Constant,Constant,Constant,Attribute,Constant,Constant,Constant,Attribute,Eq,Constant,Call,Tuple,Call,Expr,Load,Load,Load,Load,Name,Constant,Name,Store,Name,Eq,Call,Attribute,Constant,Compare,Assign,If,Name,Name,Load,Load,Name,Eq,Attribute,Name,Load,Name,Load,Name,Load,Name,Add,Constant,Constant,FormattedValue,Load,Load,Name,Load,Name,Load,Name,Load,Attribute,Constant,Constant,Constant,Name,Name,Store,Name,Attribute,Call,Load,Load,Load,Name,Constant,Name,Store,Name,Eq,Call,Attribute,Constant,Compare,Assign,If,Load,Load,Load,Name,Load,Load,Load,Load,Load,Name,Load,Load,Load,Name,Load,Store,Store,Load,Name,Load,Attribute,BinOp,Constant,JoinedStr,Load,Load,Load,Name,Constant,Name,Store,Name,Eq,Attribute,Attribute,BinOp,Compare,Assign,Load,Load,Load,Load,Name,Load,Name,Add,Constant,Constant,FormattedValue,Load,Load,Load,Name,Load,Name,Store,BinOp,Mod,Call,Name,Eq,Attribute,Attribute,BinOp,Load,Load,Name,Load,Load,Attribute,Sub,Constant,Name,Attribute,Load,Name,Load,Name,Store,BinOp,Mod,Call,Load,Name,Load,Load,Name,Load,Load,Load,Attribute,Add,Constant,Name,Attribute,Load,Load,Name,Load,Load,Name,Load,Load,Load',1,'python');
INSERT INTO code_patterns VALUES(3,'[49, 49, 53]',1,'USER_INPUT');
INSERT INTO code_patterns VALUES(4,'VERIFY_BLOCK_99',1,'USER_INPUT');
CREATE TABLE project_nodes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT UNIQUE,
            type TEXT, -- FOLDER or FILE
            parent_id INTEGER,
            status TEXT DEFAULT 'EMPTY' -- EMPTY, MANIFESTING, STAMPED
        );
CREATE TABLE code_variants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            node_id INTEGER,
            iteration INTEGER,
            content TEXT,
            evaluation_state TEXT DEFAULT 'UNSTAMPED'
        );
CREATE TABLE topology (id INTEGER PRIMARY KEY, path TEXT UNIQUE, status TEXT);
INSERT INTO topology VALUES(1,'test_node','VERIFIED');
CREATE TABLE variants (id INTEGER PRIMARY KEY, node_id INTEGER, confidence REAL, block TEXT);
CREATE TABLE retro_queue (id INTEGER PRIMARY KEY, identifier TEXT, status TEXT);
CREATE TABLE quantum_parameters (key TEXT PRIMARY KEY, value TEXT);
INSERT INTO quantum_parameters VALUES('mean',x'342e36393136');
INSERT INTO quantum_parameters VALUES('sigma',x'302e303333');
INSERT INTO quantum_parameters VALUES('weights',x'0000c03f9a99993f3333b33f');
CREATE TABLE system_freeze (key TEXT PRIMARY KEY, value TEXT);
INSERT INTO system_freeze VALUES('phase_20_status','FROZEN');
CREATE TABLE successful_scripts (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, command TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);
INSERT INTO successful_scripts VALUES(1,'touch verify.txt','touch verify.txt','2026-05-23 19:38:10');
INSERT INTO successful_scripts VALUES(2,'echo ''hello world'' > hello.txt','echo ''hello world'' > hello.txt','2026-05-23 19:38:12');
INSERT INTO successful_scripts VALUES(3,'mkdir -p src && touch src/app.js','mkdir -p src && touch src/app.js','2026-05-23 19:38:15');
INSERT INTO successful_scripts VALUES(4,'touch verify.txt','touch verify.txt','2026-05-23 19:39:20');
INSERT INTO successful_scripts VALUES(5,'echo ''hello world'' > hello.txt','echo ''hello world'' > hello.txt','2026-05-23 19:39:21');
INSERT INTO successful_scripts VALUES(6,'mkdir -p src && touch src/app.js','mkdir -p src && touch src/app.js','2026-05-23 19:39:24');
INSERT INTO successful_scripts VALUES(7,'touch verify.txt','touch verify.txt','2026-05-23 19:40:27');
INSERT INTO successful_scripts VALUES(8,'echo ''hello world'' > hello.txt','echo ''hello world'' > hello.txt','2026-05-23 19:40:28');
INSERT INTO successful_scripts VALUES(9,'mkdir -p src && touch src/app.js','mkdir -p src && touch src/app.js','2026-05-23 19:40:31');
INSERT INTO successful_scripts VALUES(10,'echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','2026-05-23 19:40:34');
INSERT INTO successful_scripts VALUES(11,'sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','2026-05-23 19:40:37');
INSERT INTO successful_scripts VALUES(12,'touch verify.txt','touch verify.txt','2026-05-23 19:46:34');
INSERT INTO successful_scripts VALUES(13,'touch verify.txt','touch verify.txt','2026-05-23 19:47:04');
INSERT INTO successful_scripts VALUES(14,'touch verify.txt','touch verify.txt','2026-05-23 19:47:45');
INSERT INTO successful_scripts VALUES(15,'touch verify.txt','touch verify.txt','2026-05-23 19:48:30');
INSERT INTO successful_scripts VALUES(16,'echo ''hello world'' > hello.txt','echo ''hello world'' > hello.txt','2026-05-23 19:48:34');
INSERT INTO successful_scripts VALUES(17,'mkdir -p src && touch src/app.js','mkdir -p src && touch src/app.js','2026-05-23 19:48:39');
INSERT INTO successful_scripts VALUES(18,'echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','2026-05-23 19:48:44');
INSERT INTO successful_scripts VALUES(19,'sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','2026-05-23 19:48:48');
INSERT INTO successful_scripts VALUES(20,'echo ''<body style="background:blue">Matrix</body>'' > index.html','echo ''<body style="background:blue">Matrix</body>'' > index.html','2026-05-23 19:48:53');
INSERT INTO successful_scripts VALUES(21,'touch verify.txt','touch verify.txt','2026-05-23 19:53:30');
INSERT INTO successful_scripts VALUES(22,'echo ''hello world'' > hello.txt','echo ''hello world'' > hello.txt','2026-05-23 19:53:34');
INSERT INTO successful_scripts VALUES(23,'mkdir -p src && touch src/app.js','mkdir -p src && touch src/app.js','2026-05-23 19:53:37');
INSERT INTO successful_scripts VALUES(24,'echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','2026-05-23 19:53:40');
INSERT INTO successful_scripts VALUES(25,'sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','2026-05-23 19:53:42');
INSERT INTO successful_scripts VALUES(26,'echo ''<body style="background:blue">Matrix</body>'' > index.html','echo ''<body style="background:blue">Matrix</body>'' > index.html','2026-05-23 19:53:45');
INSERT INTO successful_scripts VALUES(27,'touch verify.txt','touch verify.txt','2026-05-23 19:59:05');
INSERT INTO successful_scripts VALUES(28,'echo ''hello world'' > hello.txt','echo ''hello world'' > hello.txt','2026-05-23 19:59:08');
INSERT INTO successful_scripts VALUES(29,'mkdir -p src && touch src/app.js','mkdir -p src && touch src/app.js','2026-05-23 19:59:11');
INSERT INTO successful_scripts VALUES(30,'echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','2026-05-23 19:59:14');
INSERT INTO successful_scripts VALUES(31,'sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','2026-05-23 19:59:15');
INSERT INTO successful_scripts VALUES(32,'echo ''<body style="background:blue">Matrix</body>'' > index.html','echo ''<body style="background:blue">Matrix</body>'' > index.html','2026-05-23 19:59:18');
INSERT INTO successful_scripts VALUES(33,'touch verify.txt','touch verify.txt','2026-05-23 20:03:22');
INSERT INTO successful_scripts VALUES(34,'echo ''hello world'' > hello.txt','echo ''hello world'' > hello.txt','2026-05-23 20:03:24');
INSERT INTO successful_scripts VALUES(35,'mkdir -p src && touch src/app.js','mkdir -p src && touch src/app.js','2026-05-23 20:03:26');
INSERT INTO successful_scripts VALUES(36,'echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','2026-05-23 20:03:29');
INSERT INTO successful_scripts VALUES(37,'sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','2026-05-23 20:03:33');
INSERT INTO successful_scripts VALUES(38,'touch verify.txt','touch verify.txt','2026-05-23 20:04:24');
INSERT INTO successful_scripts VALUES(39,'echo ''hello world'' > hello.txt','echo ''hello world'' > hello.txt','2026-05-23 20:04:26');
INSERT INTO successful_scripts VALUES(40,'mkdir -p src && touch src/app.js','mkdir -p src && touch src/app.js','2026-05-23 20:04:29');
INSERT INTO successful_scripts VALUES(41,'echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','2026-05-23 20:04:33');
INSERT INTO successful_scripts VALUES(42,'sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','2026-05-23 20:04:37');
INSERT INTO successful_scripts VALUES(43,'echo ''<body style="background:blue">Matrix</body>'' > index.html','echo ''<body style="background:blue">Matrix</body>'' > index.html','2026-05-23 20:04:40');
INSERT INTO successful_scripts VALUES(44,'touch verify.txt','touch verify.txt','2026-05-24 01:14:55');
INSERT INTO successful_scripts VALUES(45,'echo ''hello world'' > hello.txt','echo ''hello world'' > hello.txt','2026-05-24 01:14:56');
INSERT INTO successful_scripts VALUES(46,'mkdir -p src && touch src/app.js','mkdir -p src && touch src/app.js','2026-05-24 01:14:58');
INSERT INTO successful_scripts VALUES(47,'echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','2026-05-24 01:15:01');
INSERT INTO successful_scripts VALUES(48,'sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','2026-05-24 01:15:04');
INSERT INTO successful_scripts VALUES(49,'echo ''<body style="background:blue">Matrix</body>'' > index.html','echo ''<body style="background:blue">Matrix</body>'' > index.html','2026-05-24 01:15:07');
INSERT INTO successful_scripts VALUES(50,'touch verify.txt','touch verify.txt','2026-05-24 01:16:52');
INSERT INTO successful_scripts VALUES(51,'echo ''hello world'' > hello.txt','echo ''hello world'' > hello.txt','2026-05-24 01:16:54');
INSERT INTO successful_scripts VALUES(52,'mkdir -p src && touch src/app.js','mkdir -p src && touch src/app.js','2026-05-24 01:16:55');
INSERT INTO successful_scripts VALUES(53,'echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','2026-05-24 01:17:02');
INSERT INTO successful_scripts VALUES(54,'sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','2026-05-24 01:17:28');
INSERT INTO successful_scripts VALUES(55,'echo ''<body style="background:blue">Matrix</body>'' > index.html','echo ''<body style="background:blue">Matrix</body>'' > index.html','2026-05-24 01:17:46');
INSERT INTO successful_scripts VALUES(56,'sqlite3 store.db "CREATE TABLE items (id INT, name TEXT); INSERT INTO items VALUES (1, ''bolt''); CREATE TABLE price (id INT, cost INT); INSERT INTO price VALUES (1, 10); SELECT items.name, price.cost FROM items JOIN price ON items.id = price.id;"','sqlite3 store.db "CREATE TABLE items (id INT, name TEXT); INSERT INTO items VALUES (1, ''bolt''); CREATE TABLE price (id INT, cost INT); INSERT INTO price VALUES (1, 10); SELECT items.name, price.cost FROM items JOIN price ON items.id = price.id;"','2026-05-24 01:18:11');
INSERT INTO successful_scripts VALUES(57,'touch verify.txt','touch verify.txt','2026-05-24 01:20:47');
INSERT INTO successful_scripts VALUES(58,'echo ''hello world'' > hello.txt','echo ''hello world'' > hello.txt','2026-05-24 01:20:49');
INSERT INTO successful_scripts VALUES(59,'mkdir -p src && touch src/app.js','mkdir -p src && touch src/app.js','2026-05-24 01:20:52');
INSERT INTO successful_scripts VALUES(60,'echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','echo ''CREATE TABLE users (id INTEGER, name TEXT);'' > users.sql','2026-05-24 01:21:20');
INSERT INTO successful_scripts VALUES(61,'sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','sqlite3 users.db ''CREATE TABLE users (id INTEGER, name TEXT);''','2026-05-24 01:21:32');
INSERT INTO successful_scripts VALUES(62,'echo ''<body style="background:blue">Matrix</body>'' > index.html','echo ''<body style="background:blue">Matrix</body>'' > index.html','2026-05-24 01:21:44');
INSERT INTO successful_scripts VALUES(63,'sqlite3 store.db "CREATE TABLE items (id INT, name TEXT); INSERT INTO items VALUES (1, ''bolt''); CREATE TABLE price (id INT, cost INT); INSERT INTO price VALUES (1, 10); SELECT items.name, price.cost FROM items JOIN price ON items.id = price.id;"','sqlite3 store.db "CREATE TABLE items (id INT, name TEXT); INSERT INTO items VALUES (1, ''bolt''); CREATE TABLE price (id INT, cost INT); INSERT INTO price VALUES (1, 10); SELECT items.name, price.cost FROM items JOIN price ON items.id = price.id;"','2026-05-24 01:22:37');
PRAGMA writable_schema=ON;
CREATE TABLE IF NOT EXISTS sqlite_sequence(name,seq);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('snippets',4);
INSERT INTO sqlite_sequence VALUES('code_patterns',4);
INSERT INTO sqlite_sequence VALUES('successful_scripts',63);
CREATE UNIQUE INDEX idx_token_sequence ON code_patterns(token_sequence);
PRAGMA writable_schema=OFF;
COMMIT;
