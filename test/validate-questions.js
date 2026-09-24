import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const dataDir = path.join(__dirname, '..', 'src', 'data');
const files = ['junior.json', 'mid.json', 'senior.json'];

let totalQuestions = 0;
const seenIds = new Set();
let hasErrors = false;

for (const file of files) {
  const filePath = path.join(dataDir, file);
  if (!fs.existsSync(filePath)) {
    console.error(`❌ File not found: ${filePath}`);
    hasErrors = true;
    continue;
  }

  const content = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  console.log(`\n📋 Validating ${file}...`);
  console.log(`   Count: ${content.length} questions`);

  if (content.length < 100) {
    console.error(`❌ Error: ${file} has fewer than 100 questions (${content.length})!`);
    hasErrors = true;
  }

  const stackBreakdown = {};
  const typeBreakdown = {};

  content.forEach((q, index) => {
    // Check ID
    if (!q.id) {
      console.error(`❌ Error in ${file}[${index}]: Missing 'id'`);
      hasErrors = true;
    } else if (seenIds.has(q.id)) {
      console.error(`❌ Duplicate ID detected: ${q.id} in ${file}[${index}]`);
      hasErrors = true;
    } else {
      seenIds.add(q.id);
    }

    // Check Stack
    stackBreakdown[q.stack] = (stackBreakdown[q.stack] || 0) + 1;
    typeBreakdown[q.type] = (typeBreakdown[q.type] || 0) + 1;

    // Check Question text
    if (!q.question || q.question.trim().length === 0) {
      console.error(`❌ Empty question text in ${q.id}`);
      hasErrors = true;
    }

    // Check type-specific fields
    if (q.type === 'mcq') {
      if (!Array.isArray(q.options) || q.options.length !== 4) {
        console.error(`❌ Invalid options in ${q.id}: expected 4 options, found ${q.options?.length}`);
        hasErrors = true;
      }
      if (!['A', 'B', 'C', 'D'].includes(q.answer)) {
        console.error(`❌ Invalid MCQ answer in ${q.id}: '${q.answer}' (must be A, B, C, or D)`);
        hasErrors = true;
      }
      if (!q.explanation || q.explanation.trim().length === 0) {
        console.error(`❌ Missing explanation in MCQ ${q.id}`);
        hasErrors = true;
      }
    } else if (q.type === 'open') {
      if (!Array.isArray(q.expectedKeyPoints) || q.expectedKeyPoints.length === 0) {
        console.error(`❌ Missing or empty expectedKeyPoints in open question ${q.id}`);
        hasErrors = true;
      }
      if (!q.sampleAnswer || q.sampleAnswer.trim().length === 0) {
        console.error(`❌ Missing sampleAnswer in open question ${q.id}`);
        hasErrors = true;
      }
    } else {
      console.error(`❌ Unknown question type '${q.type}' in ${q.id}`);
      hasErrors = true;
    }
  });

  console.log(`   Type breakdown:`, typeBreakdown);
  console.log(`   Stack breakdown:`, stackBreakdown);
  totalQuestions += content.length;
}

console.log(`\n========================================`);
console.log(`🎉 Total Questions Verified: ${totalQuestions}`);
console.log(`Unique IDs Count: ${seenIds.size}`);

if (hasErrors) {
  console.error(`\n❌ Validation FAILED with errors.`);
  process.exit(1);
} else {
  console.log(`\n✅ All question banks are valid and meet all requirements!`);
}
