#!/usr/bin/env python3

def longest_common_substring(str1, str2):

    # Create the matrix as a list of lists.
    matrix = []
    for i in range(len(str1)):
        # Each row is started as a list of zeros.
        matrix.append([0] * len(str2))

    # Variables to remember the largest value, and the position it
    # occurred at.
    max_value = 0
    max_value_row = 0
    max_value_col = 0
    for row in range(len(str1)):
        for col in range(len(str2)):
        
            # Check if the characters match
            if str1[row] == str2[col]:
                # Get the value in the cell that's up and to the 
                # left, or 0 if no such cell
                up_left = 0
                if row > 0 and col > 0:
                    up_left = matrix[row - 1][col - 1]
                
                # Set the value for this cell
                matrix[row][col] = 1 + up_left
                if matrix[row][col] > max_value:
                    max_value = matrix[row][col]
                    max_value_row = row
                    max_value_col = col
            else:
                matrix[row][col] = 0

    # The longest common substring is the substring
    # in str1 from index max_value_row - max_value + 1, 
    # up to and including max_value_col.
    start_index = max_value_row - max_value + 1
    return str1[start_index : max_value_col + 1]
