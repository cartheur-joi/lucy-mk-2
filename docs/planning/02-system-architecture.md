# System Architecture

[Back to README](../../README.md)


## Top-Level Subsystems

- S1 Structural Frame
- S2 Shell and External Panels
- S3 Actuation and Transmission
- S4 Sensing
- S5 Compute and Control
- S6 Power and Safety
- S7 Harnessing and Connectivity

## S1 Structural Frame

Purpose: carry loads, maintain alignment, and provide standardized mount points.

- Primary torso spine: fabricated aluminum box or plate rib structure
- Shoulder bridge: metal crossmember with symmetric motor module mounts
- Head mast: rigid neck tower with cable pass-through
- Internal rails: printed + metal hybrid for electronics trays

Interfaces:

- S3 actuator mounting faces
- S6 power tray mounts
- S7 cable anchor points

## S2 Shell and External Panels

Purpose: visual form, impact shielding, and accessibility.

- Printed shell panels with hidden fasteners
- Service doors for electronics and harness access
- Replaceable cosmetic skins independent of structural frame

## S3 Actuation and Transmission

Purpose: controlled movement for head and arms.

- Neck: yaw + pitch + optional roll
- Shoulder: pitch + roll
- Elbow: flexion
- Wrist-lite: pitch or rotate (single axis initial)

Implementation options:

- Servo-dominant prototype path for v0.1 speed
- Belt/gear reductions where torque margin is insufficient
- Elastic couplers or compliant inserts to reduce shock loading

## S4 Sensing

- Joint position feedback (encoders or servo telemetry)
- Current sensing on motor rails
- Thermal sensing on dense motor/control zones
- IMU in head/torso for frame reference
- Camera(s) in head, microphones in bilateral arrangement

## S5 Compute and Control

- Low-level motor control microcontrollers
- Mid-level coordinator (single board computer or embedded host)
- Future GA144 module interface reserved via clean messaging boundary

Control layers:

- L0 safety and limits
- L1 homing/calibration
- L2 trajectory and reflex behavior

## S6 Power and Safety

- Battery or benchtop DC supply operation mode switch
- Separate logic and motor rails
- Fusing and emergency stop loop
- Inrush control and undervoltage protection

## S7 Harnessing and Connectivity

- Segmented harness branches: head, left arm, right arm, torso
- Locking connectors and strain relief at every moving boundary
- Connector map and pinout ownership document required pre-assembly

