import json

def split_geojson(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    features = data.get('features', [])
    
    for feature in features:
        geometry_type = feature['geometry']['type']
        if geometry_type in ['LineString', 'MultiLineString']:
            ref_name = feature.get('properties', {}).get('ref', 'unknown')
            new_geojson = {
                'type': 'FeatureCollection',
                'features': [feature]
            }
            output_file = f'{ref_name}.geojson'
            with open(output_file, 'w') as f:
                json.dump(new_geojson, f, indent=2)
            print(f'Created {output_file}')

# Replace 'input.geojson' with your GeoJSON file name
split_geojson('South African Road Network.geojson')
