import fs from 'fs';
import path from 'path';
import os from 'os';

const PREPPRO_DIR = path.join(os.homedir(), '.preppro');
const STATS_FILE = path.join(PREPPRO_DIR, 'stats.json');

const DEFAULT_STATS = {
  totalAnswered: 0,
  mcqCorrect: 0,
  mcqTotal: 0,
  openAnswered: 0,
  history: [],
  bookmarks: [],
  wrongQuestions: []
};

export function loadStats() {
  try {
    if (fs.existsSync(STATS_FILE)) {
      const data = JSON.parse(fs.readFileSync(STATS_FILE, 'utf-8'));
      return { ...DEFAULT_STATS, ...data };
    }
  } catch (err) {
    // Return default on error
  }
  return { ...DEFAULT_STATS };
}

export function saveStats(stats) {
  try {
    if (!fs.existsSync(PREPPRO_DIR)) {
      fs.mkdirSync(PREPPRO_DIR, { recursive: true });
    }
    fs.writeFileSync(STATS_FILE, JSON.stringify(stats, null, 2), 'utf-8');
    return true;
  } catch (err) {
    return false;
  }
}

export function recordMCQResult(question, selectedOption, isCorrect) {
  const stats = loadStats();
  stats.totalAnswered += 1;
  stats.mcqTotal += 1;
  if (isCorrect) {
    stats.mcqCorrect += 1;
  } else {
    // Add to wrongQuestions if not already present
    if (!stats.wrongQuestions.some(q => q.id === question.id)) {
      stats.wrongQuestions.push({
        id: question.id,
        question: question.question,
        stack: question.stack,
        level: question.level,
        topic: question.topic,
        type: 'mcq',
        yourAnswer: selectedOption,
        correctAnswer: question.answer,
        timestamp: new Date().toISOString()
      });
    }
  }
  saveStats(stats);
}

export function recordOpenResult(question, score, usedProvider) {
  const stats = loadStats();
  stats.totalAnswered += 1;
  stats.openAnswered += 1;
  stats.history.push({
    id: question.id,
    topic: question.topic,
    level: question.level,
    stack: question.stack,
    score,
    provider: usedProvider,
    timestamp: new Date().toISOString()
  });
  saveStats(stats);
}

export function toggleBookmark(question) {
  const stats = loadStats();
  const index = stats.bookmarks.findIndex(b => b.id === question.id);
  let bookmarked = false;
  if (index >= 0) {
    stats.bookmarks.splice(index, 1);
    bookmarked = false;
  } else {
    stats.bookmarks.push({
      id: question.id,
      level: question.level,
      stack: question.stack,
      type: question.type,
      topic: question.topic,
      question: question.question,
      timestamp: new Date().toISOString()
    });
    bookmarked = true;
  }
  saveStats(stats);
  return bookmarked;
}

export function isBookmarked(questionId) {
  const stats = loadStats();
  return stats.bookmarks.some(b => b.id === questionId);
}
