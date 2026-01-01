# -*- coding: utf-8 -*-
"""

This function implements a left circular shift of a four-element list. The
four-element list represents a row in the State array. 

"""
def circularShiftLeft(row, shiftAmount):
    """
    Shift [row] in the State array by an int [shiftAmount]
    """
    # Initialize an empty list to store the result
    result = [''] * 4
    
    # Use modular arithmetic to determine the index for the shift
    for element in range(len(row)):
        index = (element - shiftAmount) % len(row)
        result[index] = row[element]
    
    return result

def main():
    row_from_State = ['0x1', '0x2', '0x3', '0x4']
    print('Input:\t\t{}'.format(row_from_State))
    print('Performing circular shift to the left by one...')
    print('Output\t\t{}'.format(circularShiftLeft(row_from_State, 1)))

if __name__ == '__main__':
    main()