# Verification Plan

## Checks

Run the public-export gate before publishing changes:

```bash
python3 repo_preflight.py --repo . --profile public-export --paranoid
```

Manual review:

- Confirm examples use generic host, user, address, and cloud identifiers.
- Confirm no credentials, network secrets, real IP addresses, or private topology details are present.
- Confirm networking guidance is framed as architecture documentation, not a production security baseline.

## Release Decision

Release only when automated checks and manual boundary review pass.

