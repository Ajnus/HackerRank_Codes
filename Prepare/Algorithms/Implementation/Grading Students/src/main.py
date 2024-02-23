#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    next_mult = 0
    round_grades=[]
    
    for grade in grades:
        next_mult = ((grade//5)+1)*5
        if grade >= 38:
            #for round_grade in round_grades:
            if next_mult-grade < 3:
                round_grades.append(next_mult)
                #print(f"grade: {grade}")
            else:
                round_grades.append(grade)
        else:
            round_grades.append(grade)
                
    return round_grades
            
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
