// CI gate: nothing private or legacy may be published (FR-024, contracts/routes.md "Not published").
import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const dist = fileURLToPath(new URL('../dist/', import.meta.url));
const problems = [];

function walk(dir) {
  for (const name of readdirSync(dir)) {
    const path = join(dir, name);
    if (statSync(path).isDirectory()) {
      walk(path);
      continue;
    }
    const rel = relative(dist, path).split(sep).join('/');
    if (/\.(pdf|py|pyc)$/i.test(rel)) problems.push(`forbidden file type: ${rel}`);
    if (/^(portfolio|assets)\//.test(rel)) problems.push(`legacy path published: ${rel}`);
    if (rel.endsWith('.html') && !/<html[^>]*data-lang=/.test(readFileSync(path, 'utf8'))) {
      problems.push(`page without language runtime: ${rel}`);
    }
  }
}

walk(dist);
if (problems.length) {
  console.error(`dist check failed:\n  ${problems.join('\n  ')}`);
  process.exit(1);
}
console.log('dist check passed');
