#!/usr/bin/env pythonn3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Author:   Muhammad Wada
# Date:     Thu 25 Nov 2021
# Version:  0.1
# ----------------------------------------------------------------------------
def SubBytes(State):
    """
    SubBytes(State)
    
    Perform byte substitution on each byte of the State array
    
    State is a 4 x 4 byte array represented as a 4 x 4 list 
    
    Each byte of State is a hexadecimal string of the form '0x--', whereby '--' represents two hexadecimal characters
    """
    # ----------------------------------------------------------------------------
    # Imports
    # ----------------------------------------------------------------------------
    from S_Box import S_Box
    
    for row in range(len(State)):
        for column in range(len(State[row])):
            key = State[row][column][2:]
            State[row][column] = '0x' + S_Box[key]
            
    return State
    
# Use main() as a test harness / unit test. 
def main():
    State = [
        ['0x00', '0x01', '0x02', '0x03'],
        ['0x04', '0x05', '0x06', '0x07'],
        ['0x08', '0x09', '0x0A', '0x0B'],
        ['0x0C', '0x0D', '0x0E', '0x0F']]
    
    print('Input:')
    for row in range(len(State)):
        print(State[row])
    
    print('')
    print('Output:')
    State = SubBytes(State)
    for row in range(len(State)):
        print(State[row])

if __name__ == '__main__':
    main()