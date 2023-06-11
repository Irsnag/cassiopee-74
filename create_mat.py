# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:27:58 2023

@author: 33606
"""

import numpy as np
import re

# Function to correct the file
def correct_file(filename):
    """
    Corrects the output txt file from JM Master by updating the macroblock coordinates.

    Args:
        filename (str): The path of the file to be corrected.

    """
    
    n = -1
    lines = []
    
    # Read the file
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line)
    
    # Iterate through the lines
    for i in range(len(lines)):
        # Check if the line indicates the start of a new macroblock
        if lines[i] == 'Macroblock (0,0,0):\n':
            n += 1
        # Check if the line contains the macroblock coordinates
        if 'Macroblock (0' in lines[i]: 
            # Correct the macroblock coordinates by replacing them with the updated value of 'n'
            lines[i] = 'Macroblock (' + str(n) + lines[i][13:]
    
    # Write the corrected lines to a new file
    with open('corr_' + filename, 'w') as c:
        for line in lines:
            c.write(line)




# Function to create a matrix from the file
def create_matrix(filename):
    
    """
    Creates a matrix from the given file.

    Args:
        filename (str): The name of the file.

    Returns:
        numpy.ndarray: The matrix created from the file.

    """
    
    last_tuple = None
    all_tuples = []
    lines = []
    
    # Read the file
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line)
            tuples = re.findall(r'\([^\)]*\)', line)

            if tuples:
                last_tuple = tuples[-1]
                all_tuples.append(tuples)
    
    # Extract the dimensions of the matrix from the last tuple
    t = tuple(int(x) + 1 for x in last_tuple.strip('()').split(','))
    
    # Process the tuples
    for n in range(len(all_tuples)):
        all_tuples[n] = tuple(int(x) for x in all_tuples[n][0].strip('()').split(','))
    
    # Create a matrix with zeros
    M = np.zeros((t[0], 16 * t[2], 16 * t[1]))
    
    nb_block = t[0] * t[1] * t[2]
    
    # Iterate through the blocks
    for n in range(nb_block):
        current_index = all_tuples[n]
        
        # Extract data for each block from the lines
        data = [list(map(int, line.strip().split())) for line in lines[17 * n + 1:17 * (n + 1)]]
        
        matrix = np.array(data)
        
        # Assign the block matrix to the corresponding position in the overall matrix
        M[current_index[0], current_index[2] * 16:current_index[2] * 16 + 16, current_index[1] * 16:current_index[1] * 16 + 16] = matrix
    
        M=M[:,:,8:712]
    
    
    return M





# Uncomment the following lines if you want to execute the functions

# filename = 'input.txt'
# correct_file(filename)
# corrected_file = ''
# matrix = create_matrix(corrected_file)

    




