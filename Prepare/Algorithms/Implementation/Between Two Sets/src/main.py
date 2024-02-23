#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    i=max(a)
    mod_zero={}
    count=0
    
    while i <= min(b):
        for el in a:
            if i % el == 0:
                mod_zero[i] = mod_zero.setdefault(i, 0) + 1
                
        for el in b:
            if el % i == 0:
                mod_zero[i] = mod_zero.setdefault(i, 1) + 1
                
        i+=1
        
    for valor in mod_zero.values():
            #print(f"{chave}: {valor}")
            #print(n+m)
            if valor == n+m:
                count+=1
        
    for chave, valor in mod_zero.items():
            print(f"{chave}: {valor}")
        
    print(f"count: {count}")
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
