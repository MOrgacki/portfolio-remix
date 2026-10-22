// Language runtime (contracts/i18n.md). The inline head script already set the initial language.
export type Lang = 'en' | 'pl';

const STORAGE_KEY = 'portfolio.lang';
const ATTRS = ['alt', 'aria-label', 'placeholder', 'title'] as const;

export function currentLang(): Lang {
  return document.documentElement.dataset.lang === 'pl' ? 'pl' : 'en';
}

function applyLang(lang: Lang): void {
  const root = document.documentElement;
  root.dataset.lang = lang;
  root.lang = lang;

  for (const attr of ATTRS) {
    for (const el of document.querySelectorAll<HTMLElement>(`[data-i18n-${attr}-${lang}]`)) {
      el.setAttribute(attr, el.getAttribute(`data-i18n-${attr}-${lang}`) ?? '');
    }
  }

  const plTitle = document.querySelector<HTMLMetaElement>('meta[name="i18n-title-pl"]');
  const titleEl = document.querySelector('title');
  if (titleEl && !titleEl.dataset.en) titleEl.dataset.en = titleEl.textContent ?? '';
  document.title =
    lang === 'pl' && plTitle ? plTitle.content : (titleEl?.dataset.en ?? document.title);
}

function persist(lang: Lang): void {
  try {
    localStorage.setItem(STORAGE_KEY, lang);
  } catch {
    // Storage blocked: the choice lasts for this page view only.
  }
}

applyLang(currentLang());

document.addEventListener('click', (event) => {
  const toggle = (event.target as Element | null)?.closest('[data-lang-toggle]');
  if (!toggle) return;
  const next: Lang = currentLang() === 'en' ? 'pl' : 'en';
  persist(next);
  applyLang(next);
  window.dispatchEvent(new CustomEvent('langchange', { detail: { lang: next } }));
});
