# Distributed Robotics Infrastructure

> *This repository describes a proposed multi-node robotics topology: a host
> workstation, a cloud GPU simulation node, a Jetson edge node, and a private
> network overlay. It does not establish that these nodes are provisioned,
> connected, or running an autonomous sim-to-real pipeline.*

This is an **architecture and setup reference**, not a runnable system or a
verified end-to-end deployment. It describes example patterns for an Ubuntu /
ROS 2 host workstation, a GPU-accelerated cloud simulation node (GCP), and an
NVIDIA Jetson Orin edge device. There is nothing to install or execute from
this repo. The documents include suggested setup and verification steps; they
do not report that those steps were run or that the nodes communicate.

For repo-specific working rules, read [docs/OPERATING_STANDARD.md](docs/OPERATING_STANDARD.md).
For definitions of key terms, see the
[AI & Robotics Glossary](https://github.com/camirian/robotics-ontology-public/blob/main/GLOSSARY.md).

## 🗺️ Topology Overview

| Tier      | Node                          | Role                                                                 |
| --------- | ----------------------------- | ------------------------------------------------------------------- |
| **Host**  | Ubuntu / ROS 2 workstation    | Intended role: source control, build tooling, and local simulation. |
| **Cloud** | GPU VM on GCP                 | Proposed burst capacity for physics simulation and synthetic data. |
| **Edge**  | NVIDIA Jetson Orin            | Intended for workloads close to sensors, actuators, and rigs.      |
| **Mesh**  | Private network / VPN overlay | Proposed path for cross-tier ROS 2 discovery; connectivity is not verified here. |

## 📚 Documentation

Each document describes a setup pattern and includes suggested checks:

-   [`QUICKSTART.md`](QUICKSTART.md): How the pieces fit together and where to start.
-   [`docs/HOST_WORKSTATION.md`](docs/HOST_WORKSTATION.md): Host workstation baseline and setup pattern.
-   [`docs/CLOUD_SIMULATION_NODE.md`](docs/CLOUD_SIMULATION_NODE.md): Cloud GPU simulation node provisioning pattern.
-   [`docs/JETSON_EDGE_NODE.md`](docs/JETSON_EDGE_NODE.md): Jetson Orin edge node setup pattern.
-   [`docs/ROS2_NETWORKING.md`](docs/ROS2_NETWORKING.md): ROS 2 discovery, DDS, and cross-network considerations.
-   [`docs/OPERATING_STANDARD.md`](docs/OPERATING_STANDARD.md): Working rules and quality bar for this repo.

---

## 🛠️ Illustrative Software Stack & Key Tools

These versions and roles are examples from the reference material, not a
verified inventory of a provisioned environment.

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

## 📝 Topics Covered by the Documentation

The reference material discusses these areas. The list describes document
topics; it does not claim that the listed installations or deployments were
performed or independently verified:

-   **Systems administration:** Ubuntu workstation setup patterns, including
    dual-boot considerations.
-   **Hardware and drivers:** NVIDIA driver installation and Secure Boot
    enrollment notes.
-   **Distributed systems and networking:** Multi-machine ROS 2 and DDS
    discovery patterns.
-   **Embedded and edge AI:** Jetson Orin and JetPack setup notes.
-   **Version control and documentation:** GitHub-hosted reference material.

---

## 📜 License

This project is licensed under the Apache 2.0 License. See the [`LICENSE`](./LICENSE) file for details.
