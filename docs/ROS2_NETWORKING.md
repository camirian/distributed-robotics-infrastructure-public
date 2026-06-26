# ROS 2 Networking

Distributed robotics labs depend on predictable ROS 2 discovery and data flow across machines.

## Common Issues

- Multicast discovery blocked across subnets or cloud networks.
- Firewalls blocking DDS traffic.
- Mismatched ROS 2 distributions.
- Incorrect `ROS_DOMAIN_ID`.
- Clock and time-source differences between simulation and physical nodes.

## Checklist

On every node:

```bash
printenv ROS_DISTRO
printenv ROS_DOMAIN_ID
ros2 node list
ros2 topic list
```

For cross-network setups:

- Prefer a private network, VPN overlay, or discovery server.
- Avoid exposing ROS 2 traffic directly to the public internet.
- Document allowed ports in private deployment notes.
- Keep public docs free of real addresses and node identities.

## Security Boundary

ROS 2 development networks are often permissive by default. Treat public exposure as unsafe unless the deployment has been explicitly hardened.
