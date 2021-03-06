# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2017
"""
import os
from geomdl import BSpline
from geomdl import utilities

# Try to load the visualization module
try:
    render_surf = True
    from geomdl.visualization import VisMPL
except ImportError:
    render_surf = False

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set evaluation delta
surf.delta = 0.025

# Set up surface
surf.read_ctrlpts_from_txt("ex_surface02.cpt")
surf.degree_u = 3
surf.degree_v = 3
surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, 6)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, 6)

# Evaluate surface
surf.evaluate()

# Draw the control point grid and the evaluated surface
if render_surf:
    vis_comp = VisMPL.VisSurfScatter()
    surf.vis = vis_comp
    surf.render()

# Save control points and evaluated curve points
surf.save_surfpts_to_csv("surfpts02_orig.csv", mode='linear')
surf.save_ctrlpts_to_csv("ctrlpts02_orig.csv", mode='wireframe')

# Evaluate 1st order surface derivative at the given u and v
u = 0.2
v = 0.9
surftan = surf.tangent(u, v)
print("* Surface point at u = %.2f and v = %.2f is (%.2f, %.2f, %.2f)" % (u, v, surftan[0][0], surftan[0][1], surftan[0][2]))
print("* First derivative w.r.t. u is (%.2f, %.2f, %.2f)" % (surftan[1][0], surftan[1][1], surftan[1][2]))
print("* First derivative w.r.t. v is (%.2f, %.2f, %.2f)\n" % (surftan[2][0], surftan[2][1], surftan[2][2]))
# Evaluate normal at the given u and v
norm = surf.normal(u, v)
print("* Normal at u = %.2f and v = %.2f is [%.1f, %.1f, %.1f]\n" % (u, v, norm[1][0], norm[1][1], norm[1][2]))

# Good to have something here to put a breakpoint
pass
