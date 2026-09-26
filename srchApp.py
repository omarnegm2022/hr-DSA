#!/bin/python3

import math
import numpy as np
import os

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    assert len(arr) == n; assert len(brr) == m
    diff_numbs = []
    if n <= m and (max(brr) - min(brr))<=100:
        return sorted(set([num for num in brr if (arr.count(num) < brr.count(num))]))
        for num in set(brr):
            if (arr.count(num)<brr.count(num)):
                diff_numbs
    return None
        

    # Write your code here

# if __name__ == '__main__':

#     n = int(input("arr length: ").strip())

#     arr = np.random.randint(1, 101, size=n)   #.tolist()

#     m = int(input("brr length: ").strip())

#     brr = np.random.randint(1, 101, size=m)

#     result = missingNumbers(arr, brr)
#     print(arr,'\n', brr)
#     print(' '.join(map(str, result)))

#!/bin/python3
np.linalg.solve()
import math
import os
import random
import re
import sys
import timeit
import time
#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def balancedSums(arr):
    for itm_id in range(1,len(arr)-1):
        if sum(arr[:itm_id]) == sum(arr[itm_id+1:]):
            return "yes".capitalize()
    return "no".capitalize()
# Write your code here

# if __name__ == '__main__':
    # """TIME LIMIT EXCEEDED!"""
    # start = time.time()
    # T = 2#int(input().strip())
# 
    # for T_itr in range(T):
        # n = 3#int(input().strip())
# 
        # arr = [1,2,3]#list(map(int, input().rstrip().split()))
# 
        # result = balancedSums(arr)
        # print(result)
    # print(time.time() - start)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

# def chessboardGenerator(n):
    # for i in range(n):
        # for j in range(n):
            

def knightlOnAChessboard(n):
    import numpy as np    # Write your code here
    the_board = np.array([(i, j) for i in range(n) for j in range(n)])#NOTE: .reshape(n,n) is done inherently
    print(the_board)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    # fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    # fptr.write('\n')

    # fptr.close()
