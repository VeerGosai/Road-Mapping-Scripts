import json
import svgwrite

# Convert lat/lon to simple XY coordinates (equirectangular projection)
def lat_lon_to_xy(lat, lon, scale=1000, translate=(0, 0)):
    x = (lon + 180) * (scale / 360) + translate[0]
    y = (90 - lat) * (scale / 180) + translate[1]
    return x, y

# Function to generate SVG path data from GeoJSON (handling MultiLineString and LineString)
def geojson_to_svg(dwg, geojson, scale=1000, translate=(0, 0)):
    for feature in geojson['features']:
        geometry_type = feature['geometry']['type']
        
        if geometry_type == 'MultiLineString':
            for linestring in feature['geometry']['coordinates']:
                path_data = []
                for lon, lat in linestring:
                    x, y = lat_lon_to_xy(lat, lon, scale, translate)
                    path_data.append((x, y))
                
                # Create a polyline for the linestring
                dwg.add(dwg.polyline(path_data, stroke='black', fill='none'))
        
        elif geometry_type == 'LineString':
            path_data = []
            for lon, lat in feature['geometry']['coordinates']:
                x, y = lat_lon_to_xy(lat, lon, scale, translate)
                path_data.append((x, y))
            
            # Create a polyline for the linestring
            dwg.add(dwg.polyline(path_data, stroke='black', fill='none'))

# List of GeoJSON files to process
geojson_files = [
    'N7.geojson',
    'N6.geojson',
    'N5.geojson',
    'N4.geojson',
    'N3.geojson',
    'N2.geojson',
    'N1.geojson',
    'N18.geojson',
    'N17.geojson',
    'N14.geojson',
    'N12.geojson',
    'N11.geojson',
    'N10.geojson',
    'N9.geojson',
    'N8.geojson'
]

# Create an SVG drawing
svg_filename = 'combined_map.svg'
dwg = svgwrite.Drawing(svg_filename, size=(1000, 1000), profile='tiny')

# Process each GeoJSON file and add to the SVG
for geojson_file in geojson_files:
    # Load GeoJSON data from the file
    with open(geojson_file, 'r') as file:
        geojson_data = json.load(file)
    
    # Generate the SVG from the GeoJSON data
    geojson_to_svg(dwg, geojson_data, scale=500, translate=(0, 0))

# Save the combined SVG file
dwg.save()
