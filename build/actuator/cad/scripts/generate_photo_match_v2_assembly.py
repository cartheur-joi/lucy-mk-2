#!/usr/bin/env python3
import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import FreeCAD as App
import FreeCADGui as Gui
import Part


ROOT = os.getcwd()
if os.path.basename(ROOT) == "-c":
    ROOT = os.path.dirname(ROOT)

PARTS_DIR = os.path.join(ROOT, "build", "actuator", "photo-match-v2", "parts")
OUT_DIR = os.path.join(ROOT, "build", "actuator", "photo-match-v2", "assembly")


def ensure_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)


def load_step(doc, label, fcstd_name, x=0, y=0, z=0, rz=0):
    path = os.path.join(PARTS_DIR, fcstd_name)
    src = App.openDocument(path, hidden=True)
    src_objs = src.Objects
    if not src_objs:
        raise RuntimeError("No objects in " + fcstd_name)
    shp = src_objs[0].Shape.copy()
    App.closeDocument(src.Name)

    obj = doc.addObject("Part::Feature", label)
    obj.Shape = shp
    obj.Placement = App.Placement(App.Vector(x, y, z), App.Rotation(App.Vector(0, 0, 1), rz))
    return obj


def main():
    ensure_dir(OUT_DIR)
    Gui.showMainWindow()

    doc = App.newDocument("ACT_PhotoMatch_v2_Assembly")
    objs = []

    objs.append(load_step(doc, "P01", "P01_main_side_frame_plate_v2.FCStd", 0, 0, 0))
    objs.append(load_step(doc, "P02", "P02_opposite_side_frame_plate_v2.FCStd", 0, 40, 0))
    objs.append(load_step(doc, "P03", "P03_upper_bridge_cap_plate_v2.FCStd", 58, 8, 148))
    objs.append(load_step(doc, "P04", "P04_lower_bridge_end_plate_v2.FCStd", 58, 8, 2))

    objs.append(load_step(doc, "M01", "M01_lead_screw_v2.FCStd", 74, 20, 4))
    objs[-1].Placement.Rotation = App.Rotation(App.Vector(1, 0, 0), 90)
    objs.append(load_step(doc, "M02", "M02_guide_rod_A_v2.FCStd", 60, 15, 4))
    objs[-1].Placement.Rotation = App.Rotation(App.Vector(1, 0, 0), 90)
    objs.append(load_step(doc, "M03", "M03_guide_rod_B_v2.FCStd", 88, 25, 4))
    objs[-1].Placement.Rotation = App.Rotation(App.Vector(1, 0, 0), 90)
    objs.append(load_step(doc, "M04", "M04_traveling_carriage_nut_block_v2.FCStd", 62, 10, 78))
    objs.append(load_step(doc, "M05", "M05_output_link_fork_v2.FCStd", 26, 12, 72))
    objs.append(load_step(doc, "P06", "P06_end_clamp_yoke_v2.FCStd", 10, 8, 58))

    objs.append(load_step(doc, "P07", "P07_electronics_bracket_v2.FCStd", 126, -2, 62, 90))
    objs.append(load_step(doc, "E01", "E01_controller_pcb_v2.FCStd", 130, 0, 78, 90))

    doc.recompute()

    fcstd = os.path.join(OUT_DIR, "photo-match-v2-assembly.FCStd")
    png = os.path.join(OUT_DIR, "photo-match-v2-assembly.png")
    step = os.path.join(OUT_DIR, "photo-match-v2-assembly.step")

    gdoc = Gui.getDocument(doc.Name)
    Gui.ActiveDocument = gdoc
    view = gdoc.ActiveView
    view.viewAxometric()
    view.fitAll()
    view.saveImage(png, 1800, 1200, "White")

    doc.saveAs(fcstd)
    Part.export(objs, step)

    print("WROTE", fcstd)
    print("WROTE", png)
    print("WROTE", step)


if __name__ in ("__main__", "__builtin__"):
    main()
