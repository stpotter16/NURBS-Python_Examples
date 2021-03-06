# -*- coding: utf-8 -*-

"""
    Visualization Examples for the NURBS-Python Package
    Released under The MIT License
    Developed by Onur Rauf Bingol (c) 2017-2018

    Tested with:
    * Python v3.6.2
    * NumPy v1.13.3
    * Matplotlib v2.1.0
"""
import os
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Read surface and control points, @ref: https://stackoverflow.com/a/13550615
cpgrid = np.genfromtxt('../surface/ctrlpts01_orig.csv', delimiter=',', skip_header=1, names=['x', 'y', 'z'])
surf = np.genfromtxt('../surface/surfpts01_orig.csv', delimiter=',', skip_header=1, names=['x', 'y', 'z'])

# Arrange control points grid for plotting, @ref: https://stackoverflow.com/a/21352257
Xc = cpgrid['x']
Yc = cpgrid['y']
Zc = cpgrid['z']

# Arrange surface points array for plotting, @ref: https://stackoverflow.com/a/21352257
X = surf['x'].reshape(-1, surf['x'].shape[0])
Y = surf['y'].reshape(-1, surf['x'].shape[0])
Z = surf['z'].reshape(-1, surf['x'].shape[0])

# Plot colors array
colors = ['gray', 'brown']

# Start plotting of the surface and the control points grid
fig = plt.figure(figsize=(10.67, 8), dpi=96)
ax = fig.gca(projection='3d')

# Control points as a wireframe plot (use mode='wireframe' while saving CSV file)
ax.plot(Xc, Yc, Zc, color=colors[0], linestyle='-.', marker='o', markerfacecolor='orange', markersize=5)

# Surface points as a wireframe plot (use mode='wireframe' while saving CSV file)
ax.plot_wireframe(X, Y, Z, color=colors[1])

# Add legend to 3D plot, @ref: https://stackoverflow.com/a/20505720
plot1_proxy = matplotlib.lines.Line2D([0], [0], linestyle='-.', color=colors[0], marker='o')
plot2_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color=colors[1], marker='^')
ax.legend([plot1_proxy, plot2_proxy], ['Control Points Grid', 'Surface Plot'], numpoints=1)

# Display the 3D plot
plt.show()
