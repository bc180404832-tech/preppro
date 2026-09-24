import chalk from 'chalk';
import { select, confirm } from '@inquirer/prompts';
import { ui } from './ui.js';
import { promptMCQAnswer, promptOpenAnswer } from './menus.js';
import { AIAnswerAnalyzer } from '../ai/analyzer.js';
import { loadConfig } from '../ai/config.js';
import { recordMCQResult, recordOpenResult, toggleBookmark, isBookmarked } from '../utils/storage.js';

export class QuizSession {
  constructor(questions, { level, stack, mode }) {
    this.questions = questions;
    this.level = level;
    this.stack = stack;
    this.mode = mode;

    this.currentIndex = 0;
    this.totalAnswered = 0;
    this.mcqCorrect = 0;
    this.openCount = 0;
    this.openScores = [];
    this.startTime = Date.now();
  }

  async start() {
    for (let i = 0; i < this.questions.length; i++) {
      this.currentIndex = i;
      const q = this.questions[i];
      const shouldContinue = await this.renderQuestion(q, i + 1, this.questions.length);
      if (!shouldContinue) {
        break;
      }
    }

    this.finish();
  }

  async renderQuestion(question, number, total) {
    const config = loadConfig();
    console.clear();
    ui.banner(this.stack, this.level, config.primaryProvider);
    ui.renderQuestionCard(question, number, total);

    const bookmarked = isBookmarked(question.id);
    if (bookmarked) {
      console.log(chalk.yellow('★ Bookmarked\n'));
    }

    if (question.type === 'mcq') {
      return await this.handleMCQ(question);
    } else {
      return await this.handleOpen(question);
    }
  }

  async handleMCQ(question) {
    const selected = await promptMCQAnswer(question.options);
    const isCorrect = selected.toUpperCase() === question.answer.toUpperCase();

    this.totalAnswered += 1;
    if (isCorrect) this.mcqCorrect += 1;
    recordMCQResult(question, selected, isCorrect);

    ui.renderMCQFeedback(isCorrect, question.answer, question.explanation);

    // Post-question action menu
    const nextAction = await select({
      message: 'Next step:',
      choices: [
        { name: '➡️  Next Question', value: 'next' },
        { name: `🔖 ${isBookmarked(question.id) ? 'Remove Bookmark' : 'Bookmark Question'}`, value: 'bookmark' },
        { name: '🤖 Ask AI for Deeper Context & Edge Cases', value: 'ai_deep' },
        { name: '🚪 End Session & View Summary', value: 'exit' }
      ]
    });

    if (nextAction === 'bookmark') {
      const state = toggleBookmark(question);
      console.log(chalk.yellow(state ? '\n✔ Question added to bookmarks!' : '\n✔ Question removed from bookmarks!'));
      await new Promise(r => setTimeout(r, 800));
      return true;
    }

    if (nextAction === 'ai_deep') {
      const spinner = ui.spinner('Consulting AI for in-depth breakdown...');
      try {
        const result = await AIAnswerAnalyzer.explainMCQ(
          question,
          (notice) => { spinner.text = notice; }
        );
        spinner.stop();
        ui.renderAIEvaluation(result.text, result.usedProvider);
      } catch (err) {
        spinner.fail(`AI Request Failed: ${err.message}`);
        console.log(chalk.dim('\nCheck your API key in Settings if needed.'));
      }

      await select({
        message: 'Proceed to next question:',
        choices: [{ name: 'Continue ➡️', value: 'continue' }]
      });
      return true;
    }

    if (nextAction === 'exit') {
      return false;
    }

    return true;
  }

  async handleOpen(question) {
    const userAnswer = await promptOpenAnswer();
    const config = loadConfig();
    const hasKey = Boolean(config.gemini.apiKey || config.openrouter.apiKey);

    this.totalAnswered += 1;
    this.openCount += 1;

    if (!hasKey) {
      console.log(chalk.yellow('\n⚠️ No API key configured. Showing built-in reference model rubric:'));
      console.log(chalk.bold.cyan('\nKey Points Expected:'));
      question.expectedKeyPoints?.forEach((pt, idx) => {
        console.log(`  ${idx + 1}. ${pt}`);
      });
      console.log(chalk.bold.green('\nModel Senior Answer:'));
      console.log(chalk.white(question.sampleAnswer || 'No sample answer provided.'));
      console.log(chalk.dim('\n💡 To enable AI grading with scores & personalized feedback, set your API key in Settings (Option 5).'));
    } else {
      const spinner = ui.spinner(`Analyzing your answer with ${config.primaryProvider.toUpperCase()}...`);
      try {
        const evaluation = await AIAnswerAnalyzer.evaluateAnswer(
          {
            question: question.question,
            level: question.level,
            stack: question.stack,
            topic: question.topic,
            expectedKeyPoints: question.expectedKeyPoints,
            sampleAnswer: question.sampleAnswer,
            userAnswer
          },
          (notice) => {
            spinner.text = notice;
          }
        );

        spinner.stop();
        ui.renderAIEvaluation(evaluation.rawOutput, evaluation.usedProvider);

        // Try extracting score from text
        const scoreMatch = evaluation.rawOutput.match(/SCORE:\s*([\d.]+)\s*\/\s*10/i);
        const score = scoreMatch ? parseFloat(scoreMatch[1]) : 7.5;
        this.openScores.push(score);
        recordOpenResult(question, score, evaluation.usedProvider);
      } catch (err) {
        spinner.fail(`AI Evaluation Error: ${err.message}`);
        console.log(chalk.yellow('\nDisplaying reference model answer instead:'));
        console.log(chalk.white(question.sampleAnswer));
      }
    }

    const nextAction = await select({
      message: 'Next step:',
      choices: [
        { name: '➡️  Next Question', value: 'next' },
        { name: `🔖 ${isBookmarked(question.id) ? 'Remove Bookmark' : 'Bookmark Question'}`, value: 'bookmark' },
        { name: '🚪 End Session & View Summary', value: 'exit' }
      ]
    });

    if (nextAction === 'bookmark') {
      const state = toggleBookmark(question);
      console.log(chalk.yellow(state ? '\n✔ Question bookmarked!' : '\n✔ Bookmark removed!'));
      await new Promise(r => setTimeout(r, 800));
      return true;
    }

    if (nextAction === 'exit') {
      return false;
    }

    return true;
  }

  finish() {
    console.clear();
    const durationSeconds = Math.round((Date.now() - this.startTime) / 1000);
    const minutes = Math.floor(durationSeconds / 60);
    const seconds = durationSeconds % 60;
    const timeSpent = `${minutes}m ${seconds}s`;

    const avgScore = this.openScores.length > 0
      ? (this.openScores.reduce((a, b) => a + b, 0) / this.openScores.length)
      : 0;

    ui.banner(this.stack, this.level);
    ui.renderSummary({
      total: this.totalAnswered,
      correct: this.mcqCorrect,
      openCount: this.openCount,
      avgScore,
      timeSpent
    });
  }
}
