# main.py

import gdspy
import numpy as np
import optics
import geometricElements

photonicsLib = gdspy.GdsLibrary()

# Constants
DIAMETER = 10000 #1 cm
N_NP = 10**6 # 10^8 for real, 10^5 for dummy
HEIGHT = 3 # layer 0 is z = 0 (metasurface), layer 1 is z = HEIGHT (nanopillars)
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

        # REFERENCE METHOD - LOWER MEMORY USAGE
        radius_index = Radii.tolist().index(radius)
        nanopillar_ref = gdspy.CellReference(nanopillar_cells[f"NANOPILLAR_{radius_index}"], (x, y))
        layout.add(nanopillar_ref)

        # NON-REFERENCE METHOD - HIGHER MEMORY USAGE
        # Create a new cell for each nanopillar
        #nanopillar_cell = gdspy.Cell(f"NANOPILLAR_{np.where(x_coords == x)[0][0]}_{np.where(x_coords == y)[0][0]}")
        #circle = gdspy.Round((0, 0), radius, layer=1)
        #nanopillar_cell.add(circle)
        #layout.add(gdspy.CellReference(nanopillar_cell, (x, y)))

# Save GDSII
photonicsLib.add(layout)
photonicsLib.write_gds("optimized_vortex_metasurface_dummy_NO_refs.gds")
#gdspy.LayoutViewer(photonicsLib)
print("GDSII file saved as optimized_vortex_metasurface.gds")