#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    number_of_pairs = 0
    print(f"n: {n}")
    print(f"k: {k}")
    
    if not ar:
        return 0
    
    i=0
    while i < n:
        j=i+1
        while j < n:
            soma = ar[i] + ar[j]
            print(f"i: {i}")
            print(f"j: {j}")
            print(f"soma: {soma}")
            
            if soma % k == 0:
                number_of_pairs+=1
            j+=1
        i+=1
                    
    return number_of_pairs
            
        

        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
