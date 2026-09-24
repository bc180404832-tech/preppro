import { select, input, confirm, password } from '@inquirer/prompts';
import chalk from 'chalk';
import { loadConfig, saveConfig } from '../ai/config.js';
import { aiService } from '../ai/provider.js';
import { ui } from './ui.js';
import { getBankStats } from '../data/index.js';

export async function promptSelectLevel(current = 'senior') {
  return await select({
    message: chalk.bold.cyan('Select your Target Engineering Level:'),
    default: current,
    choices: [
      {
        name: `${chalk.green('🟢 Junior')}     - Core syntax, fundamental mechanics, basic APIs & lifecycle`,
        value: 'junior'
      },
      {
        name: `${chalk.yellow('🟡 Mid-Level')}  - Patterns, error handling, state management, optimization`,
        value: 'mid'
      },
      {
        name: `${chalk.red('🔴 Senior')}     - Internals, V8 GC, MVCC/sharding, concurrency & system design`,
        value: 'senior'
      }
    ]
  });
}

export async function promptSelectStack(current = 'pern') {
  return await select({
    message: chalk.bold.cyan('Select your Target Technology Stack:'),
    default: current,
    choices: [
      {
        name: `${chalk.hex('#3B82F6')('🐘 PERN')}        - PostgreSQL, Express, React, Node.js`,
        value: 'pern'
      },
      {
        name: `${chalk.hex('#10B981')('🍃 MERN')}        - MongoDB, Express, React, Node.js`,
        value: 'mern'
      },
      {
        name: `${chalk.hex('#8B5CF6')('🌐 All / Fullstack')} - Complete PERN + MERN (PostgreSQL, MongoDB, React, Node, Express)`,
        value: 'all'
      }
    ]
  });
}

export async function promptSelectMode() {
  return await select({
    message: chalk.bold.cyan('Choose Assessment Mode:'),
    choices: [
      {
        name: `🎯 ${chalk.bold('MCQ Practice Mode')}          - 4-choice questions with instant grading & explanations`,
        value: 'mcq'
      },
      {
        name: `🧠 ${chalk.bold('AI Technical Interview')}       - Open-ended technical questions evaluated by AI`,
        value: 'open'
      },
      {
        name: `⚡ ${chalk.bold('Mixed Rapid Fire')}             - Combined MCQs + AI Open Questions`,
        value: 'mixed'
      },
      {
        name: `🔖 ${chalk.bold('Review Weak Spots & Bookmarks')} - Revisit incorrect answers and saved questions`,
        value: 'review'
      },
      {
        name: `⚙️  ${chalk.bold('Settings & AI Provider')}       - Configure Gemini / OpenRouter API keys & fallback`,
        value: 'settings'
      },
      {
        name: `🚪 ${chalk.dim('Exit')}`,
        value: 'exit'
      }
    ]
  });
}

export async function promptQuestionCount() {
  return await select({
    message: chalk.bold.cyan('How many questions for this session?'),
    default: 10,
    choices: [
      { name: '5 Questions (Quick warmup)', value: 5 },
      { name: '10 Questions (Standard sprint)', value: 10 },
      { name: '20 Questions (Deep dive)', value: 20 },
      { name: '50 Questions (Comprehensive drill)', value: 50 },
      { name: 'All available matching questions', value: 9999 }
    ]
  });
}

export async function promptMCQAnswer(options) {
  const choices = options.map((opt) => {
    const letter = opt.substring(0, 1);
    return {
      name: opt,
      value: letter
    };
  });

  return await select({
    message: chalk.bold.yellow('Select the correct answer:'),
    choices
  });
}

export async function promptOpenAnswer() {
  console.log(chalk.dim('\n💡 Tip: Write a detailed, senior-grade response. AI will analyze depth, accuracy, and edge cases.'));
  console.log(chalk.dim('   Press Enter when finished (multi-line supported by pasting text):\n'));

  return await input({
    message: chalk.bold.yellow('Your Answer:'),
    validate: (val) => val.trim().length > 5 ? true : 'Please enter a more detailed response for accurate AI evaluation.'
  });
}

/**
 * Interactive Settings Menu for API Keys, Providers, and Fallback
 */
export async function runSettingsMenu() {
  while (true) {
    const config = loadConfig();
    const geminiMasked = config.gemini.apiKey
      ? chalk.green(`Configured (${config.gemini.apiKey.slice(0, 6)}...${config.gemini.apiKey.slice(-4)})`)
      : chalk.red('Not Configured');

    const openrouterMasked = config.openrouter.apiKey
      ? chalk.green(`Configured (${config.openrouter.apiKey.slice(0, 6)}...${config.openrouter.apiKey.slice(-4)})`)
      : chalk.red('Not Configured');

    const primaryColor = config.primaryProvider === 'gemini' ? chalk.cyan('Google AI Studio (Gemini)') : chalk.cyan('OpenRouter');
    const fallbackStatus = config.autoFallback ? chalk.green('ENABLED (Auto-switches on 429 rate limit)') : chalk.yellow('DISABLED');

    console.clear();
    ui.banner();
    console.log(chalk.bold.magenta('\n⚙️  AI CONFIGURATION & RATE-LIMIT FALLBACK SETTINGS\n'));
    console.log(`• Primary Provider:     ${primaryColor}`);
    console.log(`• Auto-Fallback:        ${fallbackStatus}`);
    console.log(`• Google AI Studio Key: ${geminiMasked}`);
    console.log(`• OpenRouter Key:       ${openrouterMasked}\n`);

    const action = await select({
      message: 'Select setting to modify:',
      choices: [
        { name: '1. Set Primary Provider (Toggle Gemini / OpenRouter)', value: 'toggle_primary' },
        { name: '2. Toggle Auto-Fallback on Rate Limit', value: 'toggle_fallback' },
        { name: '3. Enter / Update Google AI Studio (Gemini) API Key', value: 'key_gemini' },
        { name: '4. Enter / Update OpenRouter API Key', value: 'key_openrouter' },
        { name: '5. Select Models (Gemini / OpenRouter models)', value: 'models' },
        { name: '6. Test Provider Connections', value: 'test_conn' },
        { name: '⬅️  Back to Main Menu', value: 'back' }
      ]
    });

    if (action === 'back') break;

    if (action === 'toggle_primary') {
      const nextProvider = await select({
        message: 'Choose primary AI provider:',
        default: config.primaryProvider,
        choices: [
          { name: 'Google AI Studio (Gemini)', value: 'gemini' },
          { name: 'OpenRouter (Multi-model gateway)', value: 'openrouter' }
        ]
      });
      saveConfig({ primaryProvider: nextProvider });
      console.log(chalk.green(`\n✔ Primary provider set to ${nextProvider.toUpperCase()}!`));
      await new Promise(r => setTimeout(r, 1000));
    }

    if (action === 'toggle_fallback') {
      const fallback = await confirm({
        message: 'Enable automatic fallback to secondary provider when primary is rate-limited (HTTP 429)?',
        default: config.autoFallback
      });
      saveConfig({ autoFallback: fallback });
      console.log(chalk.green(`\n✔ Auto-fallback ${fallback ? 'ENABLED' : 'DISABLED'}!`));
      await new Promise(r => setTimeout(r, 1000));
    }

    if (action === 'key_gemini') {
      const key = await password({
        message: 'Paste your Google AI Studio API Key (input hidden):',
        mask: '*'
      });
      if (key.trim()) {
        saveConfig({ gemini: { ...config.gemini, apiKey: key.trim() } });
        console.log(chalk.green('\n✔ Google AI Studio API Key saved to ~/.preppro/config.json!'));
      }
      await new Promise(r => setTimeout(r, 1200));
    }

    if (action === 'key_openrouter') {
      const key = await password({
        message: 'Paste your OpenRouter API Key (input hidden):',
        mask: '*'
      });
      if (key.trim()) {
        saveConfig({ openrouter: { ...config.openrouter, apiKey: key.trim() } });
        console.log(chalk.green('\n✔ OpenRouter API Key saved to ~/.preppro/config.json!'));
      }
      await new Promise(r => setTimeout(r, 1200));
    }

    if (action === 'models') {
      const geminiModel = await select({
        message: 'Select Google Gemini Model:',
        default: config.gemini.model,
        choices: [
          { name: 'gemini-2.5-flash (Fast & recommended)', value: 'gemini-2.5-flash' },
          { name: 'gemini-2.0-flash', value: 'gemini-2.0-flash' },
          { name: 'gemini-1.5-flash', value: 'gemini-1.5-flash' },
          { name: 'gemini-1.5-pro', value: 'gemini-1.5-pro' }
        ]
      });

      const openrouterModel = await input({
        message: 'Enter OpenRouter Model ID:',
        default: config.openrouter.model || 'google/gemini-2.5-flash'
      });

      saveConfig({
        gemini: { ...config.gemini, model: geminiModel },
        openrouter: { ...config.openrouter, model: openrouterModel.trim() }
      });
      console.log(chalk.green('\n✔ Models updated successfully!'));
      await new Promise(r => setTimeout(r, 1000));
    }

    if (action === 'test_conn') {
      console.log('');
      const spinner = ui.spinner('Testing API connectivity to providers...');
      try {
        let geminiOk = false;
        let openrouterOk = false;

        if (config.gemini.apiKey) {
          spinner.text = 'Testing Google AI Studio (Gemini)...';
          try {
            await aiService.testProvider('gemini');
            geminiOk = true;
          } catch (e) {
            geminiOk = false;
          }
        }

        if (config.openrouter.apiKey) {
          spinner.text = 'Testing OpenRouter...';
          try {
            await aiService.testProvider('openrouter');
            openrouterOk = true;
          } catch (e) {
            openrouterOk = false;
          }
        }

        spinner.stop();
        console.log(chalk.bold('\nTest Results:'));
        console.log(`• Google AI Studio: ${config.gemini.apiKey ? (geminiOk ? chalk.green('✔ Connected & Valid') : chalk.red('✖ Failed / Rate Limited / Invalid Key')) : chalk.dim('Skipped (no key)')}`);
        console.log(`• OpenRouter:       ${config.openrouter.apiKey ? (openrouterOk ? chalk.green('✔ Connected & Valid') : chalk.red('✖ Failed / Rate Limited / Invalid Key')) : chalk.dim('Skipped (no key)')}`);
      } catch (err) {
        spinner.fail(`Test encountered error: ${err.message}`);
      }
      await input({ message: chalk.dim('\nPress Enter to continue...') });
    }
  }
}
