# Distributed Robotics Infrastructure

> *This repository documents the multi-node hardware topology — mesh VPN networking
> (e.g. Tailscale), a host control-plane workstation, a cloud GPU simulation node, and
> a Jetson physical edge node — used to run autonomous sim-to-real robotics pipelines.*

This is an **architecture and reference writeup**, not a runnable system. It captures
reusable, public-safe setup patterns for a distributed sim-to-real pipeline: an
Ubuntu / ROS 2 host workstation, a GPU-accelerated cloud simulation node (GCP), and an
NVIDIA Jetson Orin edge device. There is nothing to install or execute from this repo;
each document describes the pattern and the verification steps for one node or layer.

For repo-specific working rules, read [docs/OPERATING_STANDARD.md](docs/OPERATING_STANDARD.md).
For definitions of key terms, see the
[AI & Robotics Glossary](https://github.com/camirian/robotics-ontology-public/blob/main/GLOSSARY.md).

## 🗺️ Topology Overview

| Tier      | Node                          | Role                                                                 |
| --------- | ----------------------------- | ------------------------------------------------------------------- |
| **Host**  | Ubuntu / ROS 2 workstation    | Primary development node: source control, build tooling, local sim. |
| **Cloud** | GPU VM on GCP                 | Burst GPU capacity for physics simulation and synthetic data.       |
| **Edge**  | NVIDIA Jetson Orin            | Runs robotics workloads close to sensors, actuators, and rigs.      |
| **Mesh**  | Private network / VPN overlay | Connects all nodes so ROS 2 discovery and topics work across tiers. |

## 📚 Documentation

Each document is a self-contained setup pattern with a verification section:

-   [`QUICKSTART.md`](QUICKSTART.md): How the pieces fit together and where to start.
-   [`docs/HOST_WORKSTATION.md`](docs/HOST_WORKSTATION.md): Host workstation baseline and setup pattern.
-   [`docs/CLOUD_SIMULATION_NODE.md`](docs/CLOUD_SIMULATION_NODE.md): Cloud GPU simulation node provisioning pattern.
-   [`docs/JETSON_EDGE_NODE.md`](docs/JETSON_EDGE_NODE.md): Jetson Orin edge node setup pattern.
-   [`docs/ROS2_NETWORKING.md`](docs/ROS2_NETWORKING.md): ROS 2 discovery, DDS, and cross-network considerations.
-   [`docs/OPERATING_STANDARD.md`](docs/OPERATING_STANDARD.md): Working rules and quality bar for this repo.

---

## 🛠️ Software Stack & Key Tools

| Component           | Version / Type                   | Purpose                                        |
| ------------------- | -------------------------------- | ---------------------------------------------- |
| Operating System    | Ubuntu 22.04 LTS                 | Standard for robotics development              |
| Robotics Middleware | ROS 2 Humble                     | Core communication and tooling framework       |
| GPU Driver          | NVIDIA Proprietary Driver        | Enables GPU acceleration for AI / simulation   |
| Simulation Platform | Isaac Sim                        | High-fidelity physics simulation & sensor data |
| Edge AI SDK         | JetPack SDK                      | OS & libraries for the Jetson platform         |
| Version Control     | Git                              | Tracking changes and managing project history  |
| Code Hosting        | GitHub / `gh` CLI                | Publicly showcasing and managing repositories  |
| Build Tool          | Colcon                           | Building ROS 2 packages and workspaces         |

---

## 📝 Skills Demonstrated

The documented setup workflow reflects core competencies in:

-   **Systems Administration:** Installing and configuring a Linux (Ubuntu 22.04)
    environment from scratch, including disk partitioning for dual-boot systems.
-   **Hardware & Driver Management:** Installing and verifying proprietary NVIDIA
    drivers on Linux, including dependency handling and Secure Boot (MOK) enrollment.
-   **Distributed Systems & Networking:** Establishing and verifying a multi-machine
    ROS 2 network, demonstrating an understanding of the DDS discovery mechanism.
-   **Embedded & Edge AI Systems:** Flashing and configuring an embedded device
    (NVIDIA Jetson) with the JetPack SDK for sim-to-real deployment.
-   **Version Control & Technical Documentation:** Using Git and GitHub to maintain
    structured documentation for a technical project.

---

## 📜 License

This project is licensed under the Apache 2.0 License. See the [`LICENSE`](./LICENSE) file for details.
