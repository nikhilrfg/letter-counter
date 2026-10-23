from os import strerror

# Create a dictionary with letters a through z
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

# Ask the user for the file name
file_name = input("Enter the name of the file to analyze: ")

try:
    # Open the text file
    with open(file_name, "rt", encoding="utf-8") as file:

        # Read each line
        for line in file:

            # Read each character
            for char in line:

                 # If it is a letter...
                    # if char.isalpha():

                # Check whether the character is an English letter
                if 'a' <= char.lower() <= 'z':

                    # Convert to lowercase and count
                    counters[char.lower()] += 1

    # Display the letter counts
    for char in counters.keys():
        c = counters[char]

        if c > 0:
            print(char, '->', c)

    # for key, value in counters.items():
    #     print(key, value)

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))