'''
This file is supposed to contain the logic regarding the physics of the light interacting with the nanopillars
For now, I map each nanopillar point a phase (given by the vortex phase profile)
And suppose, for demonstration purposes, that the phase is linearly positively correlated with the radii
'''

import numpy as np

def PointToPhase(x, y, l=1) -> float:
    '''
    Maps a point (x,y) to its vortex phase profile
    '''
    
    theta = np.arctan2(y, x) # Azimuthal angle (phase is given by l*azimuthal angle)
    return (l * theta) % (2 * np.pi) # # Phase mod 2pi allows me to normalize this from 0 to 2pi (i bring down a large l*theta to the unit circle once again)

def PhaseToRadius(phase, radii: list) -> float:
    '''
    Maps a phase to its equivalent, and later physically determined radius
    '''

    # Linearly map phase (0 to 2π) to the range of radii
    estimatedRadius = radii[0] + (phase / (2 * np.pi)) * (radii[-1] - radii[0])
    # Find the closest value in the radii array
    return min(radii, key=lambda r: abs(estimatedRadius - r))