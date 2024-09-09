import geopandas as gpd
import pandas as pd

# List of file paths for the GeoJSON files
geojson_files = [
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N1.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N2.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N3.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N4.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N5.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N6.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N7.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N8.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N9.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N10.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N11.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N12.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N14.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N17.geojson",
    r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\N18.geojson"
]

# Load all GeoJSON files and combine them into a single GeoDataFrame
gdfs = [gpd.read_file(file) for file in geojson_files]
combined_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True))

# Save the combined GeoDataFrame to a new GeoJSON file
combined_gdf.to_file(r"C:\Users\veerg\OneDrive\Documents\Wikimedia\SA Mapping\N Roads\combined_N_roads.geojson", driver="GeoJSON")

print("GeoJSON files combined successfully!")
