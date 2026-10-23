# Letter Counter and Letter Histogram

## Project Overview

This project contains two Python programs that analyze text files and count how frequently letters appear.

The programs demonstrate Python concepts including file handling, dictionaries, loops, dictionary comprehensions, exception handling, lambda functions, and sorting.

## Project Files

```text
letter-analysis/
├── letter_counter.py
├── letter_histogram.py
├── sample.txt
└── README.md
```

## Program 1: Letter Counter

**File:** `letter_counter.py`

### Description

The Letter Counter program reads a text file, counts the occurrences of each English alphabet letter (a–z), and displays the results in the terminal.

The program is case-insensitive, meaning uppercase and lowercase letters are counted together.

### Features

- Reads a text file.
- Uses a dictionary comprehension to initialize 26 letter counters.
- Counts uppercase and lowercase letters together.
- Ignores numbers, spaces, and punctuation.
- Displays only letters that appear in the file.
- Handles file input/output errors.

### How to Run

Open the VS Code terminal and enter:

```powershell
python letter_counter.py
```

When prompted, enter the source filename:

```text
Enter the name of the file to analyze: sample.txt
```

### Sample Input

Contents of `sample.txt`:

```text
Hello World
```

### Expected Output

```text
d -> 1
e -> 1
h -> 1
l -> 3
o -> 2
r -> 1
w -> 1
```

The results are displayed alphabetically.

---

## Program 2: Letter Histogram

**File:** `letter_histogram.py`

### Description

The Letter Histogram program reads a text file, counts the occurrences of each letter, sorts the results from highest to lowest frequency, and writes them to a separate output file.

The output filename is automatically created by adding `.hist` to the original filename.

### Features

- Reads and analyzes a text file.
- Counts letters using a dictionary.
- Treats uppercase and lowercase letters equally.
- Uses a lambda function to sort letters by frequency.
- Sorts results in descending order.
- Saves results in a `.hist` file.
- Handles file input/output errors.

### How to Run

Open the VS Code terminal and enter:

```powershell
python letter_histogram.py
```

When prompted:

```text
Enter the name of the file to analyze: sample.txt
```

The program creates:

```text
sample.txt.hist
```

### Sample Input

Contents of `sample.txt`:

```text
Hello World
```

### Expected Output File

Contents of `sample.txt.hist`:

```text
l -> 3
o -> 2
d -> 1
e -> 1
h -> 1
r -> 1
w -> 1
```

The letters are sorted by frequency, with the most frequently occurring letter appearing first.

---

## Comparison of the Two Programs

| Feature | Letter Counter | Letter Histogram |
|---|---|---|
| Reads a text file | Yes | Yes |
| Counts letters | Yes | Yes |
| Case-insensitive | Yes | Yes |
| Uses a dictionary | Yes | Yes |
| Displays results in terminal | Yes | No |
| Sorts by frequency | No | Yes |
| Creates an output file | No | Yes |
| Uses a lambda function | No | Yes |

## Python Concepts Used

**1. Dictionary Comprehension**

```python
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
```

Creates a dictionary containing 26 letters, each initialized to zero.

**2. File Handling**

```python
file = open(file_name, "rt")
```

Opens a text file in read mode.

**3. Nested Loops**

```python
for line in file:
    for char in line:
```

Processes each line and each character in the file.

**4. Letter Counting**

```python
if char.isalpha():
    counters[char.lower()] += 1
```

Checks whether a character is a letter, converts it to lowercase, and increments its counter.

**5. Lambda Function and Sorting**

```python
sorted(counters.keys(), key=lambda x: counters[x], reverse=True)
```

Sorts the letters according to their frequency in descending order.

**6. Exception Handling**

```python
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
```

Handles input/output errors, such as a missing source file.

## Testing Scenarios

1. Analyze a file containing uppercase and lowercase letters.
2. Analyze a file containing repeated letters.
3. Analyze a file containing numbers and punctuation.
4. Analyze an empty file.
5. Enter a filename that does not exist.
6. Verify that the histogram output file is created correctly.

## Requirements

- Python 3
- Visual Studio Code (recommended)
- Python extension for VS Code

## Limitations

Both programs initialize counters for English letters a–z. They are intended for English-language text files. Some non-English alphabetic characters may cause a `KeyError` because they are not included in the dictionary.

## Conclusion

These programs demonstrate how Python can analyze text files using dictionaries, loops, and file-handling operations.

The Letter Counter program displays letter frequencies in alphabetical order, while the Letter Histogram program sorts the results by frequency and saves them to a file.