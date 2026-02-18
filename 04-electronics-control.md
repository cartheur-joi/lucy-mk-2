# Electronics and Control Plan

## Power Architecture

- Supply modes:
- bench mode for commissioning
- battery mode for untethered demos
- Rails:
- Motor rail: 12-24 V (selected by actuator choice)
- Logic rail: 5 V / 3.3 V regulated
- Protection:
- branch fuses
- reverse polarity guard
- brownout monitor

## Control Hardware (v0.1 Pragmatic Stack)

- Motor control MCUs:
- one per limb cluster (head, left arm, right arm)
- Mid-level supervisor:
- embedded Linux SBC or equivalent for behavior orchestration and telemetry
- Communication:
- deterministic bus (CAN, RS-485, or equivalent robust differential link)

## Sensor Plan

- Joint angle feedback:
- encoder-based where possible
- servo telemetry fallback for early stage
- IMU:
- 6-axis in torso, optional second in head
- Audio:
- matched microphone pair with known baseline distance
- Vision:
- single camera initially, stereo readiness in mounting and cable plan

## Control Software Layers

- Layer A Safety Supervisor:
- limit checks, watchdog, fault states
- Layer B Motion Primitives:
- homing, trajectory interpolation, velocity/acceleration limiting
- Layer C Behavior Hooks:
- orient-to-sound
- fixation primitives

## Calibration and Commissioning

- End-stop based homing where available
- Soft-limit derivation from calibrated endpoints
- Joint offset persistence in versioned config file

## Telemetry and Logging

- Logged channels:
- command setpoints
- measured joint states
- motor current and temperature
- safety events and mode transitions
- Timestamp source must be synchronized across all controllers

## Safety Controls

- Physical E-stop loop cuts motor rail
- Software E-stop command path with heartbeat timeout
- Fault levels:
- warning (continue)
- degraded mode (restricted motion)
- hard stop (motor rail disable)

## Reserved Path to GA144

- Keep low-level actuation and sensing interfaces protocol-stable.
- Define message contracts now so GA144 integration can replace or augment mid-level compute later without rewiring the entire system.
