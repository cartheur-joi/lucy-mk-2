# Photo-Match v2 Pass

[Back to Actuator README](../README.md)

This pass rebuilds core geometry to better resemble the actuator photo silhouette and stack-up.

## Outputs

- Parts (`.FCStd` primary): `parts/`
- Assembly: [`assembly/photo-match-v2-assembly.FCStd`](assembly/photo-match-v2-assembly.FCStd)
- Assembly preview: [`assembly/photo-match-v2-assembly.png`](assembly/photo-match-v2-assembly.png)
- Comparison image: [`assembly/photo-vs-v2-labeled.png`](assembly/photo-vs-v2-labeled.png)

## Regenerate (FreeCAD 1.1)

- Parts:
  - `scripts/freecad-1.1.sh -c "exec(open('build/actuator/cad/scripts/generate_photo_match_v2_parts.py').read())"`
- Assembly:
  - `scripts/freecad-1.1.sh -c "exec(open('build/actuator/cad/scripts/generate_photo_match_v2_assembly.py').read())"`

## What Improved vs Prior Pass

- Slimmer side-plate profile and denser hole pattern
- Closer rod/screw packing and longer vertical travel proportion
- Smaller carriage and end-yoke better aligned to photo silhouette
- Board bracket moved and proportioned for side-mounted look

## Remaining Gaps

- Exact COTS interfaces (lead-screw nut body, bearing shoulders, motor bolt circle)
- True fastener locations and hardware stack thickness
- Wiring branch routing and connector geometry details

## Next Lockdown Step

1. Pick one known reference dimension from your physical part.
2. Calibrate scale from the photo with that reference.
3. Freeze rod spacing, screw pitch/nut envelope, and bearing seat dimensions.
4. Regenerate only `P01/P02/M04/P06` until dry-fit passes.
