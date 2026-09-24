import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let cachedBanks = null;

function loadAllBanks() {
  if (cachedBanks) return cachedBanks;

  const junior = JSON.parse(fs.readFileSync(path.join(__dirname, 'junior.json'), 'utf-8'));
  const mid = JSON.parse(fs.readFileSync(path.join(__dirname, 'mid.json'), 'utf-8'));
  const senior = JSON.parse(fs.readFileSync(path.join(__dirname, 'senior.json'), 'utf-8'));

  cachedBanks = {
    junior,
    mid,
    senior,
    all: [...junior, ...mid, ...senior]
  };

  return cachedBanks;
}

/**
 * Filter questions by level, stack, and type
 * @param {Object} options
 * @param {'junior'|'mid'|'senior'|'all'} [options.level='all']
 * @param {'pern'|'mern'|'react'|'node'|'express'|'mongodb'|'postgresql'|'all'} [options.stack='all']
 * @param {'mcq'|'open'|'all'} [options.type='all']
 * @param {string} [options.topic]
 * @param {number} [options.limit]
 * @param {boolean} [options.shuffle=true]
 */
export function getQuestions({
  level = 'all',
  stack = 'all',
  type = 'all',
  topic = '',
  limit = 0,
  shuffle = true
} = {}) {
  const banks = loadAllBanks();
  let pool = [];

  if (level === 'junior') pool = [...banks.junior];
  else if (level === 'mid' || level === 'middle') pool = [...banks.mid];
  else if (level === 'senior') pool = [...banks.senior];
  else pool = [...banks.all];

  // Stack filter
  if (stack === 'pern') {
    pool = pool.filter(q => ['postgresql', 'express', 'react', 'node', 'fullstack'].includes(q.stack));
  } else if (stack === 'mern') {
    pool = pool.filter(q => ['mongodb', 'express', 'react', 'node', 'fullstack'].includes(q.stack));
  } else if (stack !== 'all') {
    pool = pool.filter(q => q.stack === stack);
  }

  // Type filter
  if (type === 'mcq') {
    pool = pool.filter(q => q.type === 'mcq');
  } else if (type === 'open') {
    pool = pool.filter(q => q.type === 'open');
  }

  // Topic filter
  if (topic) {
    const tLower = topic.toLowerCase();
    pool = pool.filter(q => q.topic.toLowerCase().includes(tLower));
  }

  // Shuffle if requested
  if (shuffle) {
    for (let i = pool.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [pool[i], pool[j]] = [pool[j], pool[i]];
    }
  }

  if (limit > 0 && limit < pool.length) {
    return pool.slice(0, limit);
  }

  return pool;
}

/**
 * Returns overall statistics of the question bank
 */
export function getBankStats() {
  const banks = loadAllBanks();
  return {
    total: banks.all.length,
    levels: {
      junior: banks.junior.length,
      mid: banks.mid.length,
      senior: banks.senior.length
    },
    stacks: {
      pern: banks.all.filter(q => ['postgresql', 'express', 'react', 'node', 'fullstack'].includes(q.stack)).length,
      mern: banks.all.filter(q => ['mongodb', 'express', 'react', 'node', 'fullstack'].includes(q.stack)).length
    },
    types: {
      mcq: banks.all.filter(q => q.type === 'mcq').length,
      open: banks.all.filter(q => q.type === 'open').length
    }
  };
}
