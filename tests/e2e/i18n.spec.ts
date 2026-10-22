import { expect, test } from '@playwright/test';
import en from '../../src/i18n/en.json' with { type: 'json' };
import pl from '../../src/i18n/pl.json' with { type: 'json' };
import { ROUTES } from './routes';

const htmlLang = (page: import('@playwright/test').Page) =>
  page.evaluate(() => document.documentElement.dataset.lang);

test.describe('language (US2)', () => {
  test.describe('Polish browser', () => {
    test.use({ locale: 'pl-PL' });
    test('first visit shows Polish', async ({ page }) => {
      await page.goto('');
      expect(await htmlLang(page)).toBe('pl');
      await expect(page.locator('main h1')).toContainText(pl.home_hello, { useInnerText: true });
      await expect(page).toHaveTitle(pl.page_title_home);
    });
  });

  test.describe('English browser', () => {
    test.use({ locale: 'en-US' });

    test('first visit shows English', async ({ page }) => {
      await page.goto('');
      expect(await htmlLang(page)).toBe('en');
    });

    test('toggle switches text, attributes and title, and persists', async ({ page }) => {
      await page.goto('experience/');
      await expect(page.locator('h1')).toHaveText(en.exp_title, { useInnerText: true });
      const toggle = page.locator('[data-lang-toggle]').last();
      await expect(toggle).toHaveAccessibleName(`EN – ${en.lang_switch_label}`);

      await toggle.click();
      expect(await htmlLang(page)).toBe('pl');
      await expect(page.locator('h1')).toHaveText(pl.exp_title, { useInnerText: true });
      await expect(page).toHaveTitle(pl.page_title_experience);
      await expect(toggle).toHaveAccessibleName(`PL – ${pl.lang_switch_label}`);

      await page.reload();
      expect(await htmlLang(page)).toBe('pl');
      await page.goto('case-studies/');
      await expect(page.locator('h1')).toHaveText(pl.case_studies_title, { useInnerText: true });

      await page.locator('[data-lang-toggle]').last().click();
      await expect(page.locator('h1')).toHaveText(en.case_studies_title, { useInnerText: true });
      await expect(page).toHaveTitle(en.page_title_case_studies);
    });

    test('invalid stored value falls back to the browser locale', async ({ page }) => {
      await page.addInitScript(() => localStorage.setItem('portfolio.lang', 'xx'));
      await page.goto('');
      expect(await htmlLang(page)).toBe('en');
    });

    test('stored Polish is applied before first paint (no flash)', async ({ page }) => {
      await page.addInitScript(() => {
        localStorage.setItem('portfolio.lang', 'pl');
        document.addEventListener('DOMContentLoaded', () => {
          const visibleEnglish = [...document.querySelectorAll('main [lang="en"]')].filter(
            (el) => getComputedStyle(el).display !== 'none',
          ).length;
          (window as any).__firstPaint = {
            lang: document.documentElement.dataset.lang,
            visibleEnglish,
          };
        });
      });
      await page.goto('');
      const snapshot = await page.evaluate(() => (window as any).__firstPaint);
      expect(snapshot).toEqual({ lang: 'pl', visibleEnglish: 0 });
    });
  });

  for (const lang of ['en', 'pl'] as const) {
    test.describe(`${lang}: no empty texts`, () => {
      test.use({ locale: lang === 'pl' ? 'pl-PL' : 'en-US' });
      for (const route of ROUTES) {
        test(`/${route.path}`, async ({ page }) => {
          await page.goto(route.path);
          const empty = await page.evaluate((active) => {
            return [...document.querySelectorAll(`[lang="${active}"]`)]
              .filter((el) => el !== document.documentElement && !el.textContent?.trim())
              .map((el) => el.outerHTML.slice(0, 80));
          }, lang);
          expect(empty).toEqual([]);
        });
      }
    });
  }
});
