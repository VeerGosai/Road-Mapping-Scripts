import re
from xml.etree import ElementTree as ET

def simplify_path_data(d: str, precision: int = 2) -> str:
    """
    Simplifies the path data by reducing the number of decimal places for coordinates.
    This helps in reducing the number of points while maintaining the shape.
    """
    # Regular expression to find coordinate pairs in the path data
    pattern = re.compile(r"([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)")

    # Function to round numbers to the specified precision
    def round_number(match):
        return f"{float(match.group()):.{precision}f}"

    # Apply rounding to all coordinate values
    simplified_d = pattern.sub(round_number, d)

    return simplified_d

def simplify_svg(input_file: str, output_file: str, precision: int = 2):
    # Load and parse the SVG file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Define the SVG namespace
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}
    
    # Find all path elements
    paths = root.findall('.//svg:path', namespaces)

    # Simplify each path
    for path in paths:
        d = path.attrib.get('d', '')
        simplified_d = simplify_path_data(d, precision)
        path.set('d', simplified_d)

    # Save the modified SVG to a new file
    tree.write(output_file)

# Example usage:
input_file = 'simplified_output5.svg'  # Path to your input SVG
output_file = 'simplified_output6.svg'  # Path to save the simplified SVG
simplify_svg(input_file, output_file, precision=2)  # Adjust precision as needed
