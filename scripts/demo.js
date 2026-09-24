#!/usr/bin/env node
import chalk from 'chalk';
import { ui } from '../src/cli/ui.js';
import { getQuestions } from '../src/data/index.js';

console.clear();

// 1. Show Banner
ui.banner('PERN', 'SENIOR', 'GEMINI');

console.log(chalk.bold.cyan('--- Sample Senior PERN MCQ Question ---\n'));

// 2. Fetch a real Senior PERN Question
const seniorQ = getQuestions({ level: 'senior', stack: 'postgresql', type: 'mcq', shuffle: false })[0];
ui.renderQuestionCard(seniorQ, 1, 10);

console.log(chalk.bold.yellow('Options:'));
seniorQ.options.forEach(opt => {
  console.log(`  ${opt}`);
});
console.log('');

// 3. Render Instant Feedback
ui.renderMCQFeedback(true, seniorQ.answer, seniorQ.explanation);

console.log(chalk.bold.cyan('\n--- Sample AI Evaluated Technical Interview Answer ---\n'));

// 4. Fetch an Open Question
const openQ = getQuestions({ level: 'senior', stack: 'react', type: 'open', shuffle: false })[0];
ui.renderQuestionCard(openQ, 2, 10);

console.log(chalk.bold.yellow('Candidate Submitted Answer:'));
console.log(chalk.italic.white(`"In React Fiber, rendering is split into two phases: the render phase which is interruptible and builds the workInProgress tree, and the commit phase which is synchronous and mutates the DOM. The work loop uses shouldYield() to check deadlines and cooperate with the browser scheduler."\n`));

// 5. Render AI Feedback
const sampleAiOutput = `### SCORE: 9.0/10
### VERDICT: Strong Senior-Level Grasp of Fiber Concurrency

### 🎯 Key Strengths
- Accurately differentiated between the interruptible **Render Phase** and the synchronous **Commit Phase**.
- Correctly identified the **Double Buffering** pattern with the \`workInProgress\` tree and cooperative scheduling via \`shouldYield()\`.

### ⚠️ Gaps & Missing Crucial Points
- Could explicitly mention the **Fiber node linked-list structure** (\`child\`, \`sibling\`, \`return\` pointers) which eliminates call stack recursion.
- Mentioning **Time-slicing** (typically 5ms budget using \`MessageChannel\`) would make the response elite.

### 💡 Level-Specific Feedback (SENIOR)
For staff/senior roles, emphasize how Fiber prevents UI tearing with \`useSyncExternalStore\` and how priority lanes (\`SyncLane\`, \`InputContinuousLane\`, \`DefaultLane\`) schedule updates.

### 🏆 Exemplary Senior-Level Model Answer
\`\`\`javascript
// React Fiber Concurrent Work Loop
function workLoopConcurrent() {
  while (workInProgress !== null && !shouldYield()) {
    performUnitOfWork(workInProgress);
  }
}
\`\`\`
Fiber models components as linked-list work units. React pauses reconciliation when the 5ms slice expires, yielding to browser layout/paint, then resumes.`;

ui.renderAIEvaluation(sampleAiOutput, 'GOOGLE AI STUDIO (Fallback: OPENROUTER)');

// 6. Show Session Summary
ui.renderSummary({
  total: 10,
  correct: 7,
  openCount: 2,
  avgScore: 9.0,
  timeSpent: '4m 32s'
});

console.log(chalk.green.bold('\n✔ Demo rendered successfully!\n'));
