#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    lowest = highest = scores[0]
    break_lowest=0
    break_highest=0
    records=[]
    
    for score in scores:
        if score > highest:
            highest = score
            break_highest+=1
        if score < lowest:
            lowest = score
            break_lowest+=1

    print(highest)
    print(lowest)
    
    records.append(break_highest)
    records.append(break_lowest)
    
    return records

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
