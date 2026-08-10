# CLAUDE.md

Guidance for AI agents (and humans) working in this repository.

## What this repo is

This is the **public** mirror of a distributed robotics infrastructure project.
It is **documentation-only**: there is no application code, no build system, and
no runtime to execute. It describes a public-safe pattern for a multi-node
sim-to-real robotics setup across a host workstation, a GPU cloud simulation
node, an NVIDIA Jetson edge node, and the ROS 2 networking that connects them.

Evidence: `SPEC.md`, `README.md`, `QUICKSTART.md`, and the per-node guides under
`docs/`.

## Repository layout (actual files)

- `README.md` — high-level overview, software stack table, public/private mirror strategy.
- `SPEC.md` — goal, non-goals, public boundary, success criteria.
- `QUICKSTART.md` — adaptation guide for host / Jetson / cloud / mesh.
- `CONTRIBUTING.md` — IaC-style contribution rules; keep examples generic.
- `PRE_RELEASE_CHECKLIST.md` — public-safety gate checklist.
- `VERIFICATION_PLAN.md` — release verification steps and manual boundary review.
- `MASTER_PLAN.md` — legacy/portfolio master plan at repo root (do not overwrite).
- `LICENSE` — Apache 2.0.
- `docs/OPERATING_STANDARD.md` — repo-local working rules and quality bar.
- `docs/HOST_WORKSTATION.md` — host/dev node setup pattern.
- `docs/JETSON_EDGE_NODE.md` — Jetson Orin edge node setup pattern.
- `docs/CLOUD_SIMULATION_NODE.md` — cloud GPU simulation node setup pattern.
- `docs/ROS2_NETWORKING.md` — ROS 2 discovery, networking, and security boundary.

There is **no** `AGENTS.md`, `BUILD_LOG.md`, `scripts/` directory, or
`repo_preflight.py` present in this repo, despite some references to them in the
prose (see "Known reference drift" below). For repo-local working rules, read
`docs/OPERATING_STANDARD.md`.

## The public boundary (most important rule)

This is a public repository. Everything committed here must be public-safe.
Per `SPEC.md` non-goals and `CONTRIBUTING.md`, never add:

- Real hostnames, LAN/IP addresses, or IP ranges.
- Usernames, VPN/tailnet identifiers, device names, or auth keys.
- Cloud project IDs, service-account material, or Terraform state.
- Credentials, private topology notes, build logs, or machine-specific procedures.

Also avoid overreach claims: do **not** describe the docs as a production
security baseline, a certified deployment, or a hardening guarantee
(`SPEC.md`, `PRE_RELEASE_CHECKLIST.md`).

Use generic placeholders only, e.g. `ssh <jetson_user>@<jetson_address>`
(see `docs/JETSON_EDGE_NODE.md`).

## Working conventions

- Documentation is organized by node role (host / edge / cloud / networking)
  plus an operating standard and verification/release docs.
- Keep hardware, networking, and verification notes separate but linked
  (`docs/OPERATING_STANDARD.md`).
- Quality bar (`docs/OPERATING_STANDARD.md`): no hardware claim without a setup
  path; no verification claim without a documented step; no hidden platform
  assumptions.
- External links to the author's robotics glossary and the private-repo name in
  `README.md` are intentional and public-safe; leave them.

## Verification

`VERIFICATION_PLAN.md` references an external/private gate:

```bash
python3 repo_preflight.py --repo . --profile public-export --paranoid
```

This script is **not present in this repo** — treat it as an external workspace
tool, not a runnable in-repo check. For self-contained verification of local
references, see `scripts/check_links.py` (added by the reference-integrity slice;
run `python3 scripts/check_links.py`).

Manual boundary review (`VERIFICATION_PLAN.md`): confirm generic identifiers,
no credentials/secrets/real addresses, and architecture-not-baseline framing.

## Git / safety

- Never commit to `main`. Branch for changes.
- Never commit secrets, real identifiers, or `.env`-style material.
- This repo is kept in sync from a private upstream; small, public-safe doc
  changes are the norm.

## Known reference drift (as of this writing)

Some prose references files that do not exist in this public mirror. The
reference-integrity slice reconciled the in-repo references; if you see a
dangling local link, fix it or mark it external rather than inventing a file.
