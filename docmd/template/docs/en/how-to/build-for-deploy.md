# How to build for deployment

## Steps

1. Run the production build:

   ```bash
   npm run build
   ```

2. Confirm static files exist under `site/`.
3. Deploy the `site/` directory to GitHub Pages, Netlify, Cloudflare Pages, or any static host.

For GitHub Actions, push to `main` after enabling Pages with the **GitHub Actions** source.
