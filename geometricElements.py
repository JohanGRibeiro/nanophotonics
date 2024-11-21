'''
This file is supposed to contain the logic regarding basic elements, such as:
- Array (dictionary with names as keys and cells as values) of figures to be referenced for nanopillars
- Metasurface plate where we will lay the nanopillars
'''

import gdspy

def Nanopillars(radii: list, layer=1) -> dict:
    '''
    Returns array of N_NP nanopillars with each indexed radius
    '''
    nanopillar_cells = {}
    for i, radius in enumerate(radii):
        cell_name = f"NANOPILLAR_{i}"
        cell = gdspy.Cell(cell_name)
        circle = gdspy.Round((0, 0), radius, layer=layer)
        cell.add(circle)
        nanopillar_cells[cell_name] = cell
    return nanopillar_cells

def drawMetasurface(layout: gdspy.Cell, center: float, layer=0, points=500) -> None:
    '''
    Receives a layout and draws a round figure in it (metasurface plate). Default is layer 0 (z = 0) and 500 points
    '''
    metasurface_plate = gdspy.Round((0, 0), center, layer=layer, number_of_points=points)
    layout.add(metasurface_plate)