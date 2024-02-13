#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    max = arr[0]
    min = arr[len(arr)-1]
    sum = 0

    for el in arr:
        sum += el
        if el > max:
            max = el
        if el < min:
            min = el

    print(sum-max, end=" ")
    print(sum-min)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
