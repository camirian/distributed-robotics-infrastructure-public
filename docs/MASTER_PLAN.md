# Documentation Maintenance Notes

This file records the maintenance boundary for the public reference. The root
[plan](../MASTER_PLAN.md) is the canonical description of repository scope.

## What belongs here

The documentation can explain generic workstation, cloud, edge-node, and ROS 2
networking patterns. It can point readers to public vendor documentation and
describe checks they can adapt to their own environments.

## What does not belong here

Do not publish a live topology, hostnames, IP addresses, usernames, VPN or
cloud identifiers, credentials, private build logs, or copy-paste deployment
automation. This repository does not contain a runnable mesh script, a hidden
local preflight tool, or production infrastructure-as-code.

## Review before sharing

1. Confirm each local Markdown link points to an included file.
2. Confirm examples remain generic and contain no real identifiers or secrets.
3. Confirm claims describe documentation patterns rather than verified runtime
   behavior, production security, or certification.
4. Use [VERIFICATION_PLAN.md](../VERIFICATION_PLAN.md) and
   [PRE_RELEASE_CHECKLIST.md](../PRE_RELEASE_CHECKLIST.md) for the final
   public-boundary review.
