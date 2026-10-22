import en from './en.json';
import pl from './pl.json';

export type Lang = 'en' | 'pl';
export type TKey = keyof typeof en;
export type Localized<T = string> = Record<Lang, T>;

export const LANGS: readonly Lang[] = ['en', 'pl'];

export const dict: Record<Lang, Record<TKey, string>> = { en, pl };

export function t(key: TKey, lang: Lang): string {
  return dict[lang][key];
}

/** Both language values of a key, for attributes swapped at runtime (contracts/i18n.md). */
export function both(key: TKey): Localized {
  return { en: dict.en[key], pl: dict.pl[key] };
}
