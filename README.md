# Distributed Robotics Infrastructure


> **Part of the Onyx Citadel Cyber-Physical AI Ecosystem**
> *This repository documents the secure, multi-node hardware topology (Tailscale mesh, control-plane, inference, and physical edge nodes) required to run the Citadel's autonomous pipelines.*
Complete architecture, setup, and configuration for an enterprise-grade distributed sim-to-real pipeline: Ubuntu/ROS 2 host PC, GPU-accelerated cloud simulation (GCP), and NVIDIA Jetson Orin edge device.

For repo-specific working rules, read [docs/OPERATING_STANDARD.md](docs/OPERATING_STANDARD.md).

This architecture serves as the foundational infrastructure for all advanced perception and manipulation projects. For definitions of key terms, please see my central **[AI & Robotics Glossary](https://github.com/camirian/robotics-ontology/blob/main/GLOSSARY.md)**.


> ## 📖 The Architecture Archive
> This README provides the high-level overview. Per-node deep dives live in the
> [`docs/`](./docs) directory (host workstation, cloud simulation node, Jetson
> edge node, and ROS 2 networking).

---

## ✅ Skills Demonstrated

Successfully completing this foundational setup demonstrates core competencies in:

-   **Systems Administration:** Proficiently installing and configuring a Linux (Ubuntu 22.04) environment from scratch, including disk partitioning for dual-boot systems.
-   **Hardware & Driver Management:** Correctly installing and verifying proprietary NVIDIA drivers on Linux, including handling dependencies and Secure Boot (MOK) enrollment.
-   **Distributed Systems & Networking:** Establishing and verifying a multi-machine ROS 2 network, proving an understanding of the DDS discovery mechanism.
-   **Embedded & Edge AI Systems:** Flashing and configuring an embedded device (NVIDIA Jetson) with the JetPack SDK, preparing it for sim-to-real deployment.
-   **Version Control & Professional Documentation:** Utilizing Git and GitHub for version control and maintaining high-quality, structured documentation for a technical project.

---

## 🛠️ Software Stack & Key Tools

| Component           | Version / Type                                                                                  | Purpose                                        |
| ------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Operating System    | Ubuntu 22.04 LTS                                                                                | Standard for robotics development              |
| Robotics Middleware | [ROS 2 Humble](https://github.com/camirian/robotics-ontology/blob/main/GLOSSARY.md#ros-ros-2)   | Core communication and tooling framework       |
| GPU Driver          | NVIDIA Proprietary Driver 5xx.xx                                                                | Enables GPU acceleration for AI/Sim            |
| Simulation Platform | [Isaac Sim](https://github.com/camirian/robotics-ontology/blob/main/GLOSSARY.md#isaac-sim)      | High-fidelity physics simulation & sensor data |
| Edge AI SDK         | [JetPack SDK](https://github.com/camirian/robotics-ontology/blob/main/GLOSSARY.md#jetpack-sdk)  | OS & libraries for the Jetson platform         |
| Version Control     | [Git](https://github.com/camirian/robotics-ontology/blob/main/GLOSSARY.md#git)                  | Tracking changes and managing project history  |
| Code Hosting        | [GitHub](https://github.com/camirian/robotics-ontology/blob/main/GLOSSARY.md#github) / `gh` CLI | Publicly showcasing and managing repositories  |
| Build Tool          | [Colcon](https://github.com/camirian/robotics-ontology/blob/main/GLOSSARY.md#colcon)            | Building ROS 2 packages and workspaces         |

---

## 📝 Setup & Verification Details

Detailed, step-by-step setup patterns and verification checklists for each component are located in the following documents:

-   [`docs/HOST_WORKSTATION.md`](./docs/HOST_WORKSTATION.md): Host workstation / development node setup pattern.
-   [`docs/CLOUD_SIMULATION_NODE.md`](./docs/CLOUD_SIMULATION_NODE.md): Cloud GPU simulation node configuration.
-   [`docs/JETSON_EDGE_NODE.md`](./docs/JETSON_EDGE_NODE.md): Jetson Orin edge node setup pattern.
-   [`docs/ROS2_NETWORKING.md`](./docs/ROS2_NETWORKING.md): ROS 2 discovery, networking, and security boundary.

---

## Private vs public variant strategy

This repo has two coordinated copies:

- `distributed-robotics-infrastructure` (private): working repo with internal setup notes and implementation context.
- `distributed-robotics-infrastructure-public` (public): sanitized, portfolio-safe publication surface.

The split exists so we keep private hardware-specific operational detail, private planning, and internal verification artifacts out of public history while keeping a clean export for external sharing.

### How to keep them aligned

From the **private** repo root (this script lives in the private repo, not in
this public mirror):

1. `scripts/sync-public.sh`
2. Review the printed status diff.
3. `scripts/sync-public.sh --push`

Preferred shorthand:

1. `make sync-check`
2. `make sync-push`

`--dry-run` is supported for preview-only operation.
`--no-manifest` skips writing `public-sync-manifest.json`.

Each successful non-dry-run sync writes an auditable `public-sync-manifest.json` into
the public repo summarizing:

- source private commit and branch
- public remote/branch
- sync mode flags
- changed paths in that sync

For deterministic full-prune exports, use:

1. `scripts/sync-public.sh --strict --dry-run` (or `make sync-dry-run`)
2. `scripts/sync-public.sh --strict --push` (or `make sync-push`)
## 📜 License

This project is licensed under the Apache 2.0 License. See the [`LICENSE`](./LICENSE) file for details.
