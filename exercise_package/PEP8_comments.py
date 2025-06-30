
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 12:30:18 2025

@author: mdiby
"""

#  This script tests PEP8 commenting and documentation standard.
#  It defines a function that summarizes metadata from an observation header.
#  Useful for testuing light curve or imaging metadata in astronomy pipelines.


def summarize_metadata(header_dict):
    """
    Summarize key information from a telescope observation header.

    Parameters
    ----------
    header_dict : dict
       A dictionary containing metadata fields such 'OBSERVER',
       'TELESCOPE', and 'FILTER'. 

    Returns
    -------
    summary : str
        A human-readable summary string of observer,
        telescope, and filter used..

    """
    #Get the observer name from the dictionary
    
    observer = header_dict.get("OBSERVER", "Unknown")
    
    #Get the telescope name; default to 'N/A' if not found 
    
    telescope = header_dict.get("TELESCOPE", "N/A")
    
    #Get the filter used during observation 
    
    filter_used = header_dict.get ("FILTER", "No Filter")
    
    
    #Build a summary sentence using f-string formatting 
    summary = (
        f"Observation by {observer} using {telescope} "
        f"telescope with the {filter_used} filter."
        )
    return summary 

#Example usage (only runs when the script is executed directly)
# if __name__ == "__main__":
#     #Create a mock FITS header dfictionary 
#     mock_header = {
#         "OBSERVER": "Dr. Nakelle",
#         "TELESCOPE": "JWST",
#         "FILTER": "F200W"
#         }
    
#     #Call the function to generate the summary 
#     result = summarize_metadata(mock_header)
    
#     #print the result to the terminal 
#     print(result)

    