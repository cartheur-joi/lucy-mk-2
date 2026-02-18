#!/usr/bin/env python3
import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import FreeCAD as App
import FreeCADGui as Gui
import Part


ROOT = os.getcwd()
PARTS_DIR = os.path.join(ROOT, "build", "actuator", "renders")
OUT_DIR = os.path.join(ROOT, "build", "actuator", "assembly")


def ensure_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)


def load_step(doc, label, step_name, x=0, y=0, z=0, rz=0):
    path = os.path.join(PARTS_DIR, step_name)
    shp = Part.read(path)
    obj = doc.addObject("Part::Feature", label)
    obj.Shape = shp
    obj.Placement = App.Placement(
        App.Vector(x, y, z),
        App.Rotation(App.Vector(0, 0, 1), rz),
    )
    return obj


def main():
    ensure_dir(OUT_DIR)
    Gui.showMainWindow()
    doc = App.newDocument("ACT_Example_Assembly")

    objs = []

    # Main frame
    objs.append(load_step(doc, "P01_main_side", "P01_main_side_frame_plate.step", 0, 0, 0))
    objs.append(load_step(doc, "P02_opposite_side", "P02_opposite_side_frame_plate.step", 0, 55, 0))
    objs.append(load_step(doc, "P03_top_bridge", "P03_upper_bridge_cap_plate.step", 42, 12.5, 130, 0))
    objs.append(load_step(doc, "P04_bottom_bridge", "P04_lower_bridge_end_plate.step", 42, 12.5, 0, 0))

    # Linear system (rough illustrative placement)
    objs.append(load_step(doc, "M01_lead_screw", "M01_lead_screw.step", 70, 27.5, 10, 0))
    objs[-1].Placement.Rotation = App.Rotation(App.Vector(1, 0, 0), 90)
    objs.append(load_step(doc, "M02_guide_rod_A", "M02_guide_rod_A.step", 50, 20, 10, 0))
    objs[-1].Placement.Rotation = App.Rotation(App.Vector(1, 0, 0), 90)
    objs.append(load_step(doc, "M03_guide_rod_B", "M03_guide_rod_B.step", 90, 35, 10, 0))
    objs[-1].Placement.Rotation = App.Rotation(App.Vector(1, 0, 0), 90)
    objs.append(load_step(doc, "M04_carriage", "M04_traveling_carriage_nut_block.step", 56, 16, 76, 0))
    objs.append(load_step(doc, "M05_output_link", "M05_output_link_fork.step", 30, 18, 70, 0))
    objs.append(load_step(doc, "M06_coupler", "M06_shaft_coupler.step", 70, 27.5, 0, 0))
    objs[-1].Placement.Rotation = App.Rotation(App.Vector(1, 0, 0), 90)

    # End-effector and brackets
    objs.append(load_step(doc, "P06_end_yoke", "P06_end_clamp_yoke.step", 20, 10, 56, 0))
    objs.append(load_step(doc, "P07_electronics_bracket", "P07_electronics_bracket.step", 116, -4, 55, 90))
    objs.append(load_step(doc, "E01_pcb", "E01_controller_pcb.step", 122, -2, 72, 90))

    # Decorative/informational placement for harness
    objs.append(load_step(doc, "W01_harness", "W01_harness_bundle.step", 115, 8, 30, 90))

    doc.recompute()

    # Save document and exports
    fcstd_path = os.path.join(OUT_DIR, "example-assembly.FCStd")
    step_path = os.path.join(OUT_DIR, "example-assembly.step")
    png_path = os.path.join(OUT_DIR, "example-assembly.png")

    gdoc = Gui.getDocument(doc.Name)
    Gui.ActiveDocument = gdoc
    view = gdoc.ActiveView
    view.viewAxometric()
    view.fitAll()
    view.saveImage(png_path, 1800, 1200, "White")

    doc.saveAs(fcstd_path)
    Part.export(objs, step_path)

    print("WROTE", fcstd_path)
    print("WROTE", step_path)
    print("WROTE", png_path)


if __name__ in ("__main__", "__builtin__"):
    main()
