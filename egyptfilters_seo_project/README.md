# المصرية للفلاتر — SEO Project

## What is included

- `app.py` — improved Streamlit app.
- `.streamlit/config.toml` — enables static file serving.
- `requirements.txt` — runtime dependencies.
- `seo-site/` — standalone SEO landing page with:
  - `index.html`
  - `robots.txt`
  - `sitemap.xml`
- `static/` — Streamlit static assets.

## Deploying the Streamlit app

Push `app.py`, `requirements.txt`, `.streamlit/`, `static/`, and `water_logo.png`
to the GitHub repository used by Streamlit Community Cloud.

## Important SEO architecture note

Streamlit Community Cloud can index public apps and supports a custom page title
and visible descriptive text. However, root-level `robots.txt` and `sitemap.xml`
are site-level resources. The `seo-site/` folder is intended to be deployed as
a normal static website (GitHub Pages, Cloudflare Pages, Netlify, Vercel, or a
custom web host).

For the strongest SEO setup, use a custom domain such as `egyptfilters.com`:

1. Deploy `seo-site/` on the custom domain.
2. Make the static site the canonical public marketing/SEO site.
3. Keep the Streamlit application at a subdomain or app path.
4. Update `SITE_URL`, canonical URLs, Open Graph URLs, sitemap URLs, and links
   after choosing the final domain.
5. Add the final domain to Google Search Console and submit `sitemap.xml`.
6. Validate structured data with Google's Rich Results Test.

## Current limitations

This project does not invent a business address, opening hours, ratings, prices,
or customer reviews. Add those only when the business actually has verified data.


## SEO landing pages added

- `/water-filters-egypt.html` — فلاتر مياه في مصر
- `/water-filter-installation.html` — تركيب فلاتر المياه
- `/water-filter-maintenance.html` — صيانة فلاتر المياه
- `/filter-cartridge-change.html` — تغيير شمعات فلاتر المياه
- `/filter-spare-parts.html` — قطع غيار فلاتر المياه

These pages use descriptive titles, meta descriptions, canonical links, internal
links, and visible Arabic content. They intentionally do not claim specific
city coverage, prices, ratings, opening hours, addresses, or product brands
because those facts were not present in the supplied app.

### Local SEO pages

- `/water-filters-cairo.html` — فلاتر مياه في القاهرة
- `/water-filters-giza.html` — فلاتر مياه في الجيزة
- `/water-filters-qalyubia.html` — فلاتر مياه في القليوبية

These pages are intentionally written as distinct service-area pages rather
than copies with only the governorate name changed.
