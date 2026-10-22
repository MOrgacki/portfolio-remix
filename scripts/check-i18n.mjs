// Build gate for bilingual parity (FR-011, constitution principle I).
import { readFileSync } from 'node:fs';

const load = (lang) =>
  JSON.parse(readFileSync(new URL(`../src/i18n/${lang}.json`, import.meta.url), 'utf8'));

const en = load('en');
const pl = load('pl');
const problems = [];

for (const key of Object.keys(en)) if (!(key in pl)) problems.push(`missing in pl.json: ${key}`);
for (const key of Object.keys(pl)) if (!(key in en)) problems.push(`missing in en.json: ${key}`);
for (const [lang, dict] of [
  ['en', en],
  ['pl', pl],
]) {
  for (const [key, value] of Object.entries(dict)) {
    if (typeof value !== 'string' || value.trim() === '')
      problems.push(`empty value in ${lang}.json: ${key}`);
  }
}

if (problems.length) {
  console.error(`i18n check failed (${problems.length} problem(s)):\n  ${problems.join('\n  ')}`);
  process.exit(1);
}
console.log(`i18n check passed: ${Object.keys(en).length} keys in en and pl`);
