#!/usr/bin/env python3
import json

questions = []

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

# ==================== REACT (SENIOR: 22 Qs) ====================
add_mcq("sr-react-01", "react", "React Fiber Architecture",
    "What was the primary architectural motivation for rewriting React's core reconciliation algorithm with React Fiber?",
    [
        "A) To switch from JavaScript to TypeScript",
        "B) To break the synchronous, un-interruptible recursive stack reconciler into incremental, interruptible units of work (fibers) that can be prioritized, paused, resumed, or aborted based on deadline schedules",
        "C) To eliminate the browser DOM completely",
        "D) To add built-in Redux support"
    ],
    "B",
    "The legacy stack reconciler executed reconciliation synchronously in one deep recursive call, blocking the main thread during heavy updates. Fiber represents each element as a linked-list work node, enabling time-slicing and prioritization of urgent tasks (like user input) over background tasks."
)

add_mcq("sr-react-02", "react", "Fiber Phases: Render vs Commit",
    "In React Fiber's two-phase processing, which phase is pure/interruptible and which phase is synchronous/side-effectful?",
    [
        "A) Render phase is synchronous; Commit phase is interruptible",
        "B) Render phase is asynchronous and can be paused/restarted without DOM mutation; Commit phase is synchronous and applies DOM mutations and invokes lifecycle effects",
        "C) Both phases run concurrently in background Web Workers",
        "D) Commit phase only runs on the Node.js server"
    ],
    "B",
    "The Render/Reconciliation phase builds the workInProgress fiber tree and is purely computational (it can be paused, restarted, or thrown away). The Commit phase is strictly synchronous, applying DOM updates and invoking layout effects to prevent visible visual tearing."
)

add_mcq("sr-react-03", "react", "useTransition Hook",
    "How does the `useTransition` hook prevent UI freezing during expensive state transitions in React 18+?",
    [
        "A) It spawns a background Node.js worker process",
        "B) It marks the state update as a non-urgent transition, allowing urgent user interactions (typing, clicking) to interrupt the render and keeping the UI responsive while providing an `isPending` flag",
        "C) It caches all component renders in localStorage",
        "D) It converts the component tree into an SVG canvas"
    ],
    "B",
    "`startTransition(() => setState(...))` deprioritizes the state update. React renders the heavy work in the background without blocking high-priority user inputs, yielding to user events before finishing the transition."
)

add_mcq("sr-react-04", "react", "useSyncExternalStore",
    "Why was `useSyncExternalStore` introduced in React 18 for subscribing to non-React external stores (e.g. Redux, Zustand, browser APIs)?",
    [
        "A) To replace all fetch calls",
        "B) To prevent 'tearing' (visual inconsistency where different components render data from different snapshots of the external store during concurrent rendering) by enforcing synchronous store reads",
        "C) To synchronize React state with PostgreSQL directly",
        "D) To store component state in Service Workers"
    ],
    "B",
    "In concurrent React, rendering can yield. If an external mutable store updates midway through a render, some components might read the old value and others the new value ('tearing'). `useSyncExternalStore` guarantees consistent, tear-free reads."
)

add_mcq("sr-react-05", "react", "React Server Components (RSC) vs SSR",
    "What is the fundamental distinction between React Server Components (RSC) and traditional Server-Side Rendering (SSR)?",
    [
        "A) RSC compiles components to WebAssembly, while SSR compiles to HTML",
        "B) SSR pre-renders HTML on the server but still ships all component JavaScript to the client for hydration; RSC execute exclusively on the server, ship zero JavaScript to the client bundle, and stream rendered UI in a compact serialized protocol",
        "C) RSC only works with MongoDB, whereas SSR only works with PostgreSQL",
        "D) SSR is deprecated and replaced entirely by RSC"
    ],
    "B",
    "Traditional SSR sends HTML for initial paint, but the client must still download, parse, and execute all component JS to hydrate event handlers. RSC components execute ONLY on the server: their dependencies (e.g., massive markdown parsers or DB drivers) never enter the client JavaScript bundle."
)

add_mcq("sr-react-06", "react", "Selective Hydration with Suspense",
    "How does Selective Hydration work with React 18's streaming SSR architecture (`renderToPipeableStream`)?",
    [
        "A) It only hydrates components on desktop computers",
        "B) React streams HTML chunks wrapped in `<Suspense>`, and begins hydrating loaded parts of the page independently before the entire HTML document finishes downloading; if the user clicks an unhydrated component, React prioritizes hydrating that specific subtree first",
        "C) It eliminates all JavaScript from the client",
        "D) It hydrates via WebSockets exclusively"
    ],
    "B",
    "Selective Hydration breaks the monolithic 'all-or-nothing' hydration model. Slow backend data subtrees wrapped in `<Suspense>` stream in later, while already-rendered components become interactive immediately. Early user interactions prioritize the hydration of the clicked component."
)

add_mcq("sr-react-07", "react", "useDeferredValue Internals",
    "What is the difference between debouncing an input state and using `useDeferredValue` in React?",
    [
        "A) Debouncing introduces a fixed artificial time delay (e.g. 300ms) regardless of machine speed, whereas `useDeferredValue` defers rendering dynamically until the main thread is idle, rendering instantly on fast machines without artificial latency",
        "B) `useDeferredValue` only works on numbers",
        "C) Debouncing does not work in React 18",
        "D) `useDeferredValue` prevents re-renders entirely"
    ],
    "A",
    "Debouncing always delays execution by N milliseconds. `useDeferredValue` is integrated into React's concurrent scheduler: on powerful machines, it renders immediately; on slower devices, it defers rendering behind user input without lag."
)

add_mcq("sr-react-08", "react", "Hydration Mismatch Errors",
    "What triggers a React Hydration Mismatch error, and what are its performance and architectural consequences?",
    [
        "A) A syntax error in CSS",
        "B) When the server-rendered HTML tree differs from the initial client-rendered Virtual DOM tree (e.g. using `window.innerWidth`, `Date.now()`, or `Math.random()` during render), forcing React to discard server DOM and perform expensive client-side re-rendering",
        "C) A mismatch between Node.js and React versions",
        "D) Missing database foreign keys"
    ],
    "B",
    "If server HTML does not match client initial render, React flags a hydration mismatch. React must throw away the mismatched DOM nodes and reconstruct them on the client, degrading initial load performance and causing visual flickering."
)

add_mcq("sr-react-09", "react", "React Compiler (Forget)",
    "What is the primary role of the React Compiler (React Forget)?",
    [
        "A) It automatically deletes unused state variables",
        "B) An optimizing compiler that analyzes JavaScript rules and auto-memoizes component values and callbacks, eliminating the need for manual `useMemo`, `useCallback`, and `React.memo` boilerplate",
        "C) It deletes stale cookies on logout",
        "D) It converts React into Svelte"
    ],
    "B",
    "The React Compiler performs static analysis of component code adhering to the Rules of React, automatically injecting fine-grained memoization so developers no longer need to manually manage dependency arrays and `useMemo`/`useCallback`."
)

add_mcq("sr-react-10", "react", "Profiling Production Builds",
    "Why does React DevTools Profiler require building with `--profile` flag in production environments?",
    [
        "A) Profiling is illegal in production without a license",
        "B) Standard production React builds strip profiling hooks and commit timestamps to maximize bundle minification and runtime execution speed",
        "C) Production builds only run in bytecode",
        "D) To prevent hackers from viewing source maps"
    ],
    "B",
    "Standard production builds remove measurement instrumentation to achieve optimal performance. The `--profile` bundle flag retains lightweight profiler markers (`react-dom/profiling`) while keeping production minification."
)

add_mcq("sr-react-11", "react", "Micro-Frontend Module Federation",
    "How does Webpack / Vite Module Federation facilitate scaling large enterprise PERN/MERN frontends?",
    [
        "A) It embeds iframes for every page component",
        "B) It allows multiple independently deployed React applications to dynamically share code, vendor libraries (like React and React-DOM as singletons), and remote components at runtime without full monolithic rebuilds",
        "C) It bundles all frontend code into a single 50MB file",
        "D) It converts React to Web Components"
    ],
    "B",
    "Module Federation enables decentralized micro-frontends: independent teams build and deploy discrete React applications that dynamically consume remote components at runtime while sharing common singleton dependencies to avoid duplicate library downloads."
)

add_mcq("sr-react-12", "react", "Custom State Machine Patterns (XState)",
    "Why are Finite State Machines (FSMs) or statecharts (like XState) superior to boolean flag soups (`isLoading`, `isError`, `isSuccess`) for complex UI flows?",
    [
        "A) Booleans are not supported in TypeScript",
        "B) Multiple boolean flags permit impossible or contradictory states (e.g. `isLoading: true && isSuccess: true`), whereas FSMs mathematically guarantee that the system can only occupy exactly one valid finite state at any given time with explicit transitions",
        "C) State machines compile directly into C++",
        "D) State machines eliminate network latency"
    ],
    "B",
    "With 4 boolean flags, there are 2^4 = 16 possible states, most of which are invalid. An FSM mathematically models explicitly allowed states and transitions, preventing bugs like showing a spinner and a success modal simultaneously."
)

add_open("sr-react-13", "react", "React Fiber Internals & Work Loop",
    "Explain how React Fiber represents the component tree using a linked-list structure (`child`, `sibling`, `return`). How does the cooperative scheduling work loop (`workLoopConcurrent`) yield execution to the browser?",
    [
        "Fibers are JavaScript objects representing units of work; each fiber has child, sibling, and return pointers",
        "workLoopConcurrent checks shouldYield() (via Scheduler / MessageChannel)",
        "If time slice expires (typically 5ms), it pauses the work loop, yields to browser for paint/input, and resumes on next micro/macro task",
        "Reconciliation produces an effect list/flags committed in the synchronous commit phase"
    ],
    "1. Fiber Linked List Architecture:\nUnlike the legacy call stack reconciler, each React element maps to a Fiber node. Relationships are maintained via three pointers:\n- `child`: Points to the first direct child component.\n- `sibling`: Points to the next sibling component.\n- `return`: Points to the parent fiber node to return to after completing a branch.\nThis linked list allows traversing the entire tree iteratively with a `while` loop rather than recursion.\n2. Work Loop & Cooperative Scheduling:\nIn concurrent mode, React executes `workLoopConcurrent()`:\n```javascript\nfunction workLoopConcurrent() {\n  while (workInProgress !== null && !shouldYield()) {\n    performUnitOfWork(workInProgress);\n  }\n}\n```\n`shouldYield()` queries the React Scheduler (using `MessageChannel` / `performance.now()`). When the ~5ms time slice budget is exhausted, React pauses reconciliation, yields the main thread to the browser to handle user keystrokes and CSS layout reflows, and resumes where it left off."
)

add_open("sr-react-14", "react", "React Server Components Architecture",
    "Explain the architecture of React Server Components (RSC). How do RSCs communicate with Client Components across the serialization boundary, and what are the strict rules regarding what data can cross this boundary?",
    [
        "Server Components execute only on the server, can directly query databases (PostgreSQL/MongoDB) or file systems",
        "Client Components are marked with 'use client' directive",
        "Serialization boundary: Props passed from Server to Client Components must be serializable (JSON, Promises, JSX elements, typed arrays; no functions, class instances, or symbols)",
        "RSC stream an intermediate serialized protocol (RSC payload) that the client reconciler merges into the Virtual DOM"
    ],
    "1. Execution Architecture:\nServer Components execute exclusively on the server. They have direct access to backend resources (PostgreSQL pools, MongoDB models, filesystem, internal microservices) with zero client bundle overhead.\n2. The 'use client' Boundary:\n`'use client'` marks the boundary where server code ends and client-interactive code begins. It is an export boundary, not a directive that the component only runs on the client (client components still pre-render on the server during SSR).\n3. Serialization Rules:\nProps passed across the boundary from a Server Component to a Client Component must be serializable into the RSC wire protocol:\n- Allowed: Primitives (strings, numbers, booleans), plain objects, arrays, Promises, React elements (JSX), BigInt, TypedArrays.\n- Forbidden: Functions (event handlers like `onClick`), class instances, symbols, and non-serializable objects.\n4. RSC Wire Protocol:\nThe server streams a compact JSON-like stream of fiber nodes. The client reconciler receives these chunks and patches them into the existing DOM tree without destroying local client state."
)

add_open("sr-react-15", "react", "Designing an Enterprise State Architecture",
    "Design an enterprise state architecture for a high-traffic PERN/MERN dashboard application. Categorize state into Server State, Global Client State, URL State, and Local UI State, citing specific libraries and best practices for each.",
    [
        "Server State: TanStack Query (React Query) for caching, invalidation, deduplication, optimistic updates",
        "Global Client State: Zustand for lightweight, selector-based atomic state (theme, notifications, auth session)",
        "URL State: nuqs / React Router searchParams for filters, sorting, pagination (shareable deep links)",
        "Local UI State: useState/useReducer for transient form inputs, modal toggles, dropdowns",
        "Avoid monolithic global stores holding server data"
    ],
    "1. Server State (Data from API/DB):\n- Tool: TanStack Query (React Query) or RTK Query.\n- Rationale: Manages asynchronous caching, background revalidation, query deduplication, optimistic mutations, and garbage collection. Never store raw API response arrays in a manual global store.\n2. URL State (Single Source of Truth for Navigation):\n- Tool: React Router / `nuqs` (search parameters).\n- Rationale: Filters, search terms, active tabs, and pagination offsets belong in query strings (`?tab=analytics&page=2`). This guarantees shareable URLs, bookmarking, and native browser back/forward navigation.\n3. Global Client State (Application-Wide UI State):\n- Tool: Zustand.\n- Rationale: Manages client-only singleton state (e.g. sidebar collapse state, active modals, user preferences). Selector subscriptions prevent unnecessary component re-renders.\n4. Local Component State:\n- Tool: `useState` / `useReducer`.\n- Rationale: Strictly transient UI interactions (accordion toggle, hover state, temporary form validation errors)."
)

add_open("sr-react-16", "react", "Architecting a Resilient Design System with Compound Components",
    "Write a production-grade, accessible Compound Component for a Modal Dialog in React using Context, Refs, and Portals that manages focus trapping, Escape key handling, and outside clicks.",
    [
        "Modal root managing open state and accessibility attributes",
        "Modal.Trigger, Modal.Content, Modal.Close subcomponents",
        "ReactDOM.createPortal to render into document.body",
        "useEffect listening for 'Escape' key and trapping tab focus",
        "Proper ARIA roles (role='dialog', aria-modal='true', aria-labelledby)"
    ],
    "```javascript\nimport React, { createContext, useContext, useState, useEffect, useRef } from 'react';\nimport ReactDOM from 'react-dom';\n\nconst ModalContext = createContext(null);\n\nexport function Modal({ children, isOpen: controlledOpen, onClose }) {\n  const [internalOpen, setInternalOpen] = useState(false);\n  const isControlled = controlledOpen !== undefined;\n  const isOpen = isControlled ? controlledOpen : internalOpen;\n\n  const handleClose = () => {\n    if (onClose) onClose();\n    if (!isControlled) setInternalOpen(false);\n  };\n\n  return (\n    <ModalContext.Provider value={{ isOpen, handleClose, openModal: () => setInternalOpen(true) }}>\n      {children}\n    </ModalContext.Provider>\n  );\n}\n\nModal.Trigger = function ModalTrigger({ children }) {\n  const { openModal } = useContext(ModalContext);\n  return React.cloneElement(children, { onClick: openModal });\n};\n\nModal.Content = function ModalContent({ children, title }) {\n  const { isOpen, handleClose } = useContext(ModalContext);\n  const dialogRef = useRef(null);\n\n  useEffect(() => {\n    if (!isOpen) return;\n    const handleKeyDown = (e) => {\n      if (e.key === 'Escape') handleClose();\n    };\n    document.addEventListener('keydown', handleKeyDown);\n    return () => document.removeEventListener('keydown', handleKeyDown);\n  }, [isOpen]);\n\n  if (!isOpen) return null;\n\n  return ReactDOM.createPortal(\n    <div className='modal-backdrop' onClick={handleClose}>\n      <div\n        className='modal-card'\n        role='dialog'\n        aria-modal='true'\n        ref={dialogRef}\n        onClick={(e) => e.stopPropagation()}\n      >\n        {title && <h2>{title}</h2>}\n        {children}\n        <button onClick={handleClose} aria-label='Close'>×</button>\n      </div>\n    </div>,\n    document.body\n  );\n};\n```"
)

# ==================== NODE.JS (SENIOR: 20 Qs) ====================
add_mcq("sr-node-01", "node", "V8 Memory Spaces",
    "In V8's garbage collection architecture, how does the Scavenge (Young Generation) algorithm differ from the Mark-Sweep-Compact (Old Generation) algorithm?",
    [
        "A) Scavenge is for files; Mark-Sweep is for network buffers",
        "B) Scavenge splits the Semi-Space into 'From' and 'To' spaces and copies surviving objects quickly (Cheney's algorithm), while Mark-Sweep-Compact pauses to mark live objects, sweeps dead ones, and compacts fragmented memory for long-lived objects",
        "C) Scavenge is executed by the OS kernel, not V8",
        "D) Mark-Sweep only runs when Node.js terminates"
    ],
    "B",
    "V8's Young Generation uses a fast generational copy collector (Scavenge) between two semi-spaces. Most objects die young. Objects that survive multiple scavenge cycles are promoted to Old Space, which is cleaned by the more expensive Mark-Sweep-Compact collector."
)

add_mcq("sr-node-02", "node", "Event Loop Starvation by ReDoS",
    "How does a Regular Expression Denial of Service (ReDoS) freeze a high-throughput Node.js microservice?",
    [
        "A) It deletes the regex engine from disk",
        "B) Vulnerable non-deterministic finite automaton (NFA) regex patterns with nested quantifiers (e.g. `(a+)+$`) trigger catastrophic backtracking with exponential time complexity (O(2^N)), monopolizing the single JavaScript thread and blocking all other HTTP requests",
        "C) It exhausts PostgreSQL connections",
        "D) It crashes the Linux network card"
    ],
    "B",
    "Because Node executes JavaScript on a single thread, an exponential backtracking regex evaluated against a malicious string stalls the CPU at 100%, causing event loop starvation where no timers, I/O, or HTTP requests can be processed."
)

add_mcq("sr-node-03", "node", "AsyncLocalStorage Context Propagation",
    "What is the primary use case of `AsyncLocalStorage` from the `async_hooks` module in enterprise Node.js services?",
    [
        "A) Storing cookies on the client browser",
        "B) Propagating request-scoped context (such as correlation IDs, transaction traces, or authenticated user identity) across asynchronous execution chains without explicitly passing variables through every function argument",
        "C) Caching SQL queries in RAM",
        "D) Replacing Redis in production"
    ],
    "B",
    "`AsyncLocalStorage` provides continuation-local storage across asynchronous Promise chains and callbacks, enabling distributed tracing, request correlation IDs, and tenant isolation without polluting function signatures."
)

add_mcq("sr-node-04", "node", "Worker Threads SharedArrayBuffer & Atomics",
    "How do Node.js Worker Threads achieve ultra-fast inter-thread communication without the overhead of structured cloning serialization?",
    [
        "A) By writing to shared JSON files on an NVMe SSD",
        "B) By sharing the same physical memory buffer using `SharedArrayBuffer` and synchronizing concurrent read/write operations safely using `Atomics` operations",
        "C) By streaming data over local loopback TCP sockets",
        "D) By using Redis in-memory pub/sub"
    ],
    "B",
    "Standard `postMessage` serializes data using the structured clone algorithm. `SharedArrayBuffer` maps the exact same memory bytes to multiple threads, and `Atomics` (e.g. `Atomics.wait`, `Atomics.notify`) provides atomic lock-free coordination."
)

add_mcq("sr-node-05", "node", "Libuv Threadpool Starvation",
    "If an Express application concurrently executes 20 heavy `crypto.pbkdf2` password hashes while using default settings, what happens to incoming `fs.readFile` calls?",
    [
        "A) `fs.readFile` runs in parallel without any delay because it uses an independent thread pool",
        "B) `fs.readFile` is queued and delayed because default libuv has only 4 worker threads (`UV_THREADPOOL_SIZE=4`), and all 4 are saturated by the synchronous crypto operations",
        "C) Node.js automatically spawns 100 operating system threads",
        "D) The operating system terminates the Node.js process"
    ],
    "B",
    "Both `fs` operations and certain `crypto` functions share the same default 4-thread libuv pool. Saturating all 4 threads causes threadpool starvation, stalling unrelated file I/O operations until threads free up."
)

add_mcq("sr-node-06", "node", "Clinic.js Diagnostics",
    "In the Node.js diagnostic tool suite Clinic.js, which tool is specifically designed to isolate event loop latency and thread pool contention?",
    [
        "A) Clinic Doctor",
        "B) Clinic Flame",
        "C) Clinic Bubbleprof",
        "D) Clinic Clean"
    ],
    "C",
    "Clinic Bubbleprof profiles async latency between operations, mapping delays across async hops to identify whether bottlenecks stem from database latency, event loop delays, or thread pool starvation."
)

add_mcq("sr-node-07", "node", "Node-API (N-API) Stability",
    "What is the core benefit of writing native C/C++ addons using Node-API (formerly N-API) instead of older V8 APIs?",
    [
        "A) Node-API compiles directly into JavaScript",
        "B) Node-API provides an Application Binary Interface (ABI) stability guarantee, meaning compiled native addons do not need to be recompiled when upgrading Node.js major versions",
        "C) Node-API eliminates C++ compiler warnings",
        "D) Node-API requires no C++ knowledge"
    ],
    "B",
    "Before Node-API, upgrading Node.js major versions broke native addons because V8 internal APIs shifted. Node-API abstracts V8, guaranteeing ABI compatibility across major Node versions."
)

add_mcq("sr-node-08", "node", "V8 Heap Snapshots Retained Size",
    "When inspecting a Node.js heap snapshot in Chrome DevTools, what is the critical difference between 'Shallow Size' and 'Retained Size'?",
    [
        "A) Shallow size is RAM; Retained size is disk space",
        "B) Shallow size is the memory held by the object itself; Retained size is the total memory freed if that object is garbage collected (including all dependent objects it keeps alive)",
        "C) Retained size is always smaller than shallow size",
        "D) Shallow size includes V8 engine code"
    ],
    "B",
    "An object holding a reference to a 100MB buffer has a tiny shallow size (just the pointer bytes), but its retained size is over 100MB because it prevents the buffer from being collected."
)

add_open("sr-node-09", "node", "V8 Garbage Collection Tuning and Heap Forensics",
    "Explain the mechanics of V8's Generational Garbage Collector (Scavenger vs Mark-Sweep-Compact). What flags and diagnostic steps do you use to diagnose and fix a production Out-Of-Memory (OOM) crash in Node.js?",
    [
        "Generational hypothesis: most objects die young (New Space: Eden/To/From)",
        "Long-lived objects promoted to Old Space; collected by Mark-Sweep-Compact with incremental marking to reduce stop-the-world pauses",
        "Flags: --max-old-space-size, --trace-gc, --heapsnapshot-on-unhandled-exception / --heapsnapshot-on-signal",
        "Forensics: Inspect Retaining Tree in Chrome DevTools, find root dominator leaking memory"
    ],
    "1. Generational GC Mechanics:\n- New Space (Young Gen): Divided into two Semi-Spaces (From/To). Allocations land in From space. A fast Scavenge cycle copies surviving objects to the To space and swaps pointers. Surviving two cycles promotes the object to Old Space.\n- Old Space: Contains long-lived data. V8 uses Mark-Sweep-Compact. It employs Incremental Marking and Concurrent Sweeping to interleave GC pauses with JavaScript execution, minimizing 'Stop-the-World' latency.\n2. Diagnosing Production OOM:\n- Enable Flags: Run with `--max-old-space-size=4096` and `--heapsnapshot-on-unhandled-exception` or capture snapshots on `SIGUSR2`.\n- Analyze GC Activity: Use `--trace-gc` or `--trace-gc-verbose` to log pause times and heap growth patterns.\n- Inspect Snapshots: Load the snapshot in Chrome DevTools. Look at the 'Dominators' and 'Summary' views. Sort by 'Retained Size'. Trace the Retaining Path back to GC roots (usually global arrays, unresolved promise closures, or event listener maps)."
)

add_open("sr-node-10", "node", "Distributed Tracing with AsyncLocalStorage",
    "Implement an enterprise Express middleware using `AsyncLocalStorage` that generates or propagates a W3C `traceparent` distributed tracing ID and makes it accessible across all database and service calls without parameter drilling.",
    [
        "Import AsyncLocalStorage from node:async_hooks",
        "Middleware extracts req.headers['traceparent'] or generates crypto.randomUUID()",
        "Calls asyncLocalStorage.run(context, () => next())",
        "Logging and database query wrappers retrieve traceId via asyncLocalStorage.getStore()"
    ],
    "```javascript\nimport { AsyncLocalStorage } from 'node:async_hooks';\nimport crypto from 'node:crypto';\n\nexport const tracer = new AsyncLocalStorage();\n\nexport function traceMiddleware(req, res, next) {\n  const traceId = req.headers['x-trace-id'] || crypto.randomUUID();\n  const store = {\n    traceId,\n    startTime: Date.now(),\n    user: null\n  };\n\n  res.setHeader('X-Trace-Id', traceId);\n  tracer.run(store, () => {\n    next();\n  });\n}\n\n// Usage anywhere in deep business logic or DB models:\nexport function logWithContext(message) {\n  const store = tracer.getStore();\n  const traceId = store ? store.traceId : 'no-trace';\n  console.log(`[${new Date().toISOString()}] [${traceId}] ${message}`);\n}\n```"
)

# ==================== EXPRESS.JS & SYSTEM ARCHITECTURE (SENIOR: 18 Qs) ====================
add_mcq("sr-express-01", "express", "Distributed Rate Limiting with Redis Lua",
    "Why must multi-instance Express microservices execute distributed rate limiting via Redis Lua scripts rather than separate Redis GET and INCR commands?",
    [
        "A) Lua scripts compile to C++",
        "B) Executing separate GET, INCR, and EXPIRE commands introduces race conditions between concurrent requests; Redis Lua scripts execute atomically in a single thread, guaranteeing thread-safe counter checks without distributed locks",
        "C) Lua scripts bypass Redis memory limits",
        "D) Express cannot run Redis commands directly"
    ],
    "B",
    "In a distributed cluster, separate `GET` and `INCR` commands suffer from race conditions. Redis guarantees that Lua scripts execute atomically, preventing two simultaneous requests from bypassing rate caps."
)

add_mcq("sr-express-02", "express", "Circuit Breaker Pattern (Opossum)",
    "In a microservices architecture, what is the role of the 'Half-Open' state in a Circuit Breaker (e.g. Opossum)?",
    [
        "A) The circuit is permanently broken and all traffic is dropped",
        "B) After a timeout period following an open failure state, the circuit allows a limited number of trial requests through to test if the downstream service has recovered, closing if successful or re-opening if failures persist",
        "C) The circuit only accepts GET requests",
        "D) It cuts CPU clock speed in half"
    ],
    "B",
    "A Circuit Breaker moves from Closed (healthy) to Open (failing, fast-failing calls). In the Half-Open state, it sends probe requests to test downstream health; if they succeed, it closes the circuit and resumes normal operations."
)

add_mcq("sr-express-03", "express", "Handling Backpressure on Large Streaming Uploads",
    "What catastrophe occurs if an Express server reads an incoming multipart video stream and pipes it into an AWS S3 stream without respecting backpressure (`stream.pipeline` / `write()` returning false)?",
    [
        "A) The video resolution is downgraded to 144p",
        "B) Data chunks buffer indefinitely in Node.js heap memory because the network read rate exceeds the upload rate, eventually triggering a fatal V8 JavaScript heap out-of-memory crash",
        "C) S3 rejects the connection",
        "D) The operating system deletes the file"
    ],
    "B",
    "If write speed is slower than read speed, unconsumed chunks accumulate in Node's internal buffer queue. Without backpressure pausing the readable source, memory balloons until the Node process crashes with OOM."
)

add_mcq("sr-express-04", "express", "gRPC vs REST for Inter-Service Calls",
    "Why do high-throughput internal microservices often communicate via gRPC (Protobuf over HTTP/2) instead of JSON REST APIs?",
    [
        "A) gRPC requires no code compilation",
        "B) Protobuf provides binary serialization (smaller payloads and faster parsing than JSON text), multiplexed bidirectional streaming over a single TCP connection via HTTP/2, and strict compile-time contract enforcement",
        "C) gRPC can only be written in Go",
        "D) REST APIs do not support HTTPS"
    ],
    "B",
    "gRPC delivers 5x-10x higher throughput than REST by eliminating verbose JSON strings, leveraging binary Protocol Buffers, and reusing persistent HTTP/2 connections with header compression (HPACK)."
)

add_mcq("sr-express-05", "express", "Reverse Proxy Load Balancing Algorithms",
    "When load-balancing traffic across 10 Express backend pods, why is 'Least Connections' generally superior to simple 'Round Robin' for heterogeneous workloads?",
    [
        "A) Round Robin is deprecated in Nginx",
        "B) Requests have variable execution times (e.g. quick cache hits vs heavy PDF generation); Least Connections routes traffic to pods with the fewest active requests, preventing slow requests from accumulating on a single overloaded worker",
        "C) Least Connections encrypts HTTP headers",
        "D) Round Robin requires sticky cookies"
    ],
    "B",
    "Round Robin blindly alternates pods regardless of workload. If Pod 1 receives three heavy reporting queries, it becomes saturated. Least Connections routes traffic dynamically to the worker with the lowest active concurrent load."
)

add_open("sr-express-06", "express", "Distributed Rate Limiter with Redis Token Bucket",
    "Write a production-ready Express rate limiting middleware using an atomic Redis Lua script implementing the Token Bucket algorithm with refill rate and maximum burst capacity.",
    [
        "Evaluates token bucket atomically in Redis using EVAL / Lua script",
        "Calculates tokens to add based on (now - lastRefillTime) * refillRate",
        "Deducts token if available and updates lastRefillTime; returns remaining tokens or reject with 429",
        "Includes standard headers (X-RateLimit-Limit, X-RateLimit-Remaining, Retry-After)"
    ],
    "```javascript\nconst tokenBucketLua = `\n  local key = KEYS[1]\n  local capacity = tonumber(ARGV[1])\n  local refillRate = tonumber(ARGV[2]) -- tokens per millisecond\n  local now = tonumber(ARGV[3])\n  local requested = tonumber(ARGV[4])\n\n  local data = redis.call('HMGET', key, 'tokens', 'lastRefill')\n  local tokens = tonumber(data[1])\n  local lastRefill = tonumber(data[2])\n\n  if not tokens then\n    tokens = capacity\n    lastRefill = now\n  else\n    local elapsed = now - lastRefill\n    tokens = math.min(capacity, tokens + (elapsed * refillRate))\n    lastRefill = now\n  end\n\n  if tokens >= requested then\n    tokens = tokens - requested\n    redis.call('HMSET', key, 'tokens', tokens, 'lastRefill', lastRefill)\n    redis.call('PEXPIRE', key, 3600000) -- 1 hr TTL\n    return { 1, math.floor(tokens) }\n  else\n    redis.call('HMSET', key, 'tokens', tokens, 'lastRefill', lastRefill)\n    return { 0, math.floor(tokens) }\n  end\n`;\n\nexport const tokenBucketLimiter = (redisClient, capacity = 100, refillPerSec = 10) => {\n  const refillRate = refillPerSec / 1000;\n  return async (req, res, next) => {\n    const key = `rate_limit:${req.ip}`;\n    const now = Date.now();\n    const [allowed, remaining] = await redisClient.eval(\n      tokenBucketLua, 1, key, capacity, refillRate, now, 1\n    );\n    res.setHeader('X-RateLimit-Remaining', remaining);\n    if (allowed === 1) return next();\n    res.setHeader('Retry-After', Math.ceil(1 / refillPerSec));\n    return res.status(429).json({ error: 'Too Many Requests (Token Bucket Exhausted)' });\n  };\n};\n```"
)

add_open("sr-express-07", "express", "Circuit Breaker Implementation for External APIs",
    "Explain the three states of the Circuit Breaker pattern (Closed, Open, Half-Open). Write a production implementation or wrapper using `opossum` protecting an Express controller from third-party payment gateway outages.",
    [
        "Closed: Normal operation, routing requests downstream",
        "Open: Error threshold exceeded (e.g. 50% failures), immediately fast-fails calls without invoking downstream",
        "Half-Open: Cooldown expires (resetTimeout), allows test requests to gauge health",
        "Opossum configuration with timeout, errorThresholdPercentage, resetTimeout, fallback response"
    ],
    "```javascript\nimport CircuitBreaker from 'opossum';\n\nasync function callPaymentGateway(paymentData) {\n  const response = await fetch('https://api.payment-gateway.com/charge', {\n    method: 'POST',\n    body: JSON.stringify(paymentData),\n    signal: AbortSignal.timeout(3000) // 3s network timeout\n  });\n  if (!response.ok) throw new Error(`Gateway Error: ${response.status}`);\n  return response.json();\n}\n\nconst options = {\n  timeout: 3000, // Trigger failure if call takes > 3s\n  errorThresholdPercentage: 50, // Open circuit if 50% fail\n  resetTimeout: 15000 // Try again after 15s (Half-Open)\n};\n\nexport const paymentBreaker = new CircuitBreaker(callPaymentGateway, options);\n\npaymentBreaker.fallback(() => ({\n  status: 'queued',\n  message: 'Payment service currently experiencing high latency. Your request is queued for processing.'\n}));\n\npaymentBreaker.on('open', () => console.warn('⚠️ Circuit Breaker OPEN: Payment gateway offline!'));\npaymentBreaker.on('halfOpen', () => console.log('⚡ Circuit Breaker HALF-OPEN: Testing gateway...'));\npaymentBreaker.on('close', () => console.log('✅ Circuit Breaker CLOSED: Gateway healthy.'));\n```"
)

# ==================== MONGODB AT SCALE (SENIOR: 18 Qs) ====================
add_mcq("sr-mongo-01", "mongodb", "Sharding & Shard Key Selection",
    "What is the catastrophic consequence of choosing a monotonically increasing shard key (like `ObjectId` or `timestamp`) in a high-write MongoDB sharded cluster?",
    [
        "A) All documents are deleted after 24 hours",
        "B) 'Hotspotting' occurs: all new inserts target the single maximum shard chunk range, directing 100% of write traffic to a single shard while other shards sit idle, destroying horizontal write scaling",
        "C) Sharded clusters cannot accept timestamps",
        "D) The database switches to read-only mode"
    ],
    "B",
    "Monotonically increasing keys always fall into the upper bound chunk on the last shard. All write throughput hammers a single machine, negating the entire purpose of horizontal sharding. Hashed shard keys or compound keys avoid hotspotting."
)

add_mcq("sr-mongo-02", "mongodb", "WiredTiger Checkpoints & Cache Eviction",
    "How does MongoDB's WiredTiger storage engine manage cache eviction and durability under heavy memory pressure?",
    [
        "A) It writes every single update directly to unbuffered raw disk sectors",
        "B) WiredTiger maintains a clean and dirty cache. When dirty cache exceeds thresholds (default 20%), background threads aggressively evict pages to disk. Every 60 seconds (or 2GB of logs), it creates a durable checkpoint across data files",
        "C) It drops old collections automatically",
        "D) It restarts the mongod process"
    ],
    "B",
    "WiredTiger uses an in-memory cache (typically 50% of RAM minus 1GB). Modifications mark cache pages as 'dirty'. Periodic checkpoints write a consistent snapshot to disk every 60s, relying on the Write-Ahead Log (journal) for recovery between checkpoints."
)

add_mcq("sr-mongo-03", "mongodb", "Read Concern Linearizable vs Majority",
    "What is the difference between Read Concern `majority` and `linearizable` in MongoDB?",
    [
        "A) `majority` reads from all nodes; `linearizable` reads from secondary nodes",
        "B) `majority` returns data acknowledged by a majority of replica set members (immune to rollback), while `linearizable` additionally performs real-time consensus with peers to guarantee the primary has not been deposed by a network partition, preventing stale reads during split-brain elections",
        "C) `linearizable` is 10x faster than `majority`",
        "D) There is no difference"
    ],
    "B",
    "In a network partition, an isolated primary might not realize it has been superseded. `readConcern: majority` could read data before the old primary discovers it was replaced. `linearizable` forces the primary to confirm its leadership with peers before returning, guaranteeing strict real-time serializability."
)

add_mcq("sr-mongo-04", "mongodb", "Jumbo Chunks in Sharding",
    "What is a 'Jumbo Chunk' in MongoDB sharding, and how does it occur?",
    [
        "A) A chunk stored on an AWS jumbo instance",
        "B) A chunk that exceeds the maximum chunk size (default 64MB) and cannot be split because all documents in the chunk share the exact same low-cardinality shard key value",
        "C) A chunk containing video files",
        "D) A compressed database file"
    ],
    "B",
    "When a shard key has low cardinality (e.g. `country: 'US'`), millions of documents share the identical key value. MongoDB cannot split documents with identical keys across chunks, creating an indivisible 'Jumbo Chunk' that the balancer cannot migrate."
)

add_mcq("sr-mongo-05", "mongodb", "Covered Queries in MongoDB",
    "What conditions must be satisfied for a MongoDB query to be a 'Covered Query' (`totalDocsExamined: 0`), and why is it optimal?",
    [
        "A) The query must run on an encrypted SSL socket",
        "B) All fields in the query filter and projection must be present in the index, and `_id` must be explicitly excluded (unless indexed), allowing MongoDB to satisfy the query entirely from RAM index memory without touching disk documents",
        "C) The query must scan the entire collection",
        "D) The collection must have fewer than 100 documents"
    ],
    "B",
    "A covered query is fulfilled entirely by index keys. Because MongoDB never accesses the actual document data on disk (`totalDocsExamined: 0`), it achieves the highest possible throughput and lowest I/O latency."
)

add_open("sr-mongo-06", "mongodb", "Designing Shard Keys for High-Throughput Systems",
    "You are architecting a global IoT analytics platform on MongoDB storing 5 billion sensor readings per month. Queries query by `tenantId` and `timestamp`. Compare a Hashed Shard Key, a Ranged Shard Key, and a Compound Shard Key `{ tenantId: 1, timestamp: 1 }`. Which do you choose and why?",
    [
        "Ranged key (timestamp) causes write hotspotting on the latest shard",
        "Hashed key on tenantId or readingId distributes writes evenly but turns range queries into scatter-gather across all shards",
        "Compound key { tenantId: 1, timestamp: 1 } clusters tenant data to specific shards, avoiding hotspotting across distinct tenants and enabling targeted shard routing for date range queries"
    ],
    "1. Ranged on `timestamp`: Causes severe write hotspotting. Every sensor reading generated right now has an increasing timestamp, so 100% of inserts hammer the single shard holding the current time range.\n2. Hashed on `_id` or `timestamp`: Distributes write I/O uniformly across all shards, but every query searching for a tenant's date range must broadcast to *every* shard in the cluster ('scatter-gather'), degrading query throughput.\n3. Compound Shard Key `{ tenantId: 1, timestamp: 1 }` (Optimal):\n- Write Distribution: High cardinality across distinct tenants distributes concurrent writes across different shards.\n- Targeted Routing: When querying a specific tenant's data (`find({ tenantId: 't1', timestamp: { ... } })`), the `mongos` router directs the query exclusively to the single shard hosting that tenant, avoiding scatter-gather and optimizing read performance."
)

add_open("sr-mongo-07", "mongodb", "Advanced Schema Design: Bucket and Subset Patterns",
    "Detail how the 'Bucket Pattern' and 'Subset Pattern' solve performance bottlenecks in massive MongoDB applications. Provide a concrete schema model for an IoT sensor or e-commerce product catalog.",
    [
        "Bucket Pattern: Groups time-series readings into fixed-size documents (e.g. 1 document per hour with array of 60-3600 measurements), reducing document count by 1000x and index size dramatically",
        "Subset Pattern: Embeds the top 5-10 most frequent items (e.g. recent reviews or product summary) in main document, offloading historical tail to separate collection to fit working set into RAM"
    ],
    "1. The Bucket Pattern (IoT / Time-Series):\nInstead of inserting 1 document per second (producing 86,400 documents/day per device with massive index bloat), aggregate measurements into 1 document per hour:\n```json\n{\n  \"deviceId\": \"sensor_42\",\n  \"bucketStart\": ISODate(\"2026-09-24T00:00:00Z\"),\n  \"count\": 3600,\n  \"readings\": [\n    { \"t\": 0, \"temp\": 21.4, \"humidity\": 55 },\n    { \"t\": 1, \"temp\": 21.5, \"humidity\": 55 }\n  ]\n}\n```\nReduces index B-Tree size by 3,600x and speeds up range queries.\n2. The Subset Pattern (E-Commerce):\nA product might have 50,000 customer reviews. Loading all reviews on the product page wastes RAM and exceeds the 16MB document limit. Embed only the 10 most recent reviews in the `products` document. Store the remaining 49,990 reviews in a separate `reviews` collection fetched on demand with pagination."
)

# ==================== POSTGRESQL AT SCALE (SENIOR: 18 Qs) ====================
add_mcq("sr-pg-01", "postgresql", "PostgreSQL MVCC & Autovacuum Tuning",
    "In PostgreSQL Multi-Version Concurrency Control (MVCC), what does an `UPDATE` statement physically do to table pages on disk, and what happens if `autovacuum` cannot keep up?",
    [
        "A) It modifies the existing bytes in place immediately without allocating disk space",
        "B) It writes an entirely new row version (tuple) with updated values and marks the old tuple as dead (`xmax` set); if autovacuum cannot keep up, dead tuples accumulate, causing severe table/index 'bloat' and degrading sequential scan performance",
        "C) It moves the row to an archive database",
        "D) It locks the entire database server"
    ],
    "B",
    "PostgreSQL does not update rows in place. An `UPDATE` performs an `INSERT` of the new version and marks the previous tuple dead. VACUUM reclaims space occupied by dead tuples. Un-vacuumed dead tuples cause massive disk and cache bloat."
)

add_mcq("sr-pg-02", "postgresql", "HOT (Heap-Only Tuples) Optimization",
    "What is the Heap-Only Tuple (HOT) optimization in PostgreSQL, and what condition must be met for it to activate?",
    [
        "A) Storing tables in GPU memory",
        "B) If an `UPDATE` does not modify any indexed columns and the new tuple fits into the exact same 8KB data page as the old tuple, PostgreSQL creates a HOT chain within the page, avoiding the need to update table indexes",
        "C) Compressing text columns with gzip",
        "D) Running queries without a WHERE clause"
    ],
    "B",
    "Index updates are expensive. With HOT, if indexed columns are untouched and the new row version fits in the same data page, PostgreSQL links old and new tuples internally on heap pages, eliminating index write amplification entirely."
)

add_mcq("sr-pg-03", "postgresql", "SELECT FOR UPDATE SKIP LOCKED",
    "Why is `SELECT ... FOR UPDATE SKIP LOCKED` the gold standard for implementing high-concurrency transactional message queues in PostgreSQL?",
    [
        "A) It prevents anyone from reading from the table",
        "B) It allows multiple concurrent worker processes to lock and process distinct unclaimed rows simultaneously without blocking each other or waiting on locked rows",
        "C) It encrypts messages in the queue",
        "D) It bypasses ACID transactions"
    ],
    "B",
    "Standard `FOR UPDATE` blocks concurrent workers when they contend for the same row. `SKIP LOCKED` instructs workers to skip already-locked rows and grab the next available unlocked job, enabling lock-free concurrent queue processing."
)

add_mcq("sr-pg-04", "postgresql", "CREATE INDEX CONCURRENTLY",
    "Why should production database migrations on active PostgreSQL tables always use `CREATE INDEX CONCURRENTLY` instead of standard `CREATE INDEX`?",
    [
        "A) Standard `CREATE INDEX` acquires an `ACCESS EXCLUSIVE` lock on the table, blocking all concurrent `SELECT`, `INSERT`, `UPDATE`, and `DELETE` operations until index construction finishes",
        "B) `CONCURRENTLY` uses less RAM",
        "C) Standard `CREATE INDEX` corrupts data if the server reboots",
        "D) `CONCURRENTLY` is required for B-Tree indexes"
    ],
    "A",
    "Building an index on a 100-million-row table can take 30 minutes. Standard `CREATE INDEX` blocks all read and write queries, causing a major outage. `CREATE INDEX CONCURRENTLY` performs two table scans without blocking writes."
)

add_mcq("sr-pg-05", "postgresql", "PgBouncer Pooling Modes",
    "What is the limitation of PgBouncer in `Transaction Pooling` mode compared to `Session Pooling` mode in a Node.js PERN stack?",
    [
        "A) It does not support SQL queries",
        "B) Named prepared statements, session-level advisory locks, and temporary tables cannot be used safely because consecutive queries in the same client session may execute over different underlying PostgreSQL backend connections",
        "C) It only permits 1 connection total",
        "D) It requires running PostgreSQL on Docker"
    ],
    "B",
    "In transaction pooling, PgBouncer assigns a server connection only for the duration of a transaction, returning it to the pool immediately upon `COMMIT`. Features tied to the physical connection session (like prepared statements) become unreliable unless configured with protocol-level workarounds."
)

add_open("sr-pg-06", "postgresql", "Mastering EXPLAIN (ANALYZE, BUFFERS) Execution Plans",
    "Analyze the following PostgreSQL query execution node:\n`Bitmap Heap Scan on orders (cost=12.40..580.12 rows=140 width=64) (actual time=0.82..4.12 rows=150 loops=1)`\n`Buffers: shared hit=42 read=18`\nExplain what Bitmap Heap Scan, shared hit, and shared read mean. How do you tune memory parameters (`shared_buffers`, `work_mem`) based on buffer stats?",
    [
        "Bitmap Index Scan gathers block locations matching predicate; Bitmap Heap Scan visits pages on disk to retrieve rows",
        "Shared hit: Pages read directly from PostgreSQL RAM buffer pool cache",
        "Shared read: Pages read from OS page cache or physical disk (I/O latency)",
        "Tuning: High shared read indicates shared_buffers is too small or missing cache; Sort spilling to disk indicates work_mem must be increased"
    ],
    "1. Bitmap Heap Scan:\nA two-stage scan. First, a `Bitmap Index Scan` scans the index and constructs an in-memory bitmap of physical page blocks containing matching rows. The `Bitmap Heap Scan` then visits those heap pages sequentially, minimizing random disk I/O.\n2. Buffer Statistics:\n- `shared hit=42`: 42 data pages (8KB each, ~336KB) were found cached in PostgreSQL's `shared_buffers` RAM, incurring zero disk I/O.\n- `shared read=18`: 18 pages were not in database RAM and had to be fetched from the OS page cache or physical NVMe disk.\n3. Memory Tuning:\n- If queries show high `shared read` ratios on hot tables, increase `shared_buffers` (typically 25% of total server RAM).\n- If an `EXPLAIN ANALYZE` sort or hash operation shows `Sort Method: external merge Disk`, increase `work_mem` for the session or database so sorts complete entirely in fast RAM."
)

add_open("sr-pg-07", "postgresql", "Declarative Partitioning at Scale",
    "You manage an `audit_logs` table in PostgreSQL growing by 20 million rows per week. Design a declarative RANGE partitioning scheme by month. Explain how partition pruning works and how to drop old logs with zero lock overhead.",
    [
        "CREATE TABLE audit_logs (...) PARTITION BY RANGE (created_at)",
        "Create monthly partitions: CREATE TABLE audit_logs_2026_09 PARTITION OF audit_logs FOR VALUES FROM ('2026-09-01') TO ('2026-10-01')",
        "Partition pruning: Query planner analyzes WHERE created_at >= ... and skips non-matching partition tables entirely",
        "Zero-lock cleanup: DROP TABLE or ALTER TABLE DETACH PARTITION is instantaneous (metadata operation), avoiding expensive DELETE FROM table that causes dead tuple bloat"
    ],
    "```sql\n-- 1. Create partitioned master table\nCREATE TABLE audit_logs (\n  id BIGINT GENERATED ALWAYS AS IDENTITY,\n  tenant_id UUID NOT NULL,\n  action TEXT NOT NULL,\n  created_at TIMESTAMPTZ NOT NULL,\n  PRIMARY KEY (id, created_at)\n) PARTITION BY RANGE (created_at);\n\n-- 2. Create monthly child partitions\nCREATE TABLE audit_logs_2026_09 PARTITION OF audit_logs\n  FOR VALUES FROM ('2026-09-01 00:00:00+00') TO ('2026-10-01 00:00:00+00');\n\nCREATE TABLE audit_logs_2026_10 PARTITION OF audit_logs\n  FOR VALUES FROM ('2026-10-01 00:00:00+00') TO ('2026-11-01 00:00:00+00');\n```\nBenefits:\n1. Partition Pruning: When a query includes `WHERE created_at >= '2026-09-15'`, the planner automatically prunes away October, November, and historical tables, scanning only the September table.\n2. Instant Zero-Overhead Purging: Instead of running a catastrophic `DELETE FROM audit_logs WHERE created_at < ...` (which bloats tables and generates millions of dead tuples), simply run:\n`ALTER TABLE audit_logs DETACH PARTITION audit_logs_2025_01;`\n`DROP TABLE audit_logs_2025_01;`\nThis metadata operation drops gigabytes of data in milliseconds without vacuum bloat."
)

# ==================== FULLSTACK SYSTEM DESIGN (SENIOR: 14 Qs) ====================
add_mcq("sr-full-01", "fullstack", "Transactional Outbox Pattern",
    "What fundamental distributed systems problem does the Transactional Outbox Pattern solve when a PERN/MERN service updates a database and publishes an event to Kafka/RabbitMQ?",
    [
        "A) It prevents users from sending spam emails",
        "B) The 'Dual-Write Problem': where updating the database succeeds but publishing to the message broker fails (or vice versa), leading to data inconsistency across distributed services; the Outbox pattern saves the event inside the database transaction and a separate worker relays it to the broker",
        "C) It encrypts network packets between microservices",
        "D) It compresses Kafka messages"
    ],
    "B",
    "Writing to a database and publishing to a message broker are two independent network operations. Without 2-phase commit, one can succeed while the other fails. Writing the message to an `outbox` database table within the same ACID transaction guarantees at-least-once delivery."
)

add_mcq("sr-full-02", "fullstack", "Saga Pattern: Choreography vs Orchestration",
    "How does Saga Orchestration differ from Saga Choreography in managing distributed transactions across multiple microservices?",
    [
        "A) Orchestration does not support rollback actions",
        "B) Choreography has services publish and listen to domain events asynchronously without a central coordinator; Orchestration uses a centralized orchestrator service that commands participants to execute local transactions and coordinates compensating transactions on failure",
        "C) Choreography only works with GraphQL",
        "D) Orchestration requires all services to share the same PostgreSQL database"
    ],
    "B",
    "In Choreography, services react to events from peers (can become hard to trace as services grow). In Orchestration, a dedicated orchestrator orchestrates the workflow step-by-step, issuing commands and handling compensating actions when a step aborts."
)

add_mcq("sr-full-03", "fullstack", "OAuth 2.0 PKCE Flow",
    "Why is Proof Key for Code Exchange (PKCE) mandatory for Single Page React Applications (SPAs) authenticating via OAuth 2.0?",
    [
        "A) Because browser SPAs are 'public clients' that cannot securely protect a client secret; PKCE dynamically generates a cryptographic code verifier and code challenge, preventing authorization code interception attacks",
        "B) PKCE speeds up network requests by 50%",
        "C) PKCE stores passwords in the browser registry",
        "D) It replaces HTTPS"
    ],
    "A",
    "Client-side JavaScript code and bundles are completely visible to users and attackers. Because SPAs cannot hold a secret, PKCE uses a dynamically generated cryptographic hash challenge to prove the entity exchanging the code is the same entity that initiated authorization."
)

add_mcq("sr-full-04", "fullstack", "Cache Stampede (Thundering Herd) Mitigation",
    "What is a 'Cache Stampede' and which technique effectively prevents it in high-traffic Redis architectures?",
    [
        "A) When Redis crashes due to high network temperature",
        "B) When a popular cache key expires and thousands of concurrent requests simultaneously miss the cache and hammer the database with identical queries; mitigated using Mutex locking (single-flight) or Probabilistic Early Expiration (XFetch)",
        "C) When Redis keys contain emoji characters",
        "D) When cache memory exceeds 1 Terabyte"
    ],
    "B",
    "A cache stampede causes database crashes when a hot key expires. Probabilistic Early Expiration (XFetch) or mutex locks allow only one worker to refresh the key while other requests serve the stale cache temporarily."
)

add_mcq("sr-full-05", "fullstack", "Zero-Downtime Blue-Green Deployments",
    "How do Blue-Green deployments achieve zero downtime and instant rollback capabilities?",
    [
        "A) By rebooting all server instances at midnight",
        "B) By running two identical production environments (Blue = live, Green = idle new version); once Green is validated, the load balancer switches 100% of traffic to Green instantly, with the ability to flip back to Blue if errors spike",
        "C) By converting the database into a Git branch",
        "D) By running Node.js in development mode"
    ],
    "B",
    "Blue-Green environments run in parallel. Traffic router/load balancer shifts incoming traffic to the newly deployed environment instantaneously. If an issue arises, traffic is immediately switched back to the old environment."
)

add_open("sr-full-06", "fullstack", "Architecting a 100,000 Req/Sec PERN/MERN System",
    "Design a system architecture capable of handling 100,000 requests/second for a live event ticketing platform. Detail your edge caching, API gateway, connection pooling, database scaling (sharding/read replicas), and queue architecture.",
    [
        "Edge: Cloudflare/Fastly CDN for static assets and caching read endpoints (stale-while-revalidate)",
        "Gateway: Nginx / Envoy / Kong load balancing across stateless Node.js clusters with horizontal pod autoscaling (HPA)",
        "Caching layer: Redis cluster (Cache-Aside with probabilistic early expiration, token bucket rate limiting)",
        "Queue: Kafka / RabbitMQ to buffer ticket reservation writes asynchronously",
        "Database: PostgreSQL with PgBouncer transaction pooling, master for writes, read replicas for browse queries, declarative partitioning by eventId"
    ],
    "1. Edge Tier:\n- Cloudflare CDN: Edge caching of static frontend bundles and read-only endpoints (event schedules, venue maps). Rate limiting and DDoS protection (WAF).\n2. API Gateway & Compute Tier:\n- Envoy / Kong reverse proxy terminating TLS, performing JWT verification, and load balancing across stateless Express / Node.js pods managed by Kubernetes (K8s HPA).\n3. In-Memory & Caching Tier:\n- Redis Cluster: Cache-Aside pattern for event availability. Distributed locking with Redlock for seat selection to prevent double bookings. Token bucket rate limiter.\n4. Write Decoupling (Queue Tier):\n- Peak ticket purchasing requests are offloaded to Apache Kafka or RabbitMQ. The Express API pushes order jobs and returns HTTP 202 Accepted. Dedicated worker pools consume orders sequentially, shielding the database from concurrency spikes.\n5. Database Tier:\n- Primary PostgreSQL cluster with PgBouncer connection poolers in Transaction Pooling mode.\n- Asynchronous Read Replicas serving read traffic.\n- Declarative table partitioning on `orders` partitioned by `event_id` or date."
)

add_open("sr-full-07", "fullstack", "The Dual-Write Problem and the Outbox Pattern",
    "Explain the Dual-Write problem in distributed architectures when an Express service must write to a database (PostgreSQL/MongoDB) and publish an event to a message broker (RabbitMQ/Kafka). Provide a full architecture and implementation pattern for the Transactional Outbox Pattern with Change Data Capture (Debezium) or a polling publisher.",
    [
        "Problem: Writing to DB and publishing to Broker cannot be combined into a single atomic transaction without 2PC (which hurts availability)",
        "Failure modes: DB commits but broker network fails (event lost); or broker publishes but DB transaction rolls back (ghost event sent)",
        "Solution: Outbox table in same DB transaction. CDC tool (Debezium) reads DB WAL/oplog and streams events to Kafka reliably with at-least-once delivery guarantee"
    ],
    "1. The Problem:\nConsider creating an order:\n```javascript\nawait db.orders.create(orderData);\nawait messageBroker.publish('order.created', orderData);\n```\nIf the broker fails or network drops after the DB write, the event is lost forever (other microservices never know the order exists). If you reverse the order and publish first, a database rollback leaves an invalid ghost event in the broker.\n2. Transactional Outbox Pattern:\nInstead of calling the broker directly, write the event into an `outbox` table *within the exact same database transaction*:\n```sql\nBEGIN;\nINSERT INTO orders (id, user_id, amount) VALUES ($1, $2, $3);\nINSERT INTO outbox_events (aggregate_type, aggregate_id, event_type, payload) \nVALUES ('Order', $1, 'OrderCreated', $payload);\nCOMMIT;\n```\nBecause both inserts happen in the same ACID transaction, both succeed or both fail atomically.\n3. Relay Options:\n- Change Data Capture (CDC with Debezium): Debezium tails the PostgreSQL Write-Ahead Log (WAL) or MongoDB Change Streams and automatically pushes outbox events to Kafka with zero polling overhead and at-least-once delivery guarantees.\n- Polling Publisher: A background Node.js worker periodically queries `SELECT * FROM outbox_events WHERE processed = false FOR UPDATE SKIP LOCKED` and publishes to the broker, marking records processed."
)

with open("/workspaces/preppro/src/data/senior.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Generated {len(questions)} Senior-Level questions in /workspaces/preppro/src/data/senior.json")
