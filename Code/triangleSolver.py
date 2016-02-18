import numpy
import time

print("Parsing triangle.txt")
startTime = time.time()
triangle_file = open("../triangle.txt")

triangle_lines = []

for line in triangle_file:
    this_line = []
    for num in line.split():
        try:
            value = int(num)
            this_line.append(value)
        except ValueError:
            continue
    triangle_lines.append(this_line)

print("DONE.")
print("Calculating maximum path")

total_number_of_elements = (100 * 101)/2 #gauss sum
max_path_to_element = numpy.zeros(total_number_of_elements, dtype=numpy.int) #array to track the maximum sum possible at each element

def get_absolute_index(line, index):
    abs_index = (line * (line + 1))/2 + (index)
    return int(abs_index)

def calculate_max_path_to_element(line, index, value):
    if line == 0: # base case
        return value
    if index == 0: # leftmost element of this line. Can only be accessed by leftmost element of line-1
        return max_path_to_element[get_absolute_index(line-1, index)] + value
    elif index == line: # rightmost element of this line. Can only be accessed by rightmost element of line-1
        return max_path_to_element[get_absolute_index(line-1, index-1)] + value
    else: # this element is in the middle.
        return max(max_path_to_element[get_absolute_index(line-1, index-1)] + value,
                   max_path_to_element[get_absolute_index(line-1, index)] + value)

for i, line in enumerate(triangle_lines):
    for j, num in enumerate(line):
        max_path_to_element[get_absolute_index(i, j)] = calculate_max_path_to_element(i, j, num)

print(str(max(max_path_to_element)))
print("DONE. Time Elapsed: %0.6f seconds" % (time.time() - startTime))
