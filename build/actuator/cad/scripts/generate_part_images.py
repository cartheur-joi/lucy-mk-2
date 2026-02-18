#!/usr/bin/env python3
import os
import sys
import math

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import FreeCAD as App
import FreeCADGui as Gui
import Part
import Mesh


def box(l, w, h, x=0, y=0, z=0):
    return Part.makeBox(l, w, h, App.Vector(x, y, z))


def cyl(r, h, x=0, y=0, z=0, dx=0, dy=0, dz=1):
    return Part.makeCylinder(r, h, App.Vector(x, y, z), App.Vector(dx, dy, dz))


def hex_prism(flat_d, h, x=0, y=0, z=0):
    r = flat_d / 1.7320508075688772
    pts = []
    for i in range(6):
        ang = i * 3.141592653589793 / 3.0
        pts.append(App.Vector(x + r * math.cos(ang), y + r * math.sin(ang), z))
    pts.append(pts[0])
    wire = Part.makePolygon(pts)
    face = Part.Face(wire)
    return face.extrude(App.Vector(0, 0, h))


def p01():
    s = box(140, 45, 8)
    for xx in (15, 70, 125):
        s = s.cut(cyl(2.0, 10, xx, 22.5, -1))
    s = s.cut(box(30, 12, 4, 55, 16.5, 4))
    return s


def p02():
    return p01()


def p03():
    s = box(55, 30, 8)
    s = s.cut(cyl(2.0, 10, 8, 15, -1))
    s = s.cut(cyl(2.0, 10, 47, 15, -1))
    return s


def p04():
    s = box(55, 30, 10)
    s = s.cut(box(22, 16, 6, 16.5, 7, 2))
    s = s.cut(cyl(2.0, 12, 8, 15, -1))
    s = s.cut(cyl(2.0, 12, 47, 15, -1))
    return s


def p05():
    s = cyl(5, 18)
    return s.cut(cyl(1.6, 20, 0, 0, -1))


def p06():
    s = box(40, 30, 22)
    s = s.cut(box(24, 20, 18, 8, 5, 4))
    s = s.cut(cyl(2.0, 32, 20, 15, -1))
    return s


def p07():
    leg_a = box(60, 4, 35)
    leg_b = box(60, 25, 4, 0, 0, 31)
    s = leg_a.fuse(leg_b)
    for xx in (8, 30, 52):
        s = s.cut(cyl(1.8, 10, xx, 2, 10, 0, 1, 0))
    return s


def m01():
    return cyl(4, 160)


def m02():
    return cyl(3, 160)


def m03():
    return cyl(3, 160)


def m04():
    s = box(28, 24, 18)
    s = s.cut(cyl(4.5, 22, 14, 12, -2))
    s = s.cut(cyl(3.2, 22, 8, 6, -2))
    s = s.cut(cyl(3.2, 22, 20, 6, -2))
    s = s.cut(cyl(3.2, 22, 8, 18, -2))
    s = s.cut(cyl(3.2, 22, 20, 18, -2))
    return s


def m05():
    s = box(90, 18, 14)
    s = s.cut(box(24, 10, 10, 66, 4, 2))
    s = s.cut(cyl(2.5, 20, 8, 9, -2))
    s = s.cut(cyl(2.0, 20, 78, 9, -2))
    return s


def m06():
    s = cyl(7, 25)
    s = s.cut(cyl(3.2, 14, 0, 0, -1))
    s = s.cut(cyl(4.2, 14, 0, 0, 12))
    return s


def m07():
    return cyl(11, 7).cut(cyl(4, 9, 0, 0, -1))


def e01():
    pcb = box(95, 45, 1.8)
    for x, y in ((5, 5), (90, 5), (5, 40), (90, 40)):
        pcb = pcb.cut(cyl(1.6, 4, x, y, -1))
    chips = box(16, 12, 2, 12, 16, 1.8).fuse(box(20, 8, 2, 36, 22, 1.8))
    return pcb.fuse(chips)


def e02():
    return box(18, 12, 10).fuse(box(6, 12, 4, 18, 0, 3))


def w01():
    a = cyl(1.8, 130, 0, -2, 0, 1, 0, 0)
    b = cyl(1.8, 130, 0, 2, 0, 1, 0, 0)
    c = cyl(1.8, 130, 0, 6, 0, 1, 0, 0)
    return a.fuse(b).fuse(c)


def w02():
    s = box(22, 12, 10)
    s = s.cut(cyl(4.0, 24, 11, 6, -2))
    s = s.cut(cyl(1.8, 12, 4, 6, -1))
    s = s.cut(cyl(1.8, 12, 18, 6, -1))
    return s


def h01():
    shaft = cyl(1.5, 20)
    head = cyl(3.0, 3, 0, 0, 20)
    return shaft.fuse(head)


def h02():
    return hex_prism(7.0, 2.4).cut(cyl(1.6, 4, 0, 0, -1))


def h03():
    return cyl(4.0, 1.0).cut(cyl(1.6, 3, 0, 0, -1))


def h04():
    return hex_prism(6.0, 12).cut(cyl(1.6, 14, 0, 0, -1))


def h05():
    return cyl(1.6, 6).fuse(cyl(2.2, 1.4, 0, 0, 6))


PARTS = [
    ("P01_main_side_frame_plate", p01),
    ("P02_opposite_side_frame_plate", p02),
    ("P03_upper_bridge_cap_plate", p03),
    ("P04_lower_bridge_end_plate", p04),
    ("P05_spacer_standoff_block", p05),
    ("P06_end_clamp_yoke", p06),
    ("P07_electronics_bracket", p07),
    ("M01_lead_screw", m01),
    ("M02_guide_rod_A", m02),
    ("M03_guide_rod_B", m03),
    ("M04_traveling_carriage_nut_block", m04),
    ("M05_output_link_fork", m05),
    ("M06_shaft_coupler", m06),
    ("M07_bearing_bushing", m07),
    ("E01_controller_pcb", e01),
    ("E02_connector_block", e02),
    ("W01_harness_bundle", w01),
    ("W02_strain_relief_anchor", w02),
    ("H01_machine_screw", h01),
    ("H02_nut_locknut", h02),
    ("H03_washer", h03),
    ("H04_standoff", h04),
    ("H05_set_screw_retainer", h05),
]


def ensure_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)


def render_part(out_dir, name, shape_builder):
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

    png_path = os.path.join(out_dir, name + ".png")
    fcstd_path = os.path.join(out_dir, name + ".FCStd")
    step_path = os.path.join(out_dir, name + ".step")
    stl_path = os.path.join(out_dir, name + ".stl")

    view.saveImage(png_path, 1400, 1000, "White")
    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)
    Mesh.export([obj], stl_path)

    App.closeDocument(doc_name)
    return png_path, fcstd_path, step_path, stl_path


def main():
    repo_root = os.getcwd()
    # FreeCAD AppImage + `freecadcmd -c` can report cwd as ".../-c".
    # If that happens, use the parent workspace root.
    if os.path.basename(repo_root) == "-c":
        parent = os.path.dirname(repo_root)
        if os.path.isdir(os.path.join(parent, "build", "actuator")):
            repo_root = parent
    out_dir = os.path.join(repo_root, "build", "actuator", "renders")
    if len(sys.argv) > 1:
        out_dir = os.path.abspath(sys.argv[1])
    ensure_dir(out_dir)

    Gui.showMainWindow()
    print("Rendering to:", out_dir)
    ok = 0
    for name, builder in PARTS:
        try:
            png_path, fcstd_path, step_path, stl_path = render_part(out_dir, name, builder)
            ok += 1
            print("OK", name, "->", png_path, fcstd_path, step_path, stl_path)
        except Exception as exc:
            print("FAIL", name, str(exc))
    print("Done:", ok, "/", len(PARTS))


if __name__ in ("__main__", "__builtin__"):
    main()
