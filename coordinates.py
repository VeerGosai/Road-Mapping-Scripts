def process_files(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    coordinates = []
    temp = []

    for line in lines:
        stripped = line.strip().strip('[],')  # Remove any unwanted characters
        if stripped:  # If the line is not empty
            temp.append(stripped)
            if len(temp) == 2:  # Collect both latitude and longitude
                coordinates.append(f"[{temp[0]},{temp[1]}],")
                temp = []  # Reset for the next pair

    # Write the output
    with open(output_file, 'w') as f:
        for coord in coordinates:
            f.write(coord + '\n')

# File paths
input_file = 'input.txt'
output_file = 'output.txt'

# Process the input and write to the output file
process_files(input_file, output_file)
