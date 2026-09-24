import chalk from 'chalk';
import boxen from 'boxen';
import ora from 'ora';
import { Marked } from 'marked';
import { markedTerminal } from 'marked-terminal';

// Initialize markdown renderer for terminal
const marked = new Marked(markedTerminal({
  width: Math.min(process.stdout.columns ? process.stdout.columns - 4 : 80, 100),
  reflowText: true,
  code: chalk.yellow,
  firstHeading: chalk.bold.cyan,
  heading: chalk.bold.magenta,
  strong: chalk.bold.white,
  em: chalk.italic.gray,
  listitem: chalk.white,
  tableOptions: {
    chars: { mid: '', 'left-mid': '', 'mid-mid': '', 'right-mid': '' }
  }
}));

export const ui = {
  /**
   * Render Main Application Header
   */
  banner(activeStack = '', activeLevel = '', activeProvider = '') {
    console.clear();
    const title = chalk.bold.hex('#6366F1')(' PrepPro ') + chalk.dim('// PERN & MERN Interview Platform');
    
    let sub = '';
    if (activeStack || activeLevel) {
      const sBadge = activeStack ? chalk.hex('#10B981')(`[${activeStack.toUpperCase()}]`) : '';
      const lBadge = activeLevel ? chalk.hex('#F59E0B')(`[${activeLevel.toUpperCase()}]`) : '';
      const pBadge = activeProvider ? chalk.hex('#EC4899')(`[AI: ${activeProvider.toUpperCase()}]`) : '';
      sub = `\n${sBadge} ${lBadge} ${pBadge}`;
    }

    const box = boxen(`${title}${sub}`, {
      padding: { top: 0, bottom: 0, left: 2, right: 2 },
      margin: { top: 0, bottom: 1 },
      borderStyle: 'round',
      borderColor: 'cyan',
      dimBorder: true
    });
    console.log(box);
  },

  /**
   * Render Question Card
   */
  renderQuestionCard(question, index = 1, total = 1) {
    const levelColors = {
      junior: '#10B981', // green
      mid: '#F59E0B',    // amber
      senior: '#EF4444'   // red
    };

    const lvlColor = levelColors[question.level] || '#6366F1';
    const levelTag = chalk.hex(lvlColor).bold(` ${question.level.toUpperCase()} `);
    const stackTag = chalk.bgHex('#374151').white.bold(` ${question.stack.toUpperCase()} `);
    const typeTag = question.type === 'mcq' ? chalk.cyan('[MCQ]') : chalk.magenta('[AI INTERVIEW]');
    const progress = chalk.dim(`Question ${index}/${total}`);

    const header = `${levelTag} ${stackTag} ${typeTag}  ${chalk.dim('•')}  ${chalk.bold(question.topic)}  ${chalk.dim('•')}  ${progress}\n`;
    const qBody = chalk.bold.white(question.question);

    console.log(boxen(`${header}\n${qBody}`, {
      padding: 1,
      margin: { top: 0, bottom: 1 },
      borderStyle: 'round',
      borderColor: lvlColor,
      backgroundColor: '#111827'
    }));
  },

  /**
   * Render MCQ feedback
   */
  renderMCQFeedback(isCorrect, correctAnswer, explanation) {
    if (isCorrect) {
      console.log(boxen(
        chalk.green.bold('✔ CORRECT!') + '\n\n' +
        chalk.dim('Explanation:\n') + chalk.white(explanation),
        {
          padding: 1,
          borderColor: 'green',
          borderStyle: 'round',
          margin: { top: 0, bottom: 1 }
        }
      ));
    } else {
      console.log(boxen(
        chalk.red.bold('✖ INCORRECT') + `  (Correct Answer: ${chalk.green.bold(correctAnswer)})\n\n` +
        chalk.dim('Explanation:\n') + chalk.white(explanation),
        {
          padding: 1,
          borderColor: 'red',
          borderStyle: 'round',
          margin: { top: 0, bottom: 1 }
        }
      ));
    }
  },

  /**
   * Render AI Evaluation Markdown
   */
  renderAIEvaluation(evalText, providerInfo = '') {
    const formatted = marked.parse(evalText);
    const providerBadge = providerInfo
      ? chalk.dim(`\n\n[Evaluated via ${providerInfo}]`)
      : '';

    console.log(boxen(formatted + providerBadge, {
      padding: 1,
      borderColor: 'magenta',
      borderStyle: 'round',
      margin: { top: 1, bottom: 1 }
    }));
  },

  /**
   * Show Spinner
   */
  spinner(text) {
    return ora({
      text: chalk.cyan(text),
      spinner: 'dots'
    }).start();
  },

  /**
   * Render Summary Card
   */
  renderSummary({ total, correct, openCount, avgScore, timeSpent }) {
    const mcqTotal = total - openCount;
    const accuracy = mcqTotal > 0 ? Math.round((correct / mcqTotal) * 100) : 0;
    const scoreColor = accuracy >= 80 ? chalk.green : accuracy >= 60 ? chalk.yellow : chalk.red;

    const content = [
      chalk.bold.cyan('📊 SESSION SUMMARY & PERFORMANCE SCORECARD'),
      chalk.dim('---------------------------------------------'),
      `${chalk.white('Total Questions Attempted:')} ${chalk.bold(total)}`,
      ...(mcqTotal > 0 ? [
        `${chalk.white('MCQ Correct Answers:')}       ${chalk.bold(correct)} / ${mcqTotal}`,
        `${chalk.white('MCQ Accuracy Rate:')}         ${scoreColor.bold(accuracy + '%')}`
      ] : []),
      ...(openCount > 0 ? [
        `${chalk.white('AI Evaluated Answers:')}     ${chalk.bold(openCount)}`,
        `${chalk.white('Average AI Rubric Score:')}  ${chalk.bold.magenta(avgScore.toFixed(1) + ' / 10')}`
      ] : []),
      `${chalk.white('Time Elapsed:')}              ${chalk.dim(timeSpent)}`
    ].join('\n');

    console.log(boxen(content, {
      padding: 1,
      margin: { top: 1, bottom: 1 },
      borderColor: 'cyan',
      borderStyle: 'double'
    }));
  }
};
