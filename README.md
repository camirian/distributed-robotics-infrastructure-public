# Distributed Robotics Infrastructure


> *This repository documents the secure, multi-node hardware topology (Tailscale mesh networking, control-plane workstation, edge inference, and Jetson physical nodes) required to run autonomous sim-to-real pipelines.*

Complete architecture, setup, and configuration for an enterprise-grade distributed sim-to-real pipeline: Ubuntu/ROS 2 host PC, GPU-accelerated cloud simulation (GCP), and NVIDIA Jetson Orin edge device.

For repo-specific working rules, read [docs/OPERATING_STANDARD.md](docs/OPERATING_STANDARD.md).

This architecture serves as the foundational infrastructure for all advanced perception and manipulation projects. For definitions of key terms, please see my central **[AI & Robotics Glossary](https://github.com/camirian/robotics-ontology/blob/main/GLOSSARY.md)**.


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

## 📝 Setup & Verification Details (DevContainer Mandatory)

> [!WARNING]
> DO NOT edit these structural architectures natively on a host text editor. Launch via **"Dev Containers: Reopen in Container"** in Visual Studio Code to enforce strict Markdown linting matrices globally.

Detailed, step-by-step instructions and verification checklists for each component are located in the following documents:

-   [`docs/HOST_WORKSTATION.md`](docs/HOST_WORKSTATION.md): Complete guide for the host workstation setup.
-   [`docs/CLOUD_SIMULATION_NODE.md`](docs/CLOUD_SIMULATION_NODE.md): Cloud-based simulation node configuration acting as the critical link.
-   [`docs/JETSON_EDGE_NODE.md`](docs/JETSON_EDGE_NODE.md): Complete guide for the Jetson Orin Nano setup.

---

## 📜 License

This project is licensed under the Apache 2.0 License. See the [`LICENSE`](./LICENSE) file for details.
