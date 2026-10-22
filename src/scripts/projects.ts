// Projects search, filters and details dialog (FR-016–FR-018, research R8).
// Filter state lives only in the form controls: it is not persisted and never touches the URL.
import { currentLang } from './lang';

const form = document.querySelector<HTMLFormElement>('[data-filters]');
const list = document.querySelector<HTMLElement>('[data-project-list]');
const empty = document.querySelector<HTMLElement>('[data-empty]');
const count = document.querySelector<HTMLElement>('[data-count]');
const dialog = document.querySelector<HTMLDialogElement>('[data-project-dialog]');
const dialogBody = dialog?.querySelector<HTMLElement>('[data-dialog-body]');

const normalize = (text: string) =>
  text
    .toLowerCase()
    .normalize('NFD')
    .replace(/\p{Diacritic}/gu, '')
    .trim();

function applyFilters(): void {
  if (!form || !list) return;
  const data = new FormData(form);
  const query = normalize(String(data.get('q') ?? ''));
  const techs = data.getAll('tech').map(String);
  const type = String(data.get('type') ?? 'all');
  const platform = String(data.get('platform') ?? 'all');
  const domain = String(data.get('domain') ?? 'all');
  const lang = currentLang();

  let visible = 0;
  for (const card of list.querySelectorAll<HTMLElement>('[data-project]')) {
    const d = card.dataset;
    const show =
      (!query || (d[lang === 'pl' ? 'searchPl' : 'searchEn'] ?? '').includes(query)) &&
      (techs.length === 0 || (d.techs ?? '').split('|').some((t) => techs.includes(t))) &&
      (type === 'all' || d.type === type) &&
      (platform === 'all' || d.platform === platform) &&
      (domain === 'all' || d.domain === domain);
    card.hidden = !show;
    if (show) visible++;
  }
  if (empty) empty.hidden = visible > 0;
  if (count) count.textContent = String(visible);
}

let opener: HTMLElement | null = null;

function openProject(slug: string, trigger: HTMLElement): void {
  const template = document.querySelector<HTMLTemplateElement>(
    `template[data-project-template="${slug}"]`,
  );
  if (!dialog || !dialogBody || !template) return;
  dialogBody.replaceChildren(template.content.cloneNode(true));
  opener = trigger;
  dialog.showModal();
  dialog.scrollTop = 0;
}

if (form && list) {
  form.addEventListener('input', applyFilters);
  form.addEventListener('change', applyFilters);
  // Reset happens after the event fires.
  form.addEventListener('reset', () => setTimeout(applyFilters));
  window.addEventListener('langchange', applyFilters);
  applyFilters();

  list.addEventListener('click', (event) => {
    const target = event.target as HTMLElement;
    if (target.closest('a')) return;
    const card = target.closest<HTMLElement>('[data-project]');
    if (!card) return;
    const trigger = card.querySelector<HTMLElement>('[data-open-project]') ?? card;
    openProject(card.dataset.project!, trigger);
  });
}

if (dialog) {
  dialog.querySelector('[data-close-dialog]')?.addEventListener('click', () => dialog.close());
  // A click on the backdrop targets the <dialog> element itself.
  dialog.addEventListener('click', (event) => {
    if (event.target === dialog) dialog.close();
  });
  dialog.addEventListener('close', () => {
    opener?.focus();
    opener = null;
  });
}
