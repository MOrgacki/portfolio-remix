// Typed access to the small page-content lists in src/data/. Every *Key is validated against the
// English dictionary at build time, so a typo fails the build instead of rendering a raw key.
import en from '../i18n/en.json';
import type { TKey } from '../i18n';
import servicesData from '../data/services.json';
import timelineData from '../data/timeline.json';
import achievementsData from '../data/achievements.json';
import skillsData from '../data/skills.json';
import languagesData from '../data/languages.json';
import certificatesData from '../data/certificates.json';
import contactData from '../data/contact.json';

export type Color = 'cyan' | 'blue' | 'purple' | 'pink' | 'orange' | 'green';

function key(value: string): TKey {
  if (!(value in en)) throw new Error(`Unknown translation key in src/data: ${value}`);
  return value as TKey;
}

export const services = servicesData.map((s) => ({
  ...s,
  color: s.color as Color,
  titleKey: key(s.titleKey),
  descKey: key(s.descKey),
}));

export const timeline = timelineData.map((s) => ({
  ...s,
  color: s.color as Color,
  titleKey: key(s.titleKey),
  descKey: key(s.descKey),
}));

export const achievements = achievementsData.map((a) => ({
  ...a,
  color: a.color as Color,
  problemKey: key(a.problemKey),
  solutionKey: key(a.solutionKey),
  resultKey: key(a.resultKey),
}));

export const skills = skillsData.map((g) => ({
  ...g,
  color: g.color as Color,
  labelKey: key(g.labelKey),
}));

export const spokenLanguages = languagesData.map((l) => ({
  ...l,
  color: l.color as Color,
  nameKey: key(l.nameKey),
  levelKey: key(l.levelKey),
}));

export const certificates = certificatesData.map((c) => ({ ...c, color: c.color as Color }));

export const contactChannels = contactData.map((c) => ({
  ...c,
  id: c.id as 'github' | 'linkedin' | 'email',
  labelKey: key(c.labelKey),
}));
