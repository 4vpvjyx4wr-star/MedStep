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
  ['transformJsonOutsideStrings', 'stripQuizJsonNoise'],
  ['stripQuizJsonNoise', 'repairQuizJsonText'],
  ['repairQuizJsonText', 'findMatchingJsonEnd'],
  ['recoverWallOfTextQuizJson', 'extractQuizQuestionsFromText'],
].map(([name, next]) => grab(name, next)).join('\n');

const context = {};
vm.createContext(context);
vm.runInContext(src + '\nthis.recover = recoverWallOfTextQuizJson;\nthis.repair = repairQuizJsonText;', context);

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
const recovered = context.repair(context.recover(prose));
const parsed = JSON.parse(recovered.slice(recovered.indexOf('['), recovered.lastIndexOf(']') + 1));
if (parsed[0].question !== q.question) throw new Error('prose string unwrap failed');

const literal = 'serialized as plain text ' + pretty.replace(/\n/g, '\\n');
const recovered2 = context.repair(context.recover(literal));
JSON.parse(recovered2.slice(recovered2.indexOf('[')));
if (!recovered2.includes('\n')) throw new Error('literal backslash-n was not expanded');

const minified = JSON.stringify([q]);
const recovered3 = context.repair(context.recover(minified));
if (JSON.parse(recovered3)[0].options[0].text !== 'Aortic dissection') {
  throw new Error('minified JSON was damaged');
}

const curly = pretty.replace(/"/g, '\u201c');
const recovered4 = context.repair(context.recover(curly));
if (JSON.parse(recovered4)[0].difficulty_order !== '1st') {
  throw new Error('curly-quote JSON was not recovered');
}
console.log('wall-json recovery ok');
