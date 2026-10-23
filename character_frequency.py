# Same as letter_histogram.py, but with a different approach to counting letters and writing the output file.
from os import strerror

# Create a dictionary containing letters a through z,
# with each letter's initial count set to 0.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

# Ask the user for the file to analyze.
file_name = input("Enter the name of the file to analyze: ")

try:
    # Open the file in text read mode.
    file = open(file_name, "rt")

    # Read each line and count the letters.
    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1

    file.close()

    # Create an output file with the .hist extension.
    file = open(file_name + '.hist', 'wt')

    # Sort letters by frequency, highest first.
    for char in sorted(counters.keys(),
                       key=lambda x: counters[x],
                       reverse=True):

        c = counters[char]

        # Write only letters that appear in the file.
        if c > 0:
            file.write(char + ' -> ' + str(c) + '\n')

    file.close()

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
