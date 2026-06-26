# Cloud Simulation Node

A cloud simulation node provides burst GPU capacity for physics simulation, synthetic data generation, or remote visualization.

## Reference Shape

- Linux GPU VM.
- NVIDIA driver and container runtime.
- Docker image for the simulation stack.
- Restricted network access.
- Remote visualization through a supported streaming mechanism.

## Setup Pattern

1. Provision a GPU-enabled VM.
2. Attach sufficient SSD storage for simulator caches and container layers.
3. Install NVIDIA drivers and container runtime.
4. Pull the simulator container image.
5. Expose only the ports required for the chosen remote access method.
6. Connect the node to a private network or mesh VPN when ROS 2 discovery is needed.

## ROS 2 Networking

Cloud networks often block multicast discovery. Use explicit peer configuration, a discovery server, or a VPN overlay that supports the required traffic.

## Verification

```bash
nvidia-smi
docker run --rm --gpus all nvidia/cuda:12.0.0-base-ubuntu22.04 nvidia-smi
ros2 topic list
```

Use provider-specific hardening and cost controls before long-running simulation jobs.
