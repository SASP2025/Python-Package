#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 11:21:10 2025

@author: mdiby
"""


def normalize_flux(flux_values):
    """
    Normalize a list of flux values using mean and standard deviation
    
    Parameters:
        flux_values (list of float): Raw brightness measurements
        
    Returns :
        list of float: Normalized flux values
    """
    
    n = len(flux_values)
    
    mean_flux = sum(flux_values) / n
    
    squared_diffs = [(f - mean_flux) ** 2 for f in flux_values]   #squared difference of mean and flux value 
    std_flux = (sum(squared_diffs) / n) ** 0.5                     # standard deviation 
    
    normalized_flux = [(f - mean_flux) / std_flux for f in flux_values]
    
    return normalized_flux

if __name__ == "__main__":
    raw_flux = [100.2, 98.4, 101.1, 99.8, 100.0, 98.6]
    norm_flux = normalize_flux(raw_flux)
    
    
    print("Normalized flux values:")
    for val in norm_flux:
        print(f"{val:.3f}")