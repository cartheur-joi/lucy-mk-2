# Work Breakdown and Milestones

## Phase 0: Definition Freeze (Week 1)

- Confirm v0.1 scope (torso + head + arms).
- Freeze joint count for first hardware pass.
- Freeze interface standards (mechanical holes, electrical connectors, protocol baseline).

Deliverables:

- signed-off architecture package
- initial BOM freeze candidate

## Phase 1: CAD and DFM (Weeks 2-4)

- Build top-level CAD skeleton and key datums.
- Complete shoulder/elbow joint module CAD first.
- Produce fabrication drawings for metal parts.
- Prepare print files and printability checks.

Gate:

- DFM review pass
- tolerance stack review pass

## Phase 2: Fabrication and Subsystem Bench Bring-up (Weeks 5-7)

- Submit metal parts to vendor.
- Print all v0.1 polymer components.
- Assemble and test one shoulder module on bench.
- Validate actuator torque and thermal envelope.

Gate:

- shoulder module benchmark pass
- no critical mechanical redesign required

## Phase 3: Full Mechanical and Electrical Integration (Weeks 8-10)

- Assemble torso, both arms, and neck/head.
- Install electronics and harnesses.
- Run staged power-up and communication checks.

Gate:

- mechanical free-run pass
- electrical smoke-test pass

## Phase 4: Calibration and Motion Validation (Weeks 11-12)

- Implement homing and limit logic.
- Validate baseline trajectories and repeatability.
- Execute safety and fault-injection tests.

Gate:

- acceptance criteria from `docs/planning/07-test-validation.md` met for v0.1

## Phase 5: Demo Package and v0.2 Backlog (Week 13)

- Build demo script with controlled motions.
- Document lessons learned and redesign priorities.
- Publish v0.2 backlog and revised BOM.

Deliverables:

- demo-ready Mk-II v0.1 platform
- engineering report with risk updates

[Back to README](../../README.md)
