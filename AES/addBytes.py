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
    """
    byteA and byteB are hexadecimal strings of the form '0x--'
    """
    #1) convert the operands from str to int (drop '0x' prefix)
    tempA = int(byteA[2:],16)
    tempB = int(byteB[2:],16)

    #2) Add the operands as ints
    tempSum = tempA + tempB
    
    #TO DO: If output is less than 16, then format it to be two hex chars"
    #3) Convert the sum back into a hex string
    if tempSum < 16:
        tempSumHex = hex(tempSum)
        tempSumHex = tempSumHex[0:2] + '0' + tempSumHex[2:]
        return tempSumHex
    else:
        return hex(tempSum)

# Use main() as a test harness / unit test. 
def main():
    operand1 = '0x01'
    operand2 = '0x0A'
    result = addBytes(operand1,operand2)
    print('0x01 + 0x0A = {0}'.format(result))
    

if __name__ == '__main__':
    main()