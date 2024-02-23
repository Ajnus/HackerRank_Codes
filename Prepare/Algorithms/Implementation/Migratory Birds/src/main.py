#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    bird_dict = {}
    max_bird_count = 0
    
    for bird in arr:
        bird_dict[bird] = bird_dict.get(bird, 0) + 1
        
    max_bird_count = max(bird_dict.values())

    max_birds = [chave for chave, valor in bird_dict.items() if valor == max_bird_count]

    print("Maior valor:", max_bird_count)
    print("Chaves correspondentes:", max_birds)
    
    return min(max_birds)
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
