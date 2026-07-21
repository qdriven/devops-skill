import { defineConfig } from '@docmd/core';

export default defineConfig({
  title: 'docmd Diátaxis Template',
  url: 'https://example.github.io/docmd-diataxis-template',

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
      content: '© ' + new Date().getFullYear() + ' docmd Diátaxis Template',
      description: 'A bilingual Diátaxis documentation template built with docmd.',
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
          title: 'About',
          links: [
            { text: 'Why Diátaxis', url: '/explanation/why-diataxis/' },
            { text: 'docmd', url: 'https://docmd.io', external: true },
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
      defaultDescription: 'docmd + Diátaxis documentation template (中文 / English)',
      openGraph: { defaultImage: '' },
      twitter: { cardType: 'summary_large_image' },
    },
    sitemap: { defaultChangefreq: 'weekly' },
    search: {},
    mermaid: {},
    llms: { fullContext: true },
  },
});
