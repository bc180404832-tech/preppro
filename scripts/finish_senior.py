#!/usr/bin/env python3
import json

with open('/workspaces/preppro/src/data/senior.json', 'r') as f:
    questions = json.load(f)

def add_mcq(qid, stack, topic, question, options, answer, explanation):
    questions.append({
        "id": qid,
        "level": "senior",
        "stack": stack,
        "type": "mcq",
        "topic": topic,
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": explanation
    })

def add_open(qid, stack, topic, question, expected_key_points, sample_answer):
    questions.append({
        "id": qid,
        "level": "senior",
        "stack": stack,
        "type": "open",
        "topic": topic,
        "question": question,
        "expectedKeyPoints": expected_key_points,
        "sampleAnswer": sample_answer
    })

# ----------------- REACT SENIOR (4 more) -----------------
add_mcq("sr-react-23", "react", "Custom React Reconciler",
    "Which package is used to build custom React renderers that target environments other than the browser DOM (e.g. CLI terminals, Canvas, Three.js)?",
    [
        "A) `react-dom`",
        "B) `react-reconciler`",
        "C) `react-native-web`",
        "D) `react-compiler`"
    ],
    "B",
    "`react-reconciler` allows developers to implement host config methods (`createInstance`, `appendInitialChild`, `commitUpdate`) to render React components to custom targets like terminal TUIs (Ink), Canvas, or WebGL."
)

add_mcq("sr-react-24", "react", "React 18 Tearing Mechanics",
    "What is 'visual tearing' in concurrent React rendering?",
    [
        "A) When an LCD screen cracks physically",
        "B) When two components on the screen display conflicting data values from the same external store during the same render pass because an external store mutation was processed between yielded render slices",
        "C) When CSS animations drop below 30 FPS",
        "D) An image decoding error in WebP"
    ],
    "B",
    "Tearing occurs when a mutable external data source updates while concurrent React is midway through a time-sliced render, leading to different components displaying inconsistent state snapshots."
)

add_open("sr-react-25", "react", "Custom Virtual DOM Terminal Renderer Architecture",
    "How does a library like Ink or a custom React terminal renderer translate JSX elements like `<Box>` and `<Text>` into terminal ANSI escape codes and manage terminal resize events?",
    [
        "Uses react-reconciler host config (createInstance, appendChild, commitUpdate)",
        "Uses Yoga layout engine (compiled C/WebAssembly flexbox) to calculate terminal row/column coordinates",
        "Writes ANSI escape sequences and cursor movement codes to process.stdout",
        "Listens for process.stdout.on('resize') to trigger re-layout and re-render"
    ],
    "1. Host Configuration with `react-reconciler`:\nImplements host methods (`createInstance`, `appendInitialChild`, `commitUpdate`). Elements like `<Box>` and `<Text>` create internal node instances representing layout and text nodes.\n2. Flexbox in the Terminal:\nUses Facebook's Yoga engine (a flexbox layout engine in WebAssembly/C) to compute exact character column and row coordinates from CSS-like properties (`flexDirection`, `padding`).\n3. ANSI Output:\nOn commit, the renderer traverses the layout tree and writes ANSI escape codes (cursor positioning, color codes, clean line sequences) directly to `process.stdout`.\n4. Resize Handling:\nListens to `process.stdout.on('resize')`, updates Yoga root node dimensions, and triggers a full reconciliation."
)

add_open("sr-react-26", "react", "Deep Profiling: Wasted Renders vs Layout Triggers",
    "Explain how to use React DevTools Profiler and Chrome DevTools Performance panel in tandem to diagnose severe frame drops caused by layout thrashing (forced synchronous reflow) inside `useLayoutEffect`.",
    [
        "React Profiler identifies which components rendered and how long commit took",
        "Chrome Performance panel captures browser main thread: Layout, Recalculate Style, Paint",
        "useLayoutEffect runs synchronously immediately after DOM mutations before browser paint; reading layout properties (offsetWidth, scrollHeight) forces browser layout thrashing",
        "Fix: Batch DOM reads before writes or move logic to useEffect / ResizeObserver"
    ],
    "1. React Profiler: Highlights components with long render or commit durations in flamecharts. However, it cannot show what the browser main thread is doing.\n2. Chrome Performance Panel: Captures bottom-up flamecharts of the browser engine. Forced synchronous layouts appear as red warning banners: 'Forced reflow is a likely performance bottleneck'.\n3. The `useLayoutEffect` Hazard:\n`useLayoutEffect` fires synchronously before the browser paints. If code mutates a DOM style (`element.style.width = '100px'`) and immediately reads a layout property (`element.offsetHeight`), it forces the browser to synchronously recalculate layout on the spot ('layout thrashing').\n4. Resolution:\n- Batch reads before writes.\n- Use `requestAnimationFrame`.\n- Prefer `ResizeObserver` for measuring DOM dimensions asynchronously."
)

# ----------------- NODE.JS SENIOR (4 more) -----------------
add_mcq("sr-node-17", "node", "V8 TurboFan De-Optimization",
    "What triggers V8's TurboFan compiler to 'de-optimize' hot machine code back to Ignition bytecode at runtime?",
    [
        "A) Running out of disk space",
        "B) Type feedback violation: when a function previously optimized assuming stable types (e.g. always receiving numbers) receives an unexpected type (e.g. an object or string), invalidating JIT optimization assumptions",
        "C) Changing the Node.js port",
        "D) Closing an HTTP socket"
    ],
    "B",
    "TurboFan generates optimized machine code based on speculative type feedback from the Ignition interpreter. Passing an unexpected data type breaks the speculative assumption, forcing V8 to 'deopt' back to interpreted bytecode."
)

add_mcq("sr-node-18", "node", "TCP_NODELAY (Nagle's Algorithm)",
    "Why does Node.js enable `socket.setNoDelay(true)` (disabling Nagle's algorithm) by default for TCP sockets?",
    [
        "A) To encrypt TCP packets",
        "B) To send small data packets immediately across the network without waiting to buffer them into full MTU frames, minimizing latency for real-time APIs and WebSockets",
        "C) To prevent packet collisions",
        "D) To reduce CPU usage on the client"
    ],
    "B",
    "Nagle's algorithm coalesces small TCP packets to reduce network overhead, but causes artificial 40ms delays when combined with TCP delayed ACKs. Disabling it (`TCP_NODELAY=1`) sends bytes instantly."
)

add_open("sr-node-19", "node", "Libuv Threadpool Contention Detection Script",
    "Write a production Node.js monitoring script that detects when libuv's internal thread pool is saturated (threadpool starvation) and alerts before API latency degrades.",
    [
        "Thread pool handles fs, crypto, zlib, dns.lookup",
        "Benchmark threadpool latency by periodically executing a lightweight crypto.pbkdf2 task and measuring drift from baseline",
        "If execution duration exceeds threshold (e.g. > 50ms for a 5ms task), thread pool starvation is occurring",
        "Logs alert with recommendations to increase UV_THREADPOOL_SIZE"
    ],
    "```javascript\nimport crypto from 'node:crypto';\n\nexport function monitorThreadpool(intervalMs = 2000, thresholdMs = 40) {\n  setInterval(() => {\n    const start = performance.now();\n    // Lightweight task dispatched to libuv threadpool\n    crypto.pbkdf2('test', 'salt', 100, 16, 'sha512', (err) => {\n      const duration = performance.now() - start;\n      if (duration > thresholdMs) {\n        console.warn(\n          `🚨 [LIBUV THREADPOOL STARVATION] Duration: ${duration.toFixed(2)}ms (expected < 5ms). ` +\n          `Thread pool is saturated! Current UV_THREADPOOL_SIZE=${process.env.UV_THREADPOOL_SIZE || 4}`\n        );\n      }\n    });\n  }, intervalMs).unref(); // unref so timer doesn't prevent clean shutdown\n}\n```"
)

add_open("sr-node-20", "node", "Handling EMFILE and Linux File Descriptor Limits",
    "What causes an `EMFILE: too many open files` error in a high-concurrency Node.js server, and how do you resolve it at the OS level (ulimit / systemd) and application level (graceful-fs / connection pooling)?",
    [
        "In Linux, every TCP socket, open file, and database connection consumes a File Descriptor (FD)",
        "Default OS limit is often 1024; high concurrency easily exceeds this limit",
        "OS resolution: Increase soft and hard limits via ulimit -n 65535 or /etc/security/limits.conf or systemd LimitNOFILE=65536",
        "Application resolution: Use connection pools with strict caps, close idle sockets with keepAliveTimeout, use graceful-fs to queue file opens"
    ],
    "1. Root Cause:\nIn Linux, 'everything is a file'. Every incoming HTTP TCP socket, outgoing database connection, and file read consumes a File Descriptor (FD). Default Linux user limits are often set to 1,024 FDs. Under moderate load (e.g. 1,500 concurrent connections), Node crashes with `Error: EMFILE, too many open files`.\n2. Operating System Resolution:\n- Temporary: `ulimit -n 65536`.\n- Permanent: In `/etc/security/limits.conf`:\n  `* soft nofile 65536`\n  `* hard nofile 65536`\n- In Systemd service files: Add `LimitNOFILE=65536`.\n3. Application Architecture Defenses:\n- Cap database connection pools (e.g. `max: 20` in `pg.Pool`).\n- Set strict HTTP agent maxSockets: `new http.Agent({ maxSockets: 100 })`.\n- Use `graceful-fs` to queue file reads when FD limits are approached instead of crashing."
)

# ----------------- EXPRESS & DISTRIBUTED SYSTEMS (4 more) -----------------
add_mcq("sr-express-13", "express", "Request Hedging (Speculative Retries)",
    "What is 'Request Hedging' (Speculative Retries) in an ultra-low-latency distributed API gateway?",
    [
        "A) Betting on foreign currencies",
        "B) If a downstream microservice has not responded within the p95 latency threshold (e.g. 50ms), the gateway sends an identical redundant request to a second replica and accepts whichever response arrives first, canceling the other",
        "C) Retrying failed requests 1,000 times",
        "D) Caching requests in browser memory"
    ],
    "B",
    "Popularized by Google's 'The Tail at Scale', request hedging eliminates latency outliers by issuing a speculative backup request to another replica when the primary takes longer than expected, slashing tail (p99) latency."
)

add_mcq("sr-express-14", "express", "CSP Nonce Generation in Express SSR",
    "Why must a Content-Security-Policy (CSP) `nonce` be cryptographically unique per HTTP request when server-rendering React?",
    [
        "A) To encrypt the CSS stylesheet",
        "B) If a nonce is static or predictable, attackers can inject malicious `<script nonce='static_val'>` tags, completely nullifying the CSP protection",
        "C) Nonces are required by SQL databases",
        "D) To save server bandwidth"
    ],
    "B",
    "A CSP nonce must be generated freshly on every request using a cryptographically secure random generator (e.g. `crypto.randomBytes(16).toString('base64')`). Predictable or reusable nonces allow attackers to bypass CSP."
)

add_open("sr-express-15", "express", "High-Throughput Zero-Copy File Serving",
    "How does Express's `res.sendFile()` utilize the Linux `sendfile(2)` system call for zero-copy file transfers? How does this outperform reading files into JavaScript memory?",
    [
        "Traditional file transfer: reads disk into kernel buffer -> copies to user space (Node RAM) -> copies back to kernel socket buffer -> NIC",
        "sendfile(2) system call transfers data directly from file descriptor to network socket descriptor inside kernel space",
        "Zero context switching between user space and kernel space, zero V8 heap allocation, line-rate throughput"
    ],
    "1. Traditional Node.js Read/Write Overhead:\nRunning `fs.readFile()` and `res.write()` requires 4 context switches and 3 memory copies:\n- Disk -> Kernel page cache (1)\n- Kernel page cache -> Node.js user-space Buffer (2)\n- Node.js user-space Buffer -> Socket buffer in kernel (3)\n- Socket buffer -> Network Interface Card (NIC) (4)\nThis causes heavy CPU context switching and V8 heap pressure.\n2. Zero-Copy `sendfile(2)`:\nWhen you use `res.sendFile()`, Node invokes the OS `sendfile` system call. The Linux kernel transfers data directly from the filesystem cache to the network card buffer entirely within kernel space.\nBenefits: Zero data is copied into Node's memory, CPU utilization drops to near zero, and file transfers saturate network line rate."
)

add_open("sr-express-16", "express", "Distributed Lock Manager with Lease Watchdog",
    "Write a production-grade Distributed Lock utility in Node.js with Redis that prevents race conditions, supports an auto-renewing heartbeat lease (watchdog pattern), and safely releases only if the lock is still owned by the caller.",
    [
        "Acquires lock with SET key uuid NX PX 10000",
        "Starts background timer (watchdog) renewing PX every 3 seconds while task runs",
        "Releases lock using atomic Lua script checking if GET key == uuid before DEL",
        "Guarantees that a long-running job does not lose lock prematurely, and never deletes a lock held by another process if it expired"
    ],
    "```javascript\nimport crypto from 'node:crypto';\n\nexport class DistributedLock {\n  constructor(redisClient) {\n    this.redis = redisClient;\n  }\n\n  async acquire(lockKey, ttlMs = 10000) {\n    const lockId = crypto.randomUUID();\n    const acquired = await this.redis.set(lockKey, lockId, 'PX', ttlMs, 'NX');\n    if (!acquired) return null;\n\n    // Start watchdog to renew lease while task executes\n    const renewalInterval = setInterval(async () => {\n      const luaRenew = `\n        if redis.call('get', KEYS[1]) == ARGV[1] then\n          return redis.call('pexpire', KEYS[1], ARGV[2])\n        else\n          return 0\n        end\n      `;\n      await this.redis.eval(luaRenew, 1, lockKey, lockId, ttlMs);\n    }, ttlMs / 3);\n\n    const release = async () => {\n      clearInterval(renewalInterval);\n      const luaRelease = `\n        if redis.call('get', KEYS[1]) == ARGV[1] then\n          return redis.call('del', KEYS[1])\n        else\n          return 0\n        end\n      `;\n      await this.redis.eval(luaRelease, 1, lockKey, lockId);\n    };\n\n    return { lockId, release };\n  }\n}\n```"
)

# ----------------- MONGODB AT SCALE (4 more) -----------------
add_mcq("sr-mongo-16", "mongodb", "Clustered Collections in MongoDB",
    "What is a 'Clustered Collection' in MongoDB 5.3+, and how does it improve write performance?",
    [
        "A) A collection that only works on clustered computers",
        "B) Documents are physically ordered and stored directly on disk within the clustered index B-Tree (by `_id`), eliminating a separate index and heap storage and avoiding double-writes",
        "C) A collection that compresses text into images",
        "D) A collection stored on multiple cloud providers simultaneously"
    ],
    "B",
    "In traditional collections, the index points to separate record store pages. In a Clustered Collection, documents are stored directly in the clustered index nodes, improving write throughput, range scan speeds, and reducing disk footprint."
)

add_mcq("sr-mongo-17", "mongodb", "Aggregation $facet Memory Limit",
    "What is the RAM limit for an individual `$facet` stage in MongoDB, and what option must be enabled for large pipelines?",
    [
        "A) 16MB limit; must use `$reduce`",
        "B) 100MB RAM limit; for operations exceeding 100MB, `allowDiskUse: true` must be specified to allow spilling temporary documents to disk",
        "C) 1GB limit; cannot be changed",
        "D) Facet has no memory limit"
    ],
    "B",
    "MongoDB limits internal aggregation pipeline stages to 100MB of RAM. If an aggregation (like `$facet` or `$sort`) exceeds 100MB, it aborts unless `{ allowDiskUse: true }` is enabled."
)

add_open("sr-mongo-18", "mongodb", "Cross-Region Replica Sets with wtimeout",
    "Why must Write Concerns with `w: 'majority'` always be accompanied by a `wtimeout` parameter in multi-region MongoDB replica sets? Trace what happens when a cross-region fiber link is severed.",
    [
        "w: 'majority' waits indefinitely by default if majority cannot acknowledge",
        "If a cross-region partition occurs, writes will block client threads forever without wtimeout",
        "wtimeout sets a maximum duration; if exceeded, MongoDB returns error but the write may still succeed on the primary (write concern error vs write error)",
        "Application must handle write concern errors gracefully"
    ],
    "1. The Danger of Omitted `wtimeout`:\nWhen `{ w: 'majority' }` is specified without `wtimeout`, the MongoDB driver blocks the application thread indefinitely until a majority of replica set nodes acknowledge the write.\n2. What Happens During a Cross-Region Partition:\nIf two of three nodes are separated across continents by a severed fiber link, the primary in Region A cannot reach the secondaries in Region B. Incoming writes block indefinitely, consuming all Express connection pool threads and freezing the entire application server.\n3. Specifying `wtimeout`:\nAlways specify `{ w: 'majority', wtimeout: 5000 }` (5 seconds). If replication is delayed past 5s, MongoDB returns a Write Concern Error, unblocking the Node.js thread so it can return an HTTP 504 Gateway Timeout or execute fallback logic."
)

add_open("sr-mongo-19", "mongodb", "MongoDB Schema Evolution: Outlier and Schema Versioning Patterns",
    "Describe the 'Outlier Pattern' and 'Schema Versioning Pattern' in enterprise MongoDB systems. How do they handle extreme edge cases (e.g. influencers with 50M followers) and zero-downtime schema evolution?",
    [
        "Outlier Pattern: Flags documents exceeding standard bounds (has_overflow: true) and offloads overflow data to an overflow collection, keeping 99.9% of documents uniform and fast",
        "Schema Versioning Pattern: Adds schema_version: 2 to documents; migration logic in application layer transforms v1 documents to v2 dynamically on read/write without massive blocking offline migrations"
    ],
    "1. The Outlier Pattern:\nMost users on a social platform have fewer than 1,000 followers, which easily embeds in a document array. However, a celebrity with 50 million followers breaks the 16MB document limit and slows queries.\n- Solution: Add a boolean flag `{ has_overflow: true }`. Normal users have all followers embedded. When followers exceed 1,000, overflow followers are written to a separate `follower_overflow` collection. Queries optimize for the 99.9% normal cases while gracefully handling outliers.\n2. The Schema Versioning Pattern:\nInstead of running a multi-terabyte offline update script that locks collections for days, include a version field `{ schema_version: 2 }` in documents.\n- In the application layer: When reading a document, if `schema_version === 1`, transform the shape in memory. When saving, write it back as version 2. The database migrates organically and continuously with zero downtime."
)

# ----------------- POSTGRESQL AT SCALE (4 more) -----------------
add_mcq("sr-pg-16", "postgresql", "JIT Compilation Tuning in PostgreSQL",
    "When should JIT (Just-In-Time) compilation be disabled (`jit = off`) in a high-concurrency PostgreSQL OLTP database?",
    [
        "A) When using Ubuntu Linux",
        "B) For short, fast OLTP queries (like primary key lookups), because JIT compilation adds 5-15ms of planning overhead which can be 10x longer than the actual query execution time",
        "C) JIT cannot be turned off",
        "D) Only when running out of RAM"
    ],
    "B",
    "PostgreSQL 12+ enables LLVM JIT compilation by default. While beneficial for long analytical queries (OLAP), for high-concurrency OLTP workloads running in < 2ms, JIT compilation overhead degrades query throughput significantly."
)

add_mcq("sr-pg-17", "postgresql", "Foreign Data Wrappers (postgres_fdw)",
    "What capability does PostgreSQL's `postgres_fdw` extension provide?",
    [
        "A) It wraps passwords in SHA-256",
        "B) It allows querying, joining, and updating tables located on remote, separate PostgreSQL servers as if they were local tables within the current database",
        "C) It translates PostgreSQL queries into MongoDB syntax",
        "D) It connects PostgreSQL to Redis"
    ],
    "B",
    "`postgres_fdw` implements standard SQL/MED (Management of External Data). You can create foreign servers, user mappings, and query remote database tables directly in joins with local tables."
)

add_open("sr-pg-18", "postgresql", "Preventing Replication Lag in Physical Streaming Replication",
    "Explain what causes replication lag in PostgreSQL physical streaming replication and what setting `synchronous_commit = off` does. How do you monitor replication lag (`pg_stat_replication`), and how do you protect read replicas from query cancellation (`hot_standby_feedback`)?",
    [
        "Causes: High write volume on primary, slow network or disk on standby, long-running queries on standby holding locks",
        "Monitoring: pg_stat_replication (replay_lag, write_lag, flush_lag)",
        "hot_standby_feedback: Instructs standby to inform primary of oldest active transaction, preventing primary vacuum from removing rows needed by standby queries",
        "synchronous_commit = off trades slight durability (last few milliseconds of transactions lost in crash) for dramatically faster write throughput"
    ],
    "1. Causes of Replication Lag:\n- Heavy write bursts on the primary exceeding the standby's single-threaded WAL replay capability.\n- Standby query cancellation: If a long query on the standby reads rows that VACUUM on the primary wants to remove, PostgreSQL halts replay or cancels the standby query.\n2. Protection via `hot_standby_feedback`:\nEnabling `hot_standby_feedback = on` instructs the read replica to inform the primary about its oldest running snapshot. The primary delays vacuuming tuples needed by the standby, eliminating query cancellations.\n3. Monitoring:\nInspect `pg_stat_replication` on the primary:\n```sql\nSELECT application_name, client_addr, state, \n       pg_wal_lsn_diff(sent_lsn, replay_lsn) AS bytes_lag,\n       replay_lag\nFROM pg_stat_replication;\n```\n4. `synchronous_commit = off`:\nTransactions return success immediately after writing to WAL buffer in RAM without waiting for an `fsync` to disk. Guarantees zero transaction corruption, though a crash may lose the last ~20ms of committed transactions."
)

add_open("sr-pg-19", "postgresql", "PostgreSQL Forensic Audit with pg_stat_statements",
    "Explain how to configure and utilize `pg_stat_statements` to perform a performance audit of an active PostgreSQL database. Write the SQL query to locate the top 5 queries consuming the most cumulative execution time.",
    [
        "Configure: shared_preload_libraries = 'pg_stat_statements' in postgresql.conf and CREATE EXTENSION pg_stat_statements",
        "Query selects query, calls, total_exec_time, mean_exec_time, rows, shared_blks_hit, shared_blks_read",
        "Orders by total_exec_time DESC limit 5",
        "Identifies queries that run frequently with low individual cost, or rare queries with massive runtime"
    ],
    "```sql\n-- 1. Setup in postgresql.conf:\n-- shared_preload_libraries = 'pg_stat_statements'\n-- CREATE EXTENSION IF NOT EXISTS pg_stat_statements;\n\n-- 2. Top 5 most expensive queries by cumulative CPU/execution time:\nSELECT \n  queryid,\n  substring(query, 1, 100) AS clean_query,\n  calls,\n  round(total_exec_time::numeric, 2) AS total_time_ms,\n  round(mean_exec_time::numeric, 2) AS mean_time_ms,\n  rows,\n  round((100.0 * shared_blks_hit / nullif(shared_blks_hit + shared_blks_read, 0))::numeric, 2) AS cache_hit_pct\nFROM pg_stat_statements\nORDER BY total_exec_time DESC\nLIMIT 5;\n```\nAnalysis: Highlights both high-frequency queries (called 100k times taking 5ms each = 500s cumulative) and unindexed bulk scans, showing exactly where to focus indexing efforts."
)

# ----------------- FULLSTACK SYSTEM DESIGN (4 more) -----------------
add_mcq("sr-full-13", "fullstack", "Real-Time Leaderboard with Redis ZSET",
    "Why are Redis Sorted Sets (`ZSET`) preferred over SQL `ORDER BY score DESC` for real-time leaderboards with 10 million players?",
    [
        "A) SQL databases cannot store numbers",
        "B) Redis Sorted Sets use a SkipList and Hash Map data structure, providing O(log N) score updates (`ZADD`), instant O(1) rank lookups (`ZRANK`), and range queries (`ZREVRANGE`) entirely in RAM, without expensive database sorting locks",
        "C) Redis Sorted Sets encrypt scores",
        "D) They do not require a network connection"
    ],
    "B",
    "In PostgreSQL, querying top players requires scanning and sorting millions of rows. Redis Sorted Sets maintain elements in an internal SkipList, guaranteeing O(log N) insertion, update, and rank extraction at microsecond speeds."
)

add_mcq("sr-full-14", "fullstack", "Multi-Tenant SaaS Database Isolation Models",
    "Which multi-tenant architecture provides the optimal balance of data isolation, cost efficiency, and operational maintenance for an enterprise SaaS PERN/MERN application?",
    [
        "A) Buying a new physical computer for every customer",
        "B) Shared Database with Shared Schema isolated by PostgreSQL Row-Level Security (RLS) or tenant ID filtering, paired with dedicated databases for ultra-high-tier enterprise customers",
        "C) Storing all customer data in a single JSON file",
        "D) Storing data exclusively in client localStorage"
    ],
    "B",
    "A pooled shared database with Row-Level Security delivers the highest resource utilization and lowest operational maintenance for standard tiers, while allowing seamless provisioning of isolated single-tenant databases for VIP enterprise tiers."
)

add_open("sr-full-15", "fullstack", "Designing an Event-Driven Notification System at Scale",
    "Architect a resilient, high-volume Notification System (Push, Email, SMS) for a PERN/MERN platform sending 50 million notifications/day. Cover event ingestion (Kafka/RabbitMQ), rate limiting per user, template rendering, and delivery status webhooks.",
    [
        "Ingestion: Core services publish NotificationRequested event to Apache Kafka partitioned by userId",
        "Worker pool: Consumer services consume events, check user notification preferences and rate limits (Redis sliding window to prevent spamming)",
        "Rendering: Distributed template engine renders localized HTML/text",
        "Dispatch: Dispatches to third-party providers (SendGrid, Twilio, APNs/FCM) using Circuit Breaker and retry with exponential backoff",
        "Status: Ingests delivery webhooks into PostgreSQL audit log via Outbox pattern"
    ],
    "1. Event Ingestion Tier:\nMicroservices emit `NotificationRequested` events to Apache Kafka. Partitioning by `userId` guarantees sequential processing for individual users (e.g. an account verification email is sent before welcome notifications).\n2. Rate Limiting & User Preferences:\nWorkers consume events and check:\n- User notification preferences in Redis.\n- User rate limits using Redis Sliding Window (e.g. max 5 push notifications per hour to avoid spam fatigue).\n3. Rendering Tier:\nStateless Node.js workers compile localized email/push templates with data parameters.\n4. Provider Dispatch Tier (Resilience):\nDispatches to third-party gateways (SendGrid for email, Twilio for SMS, Firebase FCM for push) wrapped in Circuit Breakers (Opossum) with exponential backoff and jitter. Failed deliveries push to a Dead Letter Queue (DLQ).\n5. Ingestion Webhooks & Analytics:\nDelivery callbacks from SendGrid/Twilio hit an Express webhook endpoint, verifying HMAC signatures and updating delivery statuses in PostgreSQL."
)

add_open("sr-full-16", "fullstack", "Automated Secret Rotation with HashiCorp Vault in Node.js",
    "Explain how to architect dynamic, self-rotating database credentials in a Node.js Express service using HashiCorp Vault. How does this eliminate static database passwords in `.env` files and survive credential expiration without service restarts?",
    [
        "App authenticates with Vault using Kubernetes Service Account or AppRole",
        "Vault PostgreSQL database secrets engine generates short-lived dynamic DB user credentials (e.g. valid for 1 hour)",
        "Node service renews lease periodically using Vault SDK",
        "Before lease expiration, Vault issues new credentials; pg.Pool pool.end() and re-initializes with zero downtime"
    ],
    "1. The Problem with Static Credentials:\nStoring static credentials in `.env` or Kubernetes secrets creates major exposure risks: if leaked, attackers maintain permanent database access until manually rotated.\n2. Vault Dynamic Database Credentials Architecture:\n- Authentication: The Node.js pod authenticates to Vault via Kubernetes service account tokens (AppRole).\n- Dynamic Generation: Node requests database credentials from Vault: `vault.read('database/creds/pern-role')`. Vault talks to PostgreSQL and executes: `CREATE ROLE v_user_123 WITH LOGIN PASSWORD 'temp_secret' VALID UNTIL ...`.\n- Leases & Renewal: Credentials are valid for 1 hour. Node runs a background renewal loop (`vault.renew(lease_id)`).\n- Rotation & Pool Refresh: If a credential cannot be renewed or expires, Node fetches fresh credentials from Vault, establishes a new `pg.Pool`, and gracefully drains the old pool without dropping in-flight user requests."
)

with open('/workspaces/preppro/src/data/senior.json', 'w') as f:
    json.dump(questions, f, indent=2)

print(f"Total Senior Questions: {len(questions)}")
