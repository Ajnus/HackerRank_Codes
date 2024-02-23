#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    period = s[-2:]
    hour = s[:2]
    hour_int = int(hour)
    
    if period == 'AM':
        s = s[:-2]
        if hour == '12':
            hour = '00'
            print(hour)
            s = hour+s[2:]
            
    
    elif period == 'PM':
        if hour != '12':
            hour_int+=12
        hour = str(hour_int)
        s = hour+s[2:-2]
        
    return s
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
