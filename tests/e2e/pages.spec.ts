import { expect, test } from '@playwright/test';
import en from '../../src/i18n/en.json' with { type: 'json' };
import { ROUTES } from './routes';

test.describe('pages (US1)', () => {
  for (const route of ROUTES) {
    test(`/${route.path} loads with title, description and h1`, async ({ page }) => {
      const response = await page.goto(route.path);
      expect(response?.status()).toBe(200);
      await expect(page.locator('h1').first()).toBeVisible();
      await expect(page).toHaveTitle(/Marcin Orgacki/);
      const description = await page.locator('meta[name="description"]').getAttribute('content');
      expect(description?.length).toBeGreaterThan(10);
    });

    test(`/${route.path} survives a refresh`, async ({ page }) => {
      await page.goto(route.path);
      const response = await page.reload();
      expect(response?.status()).toBe(200);
      await expect(page.locator('h1').first()).toBeVisible();
    });
  }

  test('navigation marks the current page', async ({ page, isMobile }) => {
    await page.goto('projects/');
    if (isMobile) await page.locator('[data-menu-open]').click();
    const nav = page.getByRole('navigation', { name: isMobile ? 'Mobile' : 'Main' });
    const current = nav.locator('a[aria-current="page"]');
    await expect(current).toHaveCount(1);
    await expect(current).toContainText(en.nav_projects);
  });

  test('navigation reaches every page', async ({ page, isMobile }) => {
    for (const route of ROUTES) {
      await page.goto('');
      if (isMobile) await page.locator('[data-menu-open]').click();
      const nav = page.getByRole('navigation', { name: isMobile ? 'Mobile' : 'Main' });
      await nav.getByRole('link', { name: en[route.nav] }).click();
      await expect(page).toHaveURL(new RegExp(`${route.path}$`));
    }
  });

  test('unknown address shows the branded 404 page', async ({ page }) => {
    const response = await page.goto('does-not-exist/');
    expect(response?.status()).toBe(404);
    await expect(page.getByRole('heading', { level: 1 })).toHaveText(en.not_found_title, {
      useInnerText: true,
    });
    await page.getByRole('link', { name: en.not_found_home }).click();
    await expect(page.getByRole('heading', { level: 1 })).toBeVisible();
  });

  test.describe('without JavaScript', () => {
    test.use({ javaScriptEnabled: false, locale: 'pl-PL' });
    for (const route of ROUTES) {
      test(`/${route.path} is readable in English`, async ({ page }) => {
        await page.goto(route.path);
        await expect(page.locator('h1').first()).toBeVisible();
        const visiblePolish = await page.locator('main [lang="pl"]:visible').count();
        expect(visiblePolish).toBe(0);
      });
    }
  });

  for (const width of [320, 768, 1440, 1920]) {
    test(`no horizontal scroll at ${width}px`, async ({ page }) => {
      await page.setViewportSize({ width, height: 900 });
      for (const route of ROUTES) {
        await page.goto(route.path);
        const overflow = await page.evaluate(
          () => document.documentElement.scrollWidth - document.documentElement.clientWidth,
        );
        expect(overflow, `/${route.path} at ${width}px`).toBeLessThanOrEqual(0);
      }
    });
  }
});
