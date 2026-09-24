#!/usr/bin/env python3
import json

questions = []

def add_mcq(qid, stack, topic, question, options, answer, explanation):
    questions.append({
        "id": qid,
        "level": "junior",
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
        "level": "junior",
        "stack": stack,
        "type": "open",
        "topic": topic,
        "question": question,
        "expectedKeyPoints": expected_key_points,
        "sampleAnswer": sample_answer
    })

# ==================== REACT (JUNIOR) ====================
add_mcq("jr-react-01", "react", "JSX Basics",
    "In React, why can a component only return a single root JSX element (or a Fragment)?",
    [
        "A) Because HTML5 prohibits multiple top-level elements",
        "B) Because JSX transpires to React.createElement, which is a JavaScript function call that can only return one value",
        "C) Because the browser DOM tree engine crashes if two elements are mounted at once",
        "D) Because CSS flexbox requires a single parent element to apply layout rules"
    ],
    "B",
    "JSX compiles down to JavaScript function calls (React.createElement or jsx() runtime). In JavaScript, a function cannot return two separate values without wrapping them in an object, array, or parent element (like React.Fragment)."
)

add_mcq("jr-react-02", "react", "useState Hook",
    "What happens when you call the setState setter function returned by useState?",
    [
        "A) The browser immediately refreshes the entire HTML page",
        "B) React directly mutates the existing DOM element synchronously",
        "C) React schedules a re-render of the component with the new state value",
        "D) The state variable is stored in localStorage automatically"
    ],
    "C",
    "Calling a state setter schedules a re-render so React can compute differences via its virtual DOM diffing process."
)

add_mcq("jr-react-03", "react", "Props vs State",
    "What is the primary difference between props and state in React?",
    [
        "A) Props are mutable and managed locally, while state is read-only and passed from parents",
        "B) Props are read-only inputs passed from parent to child, while state is internal mutable data managed by the component",
        "C) Props are stored in the database, while state is stored in Redux",
        "D) Props can only hold strings, while state can hold any data type"
    ],
    "B",
    "Props are external parameters passed down the component hierarchy and must remain immutable from the child's perspective, whereas state is local data managed by the component itself."
)

add_mcq("jr-react-04", "react", "List Keys",
    "Why should you avoid using array indices as the 'key' prop when rendering dynamic lists in React?",
    [
        "A) React throws a fatal compile error if index is used as a key",
        "B) Using array indices can lead to incorrect component state and rendering bugs when items are reordered, inserted, or deleted",
        "C) Array indices take up 4x more RAM in the browser memory heap",
        "D) Browsers do not support integer keys in HTML elements"
    ],
    "B",
    "React uses keys to identify which items have changed, been added, or been removed. If items are reordered or filtered, an index key causes React to mismatch state between different list elements."
)

add_mcq("jr-react-05", "react", "useEffect Hook",
    "When does a useEffect hook with an empty dependency array `[]` run?",
    [
        "A) Before every single render cycle",
        "B) Only once after the component mounts for the first time",
        "C) Every time any state in the entire application changes",
        "D) Only when the component unmounts"
    ],
    "B",
    "An empty dependency array `[]` instructs React that the effect does not depend on any props or state, so it executes only once after the initial render (mount)."
)

add_mcq("jr-react-06", "react", "useEffect Cleanup",
    "How do you define a cleanup mechanism in a React useEffect hook?",
    [
        "A) By calling window.cleanup() inside the effect body",
        "B) By adding a second callback argument to useEffect",
        "C) By returning a cleanup function from the effect callback",
        "D) By using the unmountComponentAtNode() API"
    ],
    "C",
    "React executes the function returned by the useEffect callback before running the effect again on updates and when the component unmounts, allowing timers, subscriptions, or listeners to be cleaned up."
)

add_mcq("jr-react-07", "react", "Controlled Components",
    "What is a 'controlled component' in React form handling?",
    [
        "A) A component that can only be rendered by an administrator",
        "B) An input element whose value is driven by React component state via value and onChange props",
        "C) A component that controls the browser window's URL path",
        "D) An input element controlled entirely by DOM querySelectors"
    ],
    "B",
    "In a controlled component, the form element's current value is bound to React state, and changes are handled by event listeners that update that state, making React the single source of truth."
)

add_mcq("jr-react-08", "react", "Virtual DOM",
    "What is the Virtual DOM and what is its primary benefit?",
    [
        "A) A hardware-accelerated 3D graphics rendering engine for React VR",
        "B) A lightweight in-memory JavaScript representation of the real DOM that enables batching and minimal real DOM mutations",
        "C) A shadow copy of MongoDB documents cached in the browser",
        "D) A browser plugin required to run JSX code in Chrome"
    ],
    "B",
    "The Virtual DOM is an in-memory object tree. React compares (diffs) the new Virtual DOM with the previous one and computes the minimal set of real DOM operations required, avoiding expensive layout reflows."
)

add_mcq("jr-react-09", "react", "Conditional Rendering",
    "In React, what will `count && <span>Items: {count}</span>` render if `count === 0`?",
    [
        "A) Nothing (null)",
        "B) The number 0 rendered directly to the screen",
        "C) An error: Uncaught TypeError: 0 is not valid JSX",
        "D) <span>Items: 0</span>"
    ],
    "B",
    "In JavaScript, `0 && ...` evaluates to `0`. Since numbers are valid renderable values in JSX, React renders the literal character `0` instead of hiding the element. The safe pattern is `count > 0 && ...` or a ternary."
)

add_mcq("jr-react-10", "react", "State Immutability",
    "Why should you never mutate state directly, e.g. `items.push(newItem)` in React?",
    [
        "A) JavaScript throws a frozen object exception in strict mode",
        "B) React uses shallow reference equality checks (Object.is) to detect changes, so mutating existing references won't trigger re-renders",
        "C) React converts all arrays into binary buffers that cannot be pushed to",
        "D) Directly mutating arrays causes an immediate memory leak in V8"
    ],
    "B",
    "React compares state references. If you mutate an existing array or object in place, the memory reference remains identical, so React assumes nothing changed and skips re-rendering."
)

add_mcq("jr-react-11", "react", "Event Handling",
    "How are DOM events named in React JSX compared to native HTML?",
    [
        "A) React uses kebab-case like `on-click`, while HTML uses camelCase",
        "B) React uses camelCase like `onClick`, while HTML uses all lowercase like `onclick`",
        "C) React uses UPPERCASE like `ONCLICK`, while HTML uses lowercase",
        "D) React uses snake_case like `on_click`"
    ],
    "B",
    "React event handlers follow standard camelCase naming conventions (`onClick`, `onChange`, `onSubmit`) and accept function references rather than strings."
)

add_mcq("jr-react-12", "react", "Fragments",
    "What is the primary advantage of using `<React.Fragment>` or `<>...</>` syntax?",
    [
        "A) It compresses image assets during rendering",
        "B) It groups a list of children without adding extra wrapper nodes to the DOM",
        "C) It encrypts child components for secure transmission",
        "D) It converts children into HTML canvas elements"
    ],
    "B",
    "Fragments allow you to return multiple child elements without introducing redundant wrapper `<div>` tags that can break CSS flexbox, grid, or semantic HTML structures."
)

add_mcq("jr-react-13", "react", "Lifting State Up",
    "What does 'lifting state up' mean in React?",
    [
        "A) Uploading component state to an AWS S3 bucket",
        "B) Moving state to the closest common parent component so multiple child components can share it",
        "C) Converting a functional component into a Redux store",
        "D) Raising state variables to global window scope"
    ],
    "B",
    "When two or more sibling components need access to the same state data, the standard React pattern is to lift that state up into their closest common ancestor and pass it down as props."
)

add_mcq("jr-react-14", "react", "Functional vs Class Components",
    "Which of the following is true regarding Modern React functional components vs Class components?",
    [
        "A) Class components are faster because they don't use hooks",
        "B) Functional components with hooks are the modern standard and avoid complexities like `this` binding",
        "C) Functional components cannot hold state or manage side effects",
        "D) Class components are required when fetching data from REST APIs"
    ],
    "B",
    "Functional components combined with React Hooks are the official, modern standard in React. They eliminate `this` context binding pitfalls and simplify code sharing."
)

add_mcq("jr-react-15", "react", "Children Prop",
    "What is the special `children` prop in React?",
    [
        "A) A reference to the child processes running in Node.js",
        "B) A built-in prop that represents whatever elements or components are passed between the opening and closing JSX tags",
        "C) An array of SQL child records",
        "D) A hook that generates random child IDs"
    ],
    "B",
    "`props.children` allows components to be composed flexibly by rendering whatever content is passed inside their JSX wrapper tag."
)

add_mcq("jr-react-16", "react", "State Updates Batching",
    "In React 18+, how does automatic state batching work?",
    [
        "A) Only state updates inside React event handlers are batched",
        "B) State updates inside promises, setTimeout, and native event handlers are all automatically batched into a single re-render",
        "C) Batching is disabled by default and requires unstable_batchedUpdates()",
        "D) Batching only works for string state variables"
    ],
    "B",
    "React 18 introduced universal automatic batching across all asynchronous boundaries, including setTimeout, promises, and native event listeners, minimizing unnecessary re-renders."
)

add_mcq("jr-react-17", "react", "useRef Basics",
    "What is the primary characteristic of a value stored in a `useRef` hook?",
    [
        "A) Changing its `.current` value triggers an immediate re-render",
        "B) It persists across renders without causing a re-render when mutated",
        "C) It automatically syncs with localStorage",
        "D) It can only hold references to HTML `<button>` elements"
    ],
    "B",
    "`useRef` returns a mutable object whose `.current` property persists for the lifetime of the component. Changing `.current` does not trigger a re-render."
)

add_mcq("jr-react-18", "react", "React Router Basics",
    "In `react-router-dom` v6, which component is used to define individual route paths and corresponding element components?",
    [
        "A) `<Switch>` and `<Route component={...}>`",
        "B) `<Routes>` and `<Route path='...' element={<Component />} />`",
        "C) `<Router>` and `<Path to='...'>`",
        "D) `<Navigator>` and `<Screen>`"
    ],
    "B",
    "In React Router v6, `<Routes>` replaces `<Switch>`, and the `<Route>` component accepts `path` and `element={<Component />}` props."
)

add_open("jr-react-19", "react", "React Component Lifecycle with Hooks",
    "Explain how the three primary lifecycle stages of a component (mounting, updating, and unmounting) are handled using the `useEffect` hook in functional React components. Provide brief code examples.",
    [
        "Mounting: useEffect with empty dependency array [] runs once after initial render",
        "Updating: useEffect with specific dependencies [prop1, state1] runs when those values change",
        "Unmounting: returning a cleanup function return () => { ... } from useEffect",
        "No dependencies: useEffect(() => {}) runs on every single render"
    ],
    "In React functional components, `useEffect` unifies the component lifecycle:\n1. Mounting: Pass an empty dependency array `useEffect(() => { ... }, [])`. This runs once after the component mounts.\n2. Updating: Pass specific variables in the dependencies `useEffect(() => { ... }, [count])`. This runs whenever `count` changes.\n3. Unmounting: Return a cleanup function from inside the effect callback: `useEffect(() => { return () => { cleanup(); }; }, [])`. React calls this function when the component unmounts.\nWithout any dependency array, the effect executes after every render cycle."
)

add_open("jr-react-20", "react", "Rules of Hooks",
    "What are the two golden 'Rules of Hooks' in React, and why do these constraints exist?",
    [
        "Only call Hooks at the top level (never inside loops, conditions, or nested functions)",
        "Only call Hooks from React function components or custom Hooks",
        "React relies on the order in which Hooks are called across renders to maintain internal state pointers"
    ],
    "The two primary rules of hooks are:\n1. Only call Hooks at the top level: Do not call hooks inside loops, conditionals, or nested functions.\n2. Only call Hooks from React function components or custom hooks: Do not call them from regular JavaScript functions or class components.\nThese rules exist because React keeps track of hook state internally using an array or linked list indexed by call order. If a hook call is skipped due to an `if` condition, the order shifts, causing subsequent hooks to receive the wrong state values."
)

add_open("jr-react-21", "react", "Props Drilling and Solutions",
    "What is 'prop drilling' in React, what problems does it cause, and what are two common solutions to avoid it?",
    [
        "Definition: Passing props through multiple layers of intermediate components that do not need them",
        "Drawbacks: Boilerplate, tight coupling, fragile refactoring",
        "Solutions: React Context API, Component Composition (passing children / slots), State management libraries (Zustand, Redux)"
    ],
    "Prop drilling occurs when you have to pass data through multiple intermediate components in the tree that have no need for the data themselves, just to reach a deeply nested child.\nProblems: It creates tight coupling, adds boilerplate, and makes refactoring painful.\nSolutions:\n1. React Context API: Allows broadcasting state directly to any consuming component in the subtree without manual prop forwarding.\n2. Component Composition: Passing JSX components as `children` or props directly to the parent container.\n3. State Management Libraries: Tools like Zustand or Redux Toolkit."
)

add_open("jr-react-22", "react", "Controlled vs Uncontrolled Forms",
    "Compare Controlled and Uncontrolled inputs in React. When would you use each, and how do you access the value of an uncontrolled input?",
    [
        "Controlled: input value is bound to React state and updated via onChange",
        "Uncontrolled: input maintains its own internal DOM state; accessed via useRef()",
        "Use cases: Controlled for real-time validation, dynamic disabling, or synced fields; Uncontrolled for simple forms, file inputs, or performance"
    ],
    "In a Controlled input, the value is managed entirely by React state via `value={state}` and `onChange={(e) => setState(e.target.value)}`. Every keystroke updates React state.\nIn an Uncontrolled input, the DOM retains internal control over the input. React accesses its value imperatively using a `ref` (e.g., `inputRef.current.value`).\nUse controlled inputs when you need instant input validation, formatting (like credit cards), or conditional submit button enabling. Use uncontrolled inputs for file inputs (`<input type='file'>`) or simple, unvalidated submit forms where minimal re-renders are desired."
)

# ==================== NODE.JS (JUNIOR) ====================
add_mcq("jr-node-01", "node", "Node.js Runtime Basics",
    "What is Node.js primarily built upon?",
    [
        "A) The SpiderMonkey JavaScript engine and Apache HTTP server",
        "B) Google Chrome's V8 JavaScript engine and the libuv C library",
        "C) The Java Virtual Machine (JVM) and Python asyncio",
        "D) Microsoft Chakra engine and Nginx"
    ],
    "B",
    "Node.js is an open-source, cross-platform JavaScript runtime environment built on Google Chrome's V8 JavaScript engine and libuv for handling asynchronous I/O operations."
)

add_mcq("jr-node-02", "node", "Single-Threaded Model",
    "If Node.js is described as 'single-threaded', how does it handle non-blocking asynchronous I/O?",
    [
        "A) It executes all JavaScript code across 16 operating system threads simultaneously",
        "B) The main thread runs the JavaScript event loop, while heavy I/O tasks are delegated to libuv's thread pool and OS kernel mechanisms",
        "C) It pauses the user's CPU until the network response arrives",
        "D) It compiles JavaScript directly into GPU shaders"
    ],
    "B",
    "JavaScript execution in Node.js runs on a single main thread. However, libuv delegates asynchronous I/O (file system, DNS, cryptography, network) to OS asynchronous system calls (epoll, kqueue) and an internal C thread pool."
)

add_mcq("jr-node-03", "node", "Module Systems",
    "What is the difference in import syntax between CommonJS and ES Modules (ESM) in Node.js?",
    [
        "A) CommonJS uses `require()` and `module.exports`, while ESM uses `import` and `export`",
        "B) CommonJS uses `fetch()`, while ESM uses `include()`",
        "C) ESM can only import JSON files, while CommonJS can import anything",
        "D) CommonJS was created by WHATWG, while ESM is proprietary to Node.js"
    ],
    "A",
    "CommonJS is the legacy Node.js module system (`const mod = require('./mod')`, `module.exports = ...`), whereas ES Modules (`import mod from './mod.js'`, `export default ...`) is the standardized ECMAScript module specification."
)

add_mcq("jr-node-04", "node", "package.json dependencies",
    "What is the purpose of `devDependencies` in `package.json`?",
    [
        "A) Packages that run only when the server is deployed to AWS production",
        "B) Packages needed only during local development and testing (e.g. linters, test runners), omitted in production builds",
        "C) Packages that cannot contain JavaScript code",
        "D) Private NPM modules that require paid subscriptions"
    ],
    "B",
    "`devDependencies` are packages required during local development, testing, and building (like Jest, ESLint, TypeScript, Nodemon). They are excluded when running `npm install --omit=dev` in production environments."
)

add_mcq("jr-node-05", "node", "Event Loop Basics",
    "In what order will the following code log to the console?\n```js\nconsole.log('1');\nsetTimeout(() => console.log('2'), 0);\nPromise.resolve().then(() => console.log('3'));\nconsole.log('4');\n```",
    [
        "A) 1, 2, 3, 4",
        "B) 1, 4, 2, 3",
        "C) 1, 4, 3, 2",
        "D) 4, 3, 2, 1"
    ],
    "C",
    "Synchronous code executes first ('1', '4'). Next, the microtask queue (Promises) drains before the macrotask/timer queue, logging '3'. Finally, the timer callback executes, logging '2'."
)

add_mcq("jr-node-06", "node", "Error Handling in Callbacks",
    "What is the standard 'error-first callback' convention in Node.js?",
    [
        "A) The callback returns true if an error happened",
        "B) The first parameter of the callback is reserved for an error object (or null if successful), followed by data arguments",
        "C) Errors are automatically thrown to process.exit(1)",
        "D) Callbacks must always be wrapped in a try/catch block by the caller"
    ],
    "B",
    "In standard Node.js callback signatures `(err, result) => { ... }`, the first argument is always the error object (or null/undefined if the operation succeeded), followed by the result payload."
)

add_mcq("jr-node-07", "node", "File System (fs)",
    "Why is using `fs.readFileSync` generally discouraged in production Node.js web servers?",
    [
        "A) It is deprecated and removed in Node 20+",
        "B) It blocks the single main thread, preventing the server from handling incoming HTTP requests until the file finishes reading",
        "C) It cannot read files larger than 1 Kilobyte",
        "D) It causes an immediate memory corruption in Linux"
    ],
    "B",
    "Synchronous file operations block the entire Node.js event loop. While `readFileSync` executes, no other I/O, timers, or network requests can be processed by the server."
)

add_mcq("jr-node-08", "node", "Path Module",
    "Why should you use `path.join(__dirname, 'files', 'data.json')` instead of string concatenation like `__dirname + '/files/data.json'`?",
    [
        "A) String concatenation is not valid JavaScript syntax in Node.js",
        "B) `path.join` automatically handles cross-platform path separators (forward slashes on POSIX vs backslashes on Windows)",
        "C) String concatenation bypasses file permissions",
        "D) `path.join` encrypts the file path"
    ],
    "B",
    "Windows uses `\\` as directory separators, while macOS and Linux use `/`. `path.join` normalizes separators and handles trailing/leading slashes and `..` segments reliably across all platforms."
)

add_mcq("jr-node-09", "node", "Environment Variables",
    "How do you access environment variables in a standard Node.js application?",
    [
        "A) window.env.VARIABLE_NAME",
        "B) process.env.VARIABLE_NAME",
        "C) global.environment.VARIABLE_NAME",
        "D) system.getEnv('VARIABLE_NAME')"
    ],
    "B",
    "In Node.js, environment variables passed to the process (or loaded via tools like `dotenv`) are accessible on the global `process.env` object."
)

add_mcq("jr-node-10", "node", "package-lock.json",
    "What is the primary function of `package-lock.json`?",
    [
        "A) To lock down your repository so unauthorized users cannot clone it",
        "B) To lock down the exact dependency tree version numbers and cryptographic hashes so builds are deterministic across machines",
        "C) To prevent developers from installing new packages without an admin password",
        "D) To store encrypted API keys"
    ],
    "B",
    "`package-lock.json` guarantees reproducible and deterministic dependency installations across different environments (CI/CD, staging, production) by locking exact versions and checksums."
)

add_mcq("jr-node-11", "node", "Global Objects",
    "Which of the following is NOT a global object in Node.js?",
    [
        "A) process",
        "B) Buffer",
        "C) window",
        "D) __dirname (in CommonJS)"
    ],
    "C",
    "`window` is a browser DOM window global object and does not exist in the Node.js runtime environment (where `global` or `globalThis` is used instead)."
)

add_mcq("jr-node-12", "node", "Buffer Basics",
    "What is a `Buffer` in Node.js?",
    [
        "A) A temporary video cache for HTML5 video players",
        "B) A global class designed to handle raw binary data directly in memory outside the V8 heap",
        "C) An Express middleware that throttles slow clients",
        "D) A tool for compiling TypeScript into JavaScript"
    ],
    "B",
    "Buffers are used in Node.js to represent fixed-length sequences of raw bytes, essential when working with TCP streams, file system I/O, and binary protocols."
)

add_mcq("jr-node-13", "node", "EventEmitter Basics",
    "Which built-in core module provides the `EventEmitter` class in Node.js?",
    [
        "A) 'events'",
        "B) 'emitter'",
        "C) 'stream'",
        "D) 'net'"
    ],
    "A",
    "The core `events` module exports the `EventEmitter` class, which is fundamental to Node's event-driven architecture."
)

add_mcq("jr-node-14", "node", "process.exit",
    "What does calling `process.exit(1)` do in Node.js?",
    [
        "A) Gracefully pauses execution for 1 second",
        "B) Terminates the Node.js process immediately with an error exit status code",
        "C) Restarts the server with PID 1",
        "D) Dumps the database cache to disk"
    ],
    "B",
    "A non-zero exit code (such as 1) signifies that the process terminated with an error, whereas `process.exit(0)` indicates a clean, successful exit."
)

add_mcq("jr-node-15", "node", "NPM Scripts",
    "In package.json, which command can be executed with `npm <name>` without having to type `npm run <name>`?",
    [
        "A) build",
        "B) test",
        "C) lint",
        "D) deploy"
    ],
    "B",
    "`npm test`, `npm start`, and `npm stop` are built-in aliases that do not require typing the `run` keyword, whereas custom scripts like `npm run lint` do."
)

add_mcq("jr-node-16", "node", "SemVer Basics",
    "Given version `^2.4.1` in package.json, which version updates will `npm install` accept?",
    [
        "A) Only exact version 2.4.1",
        "B) Any minor or patch version up to but not including version 3.0.0 (e.g. 2.4.2, 2.5.0)",
        "C) Any major version including 3.0.0 and 4.0.0",
        "D) Only patch updates like 2.4.2"
    ],
    "B",
    "The caret `^` allows updates that do not modify the left-most non-zero digit in the [major, minor, patch] tuple, meaning `^2.4.1` allows `>=2.4.1 <3.0.0`."
)

add_open("jr-node-17", "node", "Synchronous vs Asynchronous I/O",
    "Explain the difference between synchronous (blocking) and asynchronous (non-blocking) operations in Node.js. Why is asynchronous programming critical for web servers?",
    [
        "Synchronous operations block the single JavaScript thread; nothing else can run",
        "Asynchronous operations offload I/O to libuv/OS and resume via callback/Promise when ready",
        "Web servers must handle hundreds or thousands of concurrent user requests without stalling"
    ],
    "Synchronous operations halt the execution of code until the task completes. In Node's single-threaded event loop, a synchronous file read or heavy computation prevents all other users from being served, destroying throughput.\nAsynchronous operations trigger an I/O task and register a callback or Promise. The main thread immediately continues handling other incoming HTTP requests. When the I/O operation finishes, the event loop picks up the callback and sends the response. This enables Node.js to achieve high concurrency on limited hardware."
)

add_open("jr-node-18", "node", "Callbacks vs Promises vs Async/Await",
    "Describe the evolution of handling asynchronous code in Node.js from Callbacks to Promises and Async/Await. What problems did each iteration solve?",
    [
        "Callbacks: Original approach, led to 'Callback Hell' / Pyramid of Doom and difficult error handling",
        "Promises: Provided .then() chaining, centralized .catch() error propagation, and composability (Promise.all)",
        "Async/Await: Syntactic sugar over Promises allowing asynchronous code to be read and written like synchronous code with try/catch"
    ],
    "1. Callbacks: The earliest model where asynchronous functions accepted a callback `(err, data) => {}`. Nesting multiple dependent operations resulted in 'Callback Hell', deeply indented code, and repetitive error checks.\n2. Promises: Introduced objects representing future values with states (pending, fulfilled, rejected). Allowed chaining `.then()` and centralized error handling via `.catch()`, solving nesting issues.\n3. Async/Await: Introduced in ES2017 as syntactic sugar over Promises. Marked with `async` and `await`, it allows developers to write asynchronous code that looks and behaves like clean, linear synchronous code, using standard `try/catch` blocks."
)

add_open("jr-node-19", "node", "Node.js Event Loop Phases Overview",
    "Give a high-level overview of what the Node.js Event Loop does and list at least three of its key phases.",
    [
        "Event loop continuously checks queues and executes callbacks when the call stack is empty",
        "Timers phase: executes callbacks scheduled by setTimeout and setInterval",
        "Poll phase: retrieves new I/O events and executes I/O related callbacks",
        "Check phase: executes setImmediate callbacks"
    ],
    "The Event Loop is the orchestration engine that allows Node.js to perform non-blocking I/O operations despite JavaScript running on a single thread. When synchronous code finishes executing on the call stack, the event loop cycles through distinct phases:\n1. Timers Phase: Executes callbacks scheduled by `setTimeout()` and `setInterval()`.\n2. Pending Callbacks: Executes I/O callbacks deferred to the next loop iteration.\n3. Poll Phase: Retrieves new I/O events (network connections, data reads) and executes their callbacks.\n4. Check Phase: Executes callbacks scheduled by `setImmediate()`.\n5. Close Callbacks: Executes cleanup callbacks like `socket.on('close')`."
)

add_open("jr-node-20", "node", "CommonJS vs ES Modules",
    "Compare CommonJS and ES Modules in Node.js. How do you configure a project to use ES Modules by default, and how are files loaded differently?",
    [
        "CommonJS: require() / module.exports, synchronous loading, default in older Node.js",
        "ES Modules: import / export, asynchronous static analysis, standardized across browser and server",
        "Configuration: set 'type': 'module' in package.json or use .mjs file extension",
        "Differences: CommonJS has __dirname and __filename in scope; ESM requires import.meta.url"
    ],
    "1. CommonJS (CJS):\n- Syntax: `const mod = require('./mod')`, `module.exports = ...`\n- Loading: Synchronous module loading at runtime.\n- Globals: Built-in `__dirname` and `__filename`.\n2. ES Modules (ESM):\n- Syntax: `import mod from './mod.js'`, `export default ...`\n- Loading: Static analysis phase before execution; supports top-level await.\n- Configuration: Add `\"type\": \"module\"` in `package.json` or use `.mjs` extensions.\n- Note: In ESM, `__dirname` is not defined by default; it is derived via `path.dirname(fileURLToPath(import.meta.url))`."
)

# ==================== EXPRESS.JS (JUNIOR) ====================
add_mcq("jr-express-01", "express", "Middleware Concept",
    "What is the purpose of the `next()` function in Express.js middleware?",
    [
        "A) It redirects the browser to the next route in the sitemap",
        "B) It passes control to the next middleware function in the request-response stack",
        "C) It immediately sends an HTTP 200 response to the client",
        "D) It restarts the Node.js server process"
    ],
    "B",
    "If the current middleware function does not terminate the request-response cycle (e.g. by sending `res.send()`), it must call `next()` to pass execution to the subsequent middleware; otherwise, the request hangs."
)

add_mcq("jr-express-02", "express", "Body Parsing",
    "In modern Express (v4.16+), which built-in middleware is required to parse incoming JSON request bodies?",
    [
        "A) `app.use(express.bodyParser())`",
        "B) `app.use(express.json())`",
        "C) `app.use(express.parseJSON())`",
        "D) `app.use(express.urlencoded())`"
    ],
    "B",
    "`express.json()` is built into modern Express (based on body-parser) to parse incoming requests with JSON payloads and populate `req.body`."
)

add_mcq("jr-express-03", "express", "Route Parameters",
    "Given the route `/users/:userId/posts/:postId`, how do you access `userId` inside the route handler?",
    [
        "A) `req.query.userId`",
        "B) `req.body.userId`",
        "C) `req.params.userId`",
        "D) `req.headers.userId`"
    ],
    "C",
    "Route path parameters defined with colons (`:param`) are captured and made available on the `req.params` dictionary object."
)

add_mcq("jr-express-04", "express", "HTTP Status Codes",
    "Which HTTP status code should be returned when a resource is successfully created via a POST endpoint?",
    [
        "A) 200 OK",
        "B) 201 Created",
        "C) 204 No Content",
        "D) 301 Moved Permanently"
    ],
    "B",
    "According to HTTP specifications, `201 Created` is the standard status code indicating that the request succeeded and led to the creation of a new resource."
)

add_mcq("jr-express-05", "express", "Error Handling Middleware",
    "How does Express differentiate an error-handling middleware function from a regular middleware function?",
    [
        "A) Error middleware must be declared with four arguments: `(err, req, res, next)`",
        "B) Error middleware must be placed at the very top of `server.js`",
        "C) Error middleware must return a Boolean value",
        "D) Error middleware must use `app.error()` instead of `app.use()`"
    ],
    "A",
    "Express inspects the function's `length` (arity). A function with four arguments `(err, req, res, next)` is identified by Express as an error-handling middleware."
)

add_mcq("jr-express-06", "express", "Express Router",
    "What is the primary advantage of using `express.Router()`?",
    [
        "A) It automatically generates React frontend routes",
        "B) It enables modular, mountable route handlers that can be split into separate files and sub-paths",
        "C) It encrypts network traffic with TLS certificates",
        "D) It connects the backend directly to MongoDB collections"
    ],
    "B",
    "`express.Router()` provides an isolated instance of middleware and routing systems, allowing you to organize routes cleanly into modular files and mount them at specific URL prefixes."
)

add_mcq("jr-express-07", "express", "Static Files",
    "How do you serve static files like images and CSS from a directory named 'public' in Express?",
    [
        "A) `app.serveStatic('/public')`",
        "B) `app.use(express.static('public'))`",
        "C) `app.get('*', express.fileServer('public'))`",
        "D) `app.use(express.public())`"
    ],
    "B",
    "`express.static(root, [options])` is the built-in middleware function in Express used to serve static assets such as HTML, CSS, JavaScript, and image files."
)

add_mcq("jr-express-08", "express", "res.send vs res.json",
    "What is the main practical difference between `res.send(data)` and `res.json(data)` in Express?",
    [
        "A) `res.send()` can only send plaintext HTML, while `res.json()` formats objects and explicitly sets the Content-Type header to `application/json`",
        "B) `res.json()` requires a paid license",
        "C) `res.send()` closes the server connection permanently",
        "D) `res.json()` automatically commits database transactions"
    ],
    "A",
    "`res.json()` converts the payload to JSON via `JSON.stringify()` (handling formatting options) and guarantees that the `Content-Type` header is set to `application/json`."
)

add_mcq("jr-express-09", "express", "req.headers",
    "How do you access the client's `Authorization` header inside an Express route?",
    [
        "A) `req.get('authorization')` or `req.headers['authorization']`",
        "B) `req.security.auth`",
        "C) `req.cookies.bearer`",
        "D) `req.params.authorization`"
    ],
    "A",
    "Headers can be accessed either via the lowercased key in `req.headers['authorization']` or using the helper method `req.get('Authorization')`."
)

add_mcq("jr-express-10", "express", "res.redirect",
    "What HTTP status code is used by default when you call `res.redirect('/login')` in Express?",
    [
        "A) 200 OK",
        "B) 302 Found (Temporary Redirect)",
        "C) 301 Moved Permanently",
        "D) 404 Not Found"
    ],
    "B",
    "`res.redirect([status,] url)` defaults to status `302 Found` if not explicitly specified."
)

add_mcq("jr-express-11", "express", "Middleware Execution Order",
    "If middleware A is defined before middleware B using `app.use()`, which one executes first when a request arrives?",
    [
        "A) Middleware B always executes first",
        "B) Middleware A executes first, and if it calls `next()`, Middleware B executes second",
        "C) They execute concurrently in separate threads",
        "D) Express randomly picks one based on server load"
    ],
    "B",
    "Express executes middleware in the exact sequential order in which they are registered with `app.use()` or route handlers."
)

add_mcq("jr-express-12", "express", "CORS Package",
    "Which popular npm package is commonly used in Express to enable Cross-Origin Resource Sharing?",
    [
        "A) helmet",
        "B) morgan",
        "C) cors",
        "D) express-validator"
    ],
    "C",
    "`cors` is the standard Express middleware for enabling CORS with various options (origin, methods, headers, credentials)."
)

add_mcq("jr-express-13", "express", "Morgan Logger",
    "What is the primary role of the `morgan` package in an Express application?",
    [
        "A) Password hashing using bcrypt",
        "B) HTTP request logger middleware for debugging and traffic monitoring",
        "C) Rate limiting DDOS attacks",
        "D) Parsing multipart form data"
    ],
    "B",
    "`morgan` logs HTTP request details (method, URL, status code, response time) to the console or log files."
)

add_mcq("jr-express-14", "express", "404 Not Found Handler",
    "Where should a generic 404 'Not Found' handler be placed in an Express application file?",
    [
        "A) At the very top before any route handlers",
        "B) After all valid route declarations, right before the global error handler",
        "C) Inside the package.json file",
        "D) In a separate cluster process"
    ],
    "B",
    "Because Express evaluates routes in order, an unmatched request falls through to the end of the stack. A wildcard 404 middleware should be placed after all defined routes."
)

add_open("jr-express-15", "express", "Middleware Architecture in Express",
    "Explain what Express middleware is, how data flows through a middleware pipeline, and what happens if a middleware neither sends a response nor calls `next()`.",
    [
        "Middleware are functions with access to req, res, and next",
        "They can execute code, modify req/res objects, end request-response cycle, or call next()",
        "If neither res is sent nor next() is invoked, the client request hangs until timeout"
    ],
    "In Express, middleware functions execute sequentially during the request-response lifecycle. Each middleware has access to the request object (`req`), the response object (`res`), and the `next` function.\nA middleware can:\n1. Execute arbitrary logic (logging, authentication checks, parsing headers).\n2. Mutate `req` or `res` (e.g. attaching `req.user = decodedToken`).\n3. Conclude the cycle by sending a response (`res.status(200).json(...)`).\n4. Pass control to the next handler by calling `next()`.\nIf a middleware neither concludes the response nor calls `next()`, the HTTP connection remains open indefinitely until the client or server times out."
)

add_open("jr-express-16", "express", "Query Parameters vs Route Parameters",
    "Contrast `req.params` and `req.query` in Express. Give an example URL and route definition for each, explaining when to choose one over the other.",
    [
        "req.params: Part of the URL path itself, defined as placeholders (e.g. /products/:id), used to identify a specific resource",
        "req.query: Key-value pairs after the question mark (e.g. /products?category=shoes&sort=asc), used for filtering, pagination, or sorting"
    ],
    "1. `req.params`: Used for route path parameters that uniquely identify a resource.\nExample Route: `app.get('/users/:id')`\nURL: `/users/42` -> `req.params.id === '42'`.\n2. `req.query`: Used for optional URL query strings appearing after `?` to filter, sort, search, or paginate resources.\nExample Route: `app.get('/users')`\nURL: `/users?role=admin&limit=10` -> `req.query.role === 'admin'`, `req.query.limit === '10'`.\nRule of thumb: Use route parameters for mandatory resource identity; use query parameters for optional filtering or options."
)

add_open("jr-express-17", "express", "Centralized Error Handling",
    "How do you implement a centralized error handling middleware in Express, and how do you forward errors to it from asynchronous routes?",
    [
        "Declare a middleware with 4 arguments: (err, req, res, next)",
        "Forward errors using next(error) inside try/catch blocks (or let express 5+ handle rejected promises automatically)",
        "Respond with appropriate HTTP status code (e.g. 500 or err.statusCode) and structured JSON error response"
    ],
    "To create a centralized error handler in Express:\n1. Define a middleware with 4 parameters: `app.use((err, req, res, next) => { ... })` at the bottom of your middleware chain.\n2. In async route handlers, wrap operations in `try/catch` and pass caught errors to `next(error)`: \n```js\napp.get('/data', async (req, res, next) => {\n  try {\n    const data = await fetchData();\n    res.json(data);\n  } catch (err) {\n    next(err);\n  }\n});\n```\n3. Inside the error handler, inspect `err.statusCode || 500` and send a consistent JSON payload `{ success: false, error: err.message }`."
)

add_open("jr-express-18", "express", "REST API Status Codes Conventions",
    "Describe what HTTP status codes 200, 201, 400, 401, 403, 404, and 500 represent in a RESTful Express API and when each should be returned.",
    [
        "200 OK: Standard successful GET/PUT/PATCH response",
        "201 Created: Successful resource creation via POST",
        "400 Bad Request: Invalid client payload or validation failure",
        "401 Unauthorized: Missing or invalid authentication token",
        "403 Forbidden: Authenticated user lacks permission/role for the resource",
        "404 Not Found: Requested resource does not exist",
        "500 Internal Server Error: Unhandled server-side bug or database crash"
    ],
    "- 200 OK: Request succeeded; standard response for GET, PUT, or DELETE.\n- 201 Created: New resource successfully persisted; return after POST.\n- 400 Bad Request: Client sent malformed JSON or failed schema validation.\n- 401 Unauthorized: Client is unauthenticated; authentication credentials missing or invalid.\n- 403 Forbidden: Client is authenticated but lacks permission (e.g. non-admin trying to delete users).\n- 404 Not Found: The requested route or database ID does not exist.\n- 500 Internal Server Error: Unexpected server crash, unhandled exception, or database outage."
)

# ==================== MONGODB & MONGOOSE (JUNIOR) ====================
add_mcq("jr-mongo-01", "mongodb", "NoSQL Basics",
    "What data format does MongoDB use internally to store documents?",
    [
        "A) Pure XML",
        "B) BSON (Binary JSON)",
        "C) YAML",
        "D) Comma-Separated Values (CSV)"
    ],
    "B",
    "MongoDB stores data records as BSON documents. BSON is a binary representation of JSON-like documents that supports richer data types (like Date, Int64, and ObjectId) and faster traversal."
)

add_mcq("jr-mongo-02", "mongodb", "Primary Key in MongoDB",
    "What is the default unique identifier field automatically assigned to every document in a MongoDB collection?",
    [
        "A) `id`",
        "B) `_id` of type ObjectId",
        "C) `uuid`",
        "D) `pk_index`"
    ],
    "B",
    "Every MongoDB document requires an immutable `_id` field. If omitted during insertion, MongoDB automatically creates an `_id` with a 12-byte `ObjectId`."
)

add_mcq("jr-mongo-03", "mongodb", "Mongoose Schema vs Model",
    "In Mongoose, what is the distinction between a Schema and a Model?",
    [
        "A) A Schema compiles into SQL tables, while a Model stores binary images",
        "B) A Schema defines the structure and validation rules for documents, while a Model provides the interface to query and update the MongoDB collection",
        "C) Schema is for frontend forms, Model is for Express controllers",
        "D) There is no difference; they are aliases of the same class"
    ],
    "B",
    "A Mongoose Schema maps to a MongoDB collection and defines the document shape, default values, and validators. A Model is a compiled constructor created from a Schema that provides methods to create, query, update, and delete documents."
)

add_mcq("jr-mongo-04", "mongodb", "Basic MongoDB Query Operators",
    "Which query operator retrieves all documents where the `age` field is greater than 18?",
    [
        "A) `{ age: { $gt: 18 } }`",
        "B) `{ age: > 18 }`",
        "C) `{ age: { $moreThan: 18 } }`",
        "D) `{ age: { $above: 18 } }`"
    ],
    "A",
    "The `$gt` (greater than) comparison operator selects documents where the value of the specified field is greater than the specified value."
)

add_mcq("jr-mongo-05", "mongodb", "Updating Documents",
    "In native MongoDB, what happens if you run `updateOne({ _id }, { status: 'active' })` without an update operator like `$set`?",
    [
        "A) MongoDB ignores the update command",
        "B) MongoDB throws an error in modern drivers because raw replacement requires `replaceOne`",
        "C) MongoDB automatically converts it to a `$set` operation",
        "D) MongoDB creates a duplicate document"
    ],
    "B",
    "In modern MongoDB drivers, `updateOne` requires atomic update operators like `$set` or `$inc`. Supplying a plain object without update operators throws an error, preventing accidental replacement of the document."
)

add_mcq("jr-mongo-06", "mongodb", "Embedded vs Referenced Documents",
    "When is embedding documents (denormalization) preferred over referencing (normalization) in MongoDB?",
    [
        "A) When data is updated by 50 different microservices simultaneously",
        "B) When child data is tightly coupled to the parent, frequently read together, and has a 1-to-few relationship that won't exceed the 16MB document limit",
        "C) When storing unbounded audit logs spanning millions of rows",
        "D) Only when using SQLite instead of MongoDB"
    ],
    "B",
    "Embedding documents provides high-performance atomic reads and writes without joins when child records belong exclusively to the parent and will not grow unboundedly past the 16MB BSON limit."
)

add_mcq("jr-mongo-07", "mongodb", "Mongoose Validation",
    "Where is schema validation executed when using Mongoose in a MERN application?",
    [
        "A) Inside the browser before form submission",
        "B) In the Node.js application layer by Mongoose before sending the write command to MongoDB",
        "C) Inside the PostgreSQL storage engine",
        "D) By the Nginx reverse proxy"
    ],
    "B",
    "Mongoose schema validations are evaluated inside the Node.js application layer prior to dispatching queries to the MongoDB server."
)

add_mcq("jr-mongo-08", "mongodb", "Find by ID",
    "Which Mongoose method is specifically optimized for finding a single document by its `_id`?",
    [
        "A) `User.find({ id: req.params.id })`",
        "B) `User.findById(req.params.id)`",
        "C) `User.lookupId(req.params.id)`",
        "D) `User.getById(req.params.id)`"
    ],
    "B",
    "`Model.findById(id)` is the standard Mongoose helper method that automatically casts the string argument to an `ObjectId` and performs a `findOne({ _id: id })`."
)

add_mcq("jr-mongo-09", "mongodb", "BSON 16MB Limit",
    "What is the maximum allowed size for an individual BSON document in MongoDB?",
    [
        "A) 1 Megabyte",
        "B) 16 Megabytes",
        "C) 64 Megabytes",
        "D) Unlimited"
    ],
    "B",
    "The maximum BSON document size is 16 Megabytes to ensure that single documents cannot monopolize excessive RAM or network bandwidth during transmission. For larger files, GridFS is used."
)

add_mcq("jr-mongo-10", "mongodb", "Logical Operators",
    "Which query matches documents where `status` is 'pending' OR `priority` is 'high'?",
    [
        "A) `{ $or: [{ status: 'pending' }, { priority: 'high' }] }`",
        "B) `{ status: 'pending' || priority: 'high' }`",
        "C) `{ either: ['status', 'priority'] }`",
        "D) `{ status: 'pending', $also: { priority: 'high' } }`"
    ],
    "A",
    "The `$or` operator performs a logical OR operation on an array of two or more expressions and selects documents that satisfy at least one expression."
)

add_mcq("jr-mongo-11", "mongodb", "Array Operations",
    "Which MongoDB operator adds an element to an array field only if that element does not already exist?",
    [
        "A) `$push`",
        "B) `$addToSet`",
        "C) `$append`",
        "D) `$insertUnique`"
    ],
    "B",
    "`$addToSet` adds a value to an array unless the value is already present, treating the array like a mathematical set."
)

add_mcq("jr-mongo-12", "mongodb", "Mongoose Timestamps",
    "In Mongoose schema options, what does `{ timestamps: true }` automatically add to documents?",
    [
        "A) `createdAt` and `updatedAt` Date fields automatically managed by Mongoose",
        "B) A UNIX timestamp field named `time`",
        "C) A clock widget in React",
        "D) An automatic expiration timer (TTL) of 24 hours"
    ],
    "A",
    "Enabling `{ timestamps: true }` instructs Mongoose to automatically create and update `createdAt` and `updatedAt` Date properties on document creation and modifications."
)

add_open("jr-mongo-13", "mongodb", "SQL vs NoSQL (MongoDB)",
    "Compare MongoDB to a traditional relational database (like PostgreSQL). What are the key architectural differences in schema flexibility, relationships, and transactions?",
    [
        "Schema: MongoDB is schema-less/schema-flexible (JSON/BSON docs); SQL requires rigid tables with predefined columns",
        "Relationships: MongoDB favors embedding or manual references; SQL uses foreign keys and relational JOINs",
        "Transactions: Relational databases are built for multi-table ACID transactions; MongoDB supports transactions but focuses on document-level atomicity"
    ],
    "1. Schema Flexibility: MongoDB documents are self-describing BSON records. Different documents in a collection can have different fields, allowing rapid iterations. Relational databases enforce rigid tabular schemas with explicit column data types.\n2. Relationships & Joins: Relational databases use primary/foreign keys with powerful JOIN operations. MongoDB favors embedding related data within the same document for fast single-lookup reads, or using `$lookup` for references.\n3. Scaling: Relational databases traditionally scale vertically. MongoDB was designed from the ground up for horizontal scaling and sharding across distributed clusters.\n4. Transactions: While MongoDB now supports multi-document ACID transactions, its core performance sweet spot is single-document atomic updates."
)

add_open("jr-mongo-14", "mongodb", "Mongoose Population",
    "What is Mongoose `.populate()` and how does it simulate a relational join? What are its performance trade-offs?",
    [
        "Replaces an ObjectId reference with the actual referenced document from another collection",
        "Under the hood, Mongoose makes additional queries to the referenced collection",
        "Performance trade-off: Multiple round-trips to the database; not as efficient as a native database engine JOIN or embedded documents"
    ],
    "In Mongoose, `.populate()` replaces a stored `ObjectId` reference in one document with the actual document data from another collection.\nHow it works: It is not a native database join. Under the hood, Mongoose executes the primary query, collects the referenced ObjectIds, executes a secondary query against the foreign collection, and merges the results in Node.js memory.\nTrade-offs: While convenient, heavy use of `.populate()` introduces multiple database round-trips, network overhead, and high memory usage compared to native joins or properly modeled embedded documents."
)

add_open("jr-mongo-15", "mongodb", "Data Modeling: Embedding vs Referencing",
    "Describe the key factors that guide the decision between Embedding (Denormalization) and Referencing (Normalization) in MongoDB schema design.",
    [
        "Embedding: 1-to-1 or 1-to-few relationships, data queried together, data rarely updated independently, within 16MB document limit",
        "Referencing: 1-to-many or many-to-many relationships, unbounded growth (e.g. logs/comments), frequently updated independently, accessed separately"
    ],
    "- Choose Embedding when: Data has a 1-to-few relationship (e.g., a user and their 2 addresses), child data does not exist independently of the parent, both parent and child are almost always queried together, and total document size stays safely under 16MB.\n- Choose Referencing when: Data has a 1-to-many or many-to-many relationship where child records grow unboundedly (e.g., thousands of user reviews or IoT sensor events), or when the child entity is queried and updated independently across multiple parts of the system."
)

# ==================== POSTGRESQL (JUNIOR) ====================
add_mcq("jr-pg-01", "postgresql", "Primary vs Foreign Keys",
    "What is the primary role of a FOREIGN KEY constraint in PostgreSQL?",
    [
        "A) It prevents users from outside the local network from querying the table",
        "B) It enforces referential integrity by ensuring the value in a child table column matches an existing primary or unique key in a parent table",
        "C) It encrypts column values using public key cryptography",
        "D) It automatically indexes all text columns in alphabetical order"
    ],
    "B",
    "A Foreign Key establishes a relationship between two tables, ensuring that records cannot point to non-existent parent rows and preventing orphaned records when updates or deletions occur."
)

add_mcq("jr-pg-02", "postgresql", "SQL Joins",
    "What is the difference between an `INNER JOIN` and a `LEFT JOIN`?",
    [
        "A) `INNER JOIN` returns only rows that have matching values in both tables, while `LEFT JOIN` returns all rows from the left table plus matching rows from the right table (with NULLs for non-matches)",
        "B) `INNER JOIN` sorts ascending; `LEFT JOIN` sorts descending",
        "C) `LEFT JOIN` only works on numbers; `INNER JOIN` works on strings",
        "D) `INNER JOIN` deletes unmatched rows from disk"
    ],
    "A",
    "`INNER JOIN` filters out any rows that lack a match in either table. `LEFT JOIN` guarantees that every record from the left table is returned; if there is no match on the right, the right-side columns are filled with `NULL`."
)

add_mcq("jr-pg-03", "postgresql", "SQL Injection",
    "How do you prevent SQL Injection vulnerabilities when querying PostgreSQL from Node.js (e.g. using `pg` library)?",
    [
        "A) Wrap all input strings with `escape()` in JavaScript",
        "B) Use parameterized queries with placeholders like `$1, $2`, letting the database driver handle value separation and escaping",
        "C) Only use GET requests for database lookups",
        "D) Run Node.js with the `--no-sql-injection` flag"
    ],
    "B",
    "Parameterized queries separate the SQL command code from user-supplied data values. The database treats `$1` strictly as a literal parameter, making it impossible for malicious SQL commands to alter query structure."
)

add_mcq("jr-pg-04", "postgresql", "Data Types in PostgreSQL",
    "Which PostgreSQL data type is recommended for storing arbitrary structured JSON data with indexing and query capabilities?",
    [
        "A) `VARCHAR(MAX)`",
        "B) `JSONB`",
        "C) `BLOB`",
        "D) `TEXT_ARRAY`"
    ],
    "B",
    "`JSONB` stores JSON data in a decomposed binary format. It supports GIN indexing, fast path lookups, and rich query operators, making it superior to plain `JSON` for querying and filtering."
)

add_mcq("jr-pg-05", "postgresql", "ACID Properties",
    "What does the 'A' in ACID transactions stand for, and what does it mean?",
    [
        "A) Asynchronous: Queries run on background threads without waiting",
        "B) Atomicity: All operations in a transaction either succeed completely or fail completely with nothing committed",
        "C) Availability: The database is guaranteed to respond 100% of the time",
        "D) Authorization: Only valid database users can execute queries"
    ],
    "B",
    "Atomicity ensures that a series of database operations either execute in full ('all') or abort with all changes rolled back ('nothing'), preventing partial updates."
)

add_mcq("jr-pg-06", "postgresql", "Basic SQL Constraints",
    "Which constraint ensures that no two rows can have the same value in a specific column, while still allowing NULL values unless combined with NOT NULL?",
    [
        "A) `CHECK`",
        "B) `UNIQUE`",
        "C) `DEFAULT`",
        "D) `PRIMARY KEY`"
    ],
    "B",
    "A `UNIQUE` constraint enforces uniqueness for non-null values across rows. Unlike `PRIMARY KEY`, it permits `NULL` values (unless `NOT NULL` is explicitly added) and tables can have multiple unique constraints."
)

add_mcq("jr-pg-07", "postgresql", "Serial and Identity Columns",
    "What is the modern standard SQL feature in PostgreSQL 10+ for creating auto-incrementing integer primary keys?",
    [
        "A) `AUTO_INCREMENT`",
        "B) `GENERATED ALWAYS AS IDENTITY`",
        "C) `SEQUENCE_INT`",
        "D) `ROWID`"
    ],
    "B",
    "While PostgreSQL supports the legacy `SERIAL` pseudotype, standard SQL compliant `GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY` is the modern standard in PostgreSQL 10+."
)

add_mcq("jr-pg-08", "postgresql", "Aggregation Functions",
    "Which SQL clause is used to filter the grouped results produced by a `GROUP BY` statement?",
    [
        "A) `WHERE`",
        "B) `HAVING`",
        "C) `FILTER BY`",
        "D) `ORDER BY`"
    ],
    "B",
    "`WHERE` filters individual rows before aggregation occurs, while `HAVING` filters aggregated groups produced by `GROUP BY`."
)

add_mcq("jr-pg-09", "postgresql", "Connection Pooling (pg-pool)",
    "Why should a Node.js application use a connection pool (e.g. `pg.Pool`) instead of opening a new `pg.Client` on every incoming HTTP request?",
    [
        "A) PostgreSQL prohibits opening more than 1 connection per IP address",
        "B) Establishing a new TCP connection and performing SSL/auth handshakes on every request is slow and quickly exhausts PostgreSQL connection limits",
        "C) `pg.Client` only works in test environments",
        "D) Connection pooling encrypts all queries automatically"
    ],
    "B",
    "Opening and tearing down PostgreSQL connections involves expensive socket creation, process forking, and authentication. A pool keeps open connections ready for reuse, dramatically improving throughput."
)

add_mcq("jr-pg-10", "postgresql", "NULL Value Comparisons",
    "In PostgreSQL, why does `SELECT * FROM users WHERE deleted_at = NULL` return 0 rows even when deleted_at contains NULL values?",
    [
        "A) In SQL, comparing anything to NULL with `=` evaluates to UNKNOWN (falsy); you must use `IS NULL` instead",
        "B) NULL is converted to empty string automatically",
        "C) PostgreSQL syntax requires `== NULL`",
        "D) NULL values are deleted from indexes"
    ],
    "A",
    "In three-valued SQL logic, `NULL` represents an unknown value. Comparing with `=` (`x = NULL`) results in `UNKNOWN`, which evaluates to false in a `WHERE` clause. You must use `IS NULL` or `IS NOT NULL`."
)

add_mcq("jr-pg-11", "postgresql", "Cascade Deletes",
    "In a foreign key definition, what does `ON DELETE CASCADE` do when a parent row is deleted?",
    [
        "A) It prevents the parent row from being deleted",
        "B) It automatically deletes all associated child rows in the child table",
        "C) It sets the child foreign key column to NULL",
        "D) It moves the child rows to an archive database"
    ],
    "B",
    "`ON DELETE CASCADE` ensures that when a referenced parent record is removed, all dependent child rows containing that foreign key are automatically deleted to maintain referential integrity."
)

add_mcq("jr-pg-12", "postgresql", "LIMIT and OFFSET",
    "Which SQL query retrieves the second page of 10 users?",
    [
        "A) `SELECT * FROM users LIMIT 10 OFFSET 10;`",
        "B) `SELECT * FROM users PAGE 2 SIZE 10;`",
        "C) `SELECT * FROM users RANGE 11 TO 20;`",
        "D) `SELECT * FROM users FETCH 10 AFTER 10;`"
    ],
    "A",
    "`LIMIT 10 OFFSET 10` skips the first 10 matching rows and retrieves the next 10 rows (rows 11-20), representing page 2."
)

add_open("jr-pg-13", "postgresql", "Database Normalization Basics",
    "Explain the concept of database normalization and describe the first three normal forms (1NF, 2NF, 3NF) in simple terms.",
    [
        "Goal: Reduce data redundancy and prevent update/delete anomalies",
        "1NF: Atomic values (no comma-separated lists or arrays), each row uniquely identifiable with a primary key",
        "2NF: In 1NF and all non-key columns depend on the entire primary key (no partial dependencies on composite keys)",
        "3NF: In 2NF and no transitive dependencies (non-key columns do not depend on other non-key columns)"
    ],
    "Database normalization organizes tables to minimize data duplication and prevent insertion, update, and deletion anomalies.\n- 1NF (First Normal Form): Data is organized into rows and columns, each cell contains a single atomic value (no lists or nested objects), and each row has a primary key.\n- 2NF (Second Normal Form): Meets 1NF, and all non-key attributes are fully functionally dependent on the primary key (no partial dependencies on part of a composite key).\n- 3NF (Third Normal Form): Meets 2NF, and no non-key attribute depends on another non-key attribute (no transitive dependencies; 'every attribute must depend on the key, the whole key, and nothing but the key')."
)

add_open("jr-pg-14", "postgresql", "ORMs vs Raw SQL (Node/Postgres)",
    "Compare using an ORM/Query Builder (like Prisma or Sequelize) versus writing raw SQL queries using the `pg` driver in a Node.js project. What are the pros and cons of each?",
    [
        "ORM Pros: Type safety, autocompletion, migrations, developer productivity, abstraction from SQL syntax",
        "ORM Cons: Performance overhead, potential N+1 query problem, complex queries can become awkward to write",
        "Raw SQL Pros: Maximum performance, complete control over query plans, ability to leverage PostgreSQL-specific features",
        "Raw SQL Cons: Vulnerable to SQL injection if not parameterized, manual type casting, tedious schema maintenance"
    ],
    "1. ORMs / Query Builders (e.g. Prisma, Sequelize, Kysely):\n- Pros: Accelerate development, provide automated migrations, offer compile-time type safety with TypeScript, and eliminate manual query formatting.\n- Cons: Can generate inefficient SQL (such as N+1 query loops), add abstraction overhead, and make complex reporting or window functions difficult to express.\n2. Raw SQL with `pg`:\n- Pros: Unmatched performance, zero abstraction overhead, direct control over `EXPLAIN ANALYZE` execution plans, and full access to advanced PostgreSQL features (CTEs, JSONB operators, triggers).\n- Cons: Developers must write repetitive mapping code, manage migrations manually, and strictly use parameterized queries to avoid SQL injection vulnerabilities."
)

add_open("jr-pg-15", "postgresql", "Transactions in PostgreSQL",
    "What is a database transaction, what commands initiate, commit, or rollback a transaction in SQL, and why is this critical for banking or e-commerce workflows?",
    [
        "Transaction bundles multiple SQL steps into an atomic single unit of work",
        "Commands: BEGIN (or START TRANSACTION), COMMIT, ROLLBACK",
        "Critical to prevent money from being deducted from account A without being credited to account B"
    ],
    "A transaction bundles multiple database modifications into a single atomic operation that adheres to ACID principles.\n- Commands: Started with `BEGIN;`, made permanent with `COMMIT;`, or canceled/reverted with `ROLLBACK;` if an error occurs.\n- Real-world critical need: In an e-commerce or banking system, transferring $100 requires deducting $100 from User A and adding $100 to User B. If a network drop or crash happens midway, a transaction ensures that User A's deduction is rolled back, preventing funds from vanishing into thin air."
)

# ==================== FULLSTACK / REST / SECURITY (JUNIOR) ====================
add_mcq("jr-full-01", "fullstack", "CORS (Cross-Origin Resource Sharing)",
    "What triggers a browser CORS error when your React app (running on localhost:3000) makes a fetch request to your Express API (running on localhost:5000)?",
    [
        "A) The Node.js server crashed due to out of memory",
        "B) The browser enforces the Same-Origin Policy, and the Express server did not respond with the appropriate `Access-Control-Allow-Origin` header",
        "C) Port 5000 is reserved exclusively for operating system services",
        "D) React requires all fetch requests to be sent via HTTPS only"
    ],
    "B",
    "Different ports constitute different origins under the browser's Same-Origin Policy. The browser blocks cross-origin responses unless the server explicitly grants permission via CORS response headers like `Access-Control-Allow-Origin`."
)

add_mcq("jr-full-02", "fullstack", "RESTful Principles",
    "Which HTTP method should be used to partially update an existing resource according to standard REST conventions?",
    [
        "A) PUT",
        "B) PATCH",
        "C) POST",
        "D) GET"
    ],
    "B",
    "`PATCH` is designated for partial updates (updating specific fields of a resource), whereas `PUT` is designed to completely replace the target resource."
)

add_mcq("jr-full-03", "fullstack", "Authentication Basics",
    "Why is storing JWT authentication tokens in `HttpOnly` cookies generally more secure against XSS attacks than storing them in browser `localStorage`?",
    [
        "A) HttpOnly cookies are stored directly on the user's hard drive in an encrypted vault",
        "B) JavaScript running in the browser cannot read or access HttpOnly cookies, preventing stolen tokens via Cross-Site Scripting (XSS)",
        "C) HttpOnly cookies automatically delete themselves every 5 minutes",
        "D) LocalStorage can only hold up to 10 characters"
    ],
    "B",
    "If a site has an XSS vulnerability, malicious scripts can easily read tokens from `localStorage` (`window.localStorage.getItem(...)`). An `HttpOnly` cookie cannot be accessed via JavaScript, insulating the token from XSS extraction."
)

add_mcq("jr-full-04", "fullstack", "Environment Variables Security",
    "Why should `.env` files never be committed to a public Git repository?",
    [
        "A) Git will refuse to push files that start with a period",
        "B) They contain sensitive secrets like database credentials, API keys, and JWT signing secrets that attackers can exploit",
        "C) Linux file permissions break if `.env` is pushed to GitHub",
        "D) It corrupts the npm cache"
    ],
    "B",
    "`.env` files store plain-text secrets. Committing them exposes sensitive credentials to automated scrapers and malicious actors on public version control."
)

add_mcq("jr-full-05", "fullstack", "JWT Structure",
    "What are the three parts separated by dots (`.`) in a JSON Web Token (JWT)?",
    [
        "A) Username, Password, Salt",
        "B) Header, Payload, Signature",
        "C) Algorithm, Public Key, Private Key",
        "D) Protocol, Host, Path"
    ],
    "B",
    "A JWT is composed of three Base64URL-encoded segments separated by dots: Header (metadata/algorithm), Payload (claims/user data), and Signature (verifies integrity)."
)

add_mcq("jr-full-06", "fullstack", "Password Hashing",
    "Why should user passwords never be stored in plain text or using simple MD5/SHA-1 hashes?",
    [
        "A) Plain text and MD5 can be easily compromised via database leaks and precomputed rainbow tables; slow, salted algorithms like bcrypt or argon2 must be used",
        "B) Databases do not accept strings with symbols in passwords",
        "C) MD5 produces strings that are too long for database columns",
        "D) Passwords in plain text crash the Express JSON parser"
    ],
    "A",
    "Modern GPU hardware can compute billions of SHA-1/MD5 hashes per second. Strong password hashing functions like bcrypt or Argon2 incorporate salts (thwarting rainbow tables) and configurable work factors to remain computationally expensive."
)

add_mcq("jr-full-07", "fullstack", "HTTPS Purpose",
    "What critical security benefit does HTTPS (TLS) provide for a PERN/MERN application?",
    [
        "A) It prevents all bugs in JavaScript code",
        "B) It encrypts network traffic between client and server, protecting sensitive data (passwords, tokens) from eavesdropping and man-in-the-middle attacks",
        "C) It speeds up database queries by 10x",
        "D) It removes the need for user authentication"
    ],
    "B",
    "HTTPS uses TLS to encrypt HTTP payloads in transit, ensuring confidentiality, integrity, and authenticity across the internet."
)

add_mcq("jr-full-08", "fullstack", "Status Code 401 vs 403",
    "What is the difference between HTTP status code 401 Unauthorized and 403 Forbidden?",
    [
        "A) 401 means the user is unknown/unauthenticated; 403 means the user is recognized but not authorized/permitted to access the resource",
        "B) 401 is for GET requests; 403 is for POST requests",
        "C) 401 is a server crash; 403 is a database crash",
        "D) They are completely interchangeable synonyms"
    ],
    "A",
    "401 Unauthorized signifies that valid authentication credentials are required or missing. 403 Forbidden indicates that the server understands who the user is, but refuses to authorize the action (e.g. insufficient role privileges)."
)

add_mcq("jr-full-09", "fullstack", "Git Branching",
    "What is the standard Git workflow for introducing a new feature in a team development environment?",
    [
        "A) Direct commit and push to `main` or `production` without testing",
        "B) Create a feature branch off `main`, commit incremental changes, push to remote, open a Pull Request (PR) for code review, and merge",
        "C) Email zip files of code changes to team members",
        "D) Delete the `.git` folder before pushing"
    ],
    "B",
    "Creating feature branches isolates experimental work, prevents breaking the stable `main` branch, and facilitates peer review through Pull/Merge Requests."
)

add_mcq("jr-full-10", "fullstack", "Pagination Purpose",
    "Why is API pagination (e.g. `limit` and `offset` or cursor) essential when returning lists from a backend database?",
    [
        "A) To prevent transferring thousands or millions of records into server/client memory, which causes high latency and crashes",
        "B) React cannot render more than 5 items",
        "C) PostgreSQL limits queries to 20 rows by default",
        "D) To charge users per page"
    ],
    "A",
    "Without pagination, an unrestricted query against a growing table will eventually load megabytes or gigabytes of records into memory, exhausting server RAM and freezing the client UI."
)

add_open("jr-full-11", "fullstack", "Client-Server Architecture in PERN/MERN",
    "Trace what happens under the hood when a user clicks 'Submit' on a React form to create a new user profile until data is stored in the database and a confirmation is shown in the UI.",
    [
        "Client event handled in React (e.g. onSubmit with e.preventDefault())",
        "Fetch/Axios sends HTTP POST request with JSON payload and auth headers over network",
        "Express server receives request, runs middleware (cors, json parser, auth)",
        "Controller validates data and invokes database query (pg INSERT or mongoose create)",
        "Database executes query, returns newly created record",
        "Express sends 201 response with JSON body",
        "React receives response, updates state, renders success feedback"
    ],
    "1. In React, the user submits the form. The `onSubmit` handler calls `e.preventDefault()` to stop the browser's default full-page reload.\n2. React gathers state and sends an asynchronous HTTP POST request (via `fetch` or `axios`) with a JSON body and headers (e.g. `Content-Type: application/json`, auth token).\n3. In Express, the request hits the server. Middleware executes: CORS validates the origin, `express.json()` parses the request body, and auth middleware verifies the session or token.\n4. The route controller validates fields and calls the database layer (Mongoose `User.create()` for MERN, or `pool.query('INSERT INTO users...')` for PERN).\n5. The database inserts the record, assigns an ID, and returns the row.\n6. Express sends an HTTP `201 Created` status code with the new record in the JSON response body.\n7. React's promise resolves; the component updates its state with the returned data and renders a success message."
)

add_open("jr-full-12", "fullstack", "JWT Authentication Flow",
    "Explain how JSON Web Token (JWT) based authentication works in a fullstack PERN/MERN application from login to protected resource access.",
    [
        "User sends credentials (email/password) via POST /api/login",
        "Server validates credentials (bcrypt.compare) and signs a JWT containing user claims",
        "Token is returned to client (in HttpOnly cookie or auth response)",
        "Client sends token in Authorization header (Bearer token) or cookie on subsequent requests",
        "Server middleware verifies token signature and extracts user identity before route access"
    ],
    "1. Login: The client submits email and password to `/api/login`.\n2. Verification & Signing: The Express backend looks up the user, compares the password hash using `bcrypt.compare()`. If valid, the server creates a signed JWT using `jwt.sign({ userId: user.id }, SECRET, { expiresIn: '1h' })`.\n3. Transmission: The server returns the JWT (preferably in an `HttpOnly` cookie or JSON payload).\n4. Protected Requests: On subsequent API calls, the client includes the token (e.g. `Authorization: Bearer <token>`).\n5. Verification: An Express auth middleware intercepts the request, verifies the signature with `jwt.verify()`, attaches the decoded user payload to `req.user`, and calls `next()`. If invalid or expired, a 401 status is returned."
)

with open("/workspaces/preppro/src/data/junior.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Generated {len(questions)} Junior questions in /workspaces/preppro/src/data/junior.json")
