import gdspy
import numpy as np

photonicsLib = gdspy.GdsLibrary()

# METASURFACE PARAMETERS

DIAMETER = 100000 # diameter of metasurface in microns, which is default unit in gds (10cm)
N_NP = 10**10 # number of nanopillars in metasurface
HEIGHT = 3 # height of nanopillars in microns
N_RADII = 10 # number of different nanopillar radii to be referenced for compression
SPACING = np.sqrt( (np.pi* (DIAMETER/2)**2) / N_NP ) #  = 0.8862269254527579 microns - Deduction for this formula at 19/11/24 

radii = np.linspace(0.1, 0.7, N_RADII)  # Array of radii in microns