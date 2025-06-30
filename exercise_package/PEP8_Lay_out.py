
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 17:34:55 2025

@author: mdiby
"""

import math      #Library



def orbital_velocity (h_m, M_Kg):        
    """
    calculate the orbital velocity at agiven altitude.

    Parameters
    ----------
    h_m : float
        Altitude above Earthh'surface in meters.
    M_Kg : float
        Mass of the central body (e.g., Earth) in kilograms.

    Returns
    -------
    velocity : float
        orbital velocity in meters per second at a given altitude.

    """    
    
     #constants
    G = 6.67e-11       #gravitational constant
    M = M_Kg           #Mass kg
    R = 6.37e6         #Earth's Radius in meter
    h = h_m            #Altitude
    
    orbital_radius = R + h
    
    velocity = math.sqrt(G * M / orbital_radius)
    
    return velocity

    
# if __name__ == "__main__":
    
#     h_m  = 4000
#     M_kg = 9.97e24 
#     velocity = orbital_velocity(h_m,M_kg)
   

#     print(f"orbital velocity at {h_m} m: {velocity: .2f} m/s")