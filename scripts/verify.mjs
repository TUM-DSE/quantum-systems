import { readFile, readdir, stat } from "node:fs/promises";
import { resolve, join, relative, extname } from "node:path";
import assert from "node:assert/strict";

const root = resolve("dist");
const data = JSON.parse(await readFile("src/data/research.json", "utf8"));
const base = (process.env.BASE_PATH || "/").replace(/\/$/, "");
const errors = [];
const pages = [];

async function walk(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const file = join(directory, entry.name);
    if (entry.isDirectory()) await walk(file);
    else if (entry.name.endsWith(".html")) pages.push(file);
  }
}

await walk(root);
assert.equal(
  new Set(data.projects.map((project) => project.slug)).size,
  data.projects.length,
  "Project slugs must be unique.",
);
assert.equal(
  new Set(data.papers.map((paper) => paper.slug)).size,
  data.papers.length,
  "Paper slugs must be unique.",
);
const sources = JSON.parse(
  await readFile("src/data/publication-sources.json", "utf8"),
);
for (const project of data.projects) {
  const html = await readFile(
    join(root, "projects", project.slug, "index.html"),
    "utf8",
  );
  if (
    !html.includes(project.name) ||
    !html.includes("Overview") ||
    !html.includes("Papers")
  )
    errors.push(`The project page has incomplete content: ${project.slug}`);
  for (const id of project.paperIds) {
    const paper = data.papers.find((entry) => entry.slug === id);
    if (!paper || paper.projectSlug !== project.slug)
      errors.push(
        `The project has an invalid paper reference: ${project.slug}: ${id}`,
      );
    if (!html.includes(`publications/${id}/`))
      errors.push(`The project page has no paper link: ${project.slug}: ${id}`);
  }
}
for (const paper of data.papers) {
  const html = await readFile(
    join(root, "publications", paper.slug, "index.html"),
    "utf8",
  );
  const source = sources.papers.find((entry) => entry.slug === paper.slug);
  if (!html.includes("Abstract") || !html.includes("BibTeX"))
    errors.push(`The paper page has incomplete content: ${paper.slug}`);
  if (!html.includes(`projects/${paper.projectSlug}/`))
    errors.push(`The paper page has no project link: ${paper.slug}`);
  if (
    !source ||
    source.abstract !== paper.abstract ||
    source.bibtex !== paper.citation
  )
    errors.push(`The paper text differs from its source record: ${paper.slug}`);
  if (!paper.resources.length)
    errors.push(`The paper has no research resources: ${paper.slug}`);
}
const home = await readFile(join(root, "index.html"), "utf8");
if (
  (home.match(/class="project-card area-card"/g) || []).length !==
  data.projects.length
)
  errors.push("The homepage needs one card per project.");

for (const page of pages) {
  const html = await readFile(page, "utf8");
  const name = relative(root, page);
  if ((html.match(/<h1(?:\s|>)/g) || []).length !== 1)
    errors.push(`The page needs one primary heading: ${name}`);
  for (const match of html.matchAll(/(?:href|src)="([^"#]+)"/g)) {
    let url = match[1].split(/[?#]/)[0];
    if (/^(https?:|data:|mailto:|tel:)/.test(url)) continue;
    if (!url.startsWith("/")) continue;
    if (base && !url.startsWith(`${base}/`)) {
      errors.push(`The URL has no deployment base: ${name}: ${url}`);
      continue;
    }
    url = decodeURIComponent(url.slice(base.length));
    let target = join(root, url);
    if (url.endsWith("/")) target = join(target, "index.html");
    else if (!extname(url)) target = join(target, "index.html");
    try {
      await stat(target);
    } catch {
      errors.push(`The local resource does not exist: ${name}: ${url}`);
    }
  }
  for (const tag of html.matchAll(/<img\b[^>]*>/g)) {
    if (!/\balt="[^"]*"/.test(tag[0]))
      errors.push(`The image needs alternative text: ${name}`);
  }
}

const explorer = await readFile(join(root, "projects/index.html"), "utf8");
for (const project of data.projects) {
  if (!explorer.includes(`projects/${project.slug}/`))
    errors.push(`The static explorer has no project link: ${project.slug}`);
}

if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}
console.log(
  `Verified ${pages.length} static pages, ${data.projects.length} projects, and ${data.papers.length} papers.`,
);
console.log(
  "Local links, images, headings, project references, abstracts, and citations passed.",
);
