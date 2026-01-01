# -*- coding: utf-8 -*-
"""
Adding bytes in bytearray() data types

This goal of this script is to explore how to perform arithmetic opertions on
bytes. This will be used to perform addition and multiplication of poly-
nomials that are elements of the finite field GF(2^8)

str sum = addBytes(str byteA, str byteB)
operands are represented as '0x' followed by two hex characters

"""
def addBytes(byteA, byteB):
    #1) convert the operands from str to int (drop '0x' prefix)
    tempA = int(byteA[2:])
    tempB = int(byteB[2:])

    #2) Add the operands as ints
    tempSum = tempA + tempB
    
    #3) Convert the sum back into a hex string
    hex()
