# Assembly and Integration Plan

[Back to README](../../README.md)


## Build Order (High Level)

1. Build and verify torso frame
2. Build shoulder modules on bench fixtures
3. Build and mount neck/head module
4. Install electronics trays and power distribution
5. Install harnesses and strain reliefs
6. Integrate arm modules
7. Run calibration and safety bring-up
8. Attach shell panels and final routing cleanup

## Bench Fixtures and Jigs

- Shoulder module alignment plate
- Joint preload setup jig
- Harness length and branch fixture board

## Detailed Sequence

### Phase A Mechanical Core

- Assemble spine + shoulder bridge.
- Validate orthogonality and mounting datums.
- Install bearings, shafts, and hard stops.

### Phase B Actuation

- Mount motors and transmissions.
- Check free motion without power.
- Verify manual movement across full safe range.

### Phase C Electrical Integration

- Install power and control boards.
- Route harness branches with service loops.
- Perform continuity and insulation checks before powering.

### Phase D Commissioning

- First power-on with current-limited supply.
- Bring up controllers one module at a time.
- Run homing and set soft limits.

### Phase E System Integration

- Validate synchronized commands across modules.
- Validate stop behavior and recovery paths.
- Install external shells and verify no cable pinch points.

## Integration Checkpoints

- C1: Mechanical free-run pass
- C2: Electrical smoke-test pass
- C3: Motion primitive pass
- C4: Safety fault injection pass
- C5: Cosmetic + serviceability review

## Serviceability Requirements

- Replace any motor module in <= 30 minutes without full teardown.
- Replace any controller board in <= 20 minutes.
- Access E-stop and main fuse without shell removal.

