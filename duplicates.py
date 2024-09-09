# Open the input file and read lines
with open('output2.txt', 'r') as infile:
    lines = infile.readlines()

# Use a set to track unique lines
unique_lines = set()

# Open the output file for writing
with open('output3.txt', 'w') as outfile:
    for line in lines:
        if line not in unique_lines:
            outfile.write(line)
            unique_lines.add(line)

print("Duplicate lines removed and unique lines written to output.txt")
