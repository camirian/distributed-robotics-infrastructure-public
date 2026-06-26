# Distributed Robotics Infrastructure: Quickstart Guide

## 1. Overview

This repository is an **architecture and reference writeup**, not a runnable system.
It documents reusable, public-safe patterns for standing up a multi-node robotics
infrastructure across local nodes (Jetson / host workstation) and a cloud
(GCP) simulation node. There is no install script to run; each section below
points to the document that describes the relevant setup pattern.

## 2. Setting Up the Host Workstation

Follow the [Host Workstation Setup](docs/HOST_WORKSTATION.md) guide to prepare your
primary development machine (Ubuntu LTS, NVIDIA driver, ROS 2, and build tools).

## 3. Preparing a Jetson Edge Node

Use the [Jetson Edge Node Setup](docs/JETSON_EDGE_NODE.md) guide to flash and
configure an Orin-class device for headless edge development.

## 4. Provisioning the Cloud Simulation Node

Follow the provisioning pattern in the
[Cloud Simulation Node](docs/CLOUD_SIMULATION_NODE.md) documentation to bring up a
GPU-enabled VM for burst simulation and synthetic data generation. The repository
does not ship infrastructure-as-code (e.g. Terraform manifests); the document
describes the setup pattern only.

## 5. Establishing the Mesh

To enable ROS 2 communication across nodes, connect every node to the same private
network or mesh VPN overlay (for example, Tailscale), then validate discovery using
the checks in [ROS 2 Networking](docs/ROS2_NETWORKING.md). Cloud networks commonly
block multicast discovery, so prefer a discovery server or explicit peer
configuration over the overlay.
