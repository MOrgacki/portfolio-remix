import { expect, test } from '@playwright/test';
import en from '../../src/i18n/en.json' with { type: 'json' };
import pl from '../../src/i18n/pl.json' with { type: 'json' };
import { ROUTES } from './routes';

test.describe('contact (US5)', () => {
  test.use({ locale: 'en-US' });

  test("home 'Let's talk' tile starts an email in the chosen language", async ({ page }) => {
    await page.goto('');
    await page.locator('[data-lang-toggle]').last().click();
    await expect(page.getByRole('link', { name: pl.about_cta_lets_talk })).toHaveAttribute(
      'href',
      'mailto:marcinorgacki@gmail.com',
    );
  });

  test('contact channels', async ({ page }) => {
    await page.goto('contact/');
    const main = page.locator('main');
    await expect(main.getByRole('link', { name: en.contact_email, exact: true })).toHaveAttribute(
      'href',
      'mailto:marcinorgacki@gmail.com',
    );
    for (const name of [en.contact_linkedin, en.contact_github]) {
      const link = main.getByRole('link', { name, exact: true });
      await expect(link).toHaveAttribute('target', '_blank');
      await expect(link).toHaveAttribute('rel', /noopener/);
    }
  });

  test('no chat UI anywhere', async ({ page }) => {
    for (const route of ROUTES) {
      await page.goto(route.path);
      const html = await page.content();
      expect(html).not.toContain('Chat interface coming soon');
      expect(html).not.toContain('AI assistant');
    }
  });
});
