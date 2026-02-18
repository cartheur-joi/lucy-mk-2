# Actuator Build Starter Pack

This folder contains a practical starting structure for designing, printing, and assembling the first actuator module.

```mermaid
flowchart LR
A[Define Params] --> B[Model Parts in FreeCAD]
B --> C[Export STL per Part]
C --> D[Print Fit Iteration]
D --> E[Assemble Submodules]
E --> F[Bench Validate]
```

## Folder Map

- `cad/`: FreeCAD source files (`.FCStd`)
- `stl/`: production STL files, one per printable part and revision
- `drawings/`: dimensioned PDFs and interface sketches
- `bom/`: fasteners, bearings, shafts, motor, inserts
- `assembly/`: step-by-step assembly notes and photos
- `checklists/`: print and assembly checklists
- `exports/`: temporary exports (test meshes, screenshots)
- `renders/`: generated CAD preview images and exports for part IDs

## Start Here

1. Read `01-naming-spec.md`.
2. Populate `02-freecad-parameter-template.csv`.
3. Use `checklists/print-checklist.md` for each printed part.
4. Use `checklists/assembly-checklist.md` during mechanical integration.
5. Review generated previews in `renders/README.md`.

[Back to README](../../README.md)
