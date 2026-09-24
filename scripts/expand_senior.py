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

# ----------------- REACT SENIOR EXTRA -----------------
add_mcq("sr-react-17", "react", "React Fiber Double Buffering",
    "How does React Fiber use the 'Double Buffering' technique during rendering?",
    [
        "A) It renders to two different browser windows simultaneously",
        "B) React maintains two fiber trees in memory: `current` (representing what is currently mounted on screen) and `workInProgress` (representing the draft being computed); upon completion of the commit phase, it flips a single root pointer to switch trees instantly with zero flicker",
        "C) It caches all HTML in two Redis databases",
        "D) It converts the screen into an OpenGL double buffer"
    ],
    "B",
    "Borrowing from graphics rendering, Fiber avoids incomplete UI updates by assembling the new draft off-screen in the `workInProgress` tree. At the end of the commit phase, React atomically swaps the pointer so `workInProgress` becomes `current`."
)

add_mcq("sr-react-18", "react", "React 19 Action Hooks (useOptimistic)",
    "What is the primary role of the `useOptimistic` hook introduced in React 19?",
    [
        "A) It generates positive motivational messages for developers",
        "B) It allows UI state to update immediately with an optimistic value while an asynchronous server action is in flight, automatically rolling back to the confirmed server state if the action errors or completes",
        "C) It removes the need for database backups",
        "D) It forces the browser to assume all network requests will return 200"
    ],
    "B",
    "`useOptimistic` manages optimistic UI updates declaratively: the interface immediately reflects the user's expected result (e.g. sending a message or liking a post) and automatically reconciles when the actual server mutation settles."
)

add_mcq("sr-react-19", "react", "Virtual List Windowing Algorithm",
    "How does virtualized list windowing (e.g. `react-window` or `tanstack-virtual`) maintain 60 FPS when scrolling through 1,000,000 items?",
    [
        "A) It compresses all 1,000,000 items into a single string",
        "B) It calculates the visible viewport bounding box and renders only the small subset of DOM nodes (e.g. 20-30 rows) currently visible plus a small buffer, positioning them absolutely via translateY while keeping total DOM nodes O(1)",
        "C) It moves the list into a Web Worker",
        "D) It renders the list onto an HTML5 canvas"
    ],
    "B",
    "Virtual windowing calculates scroll offset and container dimensions, dynamically mounting only the items visible in the viewport. This keeps the DOM lightweight (O(1) elements) regardless of list size, preventing DOM memory leaks and layout reflow stalls."
)

add_mcq("sr-react-20", "react", "React Fiber Bailout (beginWork)",
    "Under what exact conditions will React Fiber's `beginWork` phase 'bail out' and skip reconciling an entire component subtree?",
    [
        "A) When the browser window is minimized",
        "B) If the component's `oldProps === newProps` (by reference equality), the component's state has not updated, and no context it consumes has changed, React clones the existing fiber and skips all child work",
        "C) Only if the component is written in TypeScript",
        "D) When the network connection is offline"
    ],
    "B",
    "During `beginWork`, Fiber checks reference equality on props and state. If `oldProps === newProps`, no scheduled update exists on the fiber, and no consumed context changed, React bails out, skipping work on all descendants."
)

add_open("sr-react-21", "react", "Micro-Frontend State Synchronization",
    "You have three independent React micro-frontends embedded on a single web page, each bundled with its own React root. Design a low-latency, decoupled event bus architecture using `BroadcastChannel` or `CustomEvent` to synchronize user authentication state and shopping cart updates without tight coupling.",
    [
        "Uses browser native CustomEvents on window or BroadcastChannel API for cross-frame/cross-tab communication",
        "Pub/Sub contract with typed payloads and versioned event names (e.g. APP_AUTH_STATE_CHANGED)",
        "React custom hook (useMicroFrontendEvent) that subscribes on mount and cleans up on unmount",
        "Avoids leaking memory and avoids dependency on shared global singletons across independent bundlers"
    ],
    "1. Architecture Pattern:\nUse the native browser `BroadcastChannel` API (or `window.dispatchEvent(new CustomEvent(...))` for single-window):\n```javascript\n// shared-events.js (Contract)\nexport const EVENT_BUS = new BroadcastChannel('app_enterprise_bus');\n\nexport const MicroEvents = {\n  AUTH_CHANGE: 'AUTH_CHANGE',\n  CART_UPDATE: 'CART_UPDATE'\n};\n```\n2. Reusable React Hook:\n```javascript\nexport function useMicroEvent(eventType, handler) {\n  useEffect(() => {\n    const onMessage = (event) => {\n      if (event.data?.type === eventType) {\n        handler(event.data.payload);\n      }\n    };\n    EVENT_BUS.addEventListener('message', onMessage);\n    return () => EVENT_BUS.removeEventListener('message', onMessage);\n  }, [eventType, handler]);\n}\n```\n3. Benefits: Zero bundle coupling. Each micro-frontend can be built with different React versions or deployed independently while maintaining instantaneous, tear-free event synchronization."
)

add_open("sr-react-22", "react", "React Server Actions Security Forensics",
    "Analyze the security attack surfaces of React Server Actions in modern Fullstack frameworks (like Next.js 14/15). How do you prevent unauthorized execution, data exposure through closure captures, and CSRF attacks?",
    [
        "Server Actions generate public HTTP POST endpoints that can be invoked directly by anyone with curl/fetch",
        "Must verify authentication and authorization inside the Server Action body (not just on the rendering page)",
        "Closure capture risk: Variables in server components closed over by inline actions can leak private data into the encrypted action ID payload",
        "CSRF protection: Ensure framework validates Origin/Host headers or anti-CSRF tokens"
    ],
    "1. The Core Attack Surface:\nEvery React Server Action (`'use server'`) is exported as an exposed, publicly reachable HTTP POST endpoint with a generated hash identifier. Attackers can call this action directly using `curl` or automated scripts, completely bypassing client-side button disables or form validations.\n2. Defenses:\n- Explicit Authorization: Always perform authentication and role checks inside the action body: `const session = await getSession(); if (!session?.user?.isAdmin) throw new ForbiddenError();`.\n- Strict Input Validation: Validate all incoming arguments using Zod schemas.\n- Closure Leak Prevention: Never close over sensitive server secrets or large database entities in inline Server Actions; the framework serializes closed-over variables into the action payload (often signed/encrypted), which increases payload size and risks exposure.\n- CSRF Defense: Modern frameworks verify the `Origin` and `Host` headers match for server action requests."
)

# ----------------- NODE.JS SENIOR EXTRA -----------------
add_mcq("sr-node-11", "node", "V8 Hidden Classes & Inline Caches",
    "Why does dynamically adding properties to objects in different orders (e.g. `obj.a = 1; obj.b = 2` vs `obj.b = 2; obj.a = 1`) severely degrade V8 runtime execution speed?",
    [
        "A) It causes syntax errors in strict mode",
        "B) V8 creates different Hidden Classes (Shapes/Maps) based on the order of property assignments; differing shapes cause Inline Caches (ICs) to transition from monomorphic to polymorphic or megamorphic, disabling JIT-compiled fast property access",
        "C) It causes the hard drive to fragment",
        "D) It throws a TypeError at runtime"
    ],
    "B",
    "V8 creates transitions between hidden classes as properties are added. Assigning properties in identical orders allows V8 to reuse the same hidden class and maintain monomorphic inline caches (fastest). Differing orders force megamorphic lookups (slow dictionary search)."
)

add_mcq("sr-node-12", "node", "Event Loop Latency Monitoring",
    "Which Node.js `perf_hooks` API allows measuring event loop delay percentiles (p50, p99, max) with microsecond precision?",
    [
        "A) `perf_hooks.monitorEventLoopDelay({ resolution: 20 })`",
        "B) `process.uptime()`",
        "C) `console.time()`",
        "D) `Date.now()`"
    ],
    "A",
    "`monitorEventLoopDelay()` samples the time difference between expected and actual event loop execution, recording delay distributions in an internal histogram to expose p99 latency spikes."
)

add_mcq("sr-node-13", "node", "HTTP Keep-Alive Timeout Hazards",
    "What bug occurs when Node's `server.keepAliveTimeout` is set SHORTER than an upstream reverse proxy's (e.g. AWS ALB or Nginx) keep-alive timeout?",
    [
        "A) The proxy crashes with a 500 error",
        "B) Race condition HTTP 502 Bad Gateway: Node closes the idle TCP socket just as the upstream proxy sends a new request down the wire",
        "C) All HTTP requests become unencrypted",
        "D) The server runs out of port numbers"
    ],
    "B",
    "If Node's keep-alive timeout is lower than the reverse proxy's timeout, Node sends a TCP FIN packet while the proxy is writing an incoming request, causing a socket hang-up and an intermittent 502 Bad Gateway error on the client."
)

add_mcq("sr-node-14", "node", "Diagnostic Reports (Node Report)",
    "What information is captured by `process.report.writeReport()` in Node.js?",
    [
        "A) A summary of npm package downloads",
        "B) A comprehensive diagnostic JSON dump containing native C++ call stacks, V8 heap statistics, libuv handle queues, OS resource limits, loaded dynamic libraries, and network interfaces",
        "C) A list of all database queries executed today",
        "D) Git commit history"
    ],
    "B",
    "Node.js Diagnostic Report outputs a rich JSON report detailing native thread backtraces, V8 heap memory usage, libuv event loop handles, and OS environment state, crucial for diagnosing native segmentation faults and deadlocks."
)

add_open("sr-node-15", "node", "Diagnosing Native Memory Leaks Outside V8 Heap",
    "A Node.js microservice shows its Linux container memory (RSS) growing from 300MB to 4GB until killed by Linux OOM-killer, but V8 `process.memoryUsage().heapUsed` remains flat at 150MB. What causes native memory leaks outside the V8 heap, and what tools do you use to diagnose them?",
    [
        "Causes: Unfreed Buffer allocations, zlib/crypto OpenSSL allocations, native C++ addons with memory leaks, Libuv thread allocations",
        "Diagnosis: heapdump will not show it because it is outside V8 heap",
        "Tools: jemalloc / TCMalloc with memory profiling, valgrind (massif), Linux /proc/$PID/smaps analysis, eBPF / bcc tools"
    ],
    "1. Potential Root Causes:\n- Buffer Caching: `Buffer.allocUnsafe` or native streams buffering memory in C++ space outside V8 heap limits.\n- Native C++ Addons: Memory allocated via `malloc()` or `new` in a native module that lacks corresponding `free()` / `delete` in object destructors.\n- OpenSSL / Zlib leaks: Decompression streams (`zlib.createGunzip()`) that are not destroyed upon abort.\n2. Diagnostic Strategy:\n- `heapdump` and V8 snapshots are useless here because the leak resides outside V8 heap.\n- Inspect Linux memory maps: `cat /proc/<PID>/smaps | grep -i rss`.\n- Replace glibc allocator with `jemalloc` and enable heap profiling: `MALLOC_CONF=prof:true,prof_prefix:jeprof.out`.\n- Run load testing and analyze allocation dumps with `jeprof --show_bytes --pdf` to inspect the exact C++ allocation call tree."
)

add_open("sr-node-16", "node", "High-Throughput Zero-Downtime Cluster Orchestration",
    "Design and write a master-worker cluster supervisor in Node.js that performs rolling zero-downtime reloads upon receiving `SIGHUP`. The supervisor must spawn a new worker, verify it is healthy, gracefully disconnect the old worker, and handle worker crashes automatically.",
    [
        "Uses cluster module to fork workers matching os.cpus().length",
        "Listens for SIGHUP to initiate rolling replacement",
        "Spawns replacement worker, waits for 'listening' event, then sends disconnect to old worker with timeout",
        "Listens for 'exit' event to auto-restart crashed workers unless intentionally killed"
    ],
    "```javascript\nimport cluster from 'node:cluster';\nimport os from 'node:os';\n\nif (cluster.isPrimary) {\n  const numCPUs = os.cpus().length;\n  console.log(`Primary ${process.pid} running. Spawning ${numCPUs} workers...`);\n\n  for (let i = 0; i < numCPUs; i++) {\n    cluster.fork();\n  }\n\n  // Rolling reload on SIGHUP\n  process.on('SIGHUP', async () => {\n    console.log('Received SIGHUP. Initiating rolling reload...');\n    const workers = Object.values(cluster.workers);\n    for (const worker of workers) {\n      await new Promise((resolve) => {\n        const newWorker = cluster.fork();\n        newWorker.once('listening', () => {\n          worker.disconnect();\n          const timer = setTimeout(() => worker.kill(), 5000);\n          worker.once('exit', () => {\n            clearTimeout(timer);\n            resolve();\n          });\n        });\n      });\n    }\n    console.log('Rolling reload completed successfully.');\n  });\n\n  cluster.on('exit', (worker, code, signal) => {\n    if (!worker.exitedAfterDisconnect) {\n      console.warn(`Worker ${worker.process.pid} crashed (${signal || code}). Replacing...`);\n      cluster.fork();\n    }\n  });\n} else {\n  import('./server.js'); // Worker application code\n}\n```"
)

# ----------------- EXPRESS & ARCHITECTURE SENIOR EXTRA -----------------
add_mcq("sr-express-08", "express", "Idempotency via Redis Redlock",
    "When multiple microservices process distributed payments, why is the Redlock algorithm used over single-instance Redis locks?",
    [
        "A) Redlock automatically encrypts credit cards",
        "B) Single-instance Redis locks are vulnerable to single-point-of-failure and split-brain asynchronous replication race conditions; Redlock acquires locks across N independent master nodes with consensus, guaranteeing mutual exclusion even if nodes crash",
        "C) Redlock is built into the HTTP specification",
        "D) It requires no network requests"
    ],
    "B",
    "Redis replication is asynchronous. If Master A grants a lock and immediately crashes before replicating to its replica, the newly promoted replica will grant the same lock to another client. Redlock acquires locks across majority independent Redis masters to guarantee true distributed mutual exclusion."
)

add_mcq("sr-express-09", "express", "Load Shedding & Request Prioritization",
    "What is 'Load Shedding' in a high-concurrency Express API Gateway, and how does it prevent cascading catastrophic failures?",
    [
        "A) Turning off server room lights to save electricity",
        "B) When system metrics (CPU, event loop latency) exceed safety thresholds, the server intentionally drops low-priority background requests (e.g. analytics, recommendations) with HTTP 503 so core revenue-critical transactions (checkout, login) can continue processing within SLA",
        "C) Rebooting the database server every hour",
        "D) Deleting cold database records"
    ],
    "B",
    "When a service is overloaded, continuing to accept all traffic causes queue buildup, timeouts, and system-wide collapse. Load shedding proactively rejects low-tier traffic, allowing the system to operate stably at peak capacity."
)

add_mcq("sr-express-10", "express", "Singleflight Pattern (Request Collapsing)",
    "What is the Singleflight pattern (Request Collapsing / Deduplication) in an Express API gateway or proxy?",
    [
        "A) Running all flights on a single airline",
        "B) Suppressing duplicate concurrent identical read requests (e.g. 500 users requesting the exact same homepage config at the same millisecond) so that only ONE call goes downstream, sharing the result with all 500 callers",
        "C) Forcing all HTTP requests through a single TCP packet",
        "D) Compiling Express code into a single file"
    ],
    "B",
    "Singleflight intercepts identical in-flight read requests. Instead of hitting the database 500 times, it shares the single executing Promise across all simultaneous callers, preventing sudden stampedes on downstream services."
)

add_open("sr-express-11", "express", "Implementing Singleflight Request Collapsing",
    "Write a production-ready Singleflight request deduplication wrapper in Node.js that coalesces concurrent identical asynchronous operations (by cache key) into a single execution.",
    [
        "Maintains in-flight Map<string, Promise>",
        "If key exists in map, return existing Promise",
        "If not, create Promise, store in map, execute async operation",
        "Always delete key from map in finally block after Promise settles (whether resolved or rejected)"
    ],
    "```javascript\nexport class Singleflight {\n  constructor() {\n    this.inFlight = new Map();\n  }\n\n  async do(key, fn) {\n    if (this.inFlight.has(key)) {\n      return this.inFlight.get(key);\n    }\n\n    const promise = (async () => {\n      try {\n        return await fn();\n      } finally {\n        this.inFlight.delete(key);\n      }\n    })();\n\n    this.inFlight.set(key, promise);\n    return promise;\n  }\n}\n\n// Usage in Express controller:\n// const group = new Singleflight();\n// app.get('/products/:id', async (req, res) => {\n//   const data = await group.do(`product:${req.params.id}`, () => fetchProductFromDb(req.params.id));\n//   res.json(data);\n// });\n```"
)

add_open("sr-express-12", "express", "Zero-Trust mTLS Architecture for Microservices",
    "Explain how Mutual TLS (mTLS) works between Express-based microservices. How does it eliminate perimeter-only security and enforce cryptographic authentication, authorization, and encryption between internal services?",
    [
        "Both client and server present X.509 digital certificates to authenticate each other (two-way handshake)",
        "Eliminates perimeter-only security (where internal network is trusted)",
        "Enforces encryption in transit and identity verification via SAN (Subject Alternative Name) / SPIFFE ID",
        "Can be implemented at application layer (https.createServer with requestCert: true) or infrastructure layer (Envoy / Istio service mesh)"
    ],
    "1. Handshake Mechanics:\nIn standard TLS, only the server proves its identity with a certificate. In mTLS:\n- The server presents its certificate to the client.\n- The server requests the client's certificate (`requestCert: true, rejectUnauthorized: true`).\n- The client presents its certificate signed by an internal Root Certificate Authority (CA).\n- Both parties cryptographically authenticate each other before any HTTP/gRPC data flows.\n2. Zero-Trust Defense:\nTraditional architectures trust all internal network traffic once past the outer firewall. If an attacker breaches one pod, they can eavesdrop on all plaintext traffic. mTLS ensures that every inter-service call is encrypted and authenticated.\n3. Identity & Authorization:\nUsing SPIFFE IDs embedded in the certificate's SAN (e.g. `spiffe://cluster.local/ns/prod/sa/order-service`), the receiving service inspects who is calling and enforces fine-grained authorization (e.g., only `order-service` can call `/charge`)."
)

# ----------------- MONGODB AT SCALE SENIOR EXTRA -----------------
add_mcq("sr-mongo-11", "mongodb", "Replica Set Arbiters Hazards",
    "Why does MongoDB officially discourage the use of Arbiters in production replica set clusters?",
    [
        "A) Arbiters consume 100GB of RAM",
        "B) Arbiters hold no data; if a network partition isolates the primary and arbiter together, they can acknowledge writes that cannot meet `w: 'majority'`, and arbiters can trigger election loops and rollback hazards during complex partitions",
        "C) Arbiters require paid licenses",
        "D) Arbiters cannot run on Linux"
    ],
    "B",
    "Arbiters participate in elections but hold no data. Because they cannot vote on write concerns (`w: 'majority'`), losing a data node can prevent the cluster from acknowledging writes even if an arbiter is alive. A dedicated odd number of data-bearing nodes is far safer."
)

add_mcq("sr-mongo-12", "mongodb", "Change Streams with Resume Tokens",
    "How do MongoDB Change Streams achieve fault-tolerant, resilient event streaming after a network disconnect or consumer crash?",
    [
        "A) By re-reading the entire database from document 1",
        "B) Every change stream notification includes a unique `_id` resume token (`resumeAfter`); upon reconnection, the consumer passes this token to resume reading the oplog from the exact point of interruption without losing or duplicating events",
        "C) By saving events to text files",
        "D) Change streams cannot resume after a crash"
    ],
    "B",
    "Change Streams tail the internal MongoDB `oplog.rs`. Each event emits an opaque resume token. Supplying `{ resumeAfter: lastToken }` instructs MongoDB to resume streaming immediately following that specific oplog entry."
)

add_mcq("sr-mongo-13", "mongodb", "Zone Sharding (Geo-Partitioning)",
    "What is Zone Sharding in MongoDB and how does it fulfill regulatory requirements like GDPR?",
    [
        "A) It groups shards by temperature",
        "B) It maps specific shard key ranges (e.g. `country: 'DE'`) to designated geographic shard hardware zones located physically within the European Union, ensuring German citizens' data never leaves EU borders",
        "C) It encrypts Wi-Fi zones",
        "D) It partitions collections by file extension"
    ],
    "B",
    "Zone Sharding associates key ranges with tagged shard clusters in specific data centers. The MongoDB balancer migrates and pins documents to shards located in compliance regions, fulfilling strict data sovereignty laws (GDPR, HIPAA)."
)

add_open("sr-mongo-14", "mongodb", "WiredTiger Memory Stalls & Eviction Tuning",
    "Explain what causes WiredTiger cache eviction stalls in write-heavy MongoDB systems. How do you monitor dirty cache percentage (`serverStatus().wiredTiger.cache`), and what settings mitigate eviction thrashing?",
    [
        "When dirty cache exceeds eviction target (default 20%) or bytes in cache exceeds 80%, user application threads are forced to perform disk writes (eviction stalls)",
        "Monitored via db.serverStatus().wiredTiger.cache['tracked dirty bytes in the cache']",
        "Mitigation: Provision faster NVMe storage, increase wiredTigerEngineConfig.cacheSizeGB, adjust eviction trigger thresholds, scale horizontally via sharding"
    ],
    "1. Eviction Stalls:\nWiredTiger relies on dedicated background eviction worker threads. If the write arrival rate outpaces disk I/O, dirty data builds up in RAM. When dirty bytes exceed the critical ceiling (default 20% of cache) or total cache exceeds 95%, WiredTiger forces the incoming application client threads to perform synchronous eviction before accepting new writes. Application latency spikes from 2ms to multiple seconds.\n2. Monitoring:\nInspect `db.serverStatus().wiredTiger.cache`:\n- `tracked dirty bytes in the cache` vs `maximum bytes configured`\n- `application threads page read from disk to cache count` (indicates cache misses)\n3. Mitigation:\n- Upgrade to high-IOPS NVMe SSD storage.\n- Tune `wiredTigerEngineConfig.cacheSizeGB`.\n- Partition write-heavy workloads using Sharding to distribute the dirty page eviction burden across multiple physical machines."
)

add_open("sr-mongo-15", "mongodb", "Change Streams for Event-Driven Microservices",
    "Write a production Node.js service using MongoDB Change Streams that monitors updates to an `orders` collection, processes newly completed payments, and guarantees fault tolerance using stored resume tokens in Redis.",
    [
        "Opens change stream with pipeline filter { 'updateDescription.updatedFields.status': 'completed' }",
        "Retrieves resume token from Redis on startup (resumeAfter)",
        "Processes event idempotently and writes new resume token (_id) to Redis after each event",
        "Handles error events and reconnects with stored resume token"
    ],
    "```javascript\nimport { MongoClient } from 'mongodb';\nimport Redis from 'ioredis';\n\nconst redis = new Redis();\nconst mongo = new MongoClient(process.env.MONGO_URI);\n\nexport async function startOrderStream() {\n  await mongo.connect();\n  const collection = mongo.db('commerce').collection('orders');\n  \n  const lastToken = await redis.get('mongo:stream:orders:resume_token');\n  const options = lastToken ? { resumeAfter: JSON.parse(lastToken) } : {};\n\n  const pipeline = [\n    { $match: { operationType: 'update', 'updateDescription.updatedFields.status': 'completed' } }\n  ];\n\n  const stream = collection.watch(pipeline, options);\n  console.log('⚡ Order Change Stream active with resume token recovery...');\n\n  for await (const change of stream) {\n    try {\n      const orderId = change.documentKey._id;\n      console.log(`Processing completed order: ${orderId}`);\n      \n      // Execute business logic (e.g. dispatch invoice email, trigger fulfillment)\n      await processFulfillment(orderId);\n      \n      // Persist resume token only AFTER successful processing\n      await redis.set('mongo:stream:orders:resume_token', JSON.stringify(change._id));\n    } catch (err) {\n      console.error('Error processing change event:', err);\n      // Implement backoff or dead letter alert\n    }\n  }\n}\n```"
)

# ----------------- POSTGRESQL AT SCALE SENIOR EXTRA -----------------
add_mcq("sr-pg-11", "postgresql", "Transaction ID (TXID) Wraparound Disaster",
    "What catastrophic event occurs if PostgreSQL reaches the 2-billion transaction limit without freezing old transaction IDs via VACUUM?",
    [
        "A) The database switches all numbers to negative",
        "B) Transaction ID Wraparound: Past transactions appear to have occurred in the future due to modular arithmetic, making past data invisible; to prevent silent data corruption, PostgreSQL shuts down and refuses all write connections until vacuumed in single-user mode",
        "C) The database deletes all indexes",
        "D) The operating system crashes"
    ],
    "B",
    "PostgreSQL transaction IDs are 32-bit unsigned integers (modulo 2^32). Without VACUUM freezing old tuples (`FreezeLimit`), ID wraparound causes past commits to appear in the future, rendering data invisible. PostgreSQL halts to protect integrity."
)

add_mcq("sr-pg-12", "postgresql", "Row-Level Security (RLS) in Multi-Tenant SaaS",
    "How does PostgreSQL Row-Level Security (RLS) eliminate multi-tenant data leakage risks in a PERN architecture?",
    [
        "A) It encrypts each row with a different password",
        "B) It enforces security policies directly at the database engine level (e.g. `USING (tenant_id = current_setting('app.current_tenant_id'))`), ensuring queries can never access another tenant's rows even if a developer forgets a `WHERE tenant_id = ...` clause in Node.js",
        "C) It creates a separate database table for every single customer",
        "D) It disables SQL joins"
    ],
    "B",
    "RLS injects mandatory security filter conditions into every query plan behind the scenes. Even if an Express route has an IDOR vulnerability or a missing WHERE clause, PostgreSQL refuses to return rows outside the current session's tenant ID."
)

add_mcq("sr-pg-13", "postgresql", "Advisory Locks for Distributed Coordination",
    "What is the unique advantage of PostgreSQL Advisory Locks (`pg_advisory_lock`) for distributed task synchronization over row-level locks?",
    [
        "A) Advisory locks never unlock",
        "B) They are application-defined cooperative locks identified by an arbitrary 64-bit integer that do not require creating, locking, or modifying any physical table rows",
        "C) Advisory locks work without a database connection",
        "D) They speed up SELECT queries by 10x"
    ],
    "B",
    "Advisory locks allow applications to coordinate distributed mutexes using PostgreSQL's high-speed in-memory lock table without modifying tables or dealing with deadlocks on data rows."
)

add_open("sr-pg-14", "postgresql", "PostgreSQL Autovacuum Tuning for High-Write Systems",
    "Explain why default PostgreSQL autovacuum settings are inadequate for high-throughput transactional databases. Which configuration parameters (`autovacuum_vacuum_scale_factor`, `autovacuum_vacuum_cost_limit`, `autovacuum_max_workers`) must be tuned and why?",
    [
        "Default scale factor is 0.2 (20% of rows must change before vacuum triggers); on a 100M-row table, that requires 20M dead tuples before vacuuming starts, causing massive bloat",
        "Tune autovacuum_vacuum_scale_factor to 0.01-0.05 (or per-table threshold) so vacuum runs continuously in small increments",
        "Default autovacuum_vacuum_cost_limit (200) throttles I/O severely; increase to 1000-2000 on modern NVMe drives",
        "Tune maintenance_work_mem to allow workers to store more dead tuple pointers in RAM before scanning indexes"
    ],
    "1. The Problem with Defaults:\nBy default, `autovacuum_vacuum_scale_factor = 0.2`. On a table with 100 million rows, autovacuum will not even trigger until 20 million rows are modified! By that time, 20 million dead tuples have bloated the table and indexes, crippling cache efficiency.\n2. Parameter Tuning for High Throughput:\n- `autovacuum_vacuum_scale_factor = 0.02`: Lowers trigger threshold to 2% (or set per-table with `ALTER TABLE hot_table SET (autovacuum_vacuum_scale_factor = 0.01)`).\n- `autovacuum_vacuum_cost_limit = 2000` (up from default 200): Modern NVMe SSDs can handle vastly higher I/O; increasing the cost limit prevents workers from sleeping unnecessarily.\n- `autovacuum_vacuum_cost_delay = 2ms` (down from 20ms in older versions).\n- `maintenance_work_mem = 1GB`: Allows workers to track up to 1 billion dead tuple pointers in fast memory per pass, minimizing index re-scans."
)

add_open("sr-pg-15", "postgresql", "Zero-Downtime Safe DDL Migrations in PostgreSQL",
    "Detail how to safely perform three dangerous DDL operations on an active PostgreSQL table with 100 million rows without blocking user transactions: 1) Adding a `NOT NULL` column, 2) Creating a foreign key constraint, 3) Dropping a column.",
    [
        "1. NOT NULL: Add column as NULLABLE -> Add CHECK (col IS NOT NULL) NOT VALID -> VALIDATE CONSTRAINT -> Set NOT NULL (avoids full table rewrite lock)",
        "2. Foreign Key: ADD CONSTRAINT ... FOREIGN KEY ... NOT VALID (takes brief SHARE ROW EXCLUSIVE lock without scanning table) -> VALIDATE CONSTRAINT (scans table with non-blocking SHARE UPDATE EXCLUSIVE lock)",
        "3. Drop Column: Set lock_timeout to 2s to avoid blocking queue; ALTER TABLE DROP COLUMN is metadata-only in modern Postgres (PG 11+)"
    ],
    "1. Adding a `NOT NULL` Column Safely:\nRunning `ALTER TABLE users ADD COLUMN status TEXT NOT NULL DEFAULT 'active'` rewrites the entire table and holds an `ACCESS EXCLUSIVE` lock for hours.\n- Safe Solution:\n  Step 1: `ALTER TABLE users ADD COLUMN status TEXT DEFAULT 'active';` (Instant metadata in PG 11+).\n  Step 2: `ALTER TABLE users ADD CONSTRAINT status_not_null CHECK (status IS NOT NULL) NOT VALID;` (Instant, no scan).\n  Step 3: `ALTER TABLE users VALIDATE CONSTRAINT status_not_null;` (Scans table in background without write locks).\n2. Adding a Foreign Key Safely:\n- `ALTER TABLE orders ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) NOT VALID;`\n- `ALTER TABLE orders VALIDATE CONSTRAINT fk_user;`\n3. Lock Queue Defense:\nAlways set `SET lock_timeout = '2s';` before any DDL so if a lock cannot be acquired immediately, the query fails fast rather than piling up behind a slow transaction and stalling all incoming production queries."
)

# ----------------- FULLSTACK SYSTEM DESIGN SENIOR EXTRA -----------------
add_mcq("sr-full-08", "fullstack", "CRDTs vs Operational Transformation (OT)",
    "Why are Conflict-free Replicated Data Types (CRDTs, like Yjs / Automerge) replacing Operational Transformation (OT) in modern real-time collaborative web applications?",
    [
        "A) CRDTs only work without an internet connection",
        "B) OT requires a central authoritative server to order and transform all concurrent operations sequentially; CRDTs are mathematically commutative and converge deterministically on all peers, enabling true peer-to-peer, decentralized, and offline-first collaboration",
        "C) CRDTs encrypt all text with SHA-512",
        "D) OT was outlawed by the W3C"
    ],
    "B",
    "Operational Transformation (Google Docs style) relies heavily on a centralized coordination server to serialize transforms. CRDTs use mathematically sound distributed data structures where operations can arrive in any order and converge deterministically to the identical state."
)

add_mcq("sr-full-09", "fullstack", "Event Sourcing vs Traditional State",
    "What is the fundamental architectural principle of Event Sourcing in enterprise PERN/MERN systems?",
    [
        "A) Deleting logs after 7 days",
        "B) Instead of storing only the current snapshot state in the database, every state transition is recorded as an immutable, append-only event; the current state is derived by replaying the event log stream",
        "C) Compiling React components into audio files",
        "D) Storing all data in browser cookies"
    ],
    "B",
    "Traditional CRUD mutates state in place, losing historical context. In Event Sourcing, the append-only event stream is the single source of truth. Current state projections are materialized views, enabling complete auditability, time-travel debugging, and historical replays."
)

add_mcq("sr-full-10", "fullstack", "Consistent Hashing with Virtual Nodes",
    "Why does consistent hashing with virtual nodes prevent data skew when scaling distributed cache nodes (Redis/Memcached)?",
    [
        "A) It prevents hackers from accessing cache keys",
        "B) In simple modulo hashing (`hash(key) % N`), adding a node reshuffles nearly 100% of keys; consistent hashing maps keys and nodes onto a circular ring, moving only K/N keys when nodes scale, while virtual nodes ensure uniform distribution across servers",
        "C) It eliminates all RAM consumption",
        "D) It only works on 64-bit systems"
    ],
    "B",
    "Standard modulo hashing invalidates the entire cache when node count changes. Consistent hashing minimizes remapping to only `1/N` keys. Virtual nodes allocate multiple positions per physical server, smoothing out hash distribution and preventing hotspotting."
)

add_open("sr-full-11", "fullstack", "Designing a Real-Time Collaborative Canvas (Figma-Style)",
    "Architect a real-time collaborative canvas (like Figma or Miro) supporting 100 concurrent editors per document. Detail your client-side data structures (CRDTs), transport protocol (WebSockets with binary Protobuf/BSON), server room coordination, and offline reconciliation.",
    [
        "Data structures: Yjs / Automerge CRDTs for deterministic convergence without central locking",
        "Transport: WebSockets transferring binary encoded delta updates (Uint8Array) rather than verbose JSON",
        "Server room coordination: Node.js WebSocket cluster with Redis Pub/Sub room sharding (rooms pinned via sticky sessions or distributed gateway)",
        "Persistence: PostgreSQL storing periodic binary snapshot checkpoints and incremental event log in outbox",
        "Offline: IndexedDB local persistence; upon reconnection, Yjs calculates state vector diffs and syncs minimal binary deltas"
    ],
    "1. Client Data Layer (CRDT):\nUse `Yjs` or `Automerge`. Document state (shapes, layers, coordinates) is represented as a shared Y.Doc. Updates generate compact binary deltas (`Y.encodeStateAsUpdate`). Because CRDTs are commutative, operations merge deterministically without server-side locking.\n2. Transport Layer:\nPersistent WebSocket connections transmitting binary frames (`Uint8Array`) using Protocol Buffers or raw Yjs delta packets, minimizing serialization latency and bandwidth.\n3. Server Architecture:\n- Stateless Node.js WebSocket gateway servers clustered behind an Nginx Layer 7 load balancer with sticky session routing by `documentId`.\n- Redis Pub/Sub backplane allows editors connected to different gateway instances in the same room to receive peer updates.\n4. Persistence Strategy:\n- Write deltas to an in-memory buffer and periodically flush compressed state vectors to PostgreSQL/S3 every 30 seconds as snapshot checkpoints.\n- Store transactional deltas in an append-only PostgreSQL table.\n5. Offline Support:\nLocal edits persist in browser `IndexedDB`. When the client reconnects, it computes a State Vector diff with the server, exchanging only missing binary delta chunks with zero data loss."
)

add_open("sr-full-12", "fullstack", "Disaster Recovery: Multi-Region Active-Active vs Active-Passive",
    "Contrast an Active-Passive (Warm Standby) disaster recovery architecture with an Active-Active multi-region deployment for an enterprise PERN application. Analyze RPO (Recovery Point Objective), RTO (Recovery Time Objective), write conflicts, and cost trade-offs.",
    [
        "Active-Passive: Primary region handles 100% of traffic; secondary region receives asynchronous replication (streaming WAL). RTO = minutes (DNS failover time), RPO = seconds (replication lag). Cheaper, zero write conflicts",
        "Active-Active: Both regions accept writes concurrently. RTO = 0 (instant failover). RPO = 0. Major challenges: Bi-directional replication latency, split-brain hazards, distributed write conflict resolution (CRDTs or last-write-wins), 2x-3x higher infrastructure cost",
        "Recommendation: Active-Passive with automated health checks and read-only secondaries is typically the optimal balance for relational databases"
    ],
    "1. Active-Passive (Warm / Hot Standby):\n- Architecture: Region A (Primary) handles all reads and writes. Data replicates asynchronously via physical streaming replication to Region B (Standby).\n- RPO (Recovery Point Objective): A few seconds (equal to replication lag).\n- RTO (Recovery Time Objective): 1-5 minutes (time to detect failure, promote standby to primary, and update Route 53 DNS records).\n- Trade-offs: Zero write-conflict anomalies, simpler operational model, lower cost.\n2. Active-Active (Multi-Region):\n- Architecture: Both Region A and Region B actively process reads and writes concurrently for local users.\n- RPO / RTO: Near zero instantaneous failover.\n- Trade-offs & Critical Hazards:\n  - Relational Conflict: Two users in different regions updating the same user profile concurrently causes cross-region split-brain. Requires bi-directional logical replication with conflict resolution rules (e.g. Last-Write-Wins or CRDT fields).\n  - Cross-Region Latency: Synchronous multi-region consensus (e.g. CockroachDB / Spanner) adds 50-100ms speed-of-light round-trip latency to every write.\n  - Cost: 2.5x higher cloud infrastructure spend."
)

with open('/workspaces/preppro/src/data/senior.json', 'w') as f:
    json.dump(questions, f, indent=2)

print(f"Total Senior Questions: {len(questions)}")
