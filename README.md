# GeoJSON Data Plotting - Python Scripts

This repository contains Python scripts that I created while learning how to plot and manipulate GeoJSON data. These scripts perform various operations on GeoJSON data, including plotting, removing duplicates, splitting, and simplifying geometries.

## Files in the Repository

1. **`combinegeo.py`**: Combines multiple GeoJSON files into one GeoJSON file.
2. **`coordinates.py`**: Extracts coordinates from GeoJSON features and saves them into a separate file.
3. **`duplicates.py`**: Identifies and removes duplicate geometries in a GeoJSON file.
4. **`plot.py`**: Plots the GeoJSON data on a simple map using Python libraries.
5. **`remove10.py`**: Removes every 10th geometry from the GeoJSON data.
6. **`simplyfy.py`**: Simplifies geometries in the GeoJSON file to reduce the number of points for faster processing and plotting.
7. **`split.py`**: Splits a GeoJSON file based on a specified attribute, creating separate GeoJSON files for each attribute value.

## Installation and Dependencies

Before running the scripts, you'll need to install the required Python libraries. You can install the necessary dependencies using `pip`:

```bash
pip install geopandas matplotlib
