def remove_every_10th_coordinate(input_file, output_file):
    with open(input_file, 'r') as f:
        coordinates = f.readlines()

    # Remove every 10th coordinate
    filtered_coordinates = [coord for i, coord in enumerate(coordinates, start=1) if i % 10 != 0]

    # Write the result to the output file
    with open(output_file, 'w') as f:
        for coord in filtered_coordinates:
            f.write(coord)

# File paths
input_file = 'output.txt'  # Input file where the original coordinates are stored
output_file = 'output2.txt'  # Output file after removing every 10th coordinate

# Process the input and write to the new output file
remove_every_10th_coordinate(input_file, output_file)
