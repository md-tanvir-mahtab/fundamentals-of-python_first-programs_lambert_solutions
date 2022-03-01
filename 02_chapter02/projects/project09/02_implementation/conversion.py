"""
Program: conversion.py
Author: Md. Tanvir Mahtab
Date: 2022-01-13

Purpose: This script contains a function that can convert kilometers to nautical miles
based on the given number of kilometers.
"""


# Define the function to convert kilometers to nautical miles
def km_to_nm(kilometers):
    """
    Returns equivalent number of nautical miles based on given number of kilometers.
    """
    
    # Convert km to nm and return it
    return kilometers * 90 * 60 / 10000