# Master Plan: Distributed Robotics Infrastructure Public

## 1. Executive Summary

### Facts

- This repository documents a public-safe distributed robotics infrastructure pattern across workstation, GPU simulation node, edge node, and ROS 2 networking layers. Evidence: `SPEC.md:5`.
- The public boundary excludes real hostnames, LAN IPs, VPN identifiers, usernames, credentials, cloud project IDs, private topology notes, build logs, and private machine-specific operating procedures. Evidence: `SPEC.md:9`, `VERIFICATION_PLAN.md:14`.
- The repo contains architecture docs for host workstation, Jetson edge node, cloud simulation node, ROS 2 networking, and an operating standard. Evidence: `docs/HOST_WORKSTATION.md`, `docs/JETSON_EDGE_NODE.md`, `docs/CLOUD_SIMULATION_NODE.md`, `docs/ROS2_NETWORKING.md`, `docs/OPERATING_STANDARD.md`.
- Recent git history includes sanitization and public mirror sync commits, including `chore: sanitize distributed robotics public mirror` and `Harden public repository surface`.

### Assumptions

- This public candidate should explain reusable infrastructure patterns without exposing live lab topology.
- The repo is documentation-only for public use, not an executable infrastructure-as-code deployment.
- Hardware and cloud nodes should be treated as documented patterns, not operated by agents through this repo.

### Recommendations

- Productize the repo as a public architecture handbook with strict placeholder discipline and release-boundary gates.
- Correct stale README references to missing files before release.
- Add self-contained static verification for public-surface safety, generic identifier use, link integrity, and artifact-boundary checks.

## 2. Current-State Findings, With File/Path Evidence

### Facts

- `README.md` says to read `AGENTS.md`, but no repo-local `AGENTS.md` is present in this public candidate. Evidence: `README.md:8`; file inventory.
- `README.md` references `BUILD_LOG.md`, `host-pc-setup.md`, `gcp-cloud-node.md`, and `jetson-setup.md`, but the visible docs use `docs/HOST_WORKSTATION.md`, `docs/CLOUD_SIMULATION_NODE.md`, and `docs/JETSON_EDGE_NODE.md`. Evidence: `README.md:14`, `README.md:52`.
- `SPEC.md` defines non-goals around real hostnames, LAN IP addresses, VPN identifiers, usernames, credentials, cloud project IDs, private topology notes, build logs, production security baseline claims, certification claims, and private machine-specific procedures. Evidence: `SPEC.md:9`.
- `VERIFICATION_PLAN.md` requires `python3 repo_preflight.py --repo . --profile public-export --paranoid` and manual boundary review. Evidence: `VERIFICATION_PLAN.md:5`, `VERIFICATION_PLAN.md:11`.
- `docs/ROS2_NETWORKING.md` warns to avoid exposing ROS 2 traffic directly to the public internet and to keep public docs free of real addresses and node identities. Evidence: `docs/ROS2_NETWORKING.md:27`, `docs/ROS2_NETWORKING.md:29`.
- `docs/JETSON_EDGE_NODE.md` uses generic SSH placeholders. Evidence: `docs/JETSON_EDGE_NODE.md:33`.
- `QUICKSTART.md` references `./scripts/init_mesh.sh`, but no `scripts/` directory is visible in the current file inventory. Evidence: `QUICKSTART.md:25`.
- `README.md` documents private/public mirror provenance and `public-sync-manifest.json`. Evidence: `README.md:58`, `README.md:83`.

### Assumptions

- Stale filenames are a public mirror drift issue rather than intentional broken references.
- `repo_preflight.py` may be an external workspace-level tool.

### Recommendations

- Reconcile naming:
  - Either update README to point at `docs/HOST_WORKSTATION.md`, `docs/CLOUD_SIMULATION_NODE.md`, and `docs/JETSON_EDGE_NODE.md`, or add the missing legacy file aliases.
- Remove or replace `./scripts/init_mesh.sh` from quickstart until a public-safe script exists.
- Treat all node identities, cloud project values, tailnet details, and network addresses as prohibited in this public repo.

## 3. Product Requirements

### Facts

- The repo is a public-safe pattern for multi-node robotics infrastructure across local edge nodes and cloud-hosted compute. Evidence: `QUICKSTART.md:4`.
- Setup examples must use generic values only. Evidence: `SPEC.md:20`.

### Assumptions

- The target reader needs a reusable mental model, not copy-paste access to a live deployment.
- The public repo can reference classes of hardware and software, but not actual user-specific topology.

### Recommendations

- Target users:
  - Robotics infrastructure reviewer.
  - Engineer adapting a generic lab topology.
  - Public mirror maintainer.
- Primary workflows:
  - Read architecture overview.
  - Select host, edge, cloud, or networking guide.
  - Adapt generic setup steps to a private environment outside this repo.
  - Run public-surface checks before publication.
- Non-goals:
  - Production security baseline.
  - Certified deployment architecture.
  - Live infrastructure automation.
  - Real topology disclosure.
- Required features:
  - Generic topology overview.
  - Workstation, edge node, cloud node, and ROS 2 networking patterns.
  - Placeholder-only examples.
  - Public/private sync provenance.
  - Release-boundary verification.
- Supporting capabilities:
  - Identifier scanner for IPs, hostnames, usernames, tailnet names, cloud IDs, and credentials.
  - File-reference/link checker.
  - Artifact-boundary checker for generated diagrams, logs, and exported archives.
- Admin/operator workflows:
  - Private repo sync review.
  - Manual public-boundary review.
  - Release checklist update.
- Error and recovery states:
  - Real identifier found: block release and audit history if public.
  - Missing doc reference: block release until fixed or marked external.
  - Security-hardening claim without evidence: downgrade wording.
- Data handling and retention:
  - Public docs contain generic patterns only.
  - Private topology, local verification logs, cloud costs, node names, and credentials stay out of this repo.

## 4. DORA AI Capability Alignment

### Facts

- This repo is documentation-only infrastructure guidance, not an AI runtime. Evidence: `CONTRIBUTING.md:3`.

### Assumptions

- AI agents may be used to maintain public docs and run static audits, but not to operate hardware or cloud nodes from this repo.

### Recommendations

- AI stance:
  - Allowed: doc maintenance, placeholder scanning, public-surface auditing, claim checking.
  - Restricted: generated scripts for networking/cloud setup until reviewed for security and public-safety.
  - Prohibited: reading or publishing private topology, credentials, service accounts, tailnet identifiers, real hostnames, real IPs, and hardware access paths.
- Data ecosystem:
  - Source register should track public docs, generic examples, and sync provenance.
  - Freshness checks should record ROS 2 distribution, OS, JetPack, driver, and cloud assumptions without exposing real nodes.
- AI-accessible internal data:
  - Public docs in this repo and public vendor docs.
  - No private deployment notes.
- Version control:
  - Small doc changes.
  - Public-surface scan on every sync.
  - Generated diagrams and reports labeled and excluded unless approved.
- Small batches:
  - First slice: fix broken references and add static public audit.
- User-centricity:
  - Named user: robotics infrastructure reviewer.
  - Job-to-be-done: understand the topology pattern safely.
  - Success signal: reader can adapt the pattern without seeing private values.
- Internal platform:
  - One-command static verification for links, placeholders, and prohibited identifiers.
- Missing DORA evidence:
  - No self-contained public audit script is visible.
  - First action: document or add a static check command once write scope expands.

## 5. Architecture Plan

### Facts

- Existing architecture is documentation organized by node role:
  - Host workstation: `docs/HOST_WORKSTATION.md`.
  - Jetson edge node: `docs/JETSON_EDGE_NODE.md`.
  - Cloud simulation node: `docs/CLOUD_SIMULATION_NODE.md`.
  - ROS 2 networking: `docs/ROS2_NETWORKING.md`.
  - Operating standard: `docs/OPERATING_STANDARD.md`.

### Assumptions

- The public architecture should not provide live deployment scripts unless they are generic, reviewed, and safe.

### Recommendations

- Existing architecture:
  - Root overview and spec.
  - Per-node docs.
  - Verification and release checklist.
- Proposed architecture:
  - `docs/TOPOLOGY.md`: public generic topology diagram and data flow.
  - `docs/IDENTIFIER_POLICY.md`: allowed placeholder formats and prohibited real values.
  - `scripts/verify_public_surface.sh`: future static checker.
  - `release/`: generated local reports ignored by default.
- Data flow:
  - Developer workstation builds/tests ROS 2 packages.
  - Cloud simulation node provides GPU simulation capacity.
  - Edge node runs near sensors/actuators.
  - ROS 2 networking connects nodes over private network or discovery server.
- External integrations:
  - Ubuntu, ROS 2, NVIDIA drivers, Isaac Sim, JetPack, Docker, private network/VPN overlay.
  - All provider-specific IDs and credentials remain private.
- Configuration/secrets:
  - Use placeholders only.
  - Never commit service account material, Terraform state, tailnet details, real allowed ports, real addresses, or private node names.
- ADR needs:
  - ADR: documentation-only public architecture vs public IaC.
  - ADR: placeholder convention and prohibited identifier policy.
  - ADR: sync manifest retention in public exports.

## 6. Feature Roadmap

### Recommendations

- Milestone 1: Reference and boundary repair.
  - Acceptance: README and quickstart point only to present files or approved external resources.
- Milestone 2: Public identifier policy.
  - Acceptance: docs define placeholder format and prohibited real identifiers.
- Milestone 3: Static public-surface audit.
  - Acceptance: one command checks links, missing files, private identifiers, and generated artifacts.
- Milestone 4: Generic topology diagram.
  - Acceptance: diagram contains no real hostnames, IPs, usernames, cloud IDs, or tailnet names.
- Milestone 5: Release artifact audit.
  - Acceptance: generated archive is extracted and scanned before public use.

## 7. Parallelization Plan

### Recommendations

- Workstream A: Documentation reference repair.
  - Owns: `README.md`, `QUICKSTART.md`.
  - Verification: file-reference check.
- Workstream B: Node guide hardening.
  - Owns: `docs/HOST_WORKSTATION.md`, `docs/JETSON_EDGE_NODE.md`, `docs/CLOUD_SIMULATION_NODE.md`.
  - Verification: placeholder scan.
- Workstream C: Networking and security boundary.
  - Owns: `docs/ROS2_NETWORKING.md`, `SPEC.md`, `VERIFICATION_PLAN.md`.
  - Verification: prohibited identifier and claim scan.
- Workstream D: Release tooling.
  - Owns: future `scripts/`, `PRE_RELEASE_CHECKLIST.md`.
  - Verification: static audit command and artifact extraction.
- Sequential gates:
  - Any cloud/networking automation must wait for security review and explicit approval.
- Merge strategy:
  - Merge docs first, verification tooling second, diagrams third.

## 8. Task Backlog

| Priority | Task | Likely files | Tests/docs | Verification | Done condition |
| --- | --- | --- | --- | --- | --- |
| P0 | Fix stale README file references | `README.md` | Docs | File existence check | No references to absent local docs |
| P0 | Fix or remove missing `./scripts/init_mesh.sh` quickstart command | `QUICKSTART.md` | Docs | File existence check | Quickstart contains no absent local command |
| P0 | Add placeholder/identifier policy | future docs | Policy docs | `rg` scan for address/user/cloud patterns | Real identifiers remain prohibited |
| P0 | Add static public-surface check | future `scripts/` | Verification docs | Run script | Links, identifiers, generated artifacts checked |
| P1 | Add generic topology diagram | `docs/` | Diagram docs | Manual public audit | Diagram is generic and useful |
| P1 | Add release evidence template | `PRE_RELEASE_CHECKLIST.md` | Checklist | Manual release review | Release readiness is replayable |
| P2 | Add optional sample DDS discovery config with placeholders | `docs/ROS2_NETWORKING.md` | Docs | Security review | Config is generic and non-deployable without private values |

## 9. Testing And Verification Plan

### Facts

- Current documented verification depends on `repo_preflight.py`, which is not visible in the current file inventory. Evidence: `VERIFICATION_PLAN.md:8`.

### Recommendations

- Unit tests:
  - Not applicable until scripts are added.
- Integration tests:
  - Not applicable for documentation-only release.
- Static checks:
  - Internal file-reference check.
  - Markdown link check.
  - Prohibited identifier scan.
  - Claim scan for production/certification/security-baseline overreach.
- Security/privacy checks:
  - Scan for IP addresses, hostnames, usernames, tailnet names, auth keys, cloud project IDs, service accounts, Terraform state, local paths, and credentials.
- Artifact-boundary checks:
  - Build release archive, list manifest, extract to temp directory, scan extracted contents, and confirm only public docs/assets are present.
- Generated-vs-source separation:
  - Source: Markdown docs and approved static diagrams.
  - Generated: release reports, audit logs, sync manifests unless intentionally tracked.
- Regression loop:
  - Any doc edit -> link/reference check -> prohibited identifier scan -> claim review -> release checklist.

## 10. Release Criteria

### Recommendations

- Definition of done:
  - Docs reference present files.
  - All examples use placeholders.
  - Public boundary is explicit.
  - Verification command is runnable or documented as external.
- Public readiness:
  - No real hostnames, IP addresses, usernames, tailnet identifiers, cloud project IDs, credentials, private topology notes, build logs, or private machine-specific procedures.
  - No production security baseline, certification, or hardening guarantee claims.
- Artifact boundary:
  - Release artifact inspected, extracted, and scanned.
  - Generated logs and local reports excluded.
- Operational handoff:
  - Maintainer can safely update public docs without private context.
- Remote preservation:
  - No push, PR, release, or publication without explicit user approval.

## 11. Risks And Open Questions

### Risks

- Stale docs could mislead users into expecting missing setup files or scripts.
- Public topology language could accidentally reveal real machine roles or identifiers.
- ROS 2 networking guidance could be mistaken for a hardened production baseline.
- Sync-from-private may leak internal operational details.
- Artifact packages may include generated logs or local reports if not inspected.

### Open Questions

- Should this public repo ever include runnable infrastructure scripts, or remain documentation-only?
- Should sync manifests be committed publicly or retained only as release evidence?
- What placeholder convention should be enforced for host, user, IP, VPN, and cloud values?
- Should the public docs mention concrete hardware classes only, or also generic bill-of-material patterns?

## 12. Recommended First Implementation Slice

### Recommendation

Create a public documentation consistency and identifier-safety slice.

### Why It Is First

- The repo is documentation-only and public-boundary risk is the primary risk.
- Broken references and missing commands reduce reviewer trust.
- Identifier safety must precede any infrastructure expansion.

### What It Changes

- Fix or remove stale file references.
- Add placeholder policy.
- Add static public-surface verification.
- Add release artifact audit checklist.

### What It Does Not Change

- No real infrastructure operation.
- No cloud, Jetson, workstation, or network access.
- No private topology import.
- No public publication.

### Acceptance Criteria

- All local links and file references resolve.
- No real identifiers or credentials are present.
- All examples use generic placeholders.
- Release criteria include public-surface audit, sanitized source boundary, artifact-boundary checks, claim accuracy, generated-vs-source separation, and sync-from-private provenance.

### Verification Path

1. Run file-reference and link checks.
2. Run prohibited identifier scan.
3. Run `git diff --check`.
4. If packaging, inspect and extract the artifact, then scan extracted contents.
