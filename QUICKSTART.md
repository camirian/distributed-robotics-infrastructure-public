# Distributed Robotics Infrastructure: Quickstart Guide

## 1. Overview

This repository is an **architecture and setup reference**, not a runnable
system or a verified end-to-end deployment. It documents generic patterns for
a host workstation, a Jetson edge node, and a cloud simulation node. There is
no install script to run; the linked pages describe proposed setup patterns,
not results from a provisioned or connected system.

## 2. Setting Up the Host Workstation

See the [Host Workstation Setup](docs/HOST_WORKSTATION.md) reference for a
suggested Ubuntu LTS, NVIDIA driver, ROS 2, and build-tool setup. It is not a
verified checklist for your machine. Keep machine-specific hostnames, paths,
and credentials out of commits.

## 3. Preparing a Jetson Edge Node

See the [Jetson Edge Node Setup](docs/JETSON_EDGE_NODE.md) reference for a
suggested Orin-class device setup. It does not establish that a device was
flashed or validated. Treat it as a template: replace hardware identifiers
and network settings with values appropriate to your own environment.

## 4. Provisioning the Cloud Simulation Node

The [Cloud Simulation Node](docs/CLOUD_SIMULATION_NODE.md) page describes a
proposed provisioning pattern for a GPU-enabled VM. The repository does not
ship infrastructure-as-code (e.g. Terraform manifests), and the page does not
report a completed cloud deployment. Use a dedicated test project for any
independent implementation, and never commit cloud project identifiers,
service-account material, or Terraform state.

## 5. Establishing the Mesh

In an implementation of this topology, ROS 2 communication would require nodes
to share a private network or mesh VPN overlay (for example, Tailscale), followed
by discovery checks such as those in [ROS 2 Networking](docs/ROS2_NETWORKING.md).
This repository does not establish live connectivity. Cloud networks commonly
block multicast discovery, so a discovery server or explicit peer configuration
may be needed over the overlay.

An independent deployment would use its own private configuration and VPN
provider tooling. Do not commit tailnet names, auth keys, device names, or live
IP ranges.
This repository intentionally ships no mesh-initialization script, since any such
script would encode environment-specific values.
