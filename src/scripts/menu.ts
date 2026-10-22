// Mobile navigation drawer (port of the Reflex drawer in portfolio/header.py).
const openButton = document.querySelector<HTMLButtonElement>('[data-menu-open]');
const drawer = document.querySelector<HTMLElement>('[data-menu]');
const closeButton = document.querySelector<HTMLButtonElement>('[data-menu-close]');

if (openButton && drawer && closeButton) {
  const setOpen = (open: boolean) => {
    drawer.hidden = !open;
    openButton.setAttribute('aria-expanded', String(open));
    if (open) closeButton.focus();
    else openButton.focus();
  };

  openButton.addEventListener('click', () => setOpen(true));
  closeButton.addEventListener('click', () => setOpen(false));
  drawer.addEventListener('click', (event) => {
    if ((event.target as Element).closest('a')) drawer.hidden = true;
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !drawer.hidden) setOpen(false);
  });
  document.addEventListener('click', (event) => {
    const target = event.target as Node;
    if (!drawer.hidden && !drawer.contains(target) && !openButton.contains(target)) setOpen(false);
  });
}
