/**
 * Version-controlled analytics configuration.
 *
 * Analytics runs only in production builds so local development and preview
 * work do not affect the public dashboard.
 */
export const plausibleAnalytics = {
  enabled: import.meta.env.PROD,
  domain: 'msaidov.com',
  scriptSrc: 'https://plausible.io/js/script.js',
} as const;
