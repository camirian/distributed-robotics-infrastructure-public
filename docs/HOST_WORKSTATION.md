# Host Workstation

The host workstation is the primary development node for ROS 2, source control, and local simulation tooling.

## Baseline

- Ubuntu LTS release supported by the target ROS 2 distribution.
- NVIDIA GPU and proprietary driver when local simulation or CUDA workloads are required.
- Git, Python, Docker, and ROS 2 build tools.

## Setup Pattern

1. Install the operating system.
2. Apply OS updates.
3. Install NVIDIA drivers if a discrete GPU is present.
4. Install ROS 2 and colcon tooling.
5. Install simulation tooling as needed.
6. Verify GPU, ROS 2, and build-tool availability.

## Verification

```bash
lsb_release -a
nvidia-smi
printenv ROS_DISTRO
colcon --version
git --version
```

## Notes

- Keep host-specific paths out of shared documentation.
- Record exact versions in local notes when reproducing a lab environment.
- Prefer DevContainers or documented shell setup for repeatability.
