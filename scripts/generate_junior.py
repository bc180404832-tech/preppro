#!/usr/bin/env python3
import json

questions = [
    # ------------------- REACT (JUNIOR) -------------------
    {
        "id": "jr-react-01",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "JSX Basics",
        "question": "In React, why can a component only return a single root JSX element (or a Fragment)?",
        "options": [
            "A) Because HTML5 prohibits multiple top-level elements",
            "B) Because JSX transpires to React.createElement, which is a JavaScript function call that can only return one value",
            "C) Because the browser DOM tree engine crashes if two elements are mounted at once",
            "D) Because CSS flexbox requires a single parent element to apply layout rules"
        ],
        "answer": "B",
        "explanation": "JSX compiles down to JavaScript function calls (React.createElement or jsx() runtime). In JavaScript, a function cannot return two separate values without wrapping them in an object, array, or parent element (like React.Fragment)."
    },
    {
        "id": "jr-react-02",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "useState Hook",
        "question": "What happens when you call the setState setter function returned by useState?",
        "options": [
            "A) The browser immediately refreshes the entire HTML page",
            "B) React directly mutates the existing DOM element synchronously",
            "C) React schedules a re-render of the component with the new state value",
            "D) The state variable is stored in localStorage automatically"
        ],
        "answer": "C",
        "explanation": "Calling a state setter does not instantly mutate the DOM or refresh the page; instead, React schedules a re-render so it can compute differences via its virtual DOM diffing process."
    },
    {
        "id": "jr-react-03",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "Props vs State",
        "question": "What is the primary difference between props and state in React?",
        "options": [
            "A) Props are mutable and managed locally, while state is read-only and passed from parents",
            "B) Props are read-only inputs passed from parent to child, while state is internal mutable data managed by the component",
            "C) Props are stored in the database, while state is stored in Redux",
            "D) Props can only hold strings, while state can hold any data type"
        ],
        "answer": "B",
        "explanation": "Props are external parameters passed down the component hierarchy and must remain immutable from the child's perspective, whereas state is local, private data managed by the component itself."
    },
    {
        "id": "jr-react-04",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "List Keys",
        "question": "Why should you avoid using array indices as the 'key' prop when rendering dynamic lists in React?",
        "options": [
            "A) React throws a fatal compile error if index is used as a key",
            "B) Using array indices can lead to incorrect component state and rendering bugs when items are reordered, inserted, or deleted",
            "C) Array indices take up 4x more RAM in the browser memory heap",
            "D) Browsers do not support integer keys in HTML elements"
        ],
        "answer": "B",
        "explanation": "React uses keys to identify which items have changed, been added, or been removed. If items are reordered or filtered, an index key causes React to mismatch state between different list elements."
    },
    {
        "id": "jr-react-05",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "useEffect Hook",
        "question": "When does a useEffect hook with an empty dependency array `[]` run?",
        "options": [
            "A) Before every single render cycle",
            "B) Only once after the component mounts for the first time",
            "C) Every time any state in the entire application changes",
            "D) Only when the component unmounts"
        ],
        "answer": "B",
        "explanation": "An empty dependency array `[]` instructs React that the effect does not depend on any props or state, so it executes only once after the initial render (mount)."
    },
    {
        "id": "jr-react-06",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "useEffect Cleanup",
        "question": "How do you define a cleanup mechanism in a React useEffect hook?",
        "options": [
            "A) By calling window.cleanup() inside the effect body",
            "B) By adding a second callback argument to useEffect",
            "C) By returning a cleanup function from the effect callback",
            "D) By using the unmountComponentAtNode() API"
        ],
        "answer": "C",
        "explanation": "React executes the function returned by the useEffect callback before running the effect again on updates and when the component unmounts, allowing timers, subscriptions, or listeners to be cleaned up."
    },
    {
        "id": "jr-react-07",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "Controlled Components",
        "question": "What is a 'controlled component' in React form handling?",
        "options": [
            "A) A component that can only be rendered by an administrator",
            "B) An input element whose value is driven by React component state via value and onChange props",
            "C) A component that controls the browser window's URL path",
            "D) An input element controlled entirely by DOM querySelectors"
        ],
        "answer": "B",
        "explanation": "In a controlled component, the form element's current value is bound to React state, and changes are handled by event listeners that update that state, making React the single source of truth."
    },
    {
        "id": "jr-react-08",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "Virtual DOM",
        "question": "What is the Virtual DOM and what is its primary benefit?",
        "options": [
            "A) A hardware-accelerated 3D graphics rendering engine for React VR",
            "B) A lightweight in-memory JavaScript representation of the real DOM that enables batching and minimal real DOM mutations",
            "C) A shadow copy of MongoDB documents cached in the browser",
            "D) A browser plugin required to run JSX code in Chrome"
        ],
        "answer": "B",
        "explanation": "The Virtual DOM is an in-memory object tree. React compares (diffs) the new Virtual DOM with the previous one and computes the minimal set of real DOM operations required, avoiding expensive layout reflows."
    },
    {
        "id": "jr-react-09",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "Conditional Rendering",
        "question": "In React, what will `count && <span>Items: {count}</span>` render if `count === 0`?",
        "options": [
            "A) Nothing (null)",
            "B) The number 0 rendered directly to the screen",
            "C) An error: Uncaught TypeError: 0 is not valid JSX",
            "D) <span>Items: 0</span>"
        ],
        "answer": "B",
        "explanation": "In JavaScript, `0 && ...` evaluates to `0`. Since numbers are valid renderable values in JSX, React renders the literal character `0` instead of hiding the element. The safe pattern is `count > 0 && ...` or a ternary."
    },
    {
        "id": "jr-react-10",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "State Immutability",
        "question": "Why should you never mutate state directly, e.g. `items.push(newItem)` in React?",
        "options": [
            "A) JavaScript throws a frozen object exception in strict mode",
            "B) React uses shallow reference equality checks (Object.is) to detect changes, so mutating existing references won't trigger re-renders",
            "C) React converts all arrays into binary buffers that cannot be pushed to",
            "D) Directly mutating arrays causes an immediate memory leak in V8"
        ],
        "answer": "B",
        "explanation": "React compares state references. If you mutate an existing array or object in place, the memory reference remains identical, so React assumes nothing changed and skips re-rendering."
    },
    {
        "id": "jr-react-11",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "Event Handling",
        "question": "How are DOM events named in React JSX compared to native HTML?",
        "options": [
            "A) React uses kebab-case like `on-click`, while HTML uses camelCase",
            "B) React uses camelCase like `onClick`, while HTML uses all lowercase like `onclick`",
            "C) React uses UPPERCASE like `ONCLICK`, while HTML uses lowercase",
            "D) React uses snake_case like `on_click`"
        ],
        "answer": "B",
        "explanation": "React event handlers follow standard camelCase naming conventions (`onClick`, `onChange`, `onSubmit`) and accept function references rather than strings."
    },
    {
        "id": "jr-react-12",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "Fragments",
        "question": "What is the primary advantage of using `<React.Fragment>` or `<>...</>` syntax?",
        "options": [
            "A) It compresses image assets during rendering",
            "B) It groups a list of children without adding extra wrapper nodes to the DOM",
            "C) It encrypts child components for secure transmission",
            "D) It converts children into HTML canvas elements"
        ],
        "answer": "B",
        "explanation": "Fragments allow you to return multiple child elements without introducing redundant wrapper `<div>` tags that can break CSS flexbox, grid, or semantic HTML structures."
    },
    {
        "id": "jr-react-13",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "Lifting State Up",
        "question": "What does 'lifting state up' mean in React?",
        "options": [
            "A) Uploading component state to an AWS S3 bucket",
            "B) Moving state to the closest common parent component so multiple child components can share it",
            "C) Converting a functional component into a Redux store",
            "D) Raising state variables to global window scope"
        ],
        "answer": "B",
        "explanation": "When two or more sibling components need access to the same state data, the standard React pattern is to lift that state up into their closest common ancestor and pass it down as props."
    },
    {
        "id": "jr-react-14",
        "level": "junior",
        "stack": "react",
        "type": "mcq",
        "topic": "Functional vs Class Components",
        "question": "Which of the following is true regarding Modern React functional components vs Class components?",
        "options": [
            "A) Class components are faster because they don't use hooks",
            "B) Functional components with hooks are the modern standard and avoid complexities like `this` binding",
            "C) Functional components cannot hold state or manage side effects",
            "D) Class components are required when fetching data from REST APIs"
        ],
        "answer": "B",
        "explanation": "Functional components combined with React Hooks are the official, modern standard in React. They eliminate `this` context binding pitfalls and simplify code sharing."
    },
    {
        "id": "jr-react-15",
        "level": "junior",
        "stack": "react",
        "type": "open",
        "topic": "React Component Lifecycle with Hooks",
        "question": "Explain how the three primary lifecycle stages of a component (mounting, updating, and unmounting) are handled using the `useEffect` hook in functional React components. Provide brief code examples.",
        "expectedKeyPoints": [
            "Mounting: useEffect with empty dependency array `[]` runs once after initial render",
            "Updating: useEffect with specific dependencies `[prop1, state1]` runs when those values change",
            "Unmounting: returning a cleanup function `return () => { ... }` from useEffect",
            "No dependencies: useEffect(() => {}) runs on every single render"
        ],
        "sampleAnswer": "In React functional components, `useEffect` unifies the component lifecycle:\n1. Mounting: Pass an empty dependency array `useEffect(() => { ... }, [])`. This runs once after the component mounts.\n2. Updating: Pass specific variables in the dependencies `useEffect(() => { ... }, [count])`. This runs whenever `count` changes.\n3. Unmounting: Return a cleanup function from inside the effect callback: `useEffect(() => { return () => { cleanup(); }; }, [])`. React calls this function when the component unmounts.\nWithout any dependency array, the effect executes after every render cycle."
    },
    {
        "id": "jr-react-16",
        "level": "junior",
        "stack": "react",
        "type": "open",
        "topic": "Rules of Hooks",
        "question": "What are the two golden 'Rules of Hooks' in React, and why do these constraints exist?",
        "expectedKeyPoints": [
            "Only call Hooks at the top level (never inside loops, conditions, or nested functions)",
            "Only call Hooks from React function components or custom Hooks",
            "React relies on the order in which Hooks are called across renders to maintain internal state pointers"
        ],
        "sampleAnswer": "The two primary rules of hooks are:\n1. Only call Hooks at the top level: Do not call hooks inside loops, conditionals, or nested functions.\n2. Only call Hooks from React function components or custom hooks: Do not call them from regular JavaScript functions or class components.\nThese rules exist because React keeps track of hook state internally using an array or linked list indexed by call order. If a hook call is skipped due to an `if` condition, the order shifts, causing subsequent hooks to receive the wrong state values."
    },
    {
        "id": "jr-react-17",
        "level": "junior",
        "stack": "react",
        "type": "open",
        "topic": "Props Drilling and Solutions",
        "question": "What is 'prop drilling' in React, what problems does it cause, and what are two common solutions to avoid it?",
        "expectedKeyPoints": [
            "Definition: Passing props through multiple layers of intermediate components that do not need them",
            "Drawbacks: Boilerplate, tight coupling, fragile refactoring",
            "Solutions: React Context API, Component Composition (passing children / slots), State management libraries (Zustand, Redux)"
        ],
        "sampleAnswer": "Prop drilling occurs when you have to pass data through multiple intermediate components in the tree that have no need for the data themselves, just to reach a deeply nested child.\nProblems: It creates tight coupling, adds boilerplate, and makes refactoring painful.\nSolutions:\n1. React Context API: Allows broadcasting state directly to any consuming component in the subtree without manual prop forwarding.\n2. Component Composition: Passing JSX components as `children` or props directly to the parent container.\n3. State Management Libraries: Tools like Zustand or Redux Toolkit."
    },
    {
        "id": "jr-react-18",
        "level": "junior",
        "stack": "react",
        "type": "open",
        "topic": "Controlled vs Uncontrolled Forms",
        "question": "Compare Controlled and Uncontrolled inputs in React. When would you use each, and how do you access the value of an uncontrolled input?",
        "expectedKeyPoints": [
            "Controlled: input value is bound to React state and updated via onChange",
            "Uncontrolled: input maintains its own internal DOM state; accessed via useRef()",
            "Use cases: Controlled for real-time validation, dynamic disabling, or synced fields; Uncontrolled for simple forms, file inputs, or performance"
        ],
        "sampleAnswer": "In a Controlled input, the value is managed entirely by React state via `value={state}` and `onChange={(e) => setState(e.target.value)}`. Every keystroke updates React state.\nIn an Uncontrolled input, the DOM retains internal control over the input. React accesses its value imperatively using a `ref` (e.g., `inputRef.current.value`).\nUse controlled inputs when you need instant input validation, formatting (like credit cards), or conditional submit button enabling. Use uncontrolled inputs for file inputs (`<input type='file'>`) or simple, unvalidated submit forms where minimal re-renders are desired."
    },

    # ------------------- NODE.JS (JUNIOR) -------------------
    {
        "id": "jr-node-01",
        "level": "junior",
        "stack": "node",
        "type": "mcq",
        "topic": "Node.js Runtime Basics",
        "question": "What is Node.js primarily built upon?",
        "options": [
            "A) The SpiderMonkey JavaScript engine and Apache HTTP server",
            "B) Google Chrome's V8 JavaScript engine and the libuv C library",
            "C) The Java Virtual Machine (JVM) and Python asyncio",
            "D) Microsoft Chakra engine and Nginx"
        ],
        "answer": "B",
        "explanation": "Node.js is an open-source, cross-platform JavaScript runtime environment built on Google Chrome's V8 JavaScript engine and libuv for handling asynchronous I/O operations."
    },
    {
        "id": "jr-node-02",
        "level": "junior",
        "stack": "node",
        "type": "mcq",
        "topic": "Single-Threaded Model",
        "question": "If Node.js is described as 'single-threaded', how does it handle non-blocking asynchronous I/O?",
        "options": [
            "A) It executes all JavaScript code across 16 operating system threads simultaneously",
            "B) The main thread runs the JavaScript event loop, while heavy I/O tasks are delegated to libuv's thread pool and OS kernel mechanisms",
            "C) It pauses the user's CPU until the network response arrives",
            "D) It compiles JavaScript directly into GPU shaders"
        ],
        "answer": "B",
        "explanation": "JavaScript execution in Node.js runs on a single main thread. However, libuv delegates asynchronous I/O (file system, DNS, cryptography, network) to OS asynchronous system calls (epoll, kqueue) and an internal C thread pool."
    },
    {
        "id": "jr-node-03",
        "level": "junior",
        "stack": "node",
        "type": "mcq",
        "topic": "Module Systems",
        "question": "What is the difference in import syntax between CommonJS and ES Modules (ESM) in Node.js?",
        "options": [
            "A) CommonJS uses `require()` and `module.exports`, while ESM uses `import` and `export`",
            "B) CommonJS uses `fetch()`, while ESM uses `include()`",
            "C) ESM can only import JSON files, while CommonJS can import anything",
            "D) CommonJS was created by WHATWG, while ESM is proprietary to Node.js"
        ],
        "answer": "A",
        "explanation": "CommonJS is the legacy Node.js module system (`const mod = require('./mod')`, `module.exports = ...`), whereas ES Modules (`import mod from './mod.js'`, `export default ...`) is the standardized ECMAScript module specification."
    },
    {
        "id": "jr-node-04",
        "level": "junior",
        "stack": "node",
        "type": "mcq",
        "topic": "package.json dependencies",
        "question": "What is the purpose of `devDependencies` in `package.json`?",
        "options": [
            "A) Packages that run only when the server is deployed to AWS production",
            "B) Packages needed only during local development and testing (e.g. linters, test runners), omitted in production builds",
            "C) Packages that cannot contain JavaScript code",
            "D) Private NPM modules that require paid subscriptions"
        ],
        "answer": "B",
        "explanation": "`devDependencies` are packages required during local development, testing, and building (like Jest, ESLint, TypeScript, Nodemon). They are excluded when running `npm install --omit=dev` in production environments."
    },
    {
        "id": "jr-node-05",
        "level": "junior",
        "stack": "node",
        "type": "mcq",
        "topic": "Event Loop Basics",
        "question": "In what order will the following code log to the console?\n```js\nconsole.log('1');\nsetTimeout(() => console.log('2'), 0);\nPromise.resolve().then(() => console.log('3'));\nconsole.log('4');\n```",
        "options": [
            "A) 1, 2, 3, 4",
            "B) 1, 4, 2, 3",
            "C) 1, 4, 3, 2",
            "D) 4, 3, 2, 1"
        ],
        "answer": "C",
        "explanation": "Synchronous code executes first ('1', '4'). Next, the microtask queue (Promises) drains before the macrotask/timer queue, logging '3'. Finally, the timer callback executes, logging '2'."
    },
    {
        "id": "jr-node-06",
        "level": "junior",
        "stack": "node",
        "type": "mcq",
        "topic": "Error Handling in Callbacks",
        "question": "What is the standard 'error-first callback' convention in Node.js?",
        "options": [
            "A) The callback returns true if an error happened",
            "B) The first parameter of the callback is reserved for an error object (or null if successful), followed by data arguments",
            "C) Errors are automatically thrown to process.exit(1)",
            "D) Callbacks must always be wrapped in a try/catch block by the caller"
        ],
        "answer": "B",
        "explanation": "In standard Node.js callback signatures `(err, result) => { ... }`, the first argument is always the error object (or null/undefined if the operation succeeded), followed by the result payload."
    },
    {
        "id": "jr-node-07",
        "level": "junior",
        "stack": "node",
        "type": "mcq",
        "topic": "File System (fs)",
        "question": "Why is using `fs.readFileSync` generally discouraged in production Node.js web servers?",
        "options": [
            "A) It is deprecated and removed in Node 20+",
            "B) It blocks the single main thread, preventing the server from handling incoming HTTP requests until the file finishes reading",
            "C) It cannot read files larger than 1 Kilobyte",
            "D) It causes an immediate memory corruption in Linux"
        ],
        "answer": "B",
        "explanation": "Synchronous file operations block the entire Node.js event loop. While `readFileSync` executes, no other I/O, timers, or network requests can be processed by the server."
    },
    {
        "id": "jr-node-08",
        "level": "junior",
        "stack": "node",
        "type": "mcq",
        "topic": "Path Module",
        "question": "Why should you use `path.join(__dirname, 'files', 'data.json')` instead of string concatenation like `__dirname + '/files/data.json'`?",
        "options": [
            "A) String concatenation is not valid JavaScript syntax in Node.js",
            "B) `path.join` automatically handles cross-platform path separators (forward slashes on POSIX vs backslashes on Windows)",
            "C) String concatenation bypasses file permissions",
            "D) `path.join` encrypts the file path"
        ],
        "answer": "B",
        "explanation": "Windows uses `\\` as directory separators, while macOS and Linux use `/`. `path.join` normalizes separators and handles trailing/leading slashes and `..` segments reliably across all platforms."
    },
    {
        "id": "jr-node-09",
        "level": "junior",
        "stack": "node",
        "type": "mcq",
        "topic": "Environment Variables",
        "question": "How do you access environment variables in a standard Node.js application?",
        "options": [
            "A) window.env.VARIABLE_NAME",
            "B) process.env.VARIABLE_NAME",
            "C) global.environment.VARIABLE_NAME",
            "D) system.getEnv('VARIABLE_NAME')"
        ],
        "answer": "B",
        "explanation": "In Node.js, environment variables passed to the process (or loaded via tools like `dotenv`) are accessible on the global `process.env` object."
    },
    {
        "id": "jr-node-10",
        "level": "junior",
        "stack": "node",
        "type": "mcq",
        "topic": "package-lock.json",
        "question": "What is the primary function of `package-lock.json`?",
        "options": [
            "A) To lock down your repository so unauthorized users cannot clone it",
            "B) To lock down the exact dependency tree version numbers and cryptographic hashes so builds are deterministic across machines",
            "C) To prevent developers from installing new packages without an admin password",
            "D) To store encrypted API keys"
        ],
        "answer": "B",
        "explanation": "`package-lock.json` guarantees reproducible and deterministic dependency installations across different environments (CI/CD, staging, production) by locking exact versions and checksums."
    },
    {
        "id": "jr-node-11",
        "level": "junior",
        "stack": "node",
        "type": "open",
        "topic": "Synchronous vs Asynchronous I/O",
        "question": "Explain the difference between synchronous (blocking) and asynchronous (non-blocking) operations in Node.js. Why is asynchronous programming critical for web servers?",
        "expectedKeyPoints": [
            "Synchronous operations block the single JavaScript thread; nothing else can run",
            "Asynchronous operations offload I/O to libuv/OS and resume via callback/Promise when ready",
            "Web servers must handle hundreds or thousands of concurrent user requests without stalling"
        ],
        "sampleAnswer": "Synchronous operations halt the execution of code until the task completes. In Node's single-threaded event loop, a synchronous file read or heavy computation prevents all other users from being served, destroying throughput.\nAsynchronous operations trigger an I/O task and register a callback or Promise. The main thread immediately continues handling other incoming HTTP requests. When the I/O operation finishes, the event loop picks up the callback and sends the response. This enables Node.js to achieve high concurrency on limited hardware."
    },
    {
        "id": "jr-node-12",
        "level": "junior",
        "stack": "node",
        "type": "open",
        "topic": "Callbacks vs Promises vs Async/Await",
        "question": "Describe the evolution of handling asynchronous code in Node.js from Callbacks to Promises and Async/Await. What problems did each iteration solve?",
        "expectedKeyPoints": [
            "Callbacks: Original approach, led to 'Callback Hell' / Pyramid of Doom and difficult error handling",
            "Promises: Provided .then() chaining, centralized .catch() error propagation, and composability (Promise.all)",
            "Async/Await: Syntactic sugar over Promises allowing asynchronous code to be read and written like synchronous code with try/catch"
        ],
        "sampleAnswer": "1. Callbacks: The earliest model where asynchronous functions accepted a callback `(err, data) => {}`. Nesting multiple dependent operations resulted in 'Callback Hell', deeply indented code, and repetitive error checks.\n2. Promises: Introduced objects representing future values with states (pending, fulfilled, rejected). Allowed chaining `.then()` and centralized error handling via `.catch()`, solving nesting issues.\n3. Async/Await: Introduced in ES2017 as syntactic sugar over Promises. Marked with `async` and `await`, it allows developers to write asynchronous code that looks and behaves like clean, linear synchronous code, using standard `try/catch` blocks."
    },

    # ------------------- EXPRESS.JS (JUNIOR) -------------------
    {
        "id": "jr-express-01",
        "level": "junior",
        "stack": "express",
        "type": "mcq",
        "topic": "Middleware Concept",
        "question": "What is the purpose of the `next()` function in Express.js middleware?",
        "options": [
            "A) It redirects the browser to the next route in the sitemap",
            "B) It passes control to the next middleware function in the request-response stack",
            "C) It immediately sends an HTTP 200 response to the client",
            "D) It restarts the Node.js server process"
        ],
        "answer": "B",
        "explanation": "If the current middleware function does not terminate the request-response cycle (e.g. by sending `res.send()`), it must call `next()` to pass execution to the subsequent middleware; otherwise, the request hangs."
    },
    {
        "id": "jr-express-02",
        "level": "junior",
        "stack": "express",
        "type": "mcq",
        "topic": "Body Parsing",
        "question": "In modern Express (v4.16+), which built-in middleware is required to parse incoming JSON request bodies?",
        "options": [
            "A) `app.use(express.bodyParser())`",
            "B) `app.use(express.json())`",
            "C) `app.use(express.parseJSON())`",
            "D) `app.use(express.urlencoded())`"
        ],
        "answer": "B",
        "explanation": "`express.json()` is built into modern Express (based on body-parser) to parse incoming requests with JSON payloads and populate `req.body`."
    },
    {
        "id": "jr-express-03",
        "level": "junior",
        "stack": "express",
        "type": "mcq",
        "topic": "Route Parameters",
        "question": "Given the route `/users/:userId/posts/:postId`, how do you access `userId` inside the route handler?",
        "options": [
            "A) `req.query.userId`",
            "B) `req.body.userId`",
            "C) `req.params.userId`",
            "D) `req.headers.userId`"
        ],
        "answer": "C",
        "explanation": "Route path parameters defined with colons (`:param`) are captured and made available on the `req.params` dictionary object."
    },
    {
        "id": "jr-express-04",
        "level": "junior",
        "stack": "express",
        "type": "mcq",
        "topic": "HTTP Status Codes",
        "question": "Which HTTP status code should be returned when a resource is successfully created via a POST endpoint?",
        "options": [
            "A) 200 OK",
            "B) 201 Created",
            "C) 204 No Content",
            "D) 301 Moved Permanently"
        ],
        "answer": "B",
        "explanation": "According to HTTP specifications, `201 Created` is the standard status code indicating that the request succeeded and led to the creation of a new resource."
    },
    {
        "id": "jr-express-05",
        "level": "junior",
        "stack": "express",
        "type": "mcq",
        "topic": "Error Handling Middleware",
        "question": "How does Express differentiate an error-handling middleware function from a regular middleware function?",
        "options": [
            "A) Error middleware must be declared with four arguments: `(err, req, res, next)`",
            "B) Error middleware must be placed at the very top of `server.js`",
            "C) Error middleware must return a Boolean value",
            "D) Error middleware must use `app.error()` instead of `app.use()`"
        ],
        "answer": "A",
        "explanation": "Express inspects the function's `length` (arity). A function with four arguments `(err, req, res, next)` is identified by Express as an error-handling middleware."
    },
    {
        "id": "jr-express-06",
        "level": "junior",
        "stack": "express",
        "type": "mcq",
        "topic": "Express Router",
        "question": "What is the primary advantage of using `express.Router()`?",
        "options": [
            "A) It automatically generates React frontend routes",
            "B) It enables modular, mountable route handlers that can be split into separate files and sub-paths",
            "C) It encrypts network traffic with TLS certificates",
            "D) It connects the backend directly to MongoDB collections"
        ],
        "answer": "B",
        "explanation": "`express.Router()` provides an isolated instance of middleware and routing systems, allowing you to organize routes cleanly into modular files and mount them at specific URL prefixes."
    },
    {
        "id": "jr-express-07",
        "level": "junior",
        "stack": "express",
        "type": "mcq",
        "topic": "Static Files",
        "question": "How do you serve static files like images and CSS from a directory named 'public' in Express?",
        "options": [
            "A) `app.serveStatic('/public')`",
            "B) `app.use(express.static('public'))`",
            "C) `app.get('*', express.fileServer('public'))`",
            "D) `app.use(express.public())`"
        ],
        "answer": "B",
        "explanation": "`express.static(root, [options])` is the built-in middleware function in Express used to serve static assets such as HTML, CSS, JavaScript, and image files."
    },
    {
        "id": "jr-express-08",
        "level": "junior",
        "stack": "express",
        "type": "open",
        "topic": "Middleware Architecture in Express",
        "question": "Explain what Express middleware is, how data flows through a middleware pipeline, and what happens if a middleware neither sends a response nor calls `next()`.",
        "expectedKeyPoints": [
            "Middleware are functions with access to req, res, and next",
            "They can execute code, modify req/res objects, end request-response cycle, or call next()",
            "If neither res is sent nor next() is invoked, the client request hangs until timeout"
        ],
        "sampleAnswer": "In Express, middleware functions execute sequentially during the request-response lifecycle. Each middleware has access to the request object (`req`), the response object (`res`), and the `next` function.\nA middleware can:\n1. Execute arbitrary logic (logging, authentication checks, parsing headers).\n2. Mutate `req` or `res` (e.g. attaching `req.user = decodedToken`).\n3. Conclude the cycle by sending a response (`res.status(200).json(...)`).\n4. Pass control to the next handler by calling `next()`.\nIf a middleware neither concludes the response nor calls `next()`, the HTTP connection remains open indefinitely until the client or server times out."
    },
    {
        "id": "jr-express-09",
        "level": "junior",
        "stack": "express",
        "type": "open",
        "topic": "Query Parameters vs Route Parameters",
        "question": "Contrast `req.params` and `req.query` in Express. Give an example URL and route definition for each, explaining when to choose one over the other.",
        "expectedKeyPoints": [
            "req.params: Part of the URL path itself, defined as placeholders (e.g. /products/:id), used to identify a specific resource",
            "req.query: Key-value pairs after the question mark (e.g. /products?category=shoes&sort=asc), used for filtering, pagination, or sorting"
        ],
        "sampleAnswer": "1. `req.params`: Used for route path parameters that uniquely identify a resource.\nExample Route: `app.get('/users/:id')`\nURL: `/users/42` -> `req.params.id === '42'`.\n2. `req.query`: Used for optional URL query strings appearing after `?` to filter, sort, search, or paginate resources.\nExample Route: `app.get('/users')`\nURL: `/users?role=admin&limit=10` -> `req.query.role === 'admin'`, `req.query.limit === '10'`.\nRule of thumb: Use route parameters for mandatory resource identity; use query parameters for optional filtering or options."
    },

    # ------------------- MONGODB & MONGOOSE (JUNIOR) -------------------
    {
        "id": "jr-mongo-01",
        "level": "junior",
        "stack": "mongodb",
        "type": "mcq",
        "topic": "NoSQL Basics",
        "question": "What data format does MongoDB use internally to store documents?",
        "options": [
            "A) Pure XML",
            "B) BSON (Binary JSON)",
            "C) YAML",
            "D) Comma-Separated Values (CSV)"
        ],
        "answer": "B",
        "explanation": "MongoDB stores data records as BSON documents. BSON is a binary representation of JSON-like documents that supports richer data types (like Date, Int64, and ObjectId) and faster traversal."
    },
    {
        "id": "jr-mongo-02",
        "level": "junior",
        "stack": "mongodb",
        "type": "mcq",
        "topic": "Primary Key in MongoDB",
        "question": "What is the default unique identifier field automatically assigned to every document in a MongoDB collection?",
        "options": [
            "A) `id`",
            "B) `_id` of type ObjectId",
            "C) `uuid`",
            "D) `pk_index`"
        ],
        "answer": "B",
        "explanation": "Every MongoDB document requires an immutable `_id` field. If omitted during insertion, MongoDB automatically creates an `_id` with a 12-byte `ObjectId`."
    },
    {
        "id": "jr-mongo-03",
        "level": "junior",
        "stack": "mongodb",
        "type": "mcq",
        "topic": "Mongoose Schema vs Model",
        "question": "In Mongoose, what is the distinction between a Schema and a Model?",
        "options": [
            "A) A Schema compiles into SQL tables, while a Model stores binary images",
            "B) A Schema defines the structure and validation rules for documents, while a Model provides the interface to query and update the MongoDB collection",
            "C) Schema is for frontend forms, Model is for Express controllers",
            "D) There is no difference; they are aliases of the same class"
        ],
        "answer": "B",
        "explanation": "A Mongoose Schema maps to a MongoDB collection and defines the document shape, default values, and validators. A Model is a compiled constructor created from a Schema that provides methods to create, query, update, and delete documents."
    },
    {
        "id": "jr-mongo-04",
        "level": "junior",
        "stack": "mongodb",
        "type": "mcq",
        "topic": "Basic MongoDB Query Operators",
        "question": "Which query operator retrieves all documents where the `age` field is greater than 18?",
        "options": [
            "A) `{ age: { $gt: 18 } }`",
            "B) `{ age: > 18 }`",
            "C) `{ age: { $moreThan: 18 } }`",
            "D) `{ age: { $above: 18 } }`"
        ],
        "answer": "A",
        "explanation": "The `$gt` (greater than) comparison operator selects documents where the value of the specified field is greater than the specified value."
    },
    {
        "id": "jr-mongo-05",
        "level": "junior",
        "stack": "mongodb",
        "type": "mcq",
        "topic": "Updating Documents",
        "question": "In native MongoDB, what happens if you run `updateOne({ _id }, { status: 'active' })` without an update operator like `$set`?",
        "options": [
            "A) MongoDB ignores the update command",
            "B) MongoDB throws an error in modern drivers because raw replacement requires `replaceOne`",
            "C) MongoDB automatically converts it to a `$set` operation",
            "D) MongoDB creates a duplicate document"
        ],
        "answer": "B",
        "explanation": "In modern MongoDB drivers, `updateOne` requires atomic update operators like `$set` or `$inc`. Supplying a plain object without update operators throws an error, preventing accidental replacement of the document."
    },
    {
        "id": "jr-mongo-06",
        "level": "junior",
        "stack": "mongodb",
        "type": "mcq",
        "topic": "Embedded vs Referenced Documents",
        "question": "When is embedding documents (denormalization) preferred over referencing (normalization) in MongoDB?",
        "options": [
            "A) When data is updated by 50 different microservices simultaneously",
            "B) When child data is tightly coupled to the parent, frequently read together, and has a 1-to-few relationship that won't exceed the 16MB document limit",
            "C) When storing unbounded audit logs spanning millions of rows",
            "D) Only when using SQLite instead of MongoDB"
        ],
        "answer": "B",
        "explanation": "Embedding documents provides high-performance atomic reads and writes without joins when child records belong exclusively to the parent and will not grow unboundedly past the 16MB BSON limit."
    },
    {
        "id": "jr-mongo-07",
        "level": "junior",
        "stack": "mongodb",
        "type": "open",
        "topic": "SQL vs NoSQL (MongoDB)",
        "question": "Compare MongoDB to a traditional relational database (like PostgreSQL). What are the key architectural differences in schema flexibility, relationships, and transactions?",
        "expectedKeyPoints": [
            "Schema: MongoDB is schema-less/schema-flexible (JSON/BSON docs); SQL requires rigid tables with predefined columns",
            "Relationships: MongoDB favors embedding or manual references; SQL uses foreign keys and relational JOINs",
            "Transactions: Relational databases are built for multi-table ACID transactions; MongoDB supports transactions but focuses on document-level atomicity"
        ],
        "sampleAnswer": "1. Schema Flexibility: MongoDB documents are self-describing BSON records. Different documents in a collection can have different fields, allowing rapid iterations. Relational databases enforce rigid tabular schemas with explicit column data types.\n2. Relationships & Joins: Relational databases use primary/foreign keys with powerful JOIN operations. MongoDB favors embedding related data within the same document for fast single-lookup reads, or using `$lookup` for references.\n3. Scaling: Relational databases traditionally scale vertically. MongoDB was designed from the ground up for horizontal scaling and sharding across distributed clusters.\n4. Transactions: While MongoDB now supports multi-document ACID transactions, its core performance sweet spot is single-document atomic updates."
    },
    {
        "id": "jr-mongo-08",
        "level": "junior",
        "stack": "mongodb",
        "type": "open",
        "topic": "Mongoose Population",
        "question": "What is Mongoose `.populate()` and how does it simulate a relational join? What are its performance trade-offs?",
        "expectedKeyPoints": [
            "Replaces an ObjectId reference with the actual referenced document from another collection",
            "Under the hood, Mongoose makes additional queries to the referenced collection",
            "Performance trade-off: Multiple round-trips to the database; not as efficient as a native database engine JOIN or embedded documents"
        ],
        "sampleAnswer": "In Mongoose, `.populate()` replaces a stored `ObjectId` reference in one document with the actual document data from another collection.\nHow it works: It is not a native database join. Under the hood, Mongoose executes the primary query, collects the referenced ObjectIds, executes a secondary query against the foreign collection, and merges the results in Node.js memory.\nTrade-offs: While convenient, heavy use of `.populate()` introduces multiple database round-trips, network overhead, and high memory usage compared to native joins or properly modeled embedded documents."
    },

    # ------------------- POSTGRESQL (JUNIOR) -------------------
    {
        "id": "jr-pg-01",
        "level": "junior",
        "stack": "postgresql",
        "type": "mcq",
        "topic": "Primary vs Foreign Keys",
        "question": "What is the primary role of a FOREIGN KEY constraint in PostgreSQL?",
        "options": [
            "A) It prevents users from outside the local network from querying the table",
            "B) It enforces referential integrity by ensuring the value in a child table column matches an existing primary or unique key in a parent table",
            "C) It encrypts column values using public key cryptography",
            "D) It automatically indexes all text columns in alphabetical order"
        ],
        "answer": "B",
        "explanation": "A Foreign Key establishes a relationship between two tables, ensuring that records cannot point to non-existent parent rows and preventing orphaned records when updates or deletions occur."
    },
    {
        "id": "jr-pg-02",
        "level": "junior",
        "stack": "postgresql",
        "type": "mcq",
        "topic": "SQL Joins",
        "question": "What is the difference between an `INNER JOIN` and a `LEFT JOIN`?",
        "options": [
            "A) `INNER JOIN` returns only rows that have matching values in both tables, while `LEFT JOIN` returns all rows from the left table plus matching rows from the right table (with NULLs for non-matches)",
            "B) `INNER JOIN` sorts ascending; `LEFT JOIN` sorts descending",
            "C) `LEFT JOIN` only works on numbers; `INNER JOIN` works on strings",
            "D) `INNER JOIN` deletes unmatched rows from disk"
        ],
        "answer": "A",
        "explanation": "`INNER JOIN` filters out any rows that lack a match in either table. `LEFT JOIN` guarantees that every record from the left table is returned; if there is no match on the right, the right-side columns are filled with `NULL`."
    },
    {
        "id": "jr-pg-03",
        "level": "junior",
        "stack": "postgresql",
        "type": "mcq",
        "topic": "SQL Injection",
        "question": "How do you prevent SQL Injection vulnerabilities when querying PostgreSQL from Node.js (e.g. using `pg` library)?",
        "options": [
            "A) Wrap all input strings with `escape()` in JavaScript",
            "B) Use parameterized queries with placeholders like `$1, $2`, letting the database driver handle value separation and escaping",
            "C) Only use GET requests for database lookups",
            "D) Run Node.js with the `--no-sql-injection` flag"
        ],
        "answer": "B",
        "explanation": "Parameterized queries separate the SQL command code from user-supplied data values. The database treats `$1` strictly as a literal parameter, making it impossible for malicious SQL commands to alter query structure."
    },
    {
        "id": "jr-pg-04",
        "level": "junior",
        "stack": "postgresql",
        "type": "mcq",
        "topic": "Data Types in PostgreSQL",
        "question": "Which PostgreSQL data type is recommended for storing arbitrary structured JSON data with indexing and query capabilities?",
        "options": [
            "A) `VARCHAR(MAX)`",
            "B) `JSONB`",
            "C) `BLOB`",
            "D) `TEXT_ARRAY`"
        ],
        "answer": "B",
        "explanation": "`JSONB` stores JSON data in a decomposed binary format. It supports GIN indexing, fast path lookups, and rich query operators, making it superior to plain `JSON` for querying and filtering."
    },
    {
        "id": "jr-pg-05",
        "level": "junior",
        "stack": "postgresql",
        "type": "mcq",
        "topic": "ACID Properties",
        "question": "What does the 'A' in ACID transactions stand for, and what does it mean?",
        "options": [
            "A) Asynchronous: Queries run on background threads without waiting",
            "B) Atomicity: All operations in a transaction either succeed completely or fail completely with nothing committed",
            "C) Availability: The database is guaranteed to respond 100% of the time",
            "D) Authorization: Only valid database users can execute queries"
        ],
        "answer": "B",
        "explanation": "Atomicity ensures that a series of database operations either execute in full ('all') or abort with all changes rolled back ('nothing'), preventing partial updates."
    },
    {
        "id": "jr-pg-06",
        "level": "junior",
        "stack": "postgresql",
        "type": "mcq",
        "topic": "Basic SQL Constraints",
        "question": "Which constraint ensures that no two rows can have the same value in a specific column, while still allowing NULL values unless combined with NOT NULL?",
        "options": [
            "A) `CHECK`",
            "B) `UNIQUE`",
            "C) `DEFAULT`",
            "D) `PRIMARY KEY`"
        ],
        "answer": "B",
        "explanation": "A `UNIQUE` constraint enforces uniqueness for non-null values across rows. Unlike `PRIMARY KEY`, it permits `NULL` values (unless `NOT NULL` is explicitly added) and tables can have multiple unique constraints."
    },
    {
        "id": "jr-pg-07",
        "level": "junior",
        "stack": "postgresql",
        "type": "open",
        "topic": "Database Normalization Basics",
        "question": "Explain the concept of database normalization and describe the first three normal forms (1NF, 2NF, 3NF) in simple terms.",
        "expectedKeyPoints": [
            "Goal: Reduce data redundancy and prevent update/delete anomalies",
            "1NF: Atomic values (no comma-separated lists or arrays), each row uniquely identifiable with a primary key",
            "2NF: In 1NF and all non-key columns depend on the entire primary key (no partial dependencies on composite keys)",
            "3NF: In 2NF and no transitive dependencies (non-key columns do not depend on other non-key columns)"
        ],
        "sampleAnswer": "Database normalization organizes tables to minimize data duplication and prevent insertion, update, and deletion anomalies.\n- 1NF (First Normal Form): Data is organized into rows and columns, each cell contains a single atomic value (no lists or nested objects), and each row has a primary key.\n- 2NF (Second Normal Form): Meets 1NF, and all non-key attributes are fully functionally dependent on the primary key (no partial dependencies on part of a composite key).\n- 3NF (Third Normal Form): Meets 2NF, and no non-key attribute depends on another non-key attribute (no transitive dependencies; 'every attribute must depend on the key, the whole key, and nothing but the key')."
    },
    {
        "id": "jr-pg-08",
        "level": "junior",
        "stack": "postgresql",
        "type": "open",
        "topic": "ORMs vs Raw SQL (Node/Postgres)",
        "question": "Compare using an ORM/Query Builder (like Prisma or Sequelize) versus writing raw SQL queries using the `pg` driver in a Node.js project. What are the pros and cons of each?",
        "expectedKeyPoints": [
            "ORM Pros: Type safety, autocompletion, migrations, developer productivity, abstraction from SQL syntax",
            "ORM Cons: Performance overhead, potential N+1 query problem, complex queries can become awkward to write",
            "Raw SQL Pros: Maximum performance, complete control over query plans, ability to leverage PostgreSQL-specific features",
            "Raw SQL Cons: Vulnerable to SQL injection if not parameterized, manual type casting, tedious schema maintenance"
        ],
        "sampleAnswer": "1. ORMs / Query Builders (e.g. Prisma, Sequelize, Kysely):\n- Pros: Accelerate development, provide automated migrations, offer compile-time type safety with TypeScript, and eliminate manual query formatting.\n- Cons: Can generate inefficient SQL (such as N+1 query loops), add abstraction overhead, and make complex reporting or window functions difficult to express.\n2. Raw SQL with `pg`:\n- Pros: Unmatched performance, zero abstraction overhead, direct control over `EXPLAIN ANALYZE` execution plans, and full access to advanced PostgreSQL features (CTEs, JSONB operators, triggers).\n- Cons: Developers must write repetitive mapping code, manage migrations manually, and strictly use parameterized queries to avoid SQL injection vulnerabilities."
    },

    # ------------------- FULLSTACK / SECURITY / REST (JUNIOR) -------------------
    {
        "id": "jr-full-01",
        "level": "junior",
        "stack": "fullstack",
        "type": "mcq",
        "topic": "CORS (Cross-Origin Resource Sharing)",
        "question": "What triggers a browser CORS error when your React app (running on localhost:3000) makes a fetch request to your Express API (running on localhost:5000)?",
        "options": [
            "A) The Node.js server crashed due to out of memory",
            "B) The browser enforces the Same-Origin Policy, and the Express server did not respond with the appropriate `Access-Control-Allow-Origin` header",
            "C) Port 5000 is reserved exclusively for operating system services",
            "D) React requires all fetch requests to be sent via HTTPS only"
        ],
        "answer": "B",
        "explanation": "Different ports constitute different origins under the browser's Same-Origin Policy. The browser blocks cross-origin responses unless the server explicitly grants permission via CORS response headers like `Access-Control-Allow-Origin`."
    },
    {
        "id": "jr-full-02",
        "level": "junior",
        "stack": "fullstack",
        "type": "mcq",
        "topic": "RESTful Principles",
        "question": "Which HTTP method should be used to partially update an existing resource according to standard REST conventions?",
        "options": [
            "A) PUT",
            "B) PATCH",
            "C) POST",
            "D) GET"
        ],
        "answer": "B",
        "explanation": "`PATCH` is designated for partial updates (updating specific fields of a resource), whereas `PUT` is designed to completely replace the target resource."
    },
    {
        "id": "jr-full-03",
        "level": "junior",
        "stack": "fullstack",
        "type": "mcq",
        "topic": "Authentication Basics",
        "question": "Why is storing JWT authentication tokens in `HttpOnly` cookies generally more secure against XSS attacks than storing them in browser `localStorage`?",
        "options": [
            "A) HttpOnly cookies are stored directly on the user's hard drive in an encrypted vault",
            "B) JavaScript running in the browser cannot read or access HttpOnly cookies, preventing stolen tokens via Cross-Site Scripting (XSS)",
            "C) HttpOnly cookies automatically delete themselves every 5 minutes",
            "D) LocalStorage can only hold up to 10 characters"
        ],
        "answer": "B",
        "explanation": "If a site has an XSS vulnerability, malicious scripts can easily read tokens from `localStorage` (`window.localStorage.getItem(...)`). An `HttpOnly` cookie cannot be accessed via JavaScript, insulating the token from XSS extraction."
    },
    {
        "id": "jr-full-04",
        "level": "junior",
        "stack": "fullstack",
        "type": "mcq",
        "topic": "Environment Variables Security",
        "question": "Why should `.env` files never be committed to a public Git repository?",
        "options": [
            "A) Git will refuse to push files that start with a period",
            "B) They contain sensitive secrets like database credentials, API keys, and JWT signing secrets that attackers can exploit",
            "C) Linux file permissions break if `.env` is pushed to GitHub",
            "D) It corrupts the npm cache"
        ],
        "answer": "B",
        "explanation": "`.env` files store plain-text secrets. Committing them exposes sensitive credentials to automated scrapers and malicious actors on public version control."
    },
    {
        "id": "jr-full-05",
        "level": "junior",
        "stack": "fullstack",
        "type": "open",
        "topic": "Client-Server Architecture in PERN/MERN",
        "question": "Trace what happens under the hood when a user clicks 'Submit' on a React form to create a new user profile until data is stored in the database and a confirmation is shown in the UI.",
        "expectedKeyPoints": [
            "Client event handled in React (e.g. onSubmit with e.preventDefault())",
            "Fetch/Axios sends HTTP POST request with JSON payload and auth headers over network",
            "Express server receives request, runs middleware (cors, json parser, auth)",
            "Controller validates data and invokes database query (pg INSERT or mongoose create)",
            "Database executes query, returns newly created record",
            "Express sends 201 response with JSON body",
            "React receives response, updates state, renders success feedback"
        ],
        "sampleAnswer": "1. In React, the user submits the form. The `onSubmit` handler calls `e.preventDefault()` to stop the browser's default full-page reload.\n2. React gathers state and sends an asynchronous HTTP POST request (via `fetch` or `axios`) with a JSON body and headers (e.g. `Content-Type: application/json`, auth token).\n3. In Express, the request hits the server. Middleware executes: CORS validates the origin, `express.json()` parses the request body, and auth middleware verifies the session or token.\n4. The route controller validates fields and calls the database layer (Mongoose `User.create()` for MERN, or `pool.query('INSERT INTO users...')` for PERN).\n5. The database inserts the record, assigns an ID, and returns the row.\n6. Express sends an HTTP `201 Created` status code with the new record in the JSON response body.\n7. React's promise resolves; the component updates its state with the returned data and renders a success message."
    }
]

# We will supplement this list programmatically to reach 105+ high quality questions
print(f"Base Junior questions count: {len(questions)}")
