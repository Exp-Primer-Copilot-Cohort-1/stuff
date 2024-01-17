"""
This script creates a 2D array and prints its elements.
"""
                           
array = [[i for i in range(j, j+10)] for j in range(1, 31, 10)]

# Print the array
for row in array:
    print(' '.join(map(str, row)))
    