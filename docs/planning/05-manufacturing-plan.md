# Manufacturing Plan

[Back to README](../../README.md)


## Fabrication Split

- In-house 3D printing:
- shells, covers, sensor mounts, cable guides, jigs
- some light-load brackets
- Outsourced metal:
- load-bearing frames, shoulder bridge, precision joint plates, shaft components

## In-House Print Standards

- Layer height:
- structural parts: 0.2 mm
- cosmetic panels: 0.16-0.2 mm
- Infill:
- structural parts: 35-55 percent (gyroid or cubic)
- cosmetic: 15-25 percent
- Wall count:
- structural parts: >= 4 perimeters
- Thermal:
- material-specific profiles logged and versioned

## Metal Part Fabrication Route

- Flat parts:
- laser/waterjet cut + secondary drilling/tapping if needed
- 3D parts:
- CNC from plate/bar where tolerances matter
- Shafts/pins:
- off-the-shelf precision stock preferred

## DFM Rules

- Avoid hidden internal supports in print geometry.
- Split large shells into printer-friendly sections with alignment keys.
- Include wrench/driver access in all enclosed fastener zones.
- Use common stock thicknesses for metal plates to reduce quote complexity.

## Tolerancing Strategy

- Critical datums on metal parts.
- Printed interfaces treated as secondary and adjustable where possible.
- Slotted holes for alignment tuning at module interfaces.

## Vendor Package Checklist

- 2D drawings (PDF) with datums, tolerances, finish notes
- neutral 3D format (STEP) for complex parts
- quantity, material, and thread spec table
- deburr/chamfer requirements

## Incoming Inspection

- Verify critical dimensions on first article parts.
- Check hole patterns against fixture plates.
- Dry-fit all joint stacks before full assembly.

## Change Control

- Part naming:
- `MK2-<subsystem>-<part>-r<rev>`
- ECO log required for any geometry change affecting interfaces.

