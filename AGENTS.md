# Repository Agent Instructions

## FreeCAD Requirement

- For all CAD generation tasks in this repository, use FreeCAD `1.1` AppImage:
  - `/home/cartheur/ame/programs/freecad/FreeCAD_1.1rc2-Linux-aarch64-py311.AppImage`
- Do not use system `freecad` / `freecadcmd` unless explicitly requested.
- Use the wrapper script for consistency:
  - `scripts/freecad-1.1.sh`

## Standard Invocation

- Run Python CAD scripts with:
  - `scripts/freecad-1.1.sh -c "exec(open('<script-path>').read())"`
