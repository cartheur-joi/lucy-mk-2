#!/usr/bin/env python3
import math
import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import FreeCAD as App
import FreeCADGui as Gui
import Mesh
import Part


ROOT = os.getcwd()
if os.path.basename(ROOT) == "-c":
    ROOT = os.path.dirname(ROOT)

OUT_DIR = os.path.join(ROOT, "build", "actuator", "print-prototype-v3", "parts")


# Print-first parameters (mm)
NOZZLE = 0.4
LAYER = 0.2
FIT_CLR = 0.35
M3_CLR_D = 3.4
M3_TAP_D = 2.8
MIN_WALL = 2.4


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


def p01():
    s = box(168, 38, 7.2)
    for xx in (14, 40, 66, 102, 134, 156):
        s = s.cut(cyl(M3_CLR_D / 2.0, 12, xx, 19, -2))
    s = s.cut(box(80, 14, 4.5, 44, 12, 2.7))
    s = s.cut(box(24, 12, 4.5, 8, 13, 2.7))
    return s


def p02():
    return p01()


def p03():
    s = box(42, 28, 8)
    s = s.cut(cyl(M3_CLR_D / 2.0, 12, 9, 14, -1))
    s = s.cut(cyl(M3_CLR_D / 2.0, 12, 33, 14, -1))
    return s


def p04():
    s = box(42, 28, 10)
    s = s.cut(cyl(M3_CLR_D / 2.0, 14, 9, 14, -2))
    s = s.cut(cyl(M3_CLR_D / 2.0, 14, 33, 14, -2))
    s = s.cut(box(16, 10, 7, 13, 9, 1.5))
    return s


def p06():
    s = box(38, 30, 24)
    s = s.cut(box(24, 16, 18, 7, 7, 3))
    s = s.cut(cyl((M3_CLR_D + 0.4) / 2.0, 34, 19, 15, -3))
    return s


def p07():
    leg = box(72, 5, 38)
    shelf = box(72, 24, 4, 0, 0, 34)
    gusset = box(72, 8, 8, 0, 5, 28)
    s = leg.fuse(shelf).fuse(gusset)
    for xx in (10, 36, 62):
        s = s.cut(cyl(M3_CLR_D / 2.0, 12, xx, 2.5, 11, 0, 1, 0))
    return s


def m01():
    return cyl(4.0, 180)


def m02():
    return cyl(3.0, 180)


def m03():
    return cyl(3.0, 180)


def m04():
    s = box(28, 24, 18)
    s = s.cut(cyl((8.0 + FIT_CLR) / 2.0, 24, 14, 12, -3))
    s = s.cut(cyl(M3_CLR_D / 2.0, 24, 7, 7, -3))
    s = s.cut(cyl(M3_CLR_D / 2.0, 24, 21, 7, -3))
    s = s.cut(cyl(M3_CLR_D / 2.0, 24, 7, 17, -3))
    s = s.cut(cyl(M3_CLR_D / 2.0, 24, 21, 17, -3))
    return s


def m05():
    s = box(86, 16, 12)
    s = s.cut(box(24, 10, 9, 60, 3, 1.5))
    s = s.cut(cyl(M3_CLR_D / 2.0, 20, 8, 8, -3))
    s = s.cut(cyl(M3_CLR_D / 2.0, 20, 76, 8, -3))
    return s


def e01():
    pcb = box(86, 40, 1.8)
    for x, y in ((5, 5), (81, 5), (5, 35), (81, 35)):
        pcb = pcb.cut(cyl(M3_CLR_D / 2.0, 4, x, y, -1))
    chips = box(14, 10, 2, 10, 12, 1.8).fuse(box(18, 8, 2, 32, 18, 1.8))
    return pcb.fuse(chips)


def h04():
    return hex_prism(6.0, 12).cut(cyl(M3_TAP_D / 2.0, 14, 0, 0, -1))


PARTS = [
    ("P01_main_side_frame_plate_v3", p01),
    ("P02_opposite_side_frame_plate_v3", p02),
    ("P03_upper_bridge_cap_plate_v3", p03),
    ("P04_lower_bridge_end_plate_v3", p04),
    ("P06_end_clamp_yoke_v3", p06),
    ("P07_electronics_bracket_v3", p07),
    ("M01_lead_screw_ref_v3", m01),
    ("M02_guide_rod_A_ref_v3", m02),
    ("M03_guide_rod_B_ref_v3", m03),
    ("M04_traveling_carriage_nut_block_v3", m04),
    ("M05_output_link_fork_v3", m05),
    ("E01_controller_pcb_ref_v3", e01),
    ("H04_standoff_v3", h04),
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
    print("Print params: nozzle=%.1f layer=%.1f fit_clr=%.2f m3_clr_d=%.2f" % (NOZZLE, LAYER, FIT_CLR, M3_CLR_D))
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
