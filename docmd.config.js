import { defineConfig } from '@docmd/core';

export default defineConfig({
  title: 'devops-skill',
  url: 'https://qdriven.github.io/devops-skill',

  src: 'docs',
  out: 'site',

  i18n: {
    default: 'zh',
    position: 'options-menu',
    locales: [
      { id: 'zh', label: '中文' },
      { id: 'en', label: 'English' },
    ],
  },

  layout: {
    spa: true,
    header: { enabled: true },
    sidebar: { collapsible: true, defaultCollapsed: false },
    optionsMenu: {
      position: 'sidebar-top',
      components: { search: true, themeSwitch: true, sponsor: null },
    },
    footer: {
      style: 'complete',
      content: '© ' + new Date().getFullYear() + ' devops-skill',
      description: 'DevOps / Git workflow skills for AI agents.',
      branding: false,
      columns: [
        {
          title: 'Docs',
          links: [
            { text: 'Tutorials', url: '/tutorials/' },
            { text: 'How-to', url: '/how-to/' },
            { text: 'Explanation', url: '/explanation/' },
            { text: 'Reference', url: '/reference/' },
          ],
        },
        {
          title: 'Project',
          links: [
            {
              text: 'GitHub',
              url: 'https://github.com/qdriven/devops-skill',
              external: true,
            },
            {
              text: 'Site search',
              url: '/explanation/site-search/',
            },
          ],
        },
      ],
    },
  },

  theme: {
    name: 'sky',
    appearance: 'system',
    codeHighlight: true,
    customCss: ['assets/footer.css'],
  },

  minify: true,
  autoTitleFromH1: true,
  copyCode: true,
  pageNavigation: true,

  navigation: [
    { title: 'Home', path: '/', icon: 'home' },
    { title: 'Tutorials', path: '/tutorials/', icon: 'book-open' },
    { title: 'How-to', path: '/how-to/', icon: 'list-checks' },
    { title: 'Explanation', path: '/explanation/', icon: 'lightbulb' },
    { title: 'Reference', path: '/reference/', icon: 'book' },
  ],

  plugins: {
    seo: {
      defaultDescription: 'devops-skill — DevOps / Git workflow skills for AI agents (中文 / English)',
      openGraph: { defaultImage: '' },
      twitter: { cardType: 'summary_large_image' },
    },
    sitemap: { defaultChangefreq: 'weekly' },
    search: {},
    mermaid: {},
    llms: { fullContext: true },
  },
});
