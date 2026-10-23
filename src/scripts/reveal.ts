// Fades [data-reveal] elements in as they scroll into view (styles in global.css).
if (document.documentElement.classList.contains('reveal-on')) {
  const pending = new Set(document.querySelectorAll<HTMLElement>('[data-reveal]'));

  // Reveal everything that has reached the viewport or was scrolled past (fast scrolls and
  // anchor jumps can skip an element entirely), including off-screen timeline steps.
  const reveal = () => {
    let batch = 0;
    for (const el of pending) {
      const rect = el.getBoundingClientRect();
      if (rect.height === 0 || rect.top > innerHeight * 0.95) continue; // hidden by a filter or still below
      // Stagger elements that appear together (e.g. a row of cards), capped so none waits long.
      el.style.setProperty('--reveal-delay', `${Math.min(batch++, 5) * 90}ms`);
      el.classList.add('is-revealed');
      pending.delete(el);
      observer.unobserve(el);
    }
  };

  let queued = false;
  const schedule = () => {
    if (queued) return;
    queued = true;
    requestAnimationFrame(() => {
      queued = false;
      reveal();
    });
  };

  // Also catches project cards that become visible again after filtering, without a scroll.
  const observer = new IntersectionObserver(schedule);
  pending.forEach((el) => observer.observe(el));
  addEventListener('scroll', schedule, { passive: true });
  addEventListener('resize', schedule);
  reveal();
}
