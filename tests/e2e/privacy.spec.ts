import { expect, test } from '@playwright/test';
import { ROUTES } from './routes';

// FR-026: no tracking, no third-party requests, no cookies.
test('only same-origin requests and no cookies', async ({ page, context, baseURL }) => {
  const origin = new URL(baseURL!).origin;
  const foreign: string[] = [];
  page.on('request', (req) => {
    const url = new URL(req.url());
    if (url.protocol.startsWith('http') && url.origin !== origin) foreign.push(req.url());
  });
  for (const route of ROUTES) {
    await page.goto(route.path);
    await page.waitForLoadState('networkidle');
  }
  await page.locator('[data-lang-toggle]').last().click();
  expect(foreign).toEqual([]);
  expect(await context.cookies()).toEqual([]);
});
