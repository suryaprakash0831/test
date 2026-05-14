# Crystal Ball AI UI

A premium enterprise SaaS hero banner concept for **Crystal Ball AI**, an autonomous AI agent for Warehouse Management System operations.

The visual story connects a modern warehouse floor with an AI command center and live operations dashboard for picking, packing, shipping, receiving, docking, job monitoring, incident correlation, and next-best-action recommendations.

## Brand note

The Blue Yonder logo is expected to be supplied as an official asset. To avoid recreating or distorting the logo, this project only references a logo file path and includes a neutral placeholder when the asset is not present.

Place the official, unmodified logo here:

```text
assets/blue-yonder-logo.svg
```

If your official file is a PNG or another supported image format, put it in `assets/` and update the `img` source in `index.html`.

## Project structure

```text
.
├── .github/workflows/deploy-pages.yml
├── .nojekyll
├── assets/
│   └── README.md
├── index.html
├── package.json
├── scripts/check-static.py
├── styles.css
└── README.md
```

## Installation guide

### Prerequisites

- Python 3.9 or newer
- A modern browser such as Chrome, Edge, Safari, or Firefox
- Optional: Node.js 18+ if you want to run commands through `npm`

### Run locally with Python

```bash
python3 -m http.server 4173
```

Open:

```text
http://127.0.0.1:4173
```

### Run locally with npm

No package installation is required because the UI is static.

```bash
npm start
```

Open:

```text
http://127.0.0.1:4173
```


## GitHub Pages hosting

This repository includes a GitHub Actions workflow that validates and deploys the static UI to GitHub Pages.

### Enable Pages

1. Push or merge this branch to GitHub.
2. In the GitHub repository, open **Settings → Pages**.
3. Set **Source** to **GitHub Actions**.
4. Open **Actions → Deploy Crystal Ball AI UI to GitHub Pages** and run it manually, or push a change to `main`/`work`.

### Validation URL

After the workflow succeeds, GitHub will publish the page at the Pages URL shown in the workflow summary. The URL generally follows this pattern:

```text
https://<github-org-or-user>.github.io/<repository-name>/
```

For this workspace I cannot produce a live hosted URL because no GitHub remote is configured locally. Once the branch is pushed to GitHub and Pages is enabled, use the workflow output URL above to validate the hosted banner.

## Using in PowerPoint or a pitch deck

1. Start the local server.
2. Open the page in a browser at 16:9 dimensions.
3. Export a screenshot at high resolution.
4. Insert the screenshot into PowerPoint, Keynote, Google Slides, or your innovation event presentation.

## Customization checklist

- Add the official Blue Yonder logo to `assets/blue-yonder-logo.svg`.
- Adjust dashboard card labels in `index.html` if the demo scenario changes.
- Tune colors and visual density in `styles.css` for a specific event theme.
- Keep text minimal so the banner remains leadership-friendly.
