#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    i = 0
    j = 0
    diagleft = 0
    diagright = 0

    while i < n:
        diagleft += arr[i][i]
        i += 1
    while j < n:
        print(f"n: {n}")
        print(f"j: {j}")
        diagright += arr[n-1-j][j]
        j += 1

    return abs(diagleft-diagright)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
