// Mobile navigation drawer (port of the Reflex drawer in portfolio/header.py).
const openButton = document.querySelector<HTMLButtonElement>('[data-menu-open]');
const drawer = document.querySelector<HTMLElement>('[data-menu]');
const closeButton = document.querySelector<HTMLButtonElement>('[data-menu-close]');
const backdrop = document.querySelector<HTMLElement>('[data-menu-backdrop]');

if (openButton && drawer && closeButton) {
  const show = (open: boolean) => {
    drawer.hidden = !open;
    if (backdrop) backdrop.hidden = !open;
    // Keep the page behind the open menu from scrolling.
    document.body.style.overflow = open ? 'hidden' : '';
  };
  const setOpen = (open: boolean) => {
    show(open);
    openButton.setAttribute('aria-expanded', String(open));
    if (open) closeButton.focus();
    else openButton.focus();
  };

  openButton.addEventListener('click', () => setOpen(true));
  closeButton.addEventListener('click', () => setOpen(false));
  drawer.addEventListener('click', (event) => {
    if ((event.target as Element).closest('a')) show(false);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !drawer.hidden) setOpen(false);
  });
  document.addEventListener('click', (event) => {
    const target = event.target as Node;
    if (!drawer.hidden && !drawer.contains(target) && !openButton.contains(target)) setOpen(false);
  });
}
