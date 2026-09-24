import fs from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');

function grab(name, nextName) {
  const start = html.indexOf('function ' + name);
  if (start < 0) throw new Error('missing ' + name);
  const end = html.indexOf('\nfunction ' + nextName, start);
  if (end < 0) throw new Error('missing end ' + name);
  return html.slice(start, end);
}

const src = [
  ['quizObjectField', 'quizQuestionStem'],
  ['quizQuestionStem', 'quizQuestionOptions'],
  ['quizQuestionOptions', 'isQuizOptionCorrect'],
  ['isQuizOptionCorrect', 'normalizeQuizOption'],
  ['normalizeQuizOption', 'normalizeQuizQuestion'],
  ['normalizeQuizQuestion', 'questionsMissingMinOptions'],
  ['transformJsonOutsideStrings', 'stripQuizJsonNoise'],
  ['stripQuizJsonNoise', 'repairQuizJsonText'],
  ['repairQuizJsonText', 'findMatchingJsonEnd'],
  ['findMatchingJsonEnd', 'isQuizQuestionObject'],
  ['isQuizQuestionObject', 'coerceQuizQuestions'],
  ['coerceQuizQuestions', 'tryParseJsonValue'],
  ['tryParseJsonValue', 'scanQuizJsonValues'],
  ['scanQuizJsonValues', 'canonicalizeQuizQuestions'],
  ['canonicalizeQuizQuestions', 'recoverWallOfTextQuizJson'],
  ['recoverWallOfTextQuizJson', 'looksLikeQuizQuestionPaste'],
].map(([name, next]) => grab(name, next)).join('\n');

const context = {};
vm.createContext(context);
vm.runInContext(src + '\nthis.extract = extractQuizQuestionsFromText;', context);

const q = {
  question: 'A 54-year-old man has chest pain.',
  difficulty_order: '1st',
  cited_learning_objective: 'Name the LO.',
  options: [
    { text: 'Aortic dissection', isCorrect: true, rationale: 'Fits the vignette.' },
    { text: 'Stable angina', isCorrect: false, rationale: 'Wrong timing.' },
  ],
};
const pretty = JSON.stringify([q], null, 2);
const wall = JSON.stringify(pretty);
const prose = 'The quiz was serialized as plain text rather than presented in a clearly copyable JSON block.\n' + wall;
const fromProse = context.extract(prose);
if (fromProse[0].question !== q.question) throw new Error('prose string unwrap failed');

const literal = 'serialized as plain text ' + pretty.replace(/\n/g, '\\n');
const fromLiteral = context.extract(literal);
if (fromLiteral[0].difficulty_order !== '1st') throw new Error('literal backslash-n was not expanded');

const minified = JSON.stringify([q]);
if (context.extract(minified)[0].options[0].text !== 'Aortic dissection') {
  throw new Error('minified JSON was damaged');
}

const curly = pretty.replace(/"/g, '\u201c');
if (context.extract(curly)[0].difficulty_order !== '1st') {
  throw new Error('curly-quote JSON was not recovered');
}

const brokenLine = pretty.replace('"Fits the vignette."', '"Fits the\nvignette."');
if (context.extract(brokenLine)[0].question !== q.question) {
  throw new Error('raw newline inside a string was not recovered');
}

const titled = minified.replace(/"question"/, '"Question"');
if (context.extract(titled)[0].question !== q.question) {
  throw new Error('capital Question key was dropped');
}
console.log('wall-json recovery ok');
