/**
 * Base-path-aware URL for internal pages and public files (research R3).
 * url('') → '/portfolio-remix/', url('projects/') → '/portfolio-remix/projects/'.
 */
export function url(path = ''): string {
  const base = import.meta.env.BASE_URL.replace(/\/+$/, '');
  const clean = path.replace(/^\/+/, '');
  return `${base}/${clean}`;
}
