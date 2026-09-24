import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';
import { getQuestions, getBankStats } from './data/index.js';
import { loadConfig, saveConfig, hasAnyApiKey } from './ai/config.js';
import { aiService } from './ai/provider.js';
import { AIAnswerAnalyzer } from './ai/analyzer.js';
import {
  loadStats,
  recordMCQResult,
  recordOpenResult,
  toggleBookmark,
  isBookmarked
} from './utils/storage.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());
app.use(express.static(path.join(__dirname, '..', 'public')));

// ─── Question Bank ───────────────────────────────────────────────

app.get('/api/stats', (req, res) => {
  try {
    const stats = getBankStats();
    res.json(stats);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get('/api/questions', (req, res) => {
  try {
    const { level, stack, type, topic, limit } = req.query;
    const questions = getQuestions({
      level: level || 'all',
      stack: stack || 'all',
      type: type || 'all',
      topic: topic || '',
      limit: limit ? parseInt(limit, 10) : 0,
      shuffle: true
    });
    res.json(questions);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ─── MCQ Check ───────────────────────────────────────────────────

app.post('/api/check-mcq', (req, res) => {
  try {
    const { questionId, selectedOption, question } = req.body;
    const isCorrect = selectedOption === question.answer;

    // Record result
    recordMCQResult(question, selectedOption, isCorrect);

    res.json({
      correct: isCorrect,
      correctAnswer: question.answer,
      explanation: question.explanation || ''
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ─── AI Evaluation ───────────────────────────────────────────────

app.post('/api/evaluate', async (req, res) => {
  try {
    const { question, level, stack, topic, expectedKeyPoints, sampleAnswer, userAnswer } = req.body;

    const result = await AIAnswerAnalyzer.evaluateAnswer({
      question,
      level,
      stack,
      topic,
      expectedKeyPoints: expectedKeyPoints || [],
      sampleAnswer: sampleAnswer || '',
      userAnswer
    });

    res.json(result);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/explain-mcq', async (req, res) => {
  try {
    const { question, options, answer, explanation, topic, level } = req.body;
    const result = await AIAnswerAnalyzer.explainMCQ({
      question, options, answer, explanation, topic, level
    });
    res.json(result);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ─── AI Configuration ───────────────────────────────────────────

app.get('/api/config', (req, res) => {
  try {
    const config = loadConfig();
    res.json({
      primaryProvider: config.primaryProvider,
      autoFallback: config.autoFallback,
      hasGeminiKey: !!config.gemini.apiKey,
      hasOpenrouterKey: !!config.openrouter.apiKey,
      geminiModel: config.gemini.model,
      openrouterModel: config.openrouter.model
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/config', (req, res) => {
  try {
    const { primaryProvider, geminiKey, openrouterKey } = req.body;
    const update = {};

    if (primaryProvider) update.primaryProvider = primaryProvider;
    if (geminiKey !== undefined) update.gemini = { apiKey: geminiKey };
    if (openrouterKey !== undefined) update.openrouter = { apiKey: openrouterKey };

    const saved = saveConfig(update);
    aiService.reloadConfig();

    res.json({ success: saved });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/test-provider', async (req, res) => {
  try {
    const { provider } = req.body;
    aiService.reloadConfig();
    const ok = await aiService.testProvider(provider);
    res.json({ success: ok, provider });
  } catch (err) {
    res.status(500).json({ error: err.message, provider: req.body.provider });
  }
});

// ─── User Stats & Storage ────────────────────────────────────────

app.get('/api/user-stats', (req, res) => {
  try {
    const stats = loadStats();
    res.json(stats);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/bookmark', (req, res) => {
  try {
    const { question } = req.body;
    const bookmarked = toggleBookmark(question);
    res.json({ bookmarked });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get('/api/bookmarks', (req, res) => {
  try {
    const stats = loadStats();
    res.json(stats.bookmarks || []);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get('/api/wrong-questions', (req, res) => {
  try {
    const stats = loadStats();
    res.json(stats.wrongQuestions || []);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/record-open', (req, res) => {
  try {
    const { question, score, usedProvider } = req.body;
    recordOpenResult(question, score, usedProvider);
    res.json({ success: true });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ─── Fallback to index.html for SPA ──────────────────────────────

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'public', 'index.html'));
});

// ─── Start ───────────────────────────────────────────────────────

app.listen(PORT, () => {
  console.log(`
╔══════════════════════════════════════════════╗
║                                              ║
║   ▄▄▄▄▄▄  ▄▄▄▄▄▄  ▄▄▄▄▄▄  ▄▄▄▄▄▄  ▄▄▄▄▄▄  ║
║   █  ▄▄█  █  ▄▄█  █  ▄▄█  █  ▄▄█  █  ▄▄█  ║
║   █  ██▄  █  ██▄  █  ██▄  █  ██▄  █  ██▄  ║
║   ▀▀▀▀▀▀  ▀▀▀▀▀▀  ▀▀▀▀▀▀  ▀▀▀▀▀▀  ▀▀▀▀▀▀  ║
║                                              ║
║          PrepPro Web UI v1.0.0               ║
║     PERN / MERN Interview Prep Coach         ║
║                                              ║
║   🌐 http://localhost:${PORT}                    ║
║                                              ║
╚══════════════════════════════════════════════╝
`);
});
