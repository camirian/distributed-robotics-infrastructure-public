# Distributed Robotics Infrastructure Operating Standard

## 1. Role of This Repo
This repo documents the robotics hardware topology and the setup workflow.

## 2. Standards
- Keep the setup sequence explicit.
- Keep hardware, networking, and verification notes separate but linked.
- Keep the repo centered on reproducible robotics infrastructure.
- Keep the terminal baseline simple.

## 3. Documentation Rules
- `README.md`: high-level overview and launch context.
- `SPEC.md`, `VERIFICATION_PLAN.md`: scope, public boundary, and verification.
- `HOST_WORKSTATION.md`, `CLOUD_SIMULATION_NODE.md`, `JETSON_EDGE_NODE.md`,
  `ROS2_NETWORKING.md` (in this `docs/` directory): per-node setup patterns.

## 4. Quality Bar
- No hardware claim without a setup path.
- No verification claim without a documented step.
- No hidden assumptions about platform or driver state.
