import raw from "../data/research.json";

export interface Resource {
  label: string;
  url: string;
}

export interface Person {
  name: string;
  role: string;
  url: string;
  image: string;
  group: "current" | "alumni" | "collaborator";
}

export interface Paper {
  name: string;
  slug: string;
  projectSlug: string;
  title: string;
  authors: string[];
  year: number;
  sortDate: string;
  venue: string;
  status: string;
  abstract: string;
  abstractSource: string;
  citation: string;
  bibtexSource: string;
  image: string;
  resources: Resource[];
  note?: string;
  award?: string;
  awardSource?: string;
}

export interface Project {
  slug: string;
  name: string;
  description: string;
  overview: string[];
  method: string[];
  image: string;
  imageAlt: string;
  paperIds: string[];
  resources: Resource[];
}

export interface ProjectPreview extends Project {
  papers: Paper[];
}

export const projects = raw.projects as Project[];
export const newestFirst = (a: Paper, b: Paper) =>
  b.sortDate.localeCompare(a.sortDate) || a.name.localeCompare(b.name);
export const papers = [...(raw.papers as Paper[])].sort(newestFirst);
export const people = raw.people as Person[];
export const currentTeam = people
  .filter((person) => person.group === "current")
  .sort((a, b) => {
    if (a.name === "Pramod Bhatotia") return -1;
    if (b.name === "Pramod Bhatotia") return 1;
    return a.name
      .split(" ")
      .at(-1)!
      .localeCompare(b.name.split(" ").at(-1)!, "en");
  });
export const reviewed = raw.reviewed;
export const getProjectPapers = (project: Project) =>
  project.paperIds
    .map((id) => papers.find((paper) => paper.slug === id)!)
    .filter(Boolean)
    .sort(newestFirst);
export const projectPreviews = projects.map((project) => ({
  ...project,
  papers: getProjectPapers(project),
}));
export const path = (route = "") =>
  `${import.meta.env.BASE_URL.replace(/\/$/, "")}/${route.replace(/^\//, "")}`;
export const projectPath = (slug: string) => path(`projects/${slug}/`);
export const paperPath = (slug: string) => path(`publications/${slug}/`);
