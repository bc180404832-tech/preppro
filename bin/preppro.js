#!/usr/bin/env node

import { Command } from 'commander';
import chalk from 'chalk';
import { startApp } from '../src/index.js';
import { getBankStats, getQuestions } from '../src/data/index.js';
import { QuizSession } from '../src/cli/session.js';
import { saveConfig, loadConfig } from '../src/ai/config.js';
import { ui } from '../src/cli/ui.js';

const program = new Command();

program
  .name('preppro')
  .description('Minimal Terminal UI for PERN and MERN interview preparation with AI analysis and rate-limit fallback')
  .version('1.0.0')
  .option('-l, --level <level>', 'Engineering level (junior, mid, senior)')
  .option('-s, --stack <stack>', 'Tech stack (pern, mern, all, react, node, express, mongodb, postgresql)')
  .option('-m, --mode <mode>', 'Assessment mode (mcq, open, mixed)')
  .option('-n, --num <number>', 'Number of questions to ask', parseInt)
  .option('-p, --provider <provider>', 'Preferred AI provider (gemini, openrouter)')
  .option('--stats', 'Display question bank statistics and exit')
  .action(async (options) => {
    // If stats flag is present
    if (options.stats) {
      const stats = getBankStats();
      console.log(chalk.bold.cyan('\nPrepPro PERN & MERN Question Bank Statistics:'));
      console.log(`• Total Questions: ${chalk.green.bold(stats.total)}`);
      console.log(`• Junior:          ${stats.levels.junior}`);
      console.log(`• Mid-Level:       ${stats.levels.mid}`);
      console.log(`• Senior:          ${stats.levels.senior}`);
      console.log(`• PERN Questions:  ${stats.stacks.pern}`);
      console.log(`• MERN Questions:  ${stats.stacks.mern}`);
      console.log(`• MCQs:            ${stats.types.mcq}`);
      console.log(`• AI Open Q&A:     ${stats.types.open}\n`);
      process.exit(0);
    }

    // Set provider if specified via CLI
    if (options.provider) {
      const prov = options.provider.toLowerCase();
      if (['gemini', 'openrouter'].includes(prov)) {
        saveConfig({ primaryProvider: prov });
        console.log(chalk.green(`Primary AI provider set to ${prov.toUpperCase()}`));
      } else {
        console.error(chalk.red(`Invalid provider '${options.provider}'. Choose 'gemini' or 'openrouter'.`));
        process.exit(1);
      }
    }

    // If options are provided for a direct quiz run
    if (options.level && options.stack && options.mode) {
      const level = options.level.toLowerCase();
      const stack = options.stack.toLowerCase();
      const mode = options.mode.toLowerCase();
      const limit = options.num || 10;

      const typeFilter = mode === 'mixed' ? 'all' : mode;
      const questions = getQuestions({
        level,
        stack,
        type: typeFilter,
        limit,
        shuffle: true
      });

      if (questions.length === 0) {
        console.error(chalk.red(`No questions found matching criteria: level=${level}, stack=${stack}, mode=${mode}`));
        process.exit(1);
      }

      console.log(chalk.green(`Starting ${mode.toUpperCase()} session: ${level.toUpperCase()} ${stack.toUpperCase()} (${questions.length} questions)...`));
      await new Promise(r => setTimeout(r, 600));

      const session = new QuizSession(questions, { level, stack, mode });
      await session.start();
      process.exit(0);
    }

    // Otherwise, start interactive menu mode
    await startApp();
  });

program.parse(process.argv);
