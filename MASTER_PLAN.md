# Public Documentation Plan

## Current role

This repository is a public, documentation-only reference for distributed
robotics infrastructure patterns. It describes generic workstation, cloud
simulation, edge-node, and ROS 2 networking considerations. It is not
infrastructure-as-code, a runnable deployment, or a production security
baseline.

## Source of truth

- [README.md](README.md) provides the topology overview and document map.
- [QUICKSTART.md](QUICKSTART.md) explains how to navigate the setup patterns.
- [docs/](docs/) contains the host, cloud, edge, networking, and operating
  guidance.
- [SPEC.md](SPEC.md), [VERIFICATION_PLAN.md](VERIFICATION_PLAN.md), and
  [PRE_RELEASE_CHECKLIST.md](PRE_RELEASE_CHECKLIST.md) define the public
  boundary and release review.

## Public contract

- Use generic examples only; never include real hostnames, addresses,
  usernames, cloud identifiers, VPN details, credentials, or private topology.
- Describe reusable patterns, not a live environment or deployment recipe.
- Do not claim certification, production security, hardware validation, or
  runtime behavior that the published documents cannot establish.
- Keep public documentation aligned with the files that are actually included.

## Maintenance

Before sharing a change, inspect the exact diff for private context and
unsupported claims, confirm local links resolve, and use the manual review in
[VERIFICATION_PLAN.md](VERIFICATION_PLAN.md). Changes that add executable
automation or a third-party integration need their own documented scope and
public-boundary review.
