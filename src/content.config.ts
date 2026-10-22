// Project data validation, equivalent to specs/001-astro-github-pages/contracts/project.schema.json.
import { defineCollection } from 'astro:content';
import { file } from 'astro/loaders';
import { z } from 'astro/zod';
import techCategories from './data/tech-categories.json';

const localized = z.object({ en: z.string().trim().min(1), pl: z.string().trim().min(1) });
const categorized = new Set(techCategories.flatMap((c) => c.techs));

const projects = defineCollection({
  // `id` in the JSON is the display order; the collection id is the stable slug.
  loader: file('src/data/projects.json', {
    parser: (text) =>
      (JSON.parse(text) as Array<Record<string, unknown>>).map((p) => ({
        ...p,
        order: p.id,
        id: p.slug,
      })),
  }),
  schema: ({ image }) =>
    z
      .object({
        order: z.number().int().min(1),
        slug: z.string().regex(/^[a-z0-9]+(-[a-z0-9]+)*$/),
        title: z.string().min(1),
        description: localized,
        technologies: z
          .array(z.string().min(1))
          .min(1)
          .refine((techs) => techs.every((t) => categorized.has(t)), {
            message: 'every technology must belong to a category in src/data/tech-categories.json',
          }),
        domain: z.string().min(1),
        platform: z.enum(['Web', 'Mobile', 'Desktop', 'AI/Automation']),
        type: z.enum(['personal', 'client']),
        status: z.enum(['completed', 'in-progress']),
        achievements: z
          .object({ en: z.array(z.string().min(1)), pl: z.array(z.string().min(1)) })
          .refine((a) => a.en.length === a.pl.length, {
            message: 'en and pl achievements MUST have equal length',
          }),
        image: image().nullable(),
        imageAlt: localized.optional(),
        github: z.url().nullable(),
        demo: z.url().nullable(),
      })
      .refine((p) => p.image === null || p.imageAlt !== undefined, {
        message: 'imageAlt is required when image is set',
      }),
});

export const collections = { projects };
