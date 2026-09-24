import chalk from 'chalk';
import { select, confirm } from '@inquirer/prompts';
import { ui } from './cli/ui.js';
import {
  promptSelectLevel,
  promptSelectStack,
  promptSelectMode,
  promptQuestionCount,
  runSettingsMenu
} from './cli/menus.js';
import { getQuestions, getBankStats } from './data/index.js';
import { QuizSession } from './cli/session.js';
import { loadConfig } from './ai/config.js';
import { loadStats } from './utils/storage.js';

export async function startApp() {
  while (true) {
    const config = loadConfig();
    const stats = getBankStats();
    const userStats = loadStats();

    console.clear();
    ui.banner('', '', config.primaryProvider);

    console.log(chalk.bold('📚 Question Bank Overview:'));
    console.log(`   Total Questions: ${chalk.cyan.bold(stats.total)} (${chalk.green(stats.levels.junior + ' Junior')}, ${chalk.yellow(stats.levels.mid + ' Mid')}, ${chalk.red(stats.levels.senior + ' Senior')})`);
    console.log(`   PERN Questions:  ${chalk.blue.bold(stats.stacks.pern)} | MERN Questions: ${chalk.green.bold(stats.stacks.mern)}`);
    console.log(`   Format:          ${chalk.white(stats.types.mcq + ' MCQs')} + ${chalk.magenta(stats.types.open + ' AI Open Interview Questions')}`);
    
    if (userStats.totalAnswered > 0) {
      console.log(chalk.dim(`\n📈 Your All-Time Progress: ${userStats.totalAnswered} answered (${userStats.mcqCorrect}/${userStats.mcqTotal} MCQs correct, ${userStats.bookmarks.length} bookmarked, ${userStats.wrongQuestions.length} in review)`));
    }
    console.log('');

    const mode = await promptSelectMode();

    if (mode === 'exit') {
      console.log(chalk.cyan('\n👋 Good luck with your PERN & MERN technical interviews! Keep building.\n'));
      process.exit(0);
    }

    if (mode === 'settings') {
      await runSettingsMenu();
      continue;
    }

    if (mode === 'review') {
      await runReviewMode(userStats);
      continue;
    }

    // Assessment modes (mcq, open, mixed)
    const level = await promptSelectLevel();
    const stack = await promptSelectStack();
    const count = await promptQuestionCount();

    const typeFilter = mode === 'mixed' ? 'all' : mode; // 'mcq' | 'open' | 'all'
    const questions = getQuestions({
      level,
      stack,
      type: typeFilter,
      limit: count,
      shuffle: true
    });

    if (questions.length === 0) {
      console.log(chalk.red('\nNo questions found matching your filter criteria. Try expanding stack or level.'));
      await new Promise(r => setTimeout(r, 2000));
      continue;
    }

    const session = new QuizSession(questions, { level, stack, mode });
    await session.start();

    const playAgain = await confirm({
      message: 'Return to Main Menu?',
      default: true
    });

    if (!playAgain) {
      console.log(chalk.cyan('\n👋 Best of luck on your interviews!\n'));
      break;
    }
  }
}

async function runReviewMode(userStats) {
  console.clear();
  ui.banner();
  console.log(chalk.bold.magenta('\n🔖 REVIEW BOOKMARKS & WEAK SPOTS\n'));

  const reviewChoice = await select({
    message: 'Choose review category:',
    choices: [
      { name: `❌ Previously Incorrect MCQs (${userStats.wrongQuestions?.length || 0})`, value: 'wrong' },
      { name: `★ Bookmarked Questions (${userStats.bookmarks?.length || 0})`, value: 'bookmarks' },
      { name: '⬅️ Back', value: 'back' }
    ]
  });

  if (reviewChoice === 'back') return;

  const list = reviewChoice === 'wrong' ? userStats.wrongQuestions : userStats.bookmarks;
  if (!list || list.length === 0) {
    console.log(chalk.yellow('\nNo items saved in this category yet. Practice more questions to build your list!'));
    await new Promise(r => setTimeout(r, 2000));
    return;
  }

  // Find the actual full question objects
  const allQuestions = getQuestions({ level: 'all', stack: 'all', shuffle: false });
  const reviewQuestions = allQuestions.filter(q => list.some(item => item.id === q.id));

  if (reviewQuestions.length === 0) {
    console.log(chalk.yellow('\nCould not locate full question definitions for these items.'));
    await new Promise(r => setTimeout(r, 1500));
    return;
  }

  console.log(chalk.green(`\nLaunching review session with ${reviewQuestions.length} questions...\n`));
  await new Promise(r => setTimeout(r, 1000));

  const session = new QuizSession(reviewQuestions, {
    level: 'Review',
    stack: 'Saved',
    mode: 'review'
  });

  await session.start();
}
