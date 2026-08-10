# Master Plan (Canonical): Distributed Robotics Infrastructure (Public)

> **Relationship to `MASTER_PLAN.md` at the repo root:** the root file is a
> prior/portfolio master plan and is preserved as-is. **This file
> (`docs/MASTER_PLAN.md`) is the canonical, maintained plan.** Where the two
> differ, this file governs. This plan does not overwrite the root file.

Each section separates **FACTS** (with `file` / `file:line` evidence),
**ASSUMPTIONS**, and **RECOMMENDATIONS**.

---

## 1. Executive Summary

**FACTS**
- This repo is the public, documentation-only mirror of a distributed
  sim-to-real robotics infrastructure pattern across a host workstation, GPU
  cloud simulation node, Jetson edge node, and ROS 2 networking. Evidence:
  `SPEC.md:5`, `README.md:6`, `docs/`.
- The public boundary forbids real hostnames, IPs, usernames, VPN/cloud
  identifiers, credentials, private topology notes, and build logs. Evidence:
  `SPEC.md:9`, `CONTRIBUTING.md:8-9`, `VERIFICATION_PLAN.md:13-14`.
- The repo contains 12 tracked files: 8 root markdown docs + LICENSE + 5 docs
  under `docs/`. No source code, no `scripts/`, no `repo_preflight.py`. Evidence:
  file inventory.

**ASSUMPTIONS**
- The intended consumer wants a reusable mental model, not copy-paste access to
  a live deployment.
- The repo stays documentation-only, not executable infrastructure-as-code.

**RECOMMENDATIONS**
- Maintain it as a public architecture handbook with strict placeholder
  discipline and release gates.
- Repair in-repo reference drift and add a self-contained local link check
  before any further expansion.

---

## 2. Current-State Findings (with file evidence)

**FACTS**
- `README.md:8` says read `AGENTS.md`, but no `AGENTS.md` exists. Evidence:
  file inventory.
- `README.md:14,52-54` reference `BUILD_LOG.md`, `host-pc-setup.md`,
  `gcp-cloud-node.md`, `jetson-setup.md`; the real guides are
  `docs/HOST_WORKSTATION.md`, `docs/CLOUD_SIMULATION_NODE.md`,
  `docs/JETSON_EDGE_NODE.md`. Evidence: file inventory.
- `QUICKSTART.md:25` runs `./scripts/init_mesh.sh`, but no `scripts/` directory
  exists. Evidence: file inventory.
- `docs/OPERATING_STANDARD.md:14-15` references `BUILD_LOG.md`,
  `host-pc-setup.md`, `gcp-cloud-node.md`, `jetson-setup.md` (same legacy
  names). Evidence: file inventory.
- `VERIFICATION_PLAN.md:8` depends on `repo_preflight.py`, which is absent.
  Evidence: file inventory.
- `SPEC.md:9` and `CONTRIBUTING.md:8-9` define the prohibited-identifier set.
- `docs/ROS2_NETWORKING.md:27,29,33` correctly warns against public exposure and
  real addresses/identities; `docs/JETSON_EDGE_NODE.md:33,36` uses generic SSH
  placeholders. No real identifiers found in the docs.
- `README.md:58-94` documents the private/public mirror strategy and
  `public-sync-manifest.json` provenance.

**ASSUMPTIONS**
- The stale filenames are public-mirror drift, not intentional broken links.
- `repo_preflight.py` is an external workspace tool, not meant to ship here.

**RECOMMENDATIONS**
- Reconcile every in-repo local reference to a file/script that exists (or mark
  it external). Redirect the `AGENTS.md` reference to
  `docs/OPERATING_STANDARD.md`, which is exactly that content.
- Remove the unrunnable `./scripts/init_mesh.sh` snippet from QUICKSTART.

---

## 3. Product Requirements

**FACTS**
- Public-safe pattern for multi-node robotics infra across local edge nodes and
  cloud compute. Evidence: `QUICKSTART.md:4`.
- Setup examples must use generic values only. Evidence: `SPEC.md:20`.

**ASSUMPTIONS**
- Readers adapt generic steps to a private environment outside this repo.

**RECOMMENDATIONS**
- Target users: infrastructure reviewer, engineer adapting a generic topology,
  public-mirror maintainer.
- Core workflows: read overview -> pick host/edge/cloud/networking guide ->
  adapt generically -> run public-surface checks before publication.
- Non-goals: production security baseline, certified deployment, live
  automation, real topology disclosure (`SPEC.md:10-11`).
- Supporting capabilities: identifier scanner, local link/reference checker,
  artifact-boundary checker.
- Error states: real identifier found -> block release; dangling local
  reference -> block until fixed/marked external; unproven hardening claim ->
  downgrade wording.

---

## 4. DORA AI Capability Alignment

**FACTS**
- Repo is documentation-only infrastructure guidance, not an AI runtime.
  Evidence: `CONTRIBUTING.md:3`.

**ASSUMPTIONS**
- AI agents may maintain docs and run static audits, but must not operate
  hardware or cloud nodes from this repo.

**RECOMMENDATIONS** (mapped to DORA AI capabilities)
- **Clear & communicated AI stance:** allowed = doc maintenance, placeholder
  scanning, public-surface auditing, claim checking; prohibited = reading or
  publishing private topology, credentials, real hosts/IPs.
- **Healthy data ecosystem:** track public docs, generic examples, and sync
  provenance; no private deployment notes.
- **Version control:** small public-safe doc changes; public-surface scan on
  every sync; label generated artifacts.
- **Working in small batches:** first slice = fix references + add a static
  local link check.
- **User-centricity:** named user = infrastructure reviewer; success signal =
  reader adapts the pattern without seeing private values.
- **Internal platform / golden path:** one-command static verification for local
  links and references.
- **Missing DORA evidence:** no self-contained public audit existed before this
  plan; first action is the local link checker in the recommended slice.

---

## 5. Architecture Plan

**FACTS**
- Architecture is documentation organized by node role: `docs/HOST_WORKSTATION.md`,
  `docs/JETSON_EDGE_NODE.md`, `docs/CLOUD_SIMULATION_NODE.md`,
  `docs/ROS2_NETWORKING.md`, plus `docs/OPERATING_STANDARD.md`.
- Documented data flow: workstation builds/tests ROS 2 packages; cloud node
  provides burst GPU simulation; edge node runs near sensors/actuators; ROS 2
  networking connects them via private network / discovery server / VPN overlay.
  Evidence: `docs/HOST_WORKSTATION.md`, `docs/CLOUD_SIMULATION_NODE.md:1-3`,
  `docs/JETSON_EDGE_NODE.md:1-3`, `docs/ROS2_NETWORKING.md:24-26`.

**ASSUMPTIONS**
- The public architecture should not ship live deployment scripts unless they
  are generic, reviewed, and safe.

**RECOMMENDATIONS**
- Add (future): `docs/TOPOLOGY.md` (generic diagram), `docs/IDENTIFIER_POLICY.md`
  (placeholder formats + prohibited values), `scripts/` for static checks.
- Configuration/secrets: placeholders only; never commit service-account
  material, Terraform state, tailnet details, real ports/addresses, node names.
- ADRs worth recording: documentation-only vs public IaC; placeholder
  convention; sync-manifest retention in public exports.

---

## 6. Feature Roadmap (milestones + acceptance criteria)

**RECOMMENDATIONS**
- **M1 — Reference & boundary repair.** Acceptance: every in-repo local
  reference resolves to a present file, or is removed/marked external.
- **M2 — Static local link check.** Acceptance: one stdlib-only command flags
  any dangling local markdown link or `./script` reference; exits non-zero on
  failure.
- **M3 — Identifier policy doc.** Acceptance: placeholder format + prohibited
  real identifiers documented.
- **M4 — Generic topology diagram.** Acceptance: diagram contains no real
  hostnames/IPs/usernames/cloud IDs/tailnet names.
- **M5 — Release artifact audit.** Acceptance: release archive extracted and
  scanned before public use.

---

## 7. Parallelization Plan

**RECOMMENDATIONS**
- **Workstream A — Reference repair.** Owns `README.md`, `QUICKSTART.md`,
  `docs/OPERATING_STANDARD.md`. Verify: local link check.
- **Workstream B — Node guide hardening.** Owns the three node guides. Verify:
  placeholder scan.
- **Workstream C — Networking/security boundary.** Owns `docs/ROS2_NETWORKING.md`,
  `SPEC.md`, `VERIFICATION_PLAN.md`. Verify: prohibited-identifier + claim scan.
- **Workstream D — Release tooling.** Owns future `scripts/`,
  `PRE_RELEASE_CHECKLIST.md`. Verify: static check + artifact extraction.
- **Sequential gate:** any cloud/networking automation waits for explicit
  security review.

---

## 8. Task Backlog

| Priority | Task | Files affected | Tests/docs | Verification | Done condition |
| --- | --- | --- | --- | --- | --- |
| P0 | Fix stale README local references | `README.md` | doc | `python3 scripts/check_links.py` | No dangling local refs in README |
| P0 | Redirect `AGENTS.md` reference to existing operating standard | `README.md` | doc | local link check | README points to `docs/OPERATING_STANDARD.md` |
| P0 | Fix legacy filenames in operating standard | `docs/OPERATING_STANDARD.md` | doc | local link check | No legacy filenames referenced |
| P0 | Remove unrunnable `./scripts/init_mesh.sh` snippet | `QUICKSTART.md` | doc | local link check | No reference to absent script |
| P0 | Add stdlib local link checker | `scripts/check_links.py` | tool | run the checker | Exits 0 on clean repo, non-zero on dangling ref |
| P1 | Add identifier/placeholder policy | `docs/IDENTIFIER_POLICY.md` | doc | `rg` identifier scan | Real identifiers stay prohibited |
| P1 | Add generic topology diagram | `docs/TOPOLOGY.md` | doc | manual audit | Diagram is generic and useful |
| P2 | Add release evidence template | `PRE_RELEASE_CHECKLIST.md` | checklist | manual review | Release readiness is replayable |

---

## 9. Testing & Verification Plan

**FACTS**
- Documented release verification currently depends on the external
  `repo_preflight.py` plus manual boundary review. Evidence:
  `VERIFICATION_PLAN.md:8,11-15`.

**RECOMMENDATIONS**
- **Static checks (in-repo):** local file-reference / markdown-link check
  (`scripts/check_links.py`); prohibited-identifier scan (`rg` for IPs,
  hostnames, usernames, tailnet names, cloud IDs, keys); claim scan for
  production/certification/baseline overreach.
- **Artifact-boundary checks:** build release archive, list manifest, extract to
  temp dir, scan extracted contents, confirm only public docs/assets present.
- **Regression loop:** doc edit -> local link check -> identifier scan -> claim
  review -> release checklist.
- Unit/integration tests are N/A while the repo is documentation-only.

---

## 10. Release Criteria

**RECOMMENDATIONS**
- All in-repo local links/references resolve.
- All examples use generic placeholders; no real hostnames, IPs, usernames,
  tailnet/cloud identifiers, credentials, private topology, or build logs
  (`SPEC.md:9`).
- No production-baseline / certification / hardening guarantee claims
  (`SPEC.md:10-11`, `PRE_RELEASE_CHECKLIST.md`).
- Public-export gate run (external `repo_preflight.py`) and manual boundary
  review passed (`VERIFICATION_PLAN.md`).
- No push/publish without explicit approval.

---

## 11. Risks & Open Questions

**RISKS**
- Stale docs mislead users into expecting missing files/scripts.
- Public topology language could accidentally reveal real machine roles.
- ROS 2 networking guidance mistaken for a hardened production baseline.
- Sync-from-private could leak internal operational details.
- Release archives may include generated logs if not inspected.

**OPEN QUESTIONS**
- Should this repo ever ship runnable infrastructure scripts, or stay docs-only?
- Should sync manifests be committed publicly or kept only as release evidence?
- What exact placeholder convention should be enforced for host/user/IP/VPN/cloud?

---

## 12. Recommended First Implementation Slice

**RECOMMENDATION — Reference-integrity slice.**

Smallest meaningful, genuinely-useful, end-to-end verifiable change.

**What it changes**
- Reconcile every dangling in-repo local reference:
  - `README.md`: redirect `AGENTS.md` -> `docs/OPERATING_STANDARD.md`; point the
    setup-doc bullets at the real `docs/*` guides; drop the `BUILD_LOG.md` link.
  - `QUICKSTART.md`: remove the unrunnable `./scripts/init_mesh.sh` snippet.
  - `docs/OPERATING_STANDARD.md`: replace legacy filenames with real `docs/*`.
- Add `scripts/check_links.py` — a stdlib-only checker that validates markdown
  `[text](relative-path)` links and explicit `./script` references resolve to
  existing files. It skips `http(s)` URLs and bare `file:line` evidence prose,
  and skips the two MASTER_PLAN files (which cite `file:line` in prose).

**Why first:** the repo is documentation-only, so public-boundary and
reference trust are the primary risks; broken references erode reviewer trust;
identifier safety must precede any expansion.

**What it does NOT change:** no real infrastructure operation; no cloud / Jetson
/ workstation / network access; no private topology import; no publication.

**Acceptance criteria**
- All in-repo local links/references resolve.
- `python3 scripts/check_links.py` exits 0 on the repo.
- No real identifiers or credentials introduced; examples stay generic.

**Verification path**
1. `python3 scripts/check_links.py`
2. `git diff --check`
3. Manual scan of the diff for real identifiers.
