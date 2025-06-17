#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 17:34:55 2025

@author: mdiby
"""

import math      #Library



def orbital_velocity (h_m, M_Kg):            
     #constants
    G = 6.67e-11       #gravitational constant
    M = 5.97e24        #Earth Mass kg
    R = 6.37e6         #Earth's Radius in meter
    h = 5000
    
    orbital_radius = R + h
    
    velocity = math.sqrt(G * M / orbital_radius)
    
    return velocity

    
if __name__ == "__main__":
    
    h_m  = 4000
    M_kg = 9.97e24 
    velocity = orbital_velocity(h_m,M_kg)
   

    print(f"orbital velocity at {h_m} m: {velocity: .2f} m/s")