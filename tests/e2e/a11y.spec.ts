import AxeBuilder from '@axe-core/playwright';
import { expect, test } from '@playwright/test';
import { ROUTES } from './routes';

test.describe('accessibility (FR-020, FR-021)', () => {
  for (const lang of ['en', 'pl'] as const) {
    test.describe(lang, () => {
      test.use({ locale: lang === 'pl' ? 'pl-PL' : 'en-US' });
      for (const route of ROUTES) {
        test(`/${route.path} has no serious axe violations`, async ({ page }) => {
          await page.goto(route.path);
          // Let the scroll-reveal fades finish: half-faded text would fail the contrast check.
          await page.waitForFunction(() =>
            document
              .getAnimations()
              .every(
                (a) =>
                  a.playState === 'finished' ||
                  a.effect?.getComputedTiming().iterations === Infinity,
              ),
          );
          const results = await new AxeBuilder({ page }).analyze();
          const serious = results.violations
            .filter((v) => v.impact === 'serious' || v.impact === 'critical')
            .map(
              (v) =>
                `${v.id}: ${v.nodes
                  .map((n) => n.target.join(' '))
                  .slice(0, 3)
                  .join(', ')}`,
            );
          expect(serious).toEqual([]);
        });
      }
    });
  }

  test.describe('reduced motion', () => {
    test.use({ reducedMotion: 'reduce' });
    test('background animation is disabled', async ({ page }) => {
      await page.goto('');
      const names = await page.$$eval('.bg *', (els) =>
        els.map((el) => getComputedStyle(el).animationName),
      );
      expect(names.every((n) => n === 'none')).toBe(true);
    });
  });

  test('keyboard focus is visible', async ({ page }, info) => {
    test.skip(info.project.name === 'chromium-mobile', 'keyboard on desktop');
    await page.goto('');
    for (let i = 0; i < 8; i++) {
      await page.keyboard.press('Tab');
      const outline = await page.evaluate(() => {
        const el = document.activeElement as HTMLElement;
        const style = getComputedStyle(el);
        return style.outlineStyle !== 'none' && parseFloat(style.outlineWidth) > 0;
      });
      expect(outline).toBe(true);
    }
  });
});
