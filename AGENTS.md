# Website instructions

## Design

Use a clean, minimal, static design for the Quantum Systems @ TUM website.

Use Quantum Systems @ TUM as the full website name.

Use Quantum Systems @ TUM in the header.

Use Technical University of Munich as the footer affiliation.

Use dark TUM blue, `#003359`, white, and off-white, `#f7f8f5`.

Use blue opacity for rules and secondary text.

Use generous space, thin rules, and clear type hierarchy.

Keep backgrounds flat.

Do not add gradients, shadows, decorative badges, animated backgrounds, or rounded card grids.

Use local fonts and local assets.

Use Inter for primary titles, project names, and body text.

Use IBM Plex Mono for navigation, research group labels, metadata, and controls.

Keep monospaced labels in sentence case or title case.

Show portraits in blue tones by default.

Show their original colors on hover and keyboard focus.

Keep scientific diagrams static and editable.

## Titles

Use nouns, noun phrases, project names, or person names for all titles and navigation labels.

Examples include Research, Projects, Team, Publications, Architecture, Overview, and Citation.

Never use sentences as titles.

Never add subtitles, taglines, eyebrow text, or duplicate title descriptions.

Place explanatory prose inside the relevant content section.

Keep publication titles exact in bibliographic records.

## Writing

Use plain English.

Put one fact or instruction in each sentence.

Aim for 20 words or fewer in each sentence.

Use active voice and name the actor.

Use ASCII in source and prose.

Use commas, full stops, and colons in prose.

Preserve exact paths, identifiers, numbers, and bibliographic metadata.

Read `prose-policy.md` before changing public text.

Load the comments skill before adding comments or docstrings.

## Research records

Use `src/data/research.json` as the content source.

Preserve evidence URLs and review dates.

Use official sources for project summaries, authors, resources, and team roles.

Keep preprints distinct from published work.

Treat future venue labels as source claims.

Do not infer active work from a publication year.

Do not infer current lab membership from paper authorship.

Keep alumni and collaborators separate from current members.

Record conflicting sources in `SOURCES.md`.

Use the original abstracts with links to their sources.

Preserve abstract wording while normalizing typesetting for plain text.

Use source-provided BibTeX and preserve original exports in `src/data/publication-sources.json`.

Keep conceptual illustrations distinct from paper figures in content records.

Do not display generic illustration captions such as Conceptual illustration.

Keep useful image descriptions in alternative text.

Use these research groups in this order: Hybrid Computing and Orchestration, Error Correction and Decoding, Fault-Tolerant Compilation, Neutral-Atom Systems, Readout and Control.

Show one project card for each research area.

Show a short description and paper previews in each project card.

Put extended descriptions and paper cards on project pages.

Put original abstracts and BibTeX on individual paper pages.

Order paper cards and paper previews from newest to oldest.

Use the source-backed `sortDate` field for paper order.

Keep the research area order and the team order specified here.

Do not show project totals, index numbers, or decorative counts.

Give venue labels clear visual emphasis.

Show source-backed award distinctions and preserve their exact status.

Show the full current team on the homepage.

Put Pramod Bhatotia first.

Sort the remaining members by surname.

Keep alumni in a separate section.

Use initials when a person has no portrait.

Do not invent results, performance measurements, repository links, portraits, or affiliations.

## Implementation

Use Astro for static pages and React for project search.

Keep all research content in the generated HTML.

Make the site useful when JavaScript is disabled.

Use relative base-aware links for GitHub Pages.

Use semantic HTML, visible keyboard focus, accessible labels, and responsive layouts.

Keep controls usable at a viewport width of 320 pixels.

Use the Nix development environment for the project toolchain.

Stage new flake files before evaluating Nix.

Run `npm run check`, `npm run build`, and `npm run verify` after relevant changes.

Verify a project subpath build before changing deployment configuration.

Keep the repository independent of hosted website builders.
