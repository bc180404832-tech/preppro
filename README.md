# PrepPro 🚀
> Minimal Terminal UI for **PERN** and **MERN** Developer Interview Preparation with AI Evaluation & Rate-Limit Fallback.

PrepPro is a dedicated, production-grade terminal CLI application designed for software engineers preparing for **Junior**, **Mid-Level (Middle)**, and **Senior** fullstack technical interviews across the **PERN** (PostgreSQL, Express, React, Node.js) and **MERN** (MongoDB, Express, React, Node.js) ecosystems.

---

## ✨ Features

- 🎯 **330+ Production-Grade Technical Questions**:
  - **110 Questions** for **Junior** level (syntax, core mechanics, lifecycle, basic APIs).
  - **110 Questions** for **Mid-Level** (design patterns, error handling, state architecture, database query optimization).
  - **110 Questions** for **Senior** (React Fiber internals, V8 memory & GC, MVCC/bloat, sharding, distributed rate limiting, zero-downtime migrations, system design).
- 🔄 **PERN & MERN Coverage**:
  - Filter specifically for **PERN** (PostgreSQL, Express, React, Node.js), **MERN** (MongoDB, Express, React, Node.js), or individual topics.
- 🧪 **Dual Assessment Formats**:
  - **MCQ Practice Mode**: 4-choice questions with instant grading, answers, and technical explanations.
  - **AI Technical Interview Mode**: Open-ended conceptual, architectural, and debugging questions analyzed live by an AI interviewer.
  - **Mixed Rapid Fire**: Combines both formats for realistic mock interviews.
- ⚡ **AI-Powered Answer Analysis & Auto-Fallback**:
  - Evaluates your responses with an engineering rubric: **Score (/10)**, **Verdict**, **Key Strengths**, **Missing Points / Gaps**, and an **Exemplary Senior Model Answer**.
  - Powered by **Google AI Studio (Gemini)** or **OpenRouter**.
  - **Automatic Rate-Limit Fallback Cascade**: If your primary provider gets rate-limited (`HTTP 429` / quota exceeded), PrepPro seamlessly switches to your fallback provider without crashing or interrupting your interview session!
- 🖥️ **Minimal Terminal UI (TUI)**:
  - Clean boxes (`boxen`), vibrant formatting (`chalk`), animated spinners (`ora`), and rich terminal Markdown rendering (`marked-terminal`).
  - Interactive arrow-key navigation via `@inquirer/prompts`.
  - Works 100% out of the box even without API keys (MCQ practice and built-in model rubrics work offline).
- 🔖 **Bookmarks & Weak Spot Tracker**:
  - Automatically records incorrect answers and lets you bookmark challenging questions to revisit later in **Review Mode**.

---

## 📊 Question Bank Distribution

| Level | Total Questions | MCQs | AI Open Interview Qs | React | Node.js | Express.js | MongoDB | PostgreSQL | Fullstack & System Design |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 🟢 **Junior** | **110** | 87 | 23 | 22 | 20 | 18 | 18 | 18 | 14 |
| 🟡 **Mid-Level** | **110** | 74 | 36 | 22 | 20 | 18 | 18 | 18 | 14 |
| 🔴 **Senior** | **110** | 72 | 38 | 26 | 20 | 16 | 16 | 16 | 16 |
| **TOTAL** | **330** | **233** | **97** | **70** | **60** | **52** | **52** | **52** | **44** |

---

## 🚀 Quick Start

### 1. Installation

```bash
git clone https://github.com/bc180404832-tech/preppro.git
cd preppro
npm install
npm link
```

### 2. Run Interactively

Launch the full interactive TUI menu:

```bash
preppro
# or
npm start
```

### 3. CLI Direct Mode (Flag Shortcuts)

You can bypass menus and launch directly into a quiz:

```bash
# Senior PERN MCQ session (10 questions)
preppro --level senior --stack pern --mode mcq --num 10

# Mid-Level MERN AI Open-ended Interview (5 questions)
preppro --level mid --stack mern --mode open --num 5

# View Question Bank Statistics
preppro --stats
```

---

## 🔑 AI Setup & Rate-Limit Fallback

PrepPro supports both **Google AI Studio (Gemini)** and **OpenRouter**.

### Option A: Configure inside the TUI
1. Start `preppro` and select **Option 5: Settings & AI Provider**.
2. Paste your Google AI Studio or OpenRouter API key.
3. Test connectivity with the built-in connection tester.
4. Toggle primary provider and auto-fallback. Keys are safely saved in `~/.preppro/config.json`.

### Option B: Configure via `.env`
Create a `.env` file in the project root:

```env
# Google AI Studio
GEMINI_API_KEY=your_gemini_api_key_here

# OpenRouter
OPENROUTER_API_KEY=your_openrouter_api_key_here

# Primary provider ('gemini' or 'openrouter')
PREPPRO_PRIMARY_PROVIDER=gemini
```

### ⚡ How the Rate-Limit Fallback Works
When you submit an answer in AI Interview mode:
1. PrepPro calls your primary provider (e.g. Google Gemini).
2. If Google AI Studio returns `HTTP 429 Too Many Requests` or `RESOURCE_EXHAUSTED`, PrepPro detects the rate-limit, displays a notice:
   ```
   ⚠️ Rate limit reached on GEMINI! Switching automatically to fallback provider OPENROUTER...
   ```
3. The request is immediately retried on OpenRouter, ensuring zero disruption during practice!
4. You can also manually switch providers anytime in the Settings menu.

---

## 📁 Project Architecture

```
preppro/
├── bin/
│   └── preppro.js              # Executable CLI entrypoint (Commander + flags)
├── src/
│   ├── index.js                # Core orchestrator and main menu loop
│   ├── ai/
│   │   ├── config.js           # API key management and persistence (~/.preppro/config.json)
│   │   ├── provider.js         # Gemini & OpenRouter service with auto-fallback cascade
│   │   └── analyzer.js         # Rubric evaluation prompt engineering
│   ├── cli/
│   │   ├── ui.js               # Terminal styling, banners, cards, markdown parser
│   │   ├── menus.js            # Interactive prompts & settings submenus
│   │   └── session.js          # Assessment session lifecycle & state tracking
│   ├── data/
│   │   ├── index.js            # Question query and filtering engine
│   │   ├── junior.json         # 110 Junior questions
│   │   ├── mid.json            # 110 Mid-Level questions
│   │   └── senior.json         # 110 Senior questions
│   └── utils/
│       └── storage.js          # User progress, bookmarks, and weak spot tracking
└── test/
    ├── validate-questions.js   # Verifies question schema integrity and counts
    └── test-app-logic.js       # Verifies filtering, storage, and 429 fallback
```

---

## 🧪 Testing

Run the automated test suite verifying question validity, schema integrity, and the simulated rate-limit fallback engine:

```bash
npm test
```

---

## 📄 License
ISC