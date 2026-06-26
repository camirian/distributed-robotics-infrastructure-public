# Distributed Robotics Infrastructure: Quickstart Guide

## 1. Overview
This project provides the configuration and automation for deploying a multi-node robotics infrastructure across Local (Jetson/PC) and Cloud (GCP) environments.

## 2. Setting Up the Local Apex Node
Follow the [Host Workstation Setup](docs/HOST_WORKSTATION.md) guide to prepare your primary development machine.

## 3. Preparing a Jetson Edge Node
Use the [Jetson Edge Node Setup](docs/JETSON_EDGE_NODE.md) guide to flash and harden the Orin Nano.

## 4. Deploying the GCP Cloud Node
Execute the Terraform manifests as described in the [Cloud Simulation Node](docs/CLOUD_SIMULATION_NODE.md) documentation.

## 5. Establishing the Mesh
Initialize Tailscale across all nodes to enable seamless ROS 2 communication:
```bash
./scripts/init_mesh.sh
```
