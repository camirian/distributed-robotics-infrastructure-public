# Distributed Robotics Infrastructure: Quickstart Guide

## 1. Overview
This project documents a public-safe pattern for multi-node robotics
infrastructure across local edge nodes and cloud-hosted compute.

## 2. Setting Up the Local Apex Node
Review the host setup guidance in this repository before adapting it to your own
machine. Keep machine-specific hostnames, paths, and credentials out of commits.

## 3. Preparing a Jetson Edge Node
Use the Jetson setup notes as a template for preparing an edge node. Replace all
hardware identifiers and network settings with values appropriate for your own
environment.

## 4. Deploying the GCP Cloud Node
If adapting the cloud-node pattern, use a dedicated test project and never commit
cloud project identifiers, service-account material, or Terraform state.

## 5. Establishing the Mesh
Initialize your mesh network using your own private configuration and your VPN
provider's own tooling. Do not commit tailnet names, auth keys, device names, or
live IP ranges. This public repo intentionally ships no mesh-initialization
script, since any such script would encode environment-specific values.
