#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    res = 0
    counts = [0]*(len(arr)+1)
    rank = { v : i+1 for i, v in enumerate(sorted(arr)) }
    for x in reversed(arr):
        i = rank[x] - 1
        while i:
            res += counts[i]
            i -= i & -i
        i = rank[x]
        while i <= len(arr):
            counts[i] += 1
            i += i & -i
    return res


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         arr = list(map(int, input().rstrip().split()))

#         result = countInversions(arr)

#         fptr.write(str(result) + '\n')

#     fptr.close()



arr = [83, 70, 82, 44, 34, 98, 73, 22, 100, 18, 6, 90, 8, 65, 88, 59]
print(arr)
print(countInversions(arr))
