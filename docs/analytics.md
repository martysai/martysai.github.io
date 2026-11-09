# Analytics

This site uses [Plausible Analytics](https://plausible.io/) for lightweight,
privacy-friendly visitor reporting. It reports page views, visits, referrers,
and unique visitors over daily, weekly, monthly, and custom periods.

## Configuration as code

The tracking integration is deliberately declarative and version controlled:

- `src/config/analytics.ts` is the single source of truth for the tracked
  domain, script endpoint, and enablement rule.
- `src/components/analytics/PlausibleAnalytics.astro` renders the provider
  beacon from that configuration.
- `src/layouts/BaseLayout.astro` installs the component once for every page.

Analytics is enabled only for production builds. This keeps local development
and preview work out of the public dashboard.

To reuse the integration on another Astro site, copy the configuration and
component, set `domain` to that site's canonical hostname, and add the
component to its shared base layout. No analytics secret is embedded in the
site or committed to Git.

The repository owns the integration configuration, while the Plausible account
owns the analytics site resource. Plausible's programmatic Sites API is an
Enterprise feature, so a standard hosted account requires the one-time site
registration below. If we later need fully automated account provisioning for
many sites, it should use that API with its token stored only in CI secrets.

## One-time Plausible setup

After this code is deployed:

1. Create a Plausible account and add `msaidov.com` as a site.
2. Verify that the deployed site's page source contains the Plausible script
   with `data-domain="msaidov.com"`.
3. Visit the site and confirm page views appear in the Plausible dashboard.
4. Add a short analytics disclosure to the site's privacy notice if one is
   introduced later.

Plausible's "unique visitors" metric is a privacy-preserving browser/device
estimate. It is not a guaranteed count of distinct people: the same person on
multiple devices may count twice, and a privacy reset can create a new visitor.
