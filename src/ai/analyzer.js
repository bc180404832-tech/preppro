import { aiService } from './provider.js';

/**
 * AI Answer Analyzer for PERN / MERN Technical Interviews
 */
export class AIAnswerAnalyzer {
  /**
   * Analyzes an open-ended candidate answer
   */
  static async evaluateAnswer({
    question,
    level, // 'junior' | 'mid' | 'senior'
    stack, // 'pern' | 'mern' | 'node' | 'react' | 'mongodb' | 'postgresql' | 'express'
    topic,
    expectedKeyPoints = [],
    sampleAnswer = '',
    userAnswer
  }, onStatusUpdate) {
    const systemPrompt = `You are a Principal Software Architect and seasoned Senior Technical Interviewer conducting technical assessments for Full-Stack PERN (PostgreSQL, Express, React, Node.js) and MERN (MongoDB, Express, React, Node.js) developers.
Your job is to objectively, constructively, and rigorously evaluate candidate responses across three engineering seniority levels:
- JUNIOR: Assess fundamental understanding, accurate terminology, correct core mechanics, and basic syntax.
- MID-LEVEL: Assess architectural awareness, error handling, performance considerations, edge cases, state management, and best practices.
- SENIOR: Assess deep internals (event loop, database locking/MVCC, V8 memory, sharding/partitioning, React fiber reconciliation), scalability, security (OWASP), trade-offs, fault-tolerance, and production resilience.

Be honest, encouraging, and highly technical. If an answer has factual errors or security vulnerabilities, point them out clearly.`;

    const userPrompt = `EVALUATION TASK:
Target Level: ${level.toUpperCase()}
Topic: ${topic} (Stack: ${stack.toUpperCase()})

Question:
"${question}"

Key Rubric Points Expected:
${expectedKeyPoints.map((pt, i) => `${i + 1}. ${pt}`).join('\n') || 'Comprehensive technical explanation'}

${sampleAnswer ? `Reference Model Answer Reference:\n"${sampleAnswer}"\n` : ''}

Candidate's Submitted Answer:
"""
${userAnswer}
"""

Please provide your evaluation formatted strictly in the following Markdown structure:

### SCORE: [Number between 0.0 and 10.0]/10
### VERDICT: [One short phrase, e.g., "Exceeds Senior Expectations", "Solid Mid-Level Response", "Minor Technical Gaps", or "Requires Review of Fundamentals"]

### 🎯 Key Strengths
- [Point 1: What was accurate, precise, or well-explained]
- [Point 2...]

### ⚠️ Gaps & Missing Crucial Points
- [Point 1: Omitted edge cases, concurrency hazards, performance gotchas, or security considerations]
- [Point 2...]

### 💡 Level-Specific Feedback (${level.toUpperCase()})
[Provide actionable guidance on what would take this answer to the next level (e.g. from Junior to Mid or Mid to Senior), citing specific patterns, APIs, or architectural trade-offs.]

### 🏆 Exemplary Senior-Level Model Answer
[Provide a crisp, production-grade model answer with concise code snippets if applicable, illustrating best practices.]`;

    const result = await aiService.executeWithFallback(userPrompt, systemPrompt, onStatusUpdate);
    return {
      rawOutput: result.text,
      usedProvider: result.usedProvider,
      fallbackTriggered: result.fallbackTriggered
    };
  }

  /**
   * Quick AI explanation for an MCQ question if candidate wants deeper context
   */
  static async explainMCQ({ question, options, answer, explanation, topic, level }, onStatusUpdate) {
    const prompt = `Explain why option "${answer}" is correct and why other options are incorrect or suboptimal for this ${level} level PERN/MERN question.

Topic: ${topic}
Question: ${question}
Options:
${options.join('\n')}

Official Brief Explanation: ${explanation}

Please give a concise, high-impact breakdown:
1. Why the correct answer is technically right.
2. The core misconception behind the distractor options.
3. Real-world production implication or gotcha.`;

    const result = await aiService.executeWithFallback(prompt, 'You are an elite PERN/MERN interview tutor.', onStatusUpdate);
    return result;
  }
}
