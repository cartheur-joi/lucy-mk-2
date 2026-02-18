#!/usr/bin/env python3
import os
import math

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import FreeCAD as App
import FreeCADGui as Gui
import Part
import Mesh


ROOT = os.getcwd()
if os.path.basename(ROOT) == "-c":
    ROOT = os.path.dirname(ROOT)

OUT_DIR = os.path.join(ROOT, "build", "actuator", "photo-match-v2", "parts")


def ensure_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)


def box(l, w, h, x=0, y=0, z=0):
    return Part.makeBox(l, w, h, App.Vector(x, y, z))


def cyl(r, h, x=0, y=0, z=0, dx=0, dy=0, dz=1):
    return Part.makeCylinder(r, h, App.Vector(x, y, z), App.Vector(dx, dy, dz))


def hex_prism(flat_d, h, x=0, y=0, z=0):
    r = flat_d / 1.7320508075688772
    pts = []
    for i in range(6):
        ang = i * math.pi / 3.0
        pts.append(App.Vector(x + r * math.cos(ang), y + r * math.sin(ang), z))
    pts.append(pts[0])
    return Part.Face(Part.makePolygon(pts)).extrude(App.Vector(0, 0, h))


# Photo-match v2 assumptions:
# - Slender side plates with close rod spacing
# - Long vertical travel region
# - Compact end-yoke and board-side bracket


def p01():
    s = box(165, 34, 6)
    for xx in (12, 36, 58, 92, 124, 152):
        s = s.cut(cyl(1.8, 10, xx, 17, -2))
    s = s.cut(box(74, 12, 4, 46, 11, 2))
    s = s.cut(box(24, 10, 4, 8, 12, 2))
    return s


def p02():
    return p01()


def p03():
    s = box(38, 24, 7)
    s = s.cut(cyl(1.8, 10, 8, 12, -1))
    s = s.cut(cyl(1.8, 10, 30, 12, -1))
    return s


def p04():
    s = box(38, 24, 9)
    s = s.cut(cyl(1.8, 11, 8, 12, -1))
    s = s.cut(cyl(1.8, 11, 30, 12, -1))
    s = s.cut(box(14, 8, 6, 12, 8, 1.5))
    return s


def p06():
    s = box(34, 26, 22)
    s = s.cut(box(20, 14, 16, 7, 6, 3))
    s = s.cut(cyl(2.0, 28, 17, 13, -2))
    return s


def p07():
    leg = box(68, 4, 34)
    shelf = box(68, 20, 4, 0, 0, 30)
    s = leg.fuse(shelf)
    for xx in (10, 34, 58):
        s = s.cut(cyl(1.6, 10, xx, 2, 9, 0, 1, 0))
    return s


def m01():
    return cyl(4.0, 176)


def m02():
    return cyl(3.0, 176)


def m03():
    return cyl(3.0, 176)


def m04():
    s = box(24, 20, 16)
    s = s.cut(cyl(4.2, 20, 12, 10, -2))
    s = s.cut(cyl(3.2, 20, 6, 6, -2))
    s = s.cut(cyl(3.2, 20, 18, 6, -2))
    s = s.cut(cyl(3.2, 20, 6, 14, -2))
    s = s.cut(cyl(3.2, 20, 18, 14, -2))
    return s


def m05():
    s = box(82, 14, 12)
    s = s.cut(box(20, 8, 8, 60, 3, 2))
    s = s.cut(cyl(2.2, 18, 8, 7, -2))
    s = s.cut(cyl(2.0, 18, 72, 7, -2))
    return s


def e01():
    pcb = box(86, 40, 1.8)
    for x, y in ((5, 5), (81, 5), (5, 35), (81, 35)):
        pcb = pcb.cut(cyl(1.5, 4, x, y, -1))
    chips = box(14, 10, 2, 10, 12, 1.8).fuse(box(18, 8, 2, 32, 18, 1.8))
    return pcb.fuse(chips)


def h04():
    return hex_prism(6.0, 10).cut(cyl(1.6, 12, 0, 0, -1))


PARTS = [
    ("P01_main_side_frame_plate_v2", p01),
    ("P02_opposite_side_frame_plate_v2", p02),
    ("P03_upper_bridge_cap_plate_v2", p03),
    ("P04_lower_bridge_end_plate_v2", p04),
    ("P06_end_clamp_yoke_v2", p06),
    ("P07_electronics_bracket_v2", p07),
    ("M01_lead_screw_v2", m01),
    ("M02_guide_rod_A_v2", m02),
    ("M03_guide_rod_B_v2", m03),
    ("M04_traveling_carriage_nut_block_v2", m04),
    ("M05_output_link_fork_v2", m05),
    ("E01_controller_pcb_v2", e01),
    ("H04_standoff_v2", h04),
]


def export_part(name, shape_builder):
    doc_name = "DOC_" + name
    doc = App.newDocument(doc_name)
    obj = doc.addObject("Part::Feature", name)
    obj.Shape = shape_builder()
    doc.recompute()

    gdoc = Gui.getDocument(doc_name)
    Gui.ActiveDocument = gdoc
    view = gdoc.ActiveView
    view.viewAxometric()
    view.fitAll()

    png = os.path.join(OUT_DIR, name + ".png")
    fcstd = os.path.join(OUT_DIR, name + ".FCStd")
    stl = os.path.join(OUT_DIR, name + ".stl")

    view.saveImage(png, 1400, 1000, "White")
    doc.saveAs(fcstd)
    Mesh.export([obj], stl)
    App.closeDocument(doc_name)
    return png, fcstd, stl


def main():
    ensure_dir(OUT_DIR)
    Gui.showMainWindow()
    print("Rendering to:", OUT_DIR)
    done = 0
    for name, builder in PARTS:
        try:
            png, fcstd, stl = export_part(name, builder)
            done += 1
            print("OK", name, "->", png, fcstd, stl)
        except Exception as exc:
            print("FAIL", name, str(exc))
    print("Done:", done, "/", len(PARTS))


if __name__ in ("__main__", "__builtin__"):
    main()
