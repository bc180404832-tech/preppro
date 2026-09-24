#!/usr/bin/env python3
import json

def generate_junior():
    with open('/workspaces/preppro/src/data/junior.json', 'r') as f:
        questions = json.load(f)

    # Add 8 more questions to bring Junior to 110
    extra_junior = [
        {
            "id": "jr-mongo-16",
            "level": "junior",
            "stack": "mongodb",
            "type": "mcq",
            "topic": "Projections in MongoDB",
            "question": "How do you exclude the `password` field from the results of a MongoDB query?",
            "options": [
                "A) `find({}, { password: 0 })`",
                "B) `find({}, { remove: 'password' })`",
                "C) `find({}).without('password')`",
                "D) `find({}, { password: false })`"
            ],
            "answer": "A",
            "explanation": "In MongoDB projections, setting a field value to `0` (or `false` in Mongoose) explicitly excludes that field from the returned document."
        },
        {
            "id": "jr-mongo-17",
            "level": "junior",
            "stack": "mongodb",
            "type": "mcq",
            "topic": "Sorting Query Results",
            "question": "Which cursor method and argument sorts MongoDB documents by `createdAt` in descending order (newest first)?",
            "options": [
                "A) `.sort({ createdAt: -1 })`",
                "B) `.sort({ createdAt: 'desc' })`",
                "C) `.order('createdAt DESC')`",
                "D) `.sort({ createdAt: 1 })`"
            ],
            "answer": "A",
            "explanation": "In MongoDB, `.sort({ field: 1 })` sorts ascending (oldest/smallest first), while `.sort({ field: -1 })` sorts descending (newest/highest first)."
        },
        {
            "id": "jr-mongo-18",
            "level": "junior",
            "stack": "mongodb",
            "type": "open",
            "topic": "MongoDB Indexes Purpose",
            "question": "What is an index in MongoDB, why are indexes critical for query performance, and what is the downside of creating too many indexes?",
            "expectedKeyPoints": [
                "Index is a specialized data structure (B-tree) holding small subset of data ordered by field values",
                "Enables fast lookups (IXSCAN) without scanning every document in collection (COLLSCAN)",
                "Downside: Every index consumes RAM/disk space and adds write overhead during inserts/updates/deletions"
            ],
            "sampleAnswer": "An index in MongoDB is an ordered data structure (B-Tree) that stores field values and pointers to corresponding documents on disk.\nBenefits: Without indexes, MongoDB must perform a full collection scan (COLLSCAN), inspecting every document. An index allows fast logarithmic lookups (IXSCAN), reducing query time from seconds to milliseconds.\nDownsides: Indexes require disk and RAM to maintain. Every insert, update, or delete must also update the index entries, increasing write latency and storage costs."
        },
        {
            "id": "jr-pg-16",
            "level": "junior",
            "stack": "postgresql",
            "type": "mcq",
            "topic": "ALTER TABLE Basics",
            "question": "Which SQL statement adds a new column named `is_verified` with a default value of `false` to an existing table `users`?",
            "options": [
                "A) `ALTER TABLE users ADD COLUMN is_verified BOOLEAN DEFAULT false;`",
                "B) `UPDATE TABLE users INSERT is_verified BOOLEAN;`",
                "C) `MODIFY TABLE users NEW COLUMN is_verified BOOLEAN;`",
                "D) `TABLE users ADD is_verified;`"
            ],
            "answer": "A",
            "explanation": "In PostgreSQL, schema modifications use the `ALTER TABLE` DDL statement: `ALTER TABLE table_name ADD COLUMN column_name data_type [constraints];`."
        },
        {
            "id": "jr-pg-17",
            "level": "junior",
            "stack": "postgresql",
            "type": "mcq",
            "topic": "Date and Time Types",
            "question": "Which timestamp data type in PostgreSQL stores the timezone offset and normalizes inputs to UTC?",
            "options": [
                "A) `TIMESTAMP WITHOUT TIME ZONE`",
                "B) `TIMESTAMPTZ` (or `TIMESTAMP WITH TIME ZONE`)",
                "C) `DATETIME`",
                "D) `UNIXTIME`"
            ],
            "answer": "B",
            "explanation": "`TIMESTAMPTZ` records timestamps in UTC internally and converts them to the client's configured timezone on output, avoiding subtle daylight savings and timezone conversion bugs."
        },
        {
            "id": "jr-pg-18",
            "level": "junior",
            "stack": "postgresql",
            "type": "open",
            "topic": "Database Indexes in PostgreSQL",
            "question": "What is a B-Tree index in PostgreSQL, on which columns should you typically create an index, and when should you avoid indexing?",
            "expectedKeyPoints": [
                "Default index type in PostgreSQL that maintains balanced tree for O(log N) searches and range queries",
                "Create indexes on frequently filtered (WHERE), joined (ON), or sorted (ORDER BY) columns",
                "Avoid on small tables or columns with very low cardinality (e.g. boolean) where seq scan is faster, or tables with massive write volume"
            ],
            "sampleAnswer": "A B-Tree index is the default index in PostgreSQL, organizing keys in a balanced tree to allow O(log n) lookups, range scans (`<`, `<=`, `=`, `>=`, `>`), and ordered sorting.\nWhen to index:\n- Foreign keys used in `JOIN` clauses\n- Columns frequently used in `WHERE` filters\n- Columns used in `ORDER BY` sorting\nWhen to avoid indexing:\n- Small tables (sequential scans are faster than jumping between index and heap blocks)\n- Columns with extremely low cardinality (e.g. a boolean `is_active` where 95% of rows are true)\n- Heavy write-intensive tables where write amplification from updating multiple indexes outweighs read benefits."
        },
        {
            "id": "jr-full-13",
            "level": "junior",
            "stack": "fullstack",
            "type": "mcq",
            "topic": "HTTP Idempotence",
            "question": "Which of the following HTTP methods is considered 'idempotent' by specification?",
            "options": [
                "A) POST",
                "B) GET, PUT, and DELETE",
                "C) Only POST and PATCH",
                "D) No HTTP methods are idempotent"
            ],
            "answer": "B",
            "explanation": "An HTTP method is idempotent if executing it multiple times produces the identical server state as executing it once. GET, PUT, and DELETE are idempotent; POST is not."
        },
        {
            "id": "jr-full-14",
            "level": "junior",
            "stack": "fullstack",
            "type": "open",
            "topic": "HTTP vs HTTPS and SSL Handshake",
            "question": "Explain why HTTP is vulnerable to packet sniffing on public Wi-Fi networks and how HTTPS solves this using asymmetric and symmetric encryption.",
            "expectedKeyPoints": [
                "HTTP transmits plaintext over the wire; anyone on the local network can inspect packets with tools like Wireshark",
                "HTTPS uses TLS/SSL: Asymmetric encryption (RSA/ECC) during initial handshake to securely exchange symmetric session keys",
                "Symmetric encryption (AES) used for encrypting bulk application data during the session for performance"
            ],
            "sampleAnswer": "HTTP sends all headers and payloads in cleartext. On an untrusted network (like coffee shop Wi-Fi), any attacker with a packet sniffer can view passwords, session tokens, and personal data.\nHTTPS wraps HTTP in TLS (Transport Layer Security):\n1. Handshake (Asymmetric): The client and server verify identity using certificates and exchange a shared secret using asymmetric cryptography (public/private key pair).\n2. Session (Symmetric): Once the shared secret is established, all subsequent request/response data is encrypted using fast symmetric encryption (e.g. AES-GCM). Even if packets are intercepted, they appear as unreadable ciphertext."
        }
    ]

    questions.extend(extra_junior)
    with open('/workspaces/preppro/src/data/junior.json', 'w') as f:
        json.dump(questions, f, indent=2)
    print(f"Total Junior Questions: {len(questions)}")

generate_junior()
