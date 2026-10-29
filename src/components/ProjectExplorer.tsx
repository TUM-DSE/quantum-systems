import { useEffect, useMemo, useState } from "react";
import type { ProjectPreview } from "../lib/content";

interface Props {
  projects: ProjectPreview[];
  base: string;
}

export default function ProjectExplorer({ projects, base }: Props) {
  const [query, setQuery] = useState("");
  const [ready, setReady] = useState(false);
  useEffect(() => setReady(true), []);
  const visible = useMemo(
    () =>
      projects.filter((project) => {
        const paperTerms = project.papers
          .map(
            (paper) =>
              `${paper.name} ${paper.title} ${paper.authors.join(" ")} ${paper.year}`,
          )
          .join(" ");
        const terms =
          `${project.name} ${project.description} ${paperTerms}`.toLowerCase();
        return terms.includes(query.trim().toLowerCase());
      }),
    [query, projects],
  );

  return (
    <div className="explorer">
      <div className="explorer-controls" hidden={!ready}>
        <p className="sr-only" role="status" aria-live="polite">
          {visible.length} {visible.length === 1 ? "project" : "projects"}
        </p>
        <label className="search">
          <svg
            width="18"
            height="18"
            viewBox="0 0 24 24"
            fill="none"
            aria-hidden="true"
          >
            <circle cx="10" cy="10" r="6.5" />
            <path d="m15 15 6 6" />
          </svg>
          <span className="sr-only">Project search</span>
          <input
            type="search"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Project search"
          />
        </label>
      </div>
      <div className="area-grid">
        {visible.map((project) => (
          <a
            className="project-card area-card"
            href={`${base}projects/${project.slug}/`}
            key={project.slug}
          >
            <div className="project-image">
              <img
                src={`${base}${project.image}`}
                alt={project.imageAlt}
                width="600"
                height="320"
                loading="lazy"
              />
            </div>
            <div className="project-card-title">
              <h2>{project.name}</h2>
              <svg
                className="arrow"
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                aria-hidden="true"
              >
                <path d="M4 12h16m-7-7 7 7-7 7" />
              </svg>
            </div>
            <p className="project-description">{project.description}</p>
            <div className="paper-previews">
              {project.papers.map((paper) => (
                <div className="paper-preview" key={paper.slug}>
                  <img
                    src={`${base}${paper.image}`}
                    alt=""
                    width="612"
                    height="792"
                    loading="lazy"
                  />
                  <div>
                    <span className="paper-preview-title">{paper.name}</span>
                    <span className="paper-preview-meta">
                      <strong>{paper.venue}</strong> {paper.year}
                    </span>
                    {paper.award && <span className="paper-preview-award">{paper.award}</span>}
                  </div>
                </div>
              ))}
            </div>
          </a>
        ))}
      </div>
      {visible.length === 0 && (
        <div className="empty-state">
          <p>No projects match this search.</p>
          <button type="button" onClick={() => setQuery("")}>
            All projects
          </button>
        </div>
      )}
    </div>
  );
}
