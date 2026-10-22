import { expect, test } from '@playwright/test';

// SC-003: every same-origin link, image and stylesheet reachable from the home page returns 200.
test('internal links and images resolve', async ({ page, request, baseURL }) => {
  test.skip(test.info().project.name !== 'chromium-desktop', 'crawl once');
  const origin = new URL(baseURL!).origin;
  const queue = [new URL(baseURL!).href];
  const seenPages = new Set<string>();
  const checked = new Map<string, number>();

  while (queue.length) {
    const pageUrl = queue.shift()!;
    if (seenPages.has(pageUrl)) continue;
    seenPages.add(pageUrl);
    await page.goto(pageUrl);

    const refs = await page.evaluate(() => {
      const out: string[] = [];
      document.querySelectorAll<HTMLAnchorElement>('a[href]').forEach((a) => out.push(a.href));
      document
        .querySelectorAll<HTMLImageElement>('img')
        .forEach((img) => out.push(img.currentSrc || img.src));
      document
        .querySelectorAll<HTMLSourceElement>('source[srcset], img[srcset]')
        .forEach((el) =>
          el.srcset
            .split(',')
            .forEach((part) => out.push(new URL(part.trim().split(' ')[0], location.href).href)),
        );
      document
        .querySelectorAll<HTMLLinkElement>('link[rel="stylesheet"], link[rel="icon"]')
        .forEach((l) => out.push(l.href));
      return out;
    });

    for (const ref of refs) {
      const target = new URL(ref);
      if (target.origin !== origin || target.protocol === 'mailto:') continue;
      target.hash = '';
      const href = target.href;
      if (!checked.has(href)) {
        const response = await request.get(href);
        checked.set(href, response.status());
      }
      if (href.endsWith('/') && !seenPages.has(href)) queue.push(href);
    }
  }

  const broken = [...checked].filter(([, status]) => status !== 200);
  expect(broken, JSON.stringify(broken, null, 2)).toEqual([]);
  expect(seenPages.size).toBeGreaterThanOrEqual(6);
});
