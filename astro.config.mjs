// @ts-check
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';
import react from '@astrojs/react';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';
import svgr from 'vite-plugin-svgr';

const site = 'https://xyzmaths.org';

// https://astro.build/config
export default defineConfig({
	adapter: cloudflare(),
	site,
	integrations: [sitemap(), react()],
	vite: {
		plugins: [
			tailwindcss(),
			svgr({
				include: '**/src/assets/icons/*.svg?react',
				svgrOptions: {
					svgProps: { 'aria-hidden': 'true', focusable: 'false' },
					replaceAttrValues: { '#141B34': 'currentColor' },
				},
			}),
		],
	},
});
