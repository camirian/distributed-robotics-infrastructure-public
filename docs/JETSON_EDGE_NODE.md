# Jetson Edge Node

The Jetson edge node runs robotics workloads close to sensors, actuators, and physical test rigs.

## Baseline

- NVIDIA Jetson Orin-class device.
- JetPack SDK.
- ROS 2 version aligned with the workstation and simulation node.
- SSH access for headless development.

## Setup Pattern

1. Flash the JetPack image using NVIDIA-supported tooling.
2. Complete first-boot setup locally.
3. Install ROS 2 and required packages.
4. Enable SSH for headless operation.
5. Join the same private network or VPN overlay as the development nodes.
6. Verify ROS 2 discovery and topic exchange.

## Verification

```bash
cat /etc/nv_tegra_release
printenv ROS_DISTRO
ros2 node list
ros2 topic list
```

Use generic example addresses in shared docs:

```bash
ssh <jetson_user>@<jetson_address>
```

Do not publish real LAN IPs, hostnames, usernames, or VPN node identifiers.
