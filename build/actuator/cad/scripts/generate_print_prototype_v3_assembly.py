#!/usr/bin/env python3
import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import FreeCAD as App
import FreeCADGui as Gui
import Part


ROOT = os.getcwd()
if os.path.basename(ROOT) == "-c":
    ROOT = os.path.dirname(ROOT)

PARTS_DIR = os.path.join(ROOT, "build", "actuator", "print-prototype-v3", "parts")
OUT_DIR = os.path.join(ROOT, "build", "actuator", "print-prototype-v3", "assembly")


def ensure_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)


def load_fcstd_shape(doc, label, fcstd_name, x=0, y=0, z=0, rz=0):
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

    doc = App.newDocument("ACT_PrintPrototype_v3_Assembly")
    objs = []

    objs.append(load_fcstd_shape(doc, "P01", "P01_main_side_frame_plate_v3.FCStd", 0, 0, 0))
    objs.append(load_fcstd_shape(doc, "P02", "P02_opposite_side_frame_plate_v3.FCStd", 0, 44, 0))
    objs.append(load_fcstd_shape(doc, "P03", "P03_upper_bridge_cap_plate_v3.FCStd", 60, 8, 152))
    objs.append(load_fcstd_shape(doc, "P04", "P04_lower_bridge_end_plate_v3.FCStd", 60, 8, 3))
    objs.append(load_fcstd_shape(doc, "P06", "P06_end_clamp_yoke_v3.FCStd", 12, 7, 62))

    objs.append(load_fcstd_shape(doc, "M01", "M01_lead_screw_ref_v3.FCStd", 78, 22, 5))
    objs[-1].Placement.Rotation = App.Rotation(App.Vector(1, 0, 0), 90)
    objs.append(load_fcstd_shape(doc, "M02", "M02_guide_rod_A_ref_v3.FCStd", 62, 16, 5))
    objs[-1].Placement.Rotation = App.Rotation(App.Vector(1, 0, 0), 90)
    objs.append(load_fcstd_shape(doc, "M03", "M03_guide_rod_B_ref_v3.FCStd", 94, 28, 5))
    objs[-1].Placement.Rotation = App.Rotation(App.Vector(1, 0, 0), 90)

    objs.append(load_fcstd_shape(doc, "M04", "M04_traveling_carriage_nut_block_v3.FCStd", 64, 10, 80))
    objs.append(load_fcstd_shape(doc, "M05", "M05_output_link_fork_v3.FCStd", 26, 14, 72))

    objs.append(load_fcstd_shape(doc, "P07", "P07_electronics_bracket_v3.FCStd", 132, -2, 66, 90))
    objs.append(load_fcstd_shape(doc, "E01", "E01_controller_pcb_ref_v3.FCStd", 136, 0, 82, 90))

    doc.recompute()

    fcstd = os.path.join(OUT_DIR, "print-prototype-v3-assembly.FCStd")
    png = os.path.join(OUT_DIR, "print-prototype-v3-assembly.png")
    step = os.path.join(OUT_DIR, "print-prototype-v3-assembly.step")

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
