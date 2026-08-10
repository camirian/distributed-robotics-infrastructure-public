# Contributing: Distributed Robotics Infrastructure

This public repository is a documentation-only infrastructure pattern. Keep
changes reproducible, simulation-safe, and free of private topology details.

## 🏗️ Infrastructure-as-Code (IaC) Principles
1.  **Immutable Nodes:** Avoid manual configuration ("click-ops") where possible. When updating the `docs/CLOUD_SIMULATION_NODE.md` or `docs/JETSON_EDGE_NODE.md`, ensure the steps are scriptable and reproducible.
2.  **Keep network examples generic.** Do not publish real hostnames, IP ranges, tailnet names or auth keys, device names, cloud project identifiers, usernames, credentials, or access paths. Use placeholders.
3.  **Network Topologies:** Any changes to the mesh VPN or DDS routing paradigms must be thoroughly verified against multicast/unicast constraints common in cloud VPCs, and the verification assumptions documented alongside the change.

## 📝 Proposing Changes
1.  If proposing a significant architectural shift (e.g., migrating from VPN-based DDS bridging to Zenoh), open an Issue first to discuss the performance implications and the tradeoff being evaluated.
2.  For documentation updates, submit a Pull Request linking to the relevant Issue.
