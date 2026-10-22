import { expect, test, type Page } from '@playwright/test';
import en from '../../src/i18n/en.json' with { type: 'json' };
import pl from '../../src/i18n/pl.json' with { type: 'json' };
import projects from '../../src/data/projects.json' with { type: 'json' };

const cards = (page: Page) => page.locator('[data-project]:visible');
const normalize = (s: string) =>
  s
    .toLowerCase()
    .normalize('NFD')
    .replace(/\p{Diacritic}/gu, '');

test.describe('projects (US3)', () => {
  test.use({ locale: 'en-US' });

  test.beforeEach(async ({ page }) => {
    await page.goto('projects/');
  });

  test('lists all 35 projects newest first', async ({ page }) => {
    await expect(cards(page)).toHaveCount(35);
    const titles = await page.locator('[data-project] h2').allInnerTexts();
    const expected = [...projects].sort((a, b) => b.id - a.id).map((p) => p.title);
    expect(titles).toEqual(expected);
  });

  test('search matches title, description and technologies', async ({ page }) => {
    await page.getByRole('searchbox').fill('Playwright');
    const expected = projects.filter((p) =>
      normalize([p.title, p.description.en, ...p.technologies].join(' ')).includes('playwright'),
    ).length;
    expect(expected).toBeGreaterThan(0);
    await expect(cards(page)).toHaveCount(expected);
  });

  test('search combines with domain filter, empty state and clear', async ({ page }, info) => {
    test.skip(info.project.name === 'chromium-mobile', 'same logic on desktop');
    await page.getByRole('searchbox').fill('platform');
    await page
      .getByRole('group', { name: en.proj_domain })
      .getByText('Fintech', { exact: true })
      .filter({ visible: true })
      .click();
    const expected = projects.filter(
      (p) =>
        p.domain === 'Fintech' &&
        normalize([p.title, p.description.en, ...p.technologies].join(' ')).includes('platform'),
    ).length;
    await expect(cards(page)).toHaveCount(expected);

    await page.getByRole('searchbox').fill('zzzz-no-match');
    await expect(cards(page)).toHaveCount(0);
    await expect(page.getByText(en.projects_empty_result)).toBeVisible();

    await page.getByRole('button', { name: en.proj_clear_filters }).click();
    await expect(cards(page)).toHaveCount(35);
    await expect(page.getByText(en.projects_empty_result)).toBeHidden();
  });

  test('technology chips are multi-select with ANY semantics', async ({ page }, info) => {
    test.skip(info.project.name === 'chromium-mobile', 'same logic on desktop');
    const techs = page.getByRole('group', { name: en.proj_technologies });
    for (const more of await techs.locator('details summary').all()) await more.click();
    await techs.getByText('Python', { exact: true }).click();
    await techs.getByText('Cypress', { exact: true }).click();
    const expected = projects.filter((p) =>
      p.technologies.some((t) => t === 'Python' || t === 'Cypress'),
    ).length;
    await expect(cards(page)).toHaveCount(expected);
  });

  test('project type filter', async ({ page }) => {
    await page.getByText(en.proj_personal, { exact: true }).filter({ visible: true }).click();
    await expect(cards(page)).toHaveCount(projects.filter((p) => p.type === 'personal').length);
  });

  test('details dialog opens, closes three ways and restores focus', async ({ page }) => {
    const url = page.url();
    const first = [...projects].sort((a, b) => b.id - a.id)[0];
    const button = page.locator(`[data-project="${first.slug}"] [data-open-project]`);
    const dialog = page.locator('dialog[open]');

    await button.click();
    await expect(dialog).toBeVisible();
    await expect(dialog.getByRole('heading', { level: 2 })).toHaveText(first.title);
    await expect(dialog).toContainText(first.achievements.en[0]);
    await page.keyboard.press('Escape');
    await expect(dialog).toHaveCount(0);
    await expect(button).toBeFocused();

    await button.click();
    await dialog.getByRole('button', { name: en.proj_close }).click();
    await expect(dialog).toHaveCount(0);

    await button.click();
    await page.mouse.click(5, 5);
    await expect(dialog).toHaveCount(0);
    expect(page.url()).toBe(url);
  });

  test('no broken images and no dead code/demo buttons', async ({ page }) => {
    for (const card of await page.locator('[data-project] img').all())
      await card.scrollIntoViewIfNeeded();
    const broken = await page.$$eval(
      '[data-project] img',
      (imgs) =>
        imgs.filter(
          (i) => !(i as HTMLImageElement).complete || (i as HTMLImageElement).naturalWidth === 0,
        ).length,
    );
    expect(broken).toBe(0);

    const withoutCode = projects.find((p) => !p.github)!;
    await page.locator(`[data-project="${withoutCode.slug}"] [data-open-project]`).click();
    await expect(
      page.locator('dialog[open]').getByRole('link', { name: en.proj_view_code }),
    ).toHaveCount(0);
  });

  test('Polish: dialog and search use Polish texts', async ({ page }) => {
    await page.locator('[data-lang-toggle]').last().click();
    const target = projects.find((p) => p.slug === 'waste-management-platform')!;
    const word = normalize(
      target.description.pl
        .split(' ')
        .find((w) => /[ąćęłńóśźż]/i.test(w) && w.length > 6)!
        .replace(/[^\p{L}]/gu, ''),
    );
    await page.getByRole('searchbox').fill(word);
    await expect(page.locator(`[data-project="${target.slug}"]`)).toBeVisible();

    await page.locator(`[data-project="${target.slug}"] [data-open-project]`).click();
    const dialog = page.locator('dialog[open]');
    await expect(dialog).toContainText(target.achievements.pl[0]);
    await expect(dialog.getByText(target.achievements.en[0])).toBeHidden();
    await expect(dialog.getByRole('heading', { level: 3 }).first()).toHaveText(
      pl.proj_achievements,
      { useInnerText: true },
    );
  });
});
