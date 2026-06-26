# Verification Plan

## Checks

The author runs an external, personal public-export gate (a secret/PII scanner that
is not shipped in this repository) before publishing changes. For a stranger reading
this repo, the manual boundary review below is the authoritative check.

Manual review:

- Confirm examples use generic host, user, address, and cloud identifiers.
- Confirm no credentials, network secrets, real IP addresses, or private topology details are present.
- Confirm networking guidance is framed as architecture documentation, not a production security baseline.

## Release Decision

Release only when the export gate (run by the author) and the manual boundary review pass.

