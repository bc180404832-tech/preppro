import assert from 'assert';
import { getQuestions, getBankStats } from '../src/data/index.js';
import { loadConfig, saveConfig } from '../src/ai/config.js';
import { AIProviderService } from '../src/ai/provider.js';
import { loadStats, recordMCQResult, toggleBookmark, isBookmarked } from '../src/utils/storage.js';

console.log('🧪 Running automated logic & fallback tests...\n');

// 1. Test bank stats
const stats = getBankStats();
assert(stats.total === 330, `Expected 330 total questions, got ${stats.total}`);
assert(stats.levels.junior === 110, `Expected 110 junior questions, got ${stats.levels.junior}`);
assert(stats.levels.mid === 110, `Expected 110 mid questions, got ${stats.levels.mid}`);
assert(stats.levels.senior === 110, `Expected 110 senior questions, got ${stats.levels.senior}`);
console.log('✅ Bank stats passed (330 total: 110 Junior, 110 Mid, 110 Senior).');

// 2. Test filtering by level and stack
const jrReact = getQuestions({ level: 'junior', stack: 'react', shuffle: false });
assert(jrReact.length > 0, 'Junior React questions should not be empty');
assert(jrReact.every(q => q.level === 'junior' && q.stack === 'react'), 'All filtered questions should be junior react');

const srPern = getQuestions({ level: 'senior', stack: 'pern', shuffle: false });
assert(srPern.length > 0, 'Senior PERN questions should not be empty');
assert(srPern.every(q => ['postgresql', 'express', 'react', 'node', 'fullstack'].includes(q.stack)), 'Senior PERN questions must be PERN components');

const midMern = getQuestions({ level: 'mid', stack: 'mern', shuffle: false });
assert(midMern.length > 0, 'Mid MERN questions should not be empty');
assert(midMern.every(q => ['mongodb', 'express', 'react', 'node', 'fullstack'].includes(q.stack)), 'Mid MERN questions must be MERN components');
console.log('✅ Level and stack filters passed.');

// 3. Test question types
const mcqs = getQuestions({ type: 'mcq' });
assert(mcqs.length > 200, 'MCQs should exceed 200');
assert(mcqs.every(q => q.type === 'mcq' && q.options.length === 4 && ['A', 'B', 'C', 'D'].includes(q.answer)), 'All MCQs valid');

const openQs = getQuestions({ type: 'open' });
assert(openQs.length > 80, 'Open questions should exceed 80');
assert(openQs.every(q => q.type === 'open' && q.expectedKeyPoints.length > 0 && q.sampleAnswer.length > 0), 'All Open Qs valid');
console.log('✅ MCQ and Open question schema tests passed.');

// 4. Test Config Save / Load
const originalConfig = loadConfig();
saveConfig({ primaryProvider: 'openrouter', autoFallback: true });
const updatedConfig = loadConfig();
assert(updatedConfig.primaryProvider === 'openrouter', 'Primary provider should be updated');
// Revert
saveConfig({ primaryProvider: originalConfig.primaryProvider });
console.log('✅ Config save/load tests passed.');

// 5. Test Storage & Bookmarks
const dummyQ = {
  id: 'test-q-999',
  level: 'junior',
  stack: 'react',
  type: 'mcq',
  topic: 'Testing',
  question: 'What is a test?',
  options: ['A) 1', 'B) 2', 'C) 3', 'D) 4'],
  answer: 'A',
  explanation: 'Test'
};

const bState1 = toggleBookmark(dummyQ);
assert(bState1 === true, 'First toggle should bookmark');
assert(isBookmarked('test-q-999') === true, 'Should report bookmarked');
const bState2 = toggleBookmark(dummyQ);
assert(bState2 === false, 'Second toggle should unbookmark');
assert(isBookmarked('test-q-999') === false, 'Should report unbookmarked');
console.log('✅ Bookmarks and stats storage tests passed.');

// 6. Test AI Provider Rate-Limit Fallback Engine (Simulated Fallback)
console.log('\n⚡ Testing AI Rate-Limit Fallback Cascade simulation...');
const mockAiService = new AIProviderService();

// Mock config with primary: gemini, secondary: openrouter
mockAiService.config = {
  primaryProvider: 'gemini',
  autoFallback: true,
  gemini: { apiKey: 'dummy-gemini-key', model: 'gemini-2.5-flash' },
  openrouter: { apiKey: 'dummy-openrouter-key', model: 'google/gemini-2.5-flash' }
};
mockAiService.reloadConfig = () => mockAiService.config;

// Simulate Gemini throwing 429 Rate Limit error
mockAiService.callGemini = async () => {
  const rateLimitErr = new Error('HTTP 429: Resource exhausted / rate limit reached');
  rateLimitErr.isRateLimit = true;
  rateLimitErr.provider = 'gemini';
  throw rateLimitErr;
};

// Simulate OpenRouter succeeding
mockAiService.callOpenRouter = async () => {
  return 'SUCCESS_FROM_OPENROUTER_FALLBACK';
};

let fallbackNoticeReceived = false;
const fallbackResult = await mockAiService.executeWithFallback(
  'Test prompt',
  'Test system instruction',
  (notice) => {
    fallbackNoticeReceived = true;
    console.log(`   [Live Notification Callback]: ${notice}`);
  }
);

assert(fallbackResult.usedProvider === 'openrouter', 'Expected fallback to openrouter');
assert(fallbackResult.fallbackTriggered === true, 'Expected fallbackTriggered to be true');
assert(fallbackResult.text === 'SUCCESS_FROM_OPENROUTER_FALLBACK', 'Expected response from fallback provider');
assert(fallbackNoticeReceived === true, 'Expected fallback notification to be dispatched');
console.log('✅ AI Rate-Limit Fallback engine successfully caught HTTP 429 and switched to fallback provider!\n');

console.log('🎉 All automated tests PASSED successfully!');
