from os import strerror

# Initialize counters for letters a through z
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

file_name = input("Enter the name of the file to analyze: ")

try:
    # Read the input file
    with open(file_name, "rt", encoding="utf-8") as file:
        for line in file:
            for char in line:
                char = char.lower()

                if 'a' <= char <= 'z':
                    counters[char] += 1

                # if char.isalpha():
                #     counters[char.lower()] += 1

    # Create the histogram output file
        output_file = file_name + ".hist"

    # Sort letters by frequency (highest first)
    sorted_counters = sorted(
        counters.items(),
        key=lambda item: item[1],
        reverse=True
    )

    

    with open(output_file, "wt", encoding="utf-8") as file:
        for char, count in sorted_counters:
            if count > 0:
                file.write(f"{char} -> {count}\n")

    # with open(output_file, "wt", encoding="utf-8") as file:
    #     # Sort letters by frequency (highest first)
    #     # Note: we've used a lambda to access the directory's elements and set reverse to get a valid order.
    #     for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
    #         c = counters[char]
    #         if c > 0:
    #             file.write(char + ' -> ' + str(c) + '\n')
    
    print("Histogram saved to:", output_file)

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))