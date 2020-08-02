#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    count_bird = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(arr)):
        count_bird[arr[i]] += 1

    max_value = max(count_bird)
    max_index = []
    for i in range(len(count_bird)):
        if count_bird[i] == max_value:
            max_index.append(i)

    return max_index[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
