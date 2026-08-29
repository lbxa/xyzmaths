// @ts-check
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';

const site = process.env.PUBLIC_SITE_URL;

// https://astro.build/config
export default defineConfig({
	adapter: cloudflare(),
	...(site ? { site } : {}),
	integrations: site ? [sitemap()] : [],
	vite: {
		plugins: [tailwindcss()],
	},
});
