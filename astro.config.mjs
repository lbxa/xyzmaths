// @ts-check
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';

const site = 'https://xyzmaths.org';

// https://astro.build/config
	export default defineConfig({
	adapter: cloudflare(),
	site,
	integrations: [sitemap()],
	vite: {
		plugins: [tailwindcss()],
	},
});
