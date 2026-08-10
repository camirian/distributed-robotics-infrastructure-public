# Contributing: Distributed Sim-to-Real Infrastructure

As the foundational infrastructure layer, stability and determinism are paramount.

## 🏗️ Infrastructure-as-Code (IaC) Principles
1.  **Immutable Nodes:** Avoid manual configuration ("click-ops") where possible. When updating the `docs/CLOUD_SIMULATION_NODE.md` or `docs/JETSON_EDGE_NODE.md`, ensure the steps are scriptable and reproducible.
2.  **Network Topologies:** Any changes to the Tailscale mesh or DDS routing paradigms must be thoroughly verified against multicast/unicast constraints common in cloud VPCs (Google Cloud Platform).

## 📝 Proposing Changes
1.  If proposing a significant architectural shift (e.g., migrating from VPN-based DDS bridging to Zenoh), open an Issue first to discuss the performance implications.
2.  For documentation updates, submit a Pull Request linking to the relevant Issue.
