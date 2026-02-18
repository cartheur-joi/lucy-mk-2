# Mechanical Design Plan

## Design Intent from Concept

- Slim torso silhouette with layered panel geometry
- High shoulder articulation emphasis
- Compact head unit with forward sensor cluster
- Exposed-mechanical aesthetic permitted in v0.1 where useful

## Geometry and Coordinate Conventions

- Global origin: torso center plane, shoulder axis intersection level
- +X forward, +Y left, +Z up
- All joint CAD references use this global frame plus local joint frames

## Joint Targets (v0.1)

- Neck yaw: +/- 60 deg
- Neck pitch: +35 / -25 deg
- Shoulder pitch: +90 / -40 deg
- Shoulder roll: +/- 45 deg
- Elbow flex: 0 to 120 deg
- Wrist-lite: +/- 45 deg or 180 deg rotate (choose one based on actuator)

## Torque and Load Envelope (Preliminary)

- Assumed arm segment mass:
- upper arm 0.6-0.9 kg
- forearm 0.5-0.8 kg
- hand shell 0.2-0.4 kg
- Shoulder continuous torque target: >= 8-12 N*m with margin
- Elbow continuous torque target: >= 4-6 N*m with margin

## Material Strategy

- Printed structural plastics:
- PETG for general structural brackets
- Nylon/CF-Nylon for high-stress adapters (if printer supports)
- Printed cosmetic shells:
- PLA/PETG acceptable
- Metal:
- 6061 aluminum plates, tubes, and standoffs for primary load paths
- steel shafts/pins for pivots

## Mechanical Architecture by Zone

### Torso

- Metal spine + shoulder bridge as core skeleton
- Printed panel mounts attached to threaded inserts in metal members
- Electronics shelf with slide-out tray for serviceability

### Shoulder Modules

- Cartridge-style shoulder units for independent bench testing
- Shared mounting pattern left/right for part reuse
- Mechanical hard-stops to protect against overtravel

### Elbow/Wrist

- Coaxial shaft + bearing pair at each revolute joint
- Printed covers isolated from bearing preload paths
- Cable loops sized for full range + 20 percent slack margin

### Head/Neck

- Neck gimbal or stacked-axis module
- Camera bracket isolated from motor vibration where possible
- Microphone mount with vibration damping inserts

## Fasteners and Inserts

- Standard fastener family: M3/M4/M5
- Heat-set inserts in printed parts for repeated service
- Captive nut channels where inserts are not practical

## Tolerances and Fits

- Printed hole nominal oversize:
- M3 clearance +0.2 to +0.3 mm
- shaft fits based on post-processing allowance
- Metal-to-metal critical interfaces dimensioned from machined parts, not printed references

## CAD Deliverables

- Assembly top-level model
- Sub-assemblies: torso, neck, left arm, right arm
- Manufacturing drawings for all fabricated metal parts
- Print-ready STL/3MF package with per-part material tags
