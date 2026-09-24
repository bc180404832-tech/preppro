#!/usr/bin/env python3
import json

questions = []

def add_mcq(qid, stack, topic, question, options, answer, explanation):
    questions.append({
        "id": qid,
        "level": "mid",
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
        "level": "mid",
        "stack": stack,
        "type": "open",
        "topic": topic,
        "question": question,
        "expectedKeyPoints": expected_key_points,
        "sampleAnswer": sample_answer
    })

# ==================== REACT (MID-LEVEL) ====================
add_mcq("mid-react-01", "react", "useCallback vs useMemo",
    "What is the key technical difference between `useCallback(fn, deps)` and `useMemo(fn, deps)`?",
    [
        "A) `useCallback` executes the function immediately, while `useMemo` defers it",
        "B) `useCallback(fn, deps)` returns a memoized function instance, whereas `useMemo(fn, deps)` invokes the function and returns its memoized result value",
        "C) `useMemo` is for class components; `useCallback` is for functional components",
        "D) `useCallback` can only accept synchronous functions, while `useMemo` accepts Promises"
    ],
    "B",
    "`useCallback(fn, deps)` returns a cached reference to the function itself across renders to prevent unnecessary re-renders of memoized child components. `useMemo(() => compute(), deps)` returns the cached return value of the computation."
)

add_mcq("mid-react-02", "react", "React.memo Shallow Comparison",
    "By default, how does `React.memo` decide whether to skip re-rendering a component when parent props change?",
    [
        "A) It performs a deep recursive comparison of all nested object properties",
        "B) It performs a shallow comparison (`Object.is`) of previous and next props",
        "C) It converts props to JSON strings and compares the strings",
        "D) It only re-renders if the component's internal state changes"
    ],
    "B",
    "`React.memo` performs a shallow reference equality check (`Object.is`) on each prop. If any prop reference changes (such as an inline object `{}` or inline callback `() => {}`), `React.memo` will still trigger a re-render unless a custom comparison function is provided."
)

add_mcq("mid-react-03", "react", "useReducer vs useState",
    "When is `useReducer` generally preferred over `useState` in React?",
    [
        "A) When the state is a simple primitive boolean or string",
        "B) When managing complex state transitions where next state depends on previous state, or when multiple sub-values change together according to specific action types",
        "C) Only when connecting to Redux DevTools",
        "D) When rendering more than 100 HTML elements"
    ],
    "B",
    "`useReducer` is preferable when state logic is complex, involves multiple sub-values, or when the next state depends on the previous state. It centralizes update logic into a pure reducer function, making testing and debugging easier."
)

add_mcq("mid-react-04", "react", "useRef for Previous State",
    "How can `useRef` and `useEffect` be combined to track the previous value of a prop or state variable?",
    [
        "A) By mutating `ref.current` during the JSX render phase",
        "B) By storing the current value in `ref.current` inside `useEffect`, which runs after the render completes, preserving the previous value during the next render",
        "C) By binding `ref` to the window object",
        "D) It is impossible; React has a dedicated `usePrevious` built-in hook"
    ],
    "B",
    "Because `useEffect` executes after the render is committed to the screen, reading `ref.current` during rendering yields the value from the previous render, and the effect subsequently updates `ref.current` with the new value for the next cycle."
)

add_mcq("mid-react-05", "react", "React Context Performance",
    "What is a common performance pitfall when using React Context for global state management?",
    [
        "A) React Context crashes if more than 3 components subscribe to it",
        "B) Any change to the context value causes all components that call `useContext(MyContext)` to re-render, even if they only consume an untouched property of that context",
        "C) Context values are serialized to cookies on every render",
        "D) React Context cannot store functions"
    ],
    "B",
    "React Context does not support selector-based subscriptions natively. When a context value updates, every consumer component re-renders. Splitting contexts or using dedicated state management libraries (Zustand/Redux) prevents unnecessary re-renders."
)

add_mcq("mid-react-06", "react", "Error Boundaries",
    "Which of the following lifecycle methods or hooks can be used to create a React Error Boundary?",
    [
        "A) `useEffect(() => {}, [error])`",
        "B) Class component methods: `static getDerivedStateFromError()` and `componentDidCatch()`",
        "C) `useErrorBoundary()` hook",
        "D) `try/catch` wrapping the root `<App />` component in index.js"
    ],
    "B",
    "Currently, Error Boundaries must be class components implementing `static getDerivedStateFromError` (to render fallback UI) and/or `componentDidCatch` (to log errors). Hooks do not yet provide an error boundary equivalent."
)

add_mcq("mid-react-07", "react", "Custom Hooks Abstraction",
    "What is the primary architectural purpose of writing a Custom Hook in React?",
    [
        "A) To run JavaScript in a separate Web Worker thread",
        "B) To encapsulate and reuse stateful logic and side effects across multiple components without duplicating code or modifying component hierarchy",
        "C) To create global singleton state shared by all users across the network",
        "D) To bypass React's Virtual DOM diffing"
    ],
    "B",
    "Custom hooks allow developers to extract component logic into reusable functions. Each component invoking a custom hook gets an isolated instance of the internal state."
)

add_mcq("mid-react-08", "react", "React Portals",
    "What is the primary use case for `ReactDOM.createPortal`?",
    [
        "A) To render children into a DOM node that exists outside the DOM hierarchy of the parent component (e.g. Modals, Tooltips, Dialogs)",
        "B) To teleport network requests through a proxy",
        "C) To serialize components into WebAssembly",
        "D) To create 3D canvas viewports"
    ],
    "A",
    "Portals allow components like modals, dropdowns, and tooltips to render into `document.body` or other root containers to escape parent CSS stacking contexts (`overflow: hidden` or `z-index` traps) while retaining React event bubbling."
)

add_mcq("mid-react-09", "react", "React Lazy & Suspense",
    "How does `React.lazy` combined with `<Suspense>` improve the performance of large PERN/MERN frontends?",
    [
        "A) It compresses all PNG images on the fly",
        "B) It enables dynamic code-splitting by loading component bundles on demand only when they are rendered, displaying a fallback UI while loading",
        "C) It replaces fetch requests with WebSockets automatically",
        "D) It converts JavaScript code into C++ binaries"
    ],
    "B",
    "`React.lazy()` dynamically imports components via Webpack/Vite code-splitting, reducing initial bundle size and initial load times. `<Suspense fallback={<Spinner />}>` provides graceful loading states."
)

add_mcq("mid-react-10", "react", "Stale Closure Problem",
    "What causes a 'stale closure' bug inside a `useEffect` or `useCallback`?",
    [
        "A) Running out of heap memory in Google Chrome",
        "B) Omitting a state or prop variable from the dependency array, causing the callback to capture and retain an outdated reference from a previous render",
        "C) Calling `useState` inside a loop",
        "D) Using async/await inside React components"
    ],
    "B",
    "When a hook callback closes over variables from its render scope but omits them from the dependency array, it continues to reference the snapshot of those variables from when the callback was originally created."
)

add_mcq("mid-react-11", "react", "Redux Toolkit createSlice",
    "In Redux Toolkit (RTK), why is it safe to write 'mutating' code like `state.count += 1` inside `createSlice` reducers?",
    [
        "A) Redux Toolkit disables immutability checks in production",
        "B) RTK internally uses the Immer library, which intercepts mutations on a proxy Draft state and produces a new immutable copy",
        "C) Redux compiles JavaScript into C++ where mutation is faster",
        "D) Mutating state has always been the standard in Redux"
    ],
    "B",
    "Redux Toolkit uses Immer under the hood. You can write seemingly mutating logic (`state.todos.push(newTodo)`), and Immer records the operations to generate an immutable updated state tree."
)

add_mcq("mid-react-12", "react", "Zustand State Management",
    "What is a key architectural advantage of Zustand over React Context for application state?",
    [
        "A) Zustand only works on mobile devices",
        "B) Zustand allows components to subscribe to specific slices of state via selectors, preventing re-renders when unrelated state properties change",
        "C) Zustand does not support asynchronous actions",
        "D) Zustand requires wrapping the root component in 10 nested Providers"
    ],
    "B",
    "Zustand provides selector-based subscriptions (`useStore(state => state.user)`), ensuring a component only re-renders when the selected slice changes, completely bypassing Context Provider re-rendering cascades."
)

add_open("mid-react-13", "react", "Optimizing Re-renders in React",
    "Explain three effective techniques to diagnose and prevent unnecessary re-renders in a complex React application. Detail the trade-offs of premature memoization.",
    [
        "Techniques: React.memo with custom comparison, useCallback/useMemo for stable references, lifting content up / passing JSX as children (composition), Context splitting / Zustand selectors",
        "Diagnosis: React DevTools Profiler (flamegraph, 'record why component rendered')",
        "Trade-offs: useMemo and useCallback carry memory overhead, dependency array maintenance, and shallow comparison checks that can exceed the cost of cheap re-renders"
    ],
    "1. Diagnostic Tools: Use React DevTools Profiler with 'Record why each component rendered while profiling' enabled to identify components re-rendering unnecessarily.\n2. Prevention Techniques:\n- Component Composition: Moving state down to the component that actually needs it, or passing non-dependent subtrees as `children` props so parent renders don't force child reconciliation.\n- Stable References: Using `useCallback` for event handlers and `useMemo` for expensive computations or object props passed to `React.memo`-wrapped child components.\n- Context Splitting or Atomic State: Splitting large contexts into granular sub-contexts or using Zustand/Jotai so subscribers only listen to specific state slices.\n3. Trade-offs of Premature Memoization: `useMemo` and `useCallback` introduce memory overhead, closure allocations, and dependency array comparison costs. For simple components, running the lightweight render function is faster than maintaining memoization wrappers."
)

add_open("mid-react-14", "react", "Custom Hook Design Pattern",
    "Design and explain a custom React hook `useFetch(url, options)` that handles loading state, data caching, error handling, and aborting in-flight requests when the component unmounts or the URL changes.",
    [
        "Returns { data, loading, error, refetch }",
        "Uses AbortController in useEffect cleanup to cancel active HTTP fetch requests",
        "Handles race conditions when url changes quickly",
        "Does not call setState after component unmounts"
    ],
    "```javascript\nimport { useState, useEffect } from 'react';\n\nexport function useFetch(url, options = {}) {\n  const [data, setData] = useState(null);\n  const [loading, setLoading] = useState(true);\n  const [error, setError] = useState(null);\n\n  useEffect(() => {\n    const controller = new AbortController();\n    setLoading(true);\n    setError(null);\n\n    fetch(url, { ...options, signal: controller.signal })\n      .then(res => {\n        if (!res.ok) throw new Error(`HTTP Error: ${res.status}`);\n        return res.json();\n      })\n      .then(d => setData(d))\n      .catch(err => {\n        if (err.name !== 'AbortError') setError(err.message);\n      })\n      .finally(() => {\n        if (!controller.signal.aborted) setLoading(false);\n      });\n\n    return () => controller.abort(); // Cleanup & abort on URL change or unmount\n  }, [url]);\n\n  return { data, loading, error };\n}\n```\nKey features: Uses `AbortController` to cancel stale in-flight requests, preventing race conditions and memory leaks."
)

add_open("mid-react-15", "react", "React Router v6 Data Loaders",
    "How do Loaders and Actions in React Router v6+ shift data fetching architecture away from the traditional `useEffect` fetch-on-render pattern?",
    [
        "Fetch-on-render causes 'waterfalls' where child components wait for parents to finish rendering before starting their fetch",
        "React Router Loaders fetch data in parallel as soon as the URL route matches, before components begin rendering",
        "Actions provide declarative form submissions and automatic route re-validation"
    ],
    "Traditional React apps suffer from 'fetch-on-render waterfalls': Parent renders -> useEffect fetches data -> renders child -> child's useEffect fetches data. This creates sequential latency delays.\nReact Router v6.4+ introduces `loader` functions attached directly to route definitions. When a user navigates to `/dashboard/analytics`, React Router resolves all matching route loaders concurrently before rendering the components. The components then read pre-fetched data via `useLoaderData()`. Form actions work similarly, automatically triggering data re-validation across all active loaders after mutations."
)

# ==================== NODE.JS (MID-LEVEL) ====================
add_mcq("mid-node-01", "node", "Event Loop Microtasks vs Macrotasks",
    "Which queue has highest execution priority immediately after the current call stack completes in Node.js?",
    [
        "A) Timers queue (`setTimeout`)",
        "B) Check queue (`setImmediate`)",
        "C) `process.nextTick` queue, followed by the Promise microtask queue",
        "D) Poll queue (I/O callbacks)"
    ],
    "C",
    "In Node.js, `process.nextTick` queue executes immediately when the JavaScript call stack unwinds, even before Promise microtasks. Microtasks execute before the event loop advances to the next phase."
)

add_mcq("mid-node-02", "node", "setImmediate vs setTimeout(0)",
    "In a regular I/O callback cycle, which executes first between `setImmediate()` and `setTimeout(fn, 0)`?",
    [
        "A) `setTimeout(fn, 0)` always executes first",
        "B) `setImmediate()` always executes first because the check phase immediately follows the poll phase",
        "C) They execute in random order every single time",
        "D) Neither executes because I/O callbacks block timers"
    ],
    "B",
    "When scheduled within an I/O cycle (such as `fs.readFile` callback), the poll phase is active. The event loop moves directly from poll to the check phase, guaranteeing that `setImmediate()` executes before any timers."
)

add_mcq("mid-node-03", "node", "Streams & Backpressure",
    "What is 'backpressure' in Node.js Streams and how is it handled?",
    [
        "A) When CPU temperature rises above 90°C",
        "B) When a readable stream produces data faster than the writable stream can consume it, requiring pausing the readable stream until the writable buffer drains",
        "C) When network latency drops to zero",
        "D) A MongoDB indexing error"
    ],
    "B",
    "Backpressure occurs when data writes buffer up because the destination is slower than the source. When `writable.write()` returns `false`, reading should pause until the writable emits the `'drain'` event. `stream.pipeline` handles this automatically."
)

add_mcq("mid-node-04", "node", "stream.pipeline vs .pipe()",
    "Why is `stream.pipeline()` preferred over standard `.pipe()` in production Node.js applications?",
    [
        "A) `.pipe()` does not support binary data",
        "B) `.pipe()` does not automatically forward errors or destroy streams if one stream in the chain fails, causing memory and descriptor leaks",
        "C) `stream.pipeline()` is a third-party module",
        "D) `.pipe()` was removed in Node.js 14"
    ],
    "B",
    "`pipeline()` forwards errors across all chained streams, properly cleans up and destroys streams upon errors or completion, and accepts a callback or returns a Promise, unlike `.pipe()` which leaves streams unclosed on errors."
)

add_mcq("mid-node-05", "node", "EventEmitter Memory Leaks",
    "What warning does Node.js emit if you register more than 10 listeners on a single `EventEmitter` without modifying limits?",
    [
        "A) `FatalError: StackOverflowException`",
        "B) `MaxListenersExceededWarning: Possible EventEmitter memory leak detected`",
        "C) `SecurityWarning: DOS attack detected`",
        "D) Node.js silently discards the 11th listener"
    ],
    "B",
    "Node.js sets a default safety limit of 10 listeners per event to help developers catch memory leaks (such as repeatedly adding event listeners without removing them). You can adjust it with `emitter.setMaxListeners(n)`."
)

add_mcq("mid-node-06", "node", "Child Process exec vs spawn",
    "What is the key operational difference between `child_process.exec` and `child_process.spawn`?",
    [
        "A) `exec` spawns a shell and buffers the entire output in memory, while `spawn` streams data via I/O streams without buffering the entire output",
        "B) `spawn` only works on Linux; `exec` works on Windows",
        "C) `exec` is non-blocking, while `spawn` is blocking",
        "D) `spawn` can only run Python scripts"
    ],
    "A",
    "`exec` buffers stdout/stderr up to a configured limit (default 1MB) and passes the final string to a callback. `spawn` returns stream handles (`stdout`, `stderr`), making it suitable for large data outputs or long-running processes."
)

add_mcq("mid-node-07", "node", "Crypto Random Bytes",
    "Which method should be used in Node.js to generate cryptographically secure random tokens for password resets?",
    [
        "A) `Math.random().toString(36)`",
        "B) `crypto.randomBytes(32)` or `crypto.randomUUID()`",
        "C) `Date.now().toString()`",
        "D) `Buffer.alloc(32)`"
    ],
    "B",
    "`Math.random()` uses a pseudo-random number generator (PRNG) that is predictable. For security-sensitive tokens, you must use the cryptographically secure CSPRNG provided by `crypto.randomBytes()`."
)

add_mcq("mid-node-08", "node", "Unhandled Promise Rejections",
    "What happens in modern Node.js (v16+) when an unhandled Promise rejection occurs and no listener is attached?",
    [
        "A) The promise is automatically retried 3 times",
        "B) The Node.js process terminates immediately with a non-zero exit code",
        "C) The error is printed as a subtle warning and the process continues indefinitely",
        "D) Node.js rolls back all database queries"
    ],
    "B",
    "Starting in Node.js 15+, unhandled rejections terminate the Node process with exit code 1 (`--unhandled-rejections=throw`), preventing processes from running in unpredictable corrupted states."
)

add_mcq("mid-node-09", "node", "Buffer vs String Memory",
    "Why does reading a 500MB video file into a `Buffer` consume less overhead than reading it into a JavaScript `String`?",
    [
        "A) Strings in V8 are stored in UTF-16 (requiring up to 2 bytes per character) and are garbage collected within the V8 heap limits, whereas Buffers allocate raw binary memory outside the V8 heap",
        "B) Buffers use hardware compression",
        "C) Strings cannot exceed 10MB in V8",
        "D) Node.js automatically swaps Buffers to disk"
    ],
    "A",
    "Buffers are allocated directly in C++ memory outside the V8 JavaScript heap. Converting binary data to JavaScript strings incurs UTF-16 encoding expansion and stresses V8 garbage collection."
)

add_open("mid-node-10", "node", "Deep Dive into Node.js Event Loop",
    "Describe the 6 phases of the libuv Event Loop in Node.js in exact order. Explain where microtasks (`process.nextTick` and Promises) execute relative to these phases.",
    [
        "Order: 1. Timers -> 2. Pending I/O callbacks -> 3. Idle, prepare -> 4. Poll -> 5. Check -> 6. Close callbacks",
        "Timers: setTimeout, setInterval",
        "Poll: checks for I/O events, executes I/O callbacks",
        "Check: setImmediate callbacks",
        "Microtasks: process.nextTick and Promise callbacks execute between every phase transition and whenever the call stack clears"
    ],
    "The Node.js event loop runs via libuv across 6 distinct phases in each tick:\n1. Timers: Executes callbacks scheduled by `setTimeout()` and `setInterval()` whose thresholds have passed.\n2. Pending Callbacks: Executes I/O callbacks deferred from the previous iteration (e.g., system-level errors like ECONNREFUSED).\n3. Idle, Prepare: Internal libuv operations.\n4. Poll: Calculates how long to block and poll for I/O; retrieves and executes incoming I/O events (network, disk reads).\n5. Check: Executes `setImmediate()` callbacks immediately after the poll phase finishes.\n6. Close Callbacks: Executes close event handlers (e.g. `socket.on('close')`).\nMicrotask Priority: The `process.nextTick` queue and Promise microtask queue run immediately after the current operation finishes on the call stack and between transitions between each of these phases."
)

add_open("mid-node-11", "node", "Handling CPU-Intensive Tasks in Node.js",
    "Because Node.js runs on a single main thread, a synchronous heavy calculation (e.g., image resizing or complex hashing) blocks the event loop. Describe three architectural strategies to handle CPU-bound workloads in a Node.js backend without blocking HTTP traffic.",
    [
        "Worker Threads (worker_threads module): Run CPU-intensive JavaScript in parallel threads sharing memory (SharedArrayBuffer)",
        "Child Processes (child_process.fork / spawn): Offload to separate OS processes",
        "External Background Job Queue: Offload to Redis-backed queues (BullMQ, Celery, RabbitMQ) consumed by dedicated worker services",
        "Offloading to native C++ addons or microservices"
    ],
    "1. Worker Threads (`worker_threads`): Introduced to execute CPU-bound JavaScript concurrently in separate OS threads with isolated V8 engines, communicating via message passing or `SharedArrayBuffer` without blocking the main event loop.\n2. Child Processes (`child_process.fork()`): Spawns separate Node.js processes with dedicated memory spaces, utilizing IPC (Inter-Process Communication) to exchange tasks and results.\n3. Background Task Queues (e.g. BullMQ with Redis): Offload heavy operations to an asynchronous queue. The Express API immediately responds with an HTTP 202 Accepted and job ID, while dedicated worker instances process jobs off-thread."
)

# ==================== EXPRESS.JS (MID-LEVEL) ====================
add_mcq("mid-express-01", "express", "Helmet Middleware",
    "What security protections does the `helmet` middleware package provide for Express?",
    [
        "A) It stops SQL injections by escaping queries",
        "B) It automatically sets secure HTTP response headers (Content-Security-Policy, X-Frame-Options, Strict-Transport-Security, X-Content-Type-Options) to protect against common web vulnerabilities",
        "C) It encrypts the hard drive",
        "D) It generates SSL certificates"
    ],
    "B",
    "`helmet()` is a collection of middleware functions that set critical HTTP security headers, mitigating attacks like clickjacking (`X-Frame-Options`), MIME sniffing (`X-Content-Type-Options`), and enforcing HTTPS (`HSTS`)."
)

add_mcq("mid-express-02", "express", "Multer Storage Engines",
    "What is the difference between `multer.memoryStorage()` and `multer.diskStorage()`?",
    [
        "A) `memoryStorage` stores files in MongoDB; `diskStorage` stores them in PostgreSQL",
        "B) `memoryStorage` buffers the uploaded file in RAM as a Buffer, while `diskStorage` streams the file directly to the local filesystem",
        "C) `diskStorage` only works on Windows",
        "D) `memoryStorage` encrypts files with AES-256"
    ],
    "B",
    "`memoryStorage` is convenient when uploading directly to cloud storage (like AWS S3) via buffers, but large files can exhaust server RAM. `diskStorage` saves files to specified directories on disk, saving memory."
)

add_mcq("mid-express-03", "express", "express-rate-limit",
    "How does `express-rate-limit` help protect an Express authentication endpoint (e.g. `/api/auth/login`)?",
    [
        "A) It prevents invalid passwords from being submitted",
        "B) It limits repeated requests from the same IP within a defined timeframe, preventing brute-force password guessing and DoS floods",
        "C) It hides the server IP address behind Tor",
        "D) It verifies reCAPTCHA tokens automatically"
    ],
    "B",
    "Rate limiting caps the number of requests an IP address can make in a given time window (e.g. 5 attempts per 15 minutes for `/login`), defeating brute-force credential stuffing."
)

add_mcq("mid-express-04", "express", "Signed Cookies",
    "In Express using `cookie-parser('secret')`, what does a signed cookie provide?",
    [
        "A) Complete encryption so the client cannot see the contents",
        "B) Cryptographic HMAC signature verification to detect if the client tampered with or modified the cookie value",
        "C) Automatic renewal of expired cookies",
        "D) Prevention of cookie theft via XSS"
    ],
    "B",
    "Signed cookies are not encrypted (the user can still read the string), but they contain a cryptographic HMAC hash. If the user alters the cookie value, Express detects the signature mismatch and invalidates it."
)

add_mcq("mid-express-05", "express", "Async Error Handling in Express 4 vs 5",
    "In Express 4, what happens if an unhandled promise rejection occurs inside an `async (req, res)` handler without a try/catch or wrapper?",
    [
        "A) Express automatically catches the error and sends a 500 response",
        "B) The request hangs indefinitely until timeout, and Node emits an unhandledRejection event",
        "C) Express re-runs the route handler",
        "D) The server deletes the route"
    ],
    "B",
    "Express 4 does not automatically catch rejected promises in async middleware; errors must be passed via `next(err)`. (Express 5 natively catches rejected promises)."
)

add_mcq("mid-express-06", "express", "Content-Type Negotiation",
    "Which Express method allows a route handler to send different response formats (HTML, JSON, Text) based on the client's `Accept` HTTP header?",
    [
        "A) `res.send()`",
        "B) `res.format()`",
        "C) `res.negotiate()`",
        "D) `res.type()`"
    ],
    "B",
    "`res.format({ 'text/plain': ..., 'text/html': ..., 'application/json': ... })` performs content negotiation using the `Accept` request header."
)

add_open("mid-express-07", "express", "Role-Based Access Control (RBAC) Middleware",
    "Write an Express middleware function `authorize(...allowedRoles)` that checks whether an authenticated user has the necessary role (e.g. 'admin', 'editor') and returns a 403 status code if not.",
    [
        "Returns a middleware function (closure)",
        "Checks req.user and req.user.role",
        "Returns 401 if unauthenticated, 403 if role not included in allowedRoles",
        "Calls next() if role is valid"
    ],
    "```javascript\nexport const authorize = (...allowedRoles) => {\n  return (req, res, next) => {\n    if (!req.user) {\n      return res.status(401).json({ message: 'Authentication required' });\n    }\n    if (!allowedRoles.includes(req.user.role)) {\n      return res.status(403).json({\n        message: `Forbidden: Requires one of [${allowedRoles.join(', ')}] permissions`\n      });\n    }\n    next();\n  };\n};\n\n// Usage:\n// app.delete('/api/users/:id', authenticate, authorize('admin', 'superadmin'), deleteUserHandler);\n```"
)

add_open("mid-express-08", "express", "Request Validation with Schema Libraries (Zod / Joi)",
    "Explain why input validation should occur at the middleware boundary using libraries like Zod or Joi, and write a sample validation middleware for a user registration payload.",
    [
        "Validates req.body, req.query, or req.params before business logic executes",
        "Prevents SQL/NoSQL injection, unexpected types, and schema pollution",
        "Returns structured 400 Bad Request with field-specific validation errors"
    ],
    "Validating inputs at the middleware boundary ensures invalid or malicious payloads are rejected before reaching database queries or business controllers:\n```javascript\nimport { z } from 'zod';\n\nconst registerSchema = z.object({\n  email: z.string().email(),\n  password: z.string().min(8).regex(/[A-Z]/, 'Must contain uppercase letter'),\n  age: z.number().int().positive().optional()\n});\n\nexport const validate = (schema) => (req, res, next) => {\n  const result = schema.safeParse(req.body);\n  if (!result.success) {\n    return res.status(400).json({\n      error: 'Validation failed',\n      issues: result.error.errors.map(e => ({ field: e.path.join('.'), message: e.message }))\n    });\n  }\n  req.validatedBody = result.data;\n  next();\n};\n```"
)

# ==================== MONGODB & MONGOOSE (MID-LEVEL) ====================
add_mcq("mid-mongo-01", "mongodb", "Aggregation Pipeline Stages",
    "Which aggregation pipeline stage is used to perform an equality join with another collection in MongoDB?",
    [
        "A) `$join`",
        "B) `$lookup`",
        "C) `$merge`",
        "D) `$combine`"
    ],
    "B",
    "`$lookup` performs a left outer join to an unsharded collection in the same database, allowing you to pull matching documents into an array field."
)

add_mcq("mid-mongo-02", "mongodb", "Compound Indexes & ESR Rule",
    "What does the 'ESR Rule' stand for when ordering keys in a MongoDB compound index?",
    [
        "A) Execution, Sorting, Redundancy",
        "B) Equality, Sort, Range",
        "C) Embedded, Sharded, Replicated",
        "D) Expression, Structure, Record"
    ],
    "B",
    "The ESR rule specifies optimal compound index order: 1. Equality fields first (exact matches), 2. Sort fields second (determines sort order without in-memory sort), 3. Range fields last (filters with `$gt`, `$lt`)."
)

add_mcq("mid-mongo-03", "mongodb", "COLLSCAN vs IXSCAN",
    "In a MongoDB `explain('executionStats')` report, what does `COLLSCAN` signify and why is it problematic for large collections?",
    [
        "A) Collection Scan: MongoDB had to inspect every single document in the collection because no suitable index was available",
        "B) Collision Scan: Multiple documents shared the same hash key",
        "C) Compressed Scan: Data was read from disk cache",
        "D) Columnar Scan: Ultra-fast index reading"
    ],
    "A",
    "`COLLSCAN` means a full collection scan occurred. On a collection with millions of documents, this causes high disk I/O, CPU consumption, and slow response times. An `IXSCAN` (Index Scan) should be targeted instead."
)

add_mcq("mid-mongo-04", "mongodb", "TTL Indexes",
    "What is the function of a Time-To-Live (TTL) index in MongoDB?",
    [
        "A) It speeds up date comparisons by 50%",
        "B) It automatically deletes documents after a specified number of seconds based on a Date field value",
        "C) It logs the query execution duration",
        "D) It enforces session timeout in Express"
    ],
    "B",
    "TTL indexes are single-field indexes on date fields that MongoDB uses to automatically purge expired documents (e.g. sessions, verification codes, temporary logs) in the background."
)

add_mcq("mid-mongo-05", "mongodb", "Mongoose Pre/Post Hooks",
    "Why must you use a regular function instead of an arrow function when defining a Mongoose `pre('save')` middleware hook that hashes a password?",
    [
        "A) Arrow functions are not supported in Node.js",
        "B) Arrow functions lexically bind `this`, preventing Mongoose from binding `this` to the document instance being saved",
        "C) Mongoose throws a syntax error if arrow functions are used anywhere",
        "D) Regular functions execute asynchronously while arrow functions execute synchronously"
    ],
    "B",
    "Mongoose binds `this` to the document being validated/saved. Arrow functions inherit the enclosing lexical scope, causing `this` to be undefined or global scope."
)

add_mcq("mid-mongo-06", "mongodb", "Partial Indexes",
    "What is the advantage of a Partial Index in MongoDB?",
    [
        "A) It only indexes the first 5 characters of strings",
        "B) It only indexes documents that meet a specified filter expression (`filterExpression`), saving disk space and write overhead",
        "C) It splits the index across two servers",
        "D) It only indexes every second row"
    ],
    "B",
    "Partial indexes index only documents in a collection that satisfy a specified filter expression, reducing storage requirements and index maintenance overhead during document writes."
)

add_open("mid-mongo-07", "mongodb", "MongoDB Aggregation Pipeline",
    "Write a MongoDB aggregation pipeline that finds the top 5 highest-spending customers. Assume an `orders` collection with `{ customerId, amount, status }`. Explain each stage.",
    [
        "Stage 1: $match { status: 'completed' } to filter irrelevant orders early",
        "Stage 2: $group { _id: '$customerId', totalSpent: { $sum: '$amount' } }",
        "Stage 3: $sort { totalSpent: -1 }",
        "Stage 4: $limit 5"
    ],
    "```javascript\nawait db.orders.aggregate([\n  // 1. Filter completed orders first to minimize pipeline dataset\n  { $match: { status: 'completed' } },\n  \n  // 2. Group by customerId and sum order totals\n  {\n    $group: {\n      _id: '$customerId',\n      totalSpent: { $sum: '$amount' },\n      orderCount: { $sum: 1 }\n    }\n  },\n  \n  // 3. Sort by total expenditure in descending order\n  { $sort: { totalSpent: -1 } },\n  \n  // 4. Return top 5 records\n  { $limit: 5 },\n  \n  // 5. Optional: Project cleaner field names\n  {\n    $project: {\n      _id: 0,\n      customerId: '$_id',\n      totalSpent: 1,\n      orderCount: 1\n    }\n  }\n]);\n```"
)

add_open("mid-mongo-08", "mongodb", "Transactions in MongoDB",
    "How do multi-document transactions work in MongoDB? What prerequisites are required, and what is the code pattern for committing or aborting a session?",
    [
        "Prerequisite: Requires a Replica Set or Sharded Cluster (not standalone)",
        "Pattern: startSession(), session.startTransaction(), pass { session } to all operations",
        "Commit with session.commitTransaction(), abort with session.abortTransaction(), always endSession() in finally block"
    ],
    "MongoDB supports multi-document ACID transactions on replica sets and sharded clusters:\n```javascript\nconst session = await mongoose.startSession();\nsession.startTransaction();\ntry {\n  await Account.updateOne({ _id: fromId }, { $inc: { balance: -amount } }, { session });\n  await Account.updateOne({ _id: toId }, { $inc: { balance: amount } }, { session });\n  \n  await session.commitTransaction();\n} catch (error) {\n  await session.abortTransaction();\n  throw error;\n} finally {\n  session.endSession();\n}\n```\nAll operations must receive the `{ session }` option so they are tracked atomically."
)

# ==================== POSTGRESQL (MID-LEVEL) ====================
add_mcq("mid-pg-01", "postgresql", "Common Table Expressions (CTEs)",
    "What is the purpose of the `WITH` clause (Common Table Expression) in PostgreSQL?",
    [
        "A) To establish an SSL connection with a password",
        "B) To define a temporary named result set that exists only for the duration of a single query, improving readability and enabling recursive queries",
        "C) To create a permanent table on disk",
        "D) To add a user role to the database"
    ],
    "B",
    "CTEs provide modular, readable query structures by defining temporary named result sets. They can also perform hierarchical and graph traversals via `WITH RECURSIVE`."
)

add_mcq("mid-pg-02", "postgresql", "Transaction Isolation Levels",
    "What is a 'Non-Repeatable Read' and at which transaction isolation level is it prevented in PostgreSQL?",
    [
        "A) When a transaction reads uncommitted data; prevented in Read Uncommitted",
        "B) When a transaction re-reads a row and finds that another committed transaction modified its data; prevented in `REPEATABLE READ` and `SERIALIZABLE`",
        "C) When an index fails to read a row",
        "D) When two transactions write to the same table simultaneously"
    ],
    "B",
    "A Non-Repeatable Read occurs when a transaction reads the same row twice and observes different values because another transaction committed an update in between. `REPEATABLE READ` snapshots the data at transaction start, preventing this anomaly."
)

add_mcq("mid-pg-03", "postgresql", "GIN Indexes for JSONB",
    "Why are GIN (Generalized Inverted Index) indexes preferred over B-Tree indexes when querying keys or elements inside PostgreSQL `JSONB` columns?",
    [
        "A) B-Tree indexes cannot index JSONB at all",
        "B) GIN indexes store key/value pairs internally as inverted index entries, allowing fast containment queries (`@>`, `?`, `?&`) against arbitrary nested keys",
        "C) GIN indexes consume 90% less disk space than B-Trees",
        "D) GIN indexes automatically repair corrupt disks"
    ],
    "B",
    "A GIN index creates an inverted index mapping internal keys and values to row locations. This allows fast searches with the containment operator `@>`, whereas standard B-Tree indexes only index the entire JSON document as a scalar value."
)

add_mcq("mid-pg-04", "postgresql", "Window Functions",
    "What is the difference between a Window Function (e.g. `ROW_NUMBER() OVER (...)`) and a regular Aggregate Function with `GROUP BY`?",
    [
        "A) Window functions delete duplicate rows",
        "B) Window functions perform calculations across a set of table rows without collapsing the individual rows into a single summary output",
        "C) Window functions only run on Windows OS",
        "D) Aggregate functions cannot calculate sums"
    ],
    "B",
    "`GROUP BY` aggregates collapse multiple rows into a single output row. Window functions compute running totals, rankings, or moving averages while retaining each individual row in the output."
)

add_mcq("mid-pg-05", "postgresql", "Foreign Key Indexes",
    "Does PostgreSQL automatically create an index on child table columns defined with a FOREIGN KEY constraint?",
    [
        "A) Yes, PostgreSQL automatically creates a B-Tree index on all foreign keys",
        "B) No, PostgreSQL automatically creates indexes for PRIMARY KEY and UNIQUE constraints, but NOT for FOREIGN KEY constraints; developers must manually index foreign keys to prevent sequential scans during joins and deletes",
        "C) Foreign keys cannot be indexed",
        "D) Only if the column name ends with `_id`"
    ],
    "B",
    "PostgreSQL does NOT automatically index foreign key columns. If you frequently join on that column or delete records from the parent table, omitting an index on the foreign key can lead to slow full table scans."
)

add_mcq("mid-pg-06", "postgresql", "Database Connection Pool Tuning",
    "What is the formula guideline popularized by PostgreSQL developers for calculating optimal connection pool size: `connections = ((core_count * 2) + effective_spindle_count)`?",
    [
        "A) To demonstrate that opening thousands of concurrent DB connections improves speed",
        "B) To prevent context-switching thrashing and memory exhaustion by proving that a small pool of active connections matching CPU cores delivers highest throughput",
        "C) It applies only to USB flash drives",
        "D) To limit connections to 5 for all servers"
    ],
    "B",
    "Contrary to intuition, allowing thousands of concurrent PostgreSQL connections causes CPU context-switching thrashing, cache eviction, and lock contention. A smaller, well-tuned pool delivers significantly higher query throughput."
)

add_open("mid-pg-07", "postgresql", "Query Optimization with EXPLAIN ANALYZE",
    "What information does `EXPLAIN ANALYZE` provide in PostgreSQL, and how do you identify a performance bottleneck (such as an unintentional sequential scan or disk spill)?",
    [
        "EXPLAIN shows the planner cost estimate; ANALYZE actually executes the query and shows real runtime, loops, and row counts",
        "Bottleneck signs: Seq Scan on large table (missing index), high execution time vs planning time, Rows Removed by Filter, Sort Method: external merge disk (work_mem too low)"
    ],
    "`EXPLAIN ANALYZE` executes the SQL statement and reports real execution statistics alongside the query planner's estimates:\n1. Execution Plan: Breaks down node operations (Seq Scan, Index Scan, Bitmap Heap Scan, Nested Loop, Hash Join).\n2. Critical Indicators:\n- `Seq Scan`: Inspect if a large table is scanned sequentially; indicates a missing index on the `WHERE` or `JOIN` column.\n- `Rows Removed by Filter`: If millions of rows were scanned only to discard 99.9% of them, an index is urgently needed.\n- `Sort Method: external merge Disk`: Indicates the sort operation exceeded `work_mem` and spilled to disk, severely slowing down the query.\n- Discrepancy between `cost` estimate rows and `actual rows`: Indicates outdated table statistics; resolved by running `ANALYZE table_name`."
)

add_open("mid-pg-08", "postgresql", "PostgreSQL ACID Isolation Levels & Anomalies",
    "Contrast the four SQL standard isolation levels: Read Uncommitted, Read Committed, Repeatable Read, and Serializable. What anomalies (Dirty Read, Non-Repeatable Read, Phantom Read, Serialization Anomaly) can occur in each?",
    [
        "PostgreSQL treats Read Uncommitted as Read Committed (dirty reads are impossible in Postgres due to MVCC)",
        "Read Committed: Default; prevents dirty reads, allows non-repeatable reads and phantom reads",
        "Repeatable Read: Prevents dirty reads and non-repeatable reads; prevents phantom reads in PostgreSQL",
        "Serializable: Guarantees serializable execution; prevents serialization anomalies (e.g. write skew) via predicate locks (SSI)"
    ],
    "1. Read Uncommitted: In standard SQL, allows dirty reads. However, in PostgreSQL, it behaves identically to Read Committed because PostgreSQL's MVCC architecture never reads uncommitted tuples.\n2. Read Committed (PostgreSQL Default): Each query in a transaction sees a snapshot of committed data at the moment that specific query begins. Prevents Dirty Reads, but allows Non-Repeatable Reads.\n3. Repeatable Read: The entire transaction sees a snapshot taken when the first query in the transaction began. Prevents Dirty Reads, Non-Repeatable Reads, and Phantom Reads.\n4. Serializable: The strictest level. Simulates serial transaction execution using Serializable Snapshot Isolation (SSI) to prevent Serialization Anomalies (such as Write Skew), aborting conflicting transactions with a retry error."
)

# ==================== FULLSTACK / SECURITY / ARCHITECTURE (MID-LEVEL) ====================
add_mcq("mid-full-01", "fullstack", "CSRF Protection",
    "How does the `SameSite=Strict` cookie attribute help defend against Cross-Site Request Forgery (CSRF)?",
    [
        "A) It prevents the cookie from being accessed over HTTP",
        "B) It instructs the browser never to send the cookie in cross-site requests (e.g. following a link or submitting a form from an external domain)",
        "C) It encrypts the user's password using AES-GCM",
        "D) It only sends cookies if the user has completed a CAPTCHA"
    ],
    "B",
    "With `SameSite=Strict`, the browser will not send the cookie along with cross-site requests initiated by third-party origins, preventing attackers from forging authenticated requests on behalf of victims."
)

add_mcq("mid-full-02", "fullstack", "Redis Cache-Aside Pattern",
    "How does the 'Cache-Aside' (Lazy Loading) caching pattern work with Redis in a PERN/MERN application?",
    [
        "A) Redis automatically executes SQL queries and caches all tables",
        "B) The application first checks Redis for the data; on cache hit, it returns immediately; on cache miss, it queries the database, writes the result to Redis with a TTL, and returns",
        "C) All writes go only to Redis; the database is never updated",
        "D) Data is written to Redis only when the server restarts"
    ],
    "B",
    "In the Cache-Aside pattern, the application orchestrates reads: check cache -> if miss, read database -> populate cache with TTL -> return to client. This ensures only frequently requested data consumes cache RAM."
)

add_mcq("mid-full-03", "fullstack", "Cursor-Based vs Offset Pagination",
    "Why is cursor-based pagination superior to `OFFSET / LIMIT` pagination for large, continuously updating feeds?",
    [
        "A) Cursor-based pagination works without a database",
        "B) `OFFSET` requires the database to scan and discard all preceding offset rows (O(N) cost), and causes duplicate or skipped records when items are inserted concurrently",
        "C) Offset pagination cannot sort ascending",
        "D) Browsers do not support offset numbers higher than 1000"
    ],
    "B",
    "`OFFSET 100000` forces the database engine to fetch and count 100,000 rows only to discard them. Cursor pagination filters by index (`WHERE id < last_seen_id ORDER BY id DESC LIMIT 20`), which is O(1) indexed lookup and immune to page-drift anomalies."
)

add_mcq("mid-full-04", "fullstack", "WebSockets vs Server-Sent Events",
    "When is Server-Sent Events (SSE) a simpler and better choice than WebSockets for a PERN/MERN app?",
    [
        "A) When you need full-duplex two-way communication like an online multiplayer game",
        "B) When the communication is strictly unidirectional from server to client (e.g. live notifications, stock tickers, AI text streaming) over standard HTTP",
        "C) When binary data must be transferred over UDP",
        "D) When clients are offline"
    ],
    "B",
    "SSE runs over standard HTTP, natively supports automatic reconnection and event IDs, bypasses corporate firewalls easily, and is ideal when data only flows from server to client (like LLM token streaming)."
)

add_mcq("mid-full-05", "fullstack", "Docker Multi-Stage Builds",
    "What is the primary benefit of using multi-stage builds in a Dockerfile for a React or Node.js application?",
    [
        "A) It allows running multiple Linux distributions on the same CPU",
        "B) It separates the build environment (Node, npm dependencies, compilers) from the slim production runtime image (e.g. Nginx or alpine), resulting in dramatically smaller and more secure images",
        "C) It bypasses Docker licensing requirements",
        "D) It increases the RAM limit of Docker containers"
    ],
    "B",
    "Multi-stage builds leave behind development tools, npm devDependencies, and intermediate build artifacts in the builder stage, copying only production assets into the final runtime container."
)

add_open("mid-full-06", "fullstack", "Designing a Scalable Auth System (JWT Refresh Token Rotation)",
    "Explain how Refresh Token Rotation works in an authentication architecture. How does it mitigate the threat of stolen refresh tokens, and where should tokens be stored?",
    [
        "Access tokens have short lifespan (e.g. 15 minutes) and are stored in memory",
        "Refresh tokens have longer lifespan (e.g. 7 days) and are stored in HttpOnly, Secure, SameSite cookies",
        "Token Rotation: Whenever a refresh token is used to issue a new access token, the old refresh token is invalidated and a new one is issued",
        "Breach detection: If an invalidated refresh token is reused, all refresh tokens for that family/user are immediately revoked (reuse detection)"
    ],
    "1. Token Lifetimes: Access Tokens are short-lived (10-15 minutes) to minimize damage if intercepted. Refresh Tokens are long-lived (7-30 days).\n2. Storage: Refresh tokens are stored in `HttpOnly`, `Secure`, `SameSite=Strict` cookies to block XSS and CSRF.\n3. Rotation: When `/api/auth/refresh` is called, the server validates the refresh token, revokes it in the database/Redis, and issues both a new access token and a brand-new refresh token.\n4. Automatic Breach Detection: If an attacker steals a refresh token and uses it after the legitimate user has already rotated it, the server detects reuse of an invalidated token. It immediately invalidates the entire token family, logging out the user across all devices and neutralizing the compromised session."
)

with open("/workspaces/preppro/src/data/mid.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Generated {len(questions)} Mid-Level questions in /workspaces/preppro/src/data/mid.json")
