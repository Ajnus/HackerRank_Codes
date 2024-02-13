#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(n):
    spaces = n-1
    sharps = 1

    i = 0
    while i < n:
        j = 0
        k = 0
        while j < spaces:
            print(" ", end="")
            j += 1
        while k < sharps:
            print("#", end="")
            k += 1

        print("")
        spaces -= 1
        sharps += 1
        i += 1


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
