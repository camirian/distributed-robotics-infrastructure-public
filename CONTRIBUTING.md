# Contributing: Distributed Robotics Infrastructure

This public repository contains a documentation-only infrastructure pattern. Keep
changes reproducible, simulation-safe, and free of private topology details.

## Infrastructure-as-Code Principles
1. Prefer scriptable and reproducible setup steps over manual configuration.
2. Keep network examples generic. Do not publish real hostnames, IP ranges,
   tailnet details, cloud project identifiers, credentials, or access paths.
3. Document verification assumptions when changing cloud, edge-node, or DDS
   routing examples.

## Proposing Changes
1. For significant architectural changes, open an issue first and describe the
   tradeoff being evaluated.
2. For documentation updates, submit a pull request linking to the relevant
   issue when one exists.
