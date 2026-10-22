import { getCollection, type CollectionEntry } from 'astro:content';
import facets from '../data/facets.json';
import techCategories from '../data/tech-categories.json';

export type Project = CollectionEntry<'projects'>['data'];

export const PLATFORM_EMOJI: Record<Project['platform'], string> = {
  Web: '🌐',
  Mobile: '📱',
  Desktop: '💻',
  'AI/Automation': '🤖',
};

/** Newest first, as in the legacy app (sorted by id descending). */
export async function loadProjects(): Promise<Project[]> {
  const entries = await getCollection('projects');
  return entries.map((e) => e.data).sort((a, b) => b.order - a.order);
}

const normalize = (text: string) =>
  text
    .toLowerCase()
    .normalize('NFD')
    .replace(/\p{Diacritic}/gu, '');

export function searchText(p: Project, lang: 'en' | 'pl'): string {
  return normalize([p.title, p.description[lang], ...p.technologies].join(' '));
}

export const domainLabels = Object.fromEntries(facets.domains.map((d) => [d.value, d.label]));
export const platformLabels = Object.fromEntries(facets.platforms.map((p) => [p.value, p.label]));

export function categoryOf(tech: string) {
  return techCategories.find((c) => c.techs.includes(tech));
}

/** Filter groups: technologies used by projects, split into the most used and the rest (legacy behaviour). */
export function techGroups(projects: Project[]) {
  const counts = new Map<string, number>();
  for (const p of projects) for (const t of p.technologies) counts.set(t, (counts.get(t) ?? 0) + 1);
  const popularSize: Record<string, number> = {
    languages: 4,
    testing: 5,
    databases: 4,
    frameworks: 5,
    devops: 4,
    other: 5,
  };
  return techCategories
    .map((c) => {
      const sorted = c.techs
        .filter((t) => counts.has(t))
        .sort((a, b) => counts.get(b)! - counts.get(a)! || a.localeCompare(b));
      const n = popularSize[c.id] ?? 5;
      return { ...c, popular: sorted.slice(0, n), rest: sorted.slice(n) };
    })
    .filter((c) => c.popular.length);
}

export function domainGroups(projects: Project[]) {
  const counts = new Map<string, number>();
  for (const p of projects) counts.set(p.domain, (counts.get(p.domain) ?? 0) + 1);
  const sorted = [...counts.keys()].sort(
    (a, b) => counts.get(b)! - counts.get(a)! || a.localeCompare(b),
  );
  return { popular: sorted.slice(0, 5), rest: sorted.slice(5) };
}
