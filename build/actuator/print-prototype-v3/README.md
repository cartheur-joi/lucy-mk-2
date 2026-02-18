# Print-Prototype v3 Pass

[Back to Actuator README](../README.md)

This pass prioritizes first physical prototype success on common FDM printers over photo matching.

## Outputs

- Parts (`.FCStd` primary): `parts/`
- Assembly: [`assembly/print-prototype-v3-assembly.FCStd`](assembly/print-prototype-v3-assembly.FCStd)
- Assembly preview: [`assembly/print-prototype-v3-assembly.png`](assembly/print-prototype-v3-assembly.png)

## Print-First Assumptions

- Fit clearance for moving interfaces: `0.35 mm`
- M3 clearance hole target: `3.4 mm`
- M3 self-tap starter hole target: `2.8 mm`
- Minimum structural wall target: `2.4 mm`

## Regenerate (FreeCAD 1.1)

- Parts:
  - `scripts/freecad-1.1.sh -c "exec(open('build/actuator/cad/scripts/generate_print_prototype_v3_parts.py').read())"`
- Assembly:
  - `scripts/freecad-1.1.sh -c "exec(open('build/actuator/cad/scripts/generate_print_prototype_v3_assembly.py').read())"`

## Notes

- `M01/M02/M03/E01` are reference placeholders for fit and packaging; they are not intended as final printable hardware.
- Primary print targets in this pass: `P01/P02/P03/P04/P06/P07/M04/M05/H04`.
