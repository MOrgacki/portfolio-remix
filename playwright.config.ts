import { defineConfig, devices } from '@playwright/test';

// BASE_URL lets the same suite run against a root-base build (custom-domain readiness, FR-014).
const baseURL = process.env.BASE_URL ?? 'http://localhost:4321/portfolio-remix/';

export default defineConfig({
  testDir: 'tests/e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  reporter: [['list'], ['html', { open: 'never' }]],
  use: {
    baseURL,
    trace: 'retain-on-failure',
  },
  projects: [
    {
      name: 'chromium-desktop',
      use: { ...devices['Desktop Chrome'], viewport: { width: 1440, height: 900 } },
    },
    { name: 'chromium-mobile', use: { ...devices['Pixel 7'] } },
  ],
  webServer: {
    command: process.env.SKIP_BUILD
      ? 'npm run preview -- --port 4321'
      : 'npm run build && npm run preview -- --port 4321',
    url: baseURL,
    reuseExistingServer: !process.env.CI,
    timeout: 180_000,
  },
});
