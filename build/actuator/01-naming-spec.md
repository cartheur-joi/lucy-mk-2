# Actuator Naming Spec

Use consistent names for CAD, STL, printed parts, and assembly references.

## Part IDs

Format:

`ACT-<zone>-<part>-r<rev>`

Examples:

- `ACT-SHOULDER-motor-mount-r01`
- `ACT-SHOULDER-bearing-block-in-r02`
- `ACT-ELBOW-link-arm-r01`

## File Naming

- FreeCAD master assembly:
  `actuator-master-r01.FCStd`
- Individual part CAD exports:
  `ACT-SHOULDER-motor-mount-r01.FCStd`
- STL exports:
  `ACT-SHOULDER-motor-mount-r01.stl`
- Print profile notes:
  `ACT-SHOULDER-motor-mount-r01-print.md`

## Revision Rules

- Increase revision when geometry changes.
- Do not overwrite previous released STL files.
- If fit-critical dimensions change, note affected interfaces in commit message.

## Suggested First Part Set

- `ACT-SHOULDER-motor-mount-r01`
- `ACT-SHOULDER-primary-housing-r01`
- `ACT-SHOULDER-bearing-block-in-r01`
- `ACT-SHOULDER-bearing-block-out-r01`
- `ACT-SHOULDER-link-arm-r01`
- `ACT-SHOULDER-wire-guide-r01`
- `ACT-SHOULDER-cover-r01`

[Back to README](../../README.md)
