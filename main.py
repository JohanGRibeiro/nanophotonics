# main.py

import gdspy
import numpy as np
import optics
import geometricElements

photonicsLib = gdspy.GdsLibrary()

# Constants
DIAMETER = 1000
N_NP = 10**4
HEIGHT = 3
N_RADII = 10
SPACING = np.sqrt((np.pi * (DIAMETER / 2)**2) / N_NP)
Radii = np.linspace(0.1*SPACING , 0.40*SPACING, N_RADII)

# Create layout and boundary
layout = gdspy.Cell("METASURFACE")
center = DIAMETER / 2
geometricElements.drawMetasurface(layout, center) # draws round plate into cell with given center

# Generate nanopillar array
nanopillar_cells = geometricElements.Nanopillars(Radii)

# Grid coordinates
x_coords = np.arange(-center, center, SPACING)
y_coords = np.arange(-center, center, SPACING)

# Place nanopillars
for x in x_coords:
    for y in y_coords:
        if np.sqrt(x**2 + y**2) > center:
            continue
        phase = optics.PointToPhase(x, y, l=1)
        radius = optics.PhaseToRadius(phase, Radii)
        radius_index = Radii.tolist().index(radius)
        nanopillar_ref = gdspy.CellReference(nanopillar_cells[f"NANOPILLAR_{radius_index}"], (x, y))
        layout.add(nanopillar_ref)

# Save GDSII
photonicsLib.add(layout)
gdspy.LayoutViewer()
print("GDSII file saved as optimized_vortex_metasurface.gds")