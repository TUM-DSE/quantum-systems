# Quantum Systems @ TUM

This repository contains the Quantum Systems @ TUM research website.

Astro generates static pages.

React provides project search.

The website includes five project pages, 14 paper pages, a team directory, and a publication index.

## Development

Use the Nix development environment.

```sh
nix develop
npm ci
npm run dev
```

Open the local address that Astro prints.

The project dependency lockfile fixes the package versions.

The Nix lockfile fixes the development toolchain.

## Content

Edit `src/data/research.json` to update project descriptions, links, citations, and team records.

The `projects` array creates project pages from their `slug` fields.

Each project needs a unique slug and a conceptual illustration.

Use short nouns for diagram labels.

Keep summaries and methods grounded in the linked paper.

Use `src/data/evidence.json` for the extracted source metadata.

The `papers` array creates individual paper pages.

Each project lists its paper slugs in `paperIds`.

Each paper uses `projectSlug` to link back to its research area.

Paper lists use `sortDate` to put the newest paper first.

Record its date source in `sortDateSource`.

The `people` array records current members, alumni, and collaborators.

Store portraits in `public/people`.

Use `SOURCES.md` for source conflicts and review dates.

The homepage displays one card for each research area.

Each card shows a short description and previews of its papers.

Project pages contain extended descriptions and paper cards.

The homepage displays the full current team and a separate alumni section.

Pramod appears first.

The other members follow surname order.

`src/data/publication-sources.json` stores original abstracts and citation exports.

The paper pages link each abstract and BibTeX record to its source.

## Design

Read `AGENTS.md` before changing the website.

Read `prose-policy.md` before changing public text.

Use `src/styles/global.css` for layout, typography, and color.

The palette uses dark TUM blue, white, and off-white.

All titles use nouns or noun phrases.

The design has no subtitles.

Paper pages contain authors, resources, original abstracts, and BibTeX citations.

The project illustrations show conceptual structures.

They contain no experimental measurements.

`scripts/project-art.py` generates the editable SVG illustrations with Python.

The publication previews show the first page of each paper.

Detailed paper figure sections await a later content update.

## Checks

```sh
npm run check
npm run build
npm run verify
```

The verification script checks generated pages, local links, images, headings, project references, abstracts, and citations.

Run a subpath build before GitHub Pages deployment.

```sh
BASE_PATH=/quantum-systems SITE_URL=https://example.github.io npm run build
BASE_PATH=/quantum-systems npm run verify
```

Run `npm run build` again to restore the root-path local build.

## Repository

The source repository is [nathanieltornow/quantum-systems](https://github.com/nathanieltornow/quantum-systems).

GitHub Actions checks changes on the main branch and pull requests.

## GitHub Pages

The repository includes a manual deployment workflow.

Select GitHub Actions in the repository Pages settings.

Run the GitHub Pages workflow from the Actions page.

The workflow derives the website address and path from the repository name.

For a custom domain, set the repository variables `SITE_URL` and `BASE_PATH`.

Use `/` for `BASE_PATH` at the domain root.

Add the domain to `public/CNAME` and configure the domain in GitHub Pages.

The [Astro deployment guide](https://docs.astro.build/en/guides/deploy/github/) describes the hosting configuration.

## Assets

The website serves fonts and portraits locally.

Inter and IBM Plex Mono use the SIL Open Font License.

The font packages include their licenses.

Lab portraits retain the rights of their original owners.

`src/data/research.json` records each portrait source.
