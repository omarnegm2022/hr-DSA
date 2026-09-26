#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'introTutorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER V
#  2. INTEGER_ARRAY arr
#

def introTutorial(V, arr):
    return arr.index(V)
    # Write your code here

if False:#__name__ == '__main__':

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    print(str(result) + '\n')

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    global IS_time
    outlier = arr[-1]
    id = n-1
    while id+1 and arr[id-1] > outlier:
            arr[id] = arr[id-1]
            IS_time += 1; id -= 1
    else:#SyntaxError: 'break' outside loop
        arr[id] = outlier
        # IS_time += 1
        #TODO: Why not replacing it to while of the comparison? preventing falling with the outer case about 1st itm*
        
        # print(' '.join(list(map(str,arr))))
    
    # if arr[0] == arr[1]:
    #     #in case the outlier occurs only once!
    #     arr[0] = outlier 
    #     IS_time += 1

    # print(' '.join(list(map(str,arr))))
    # return arr

def insertionSort2(n, arr):
    """
# 🔍 **Why** This Works Better Than Standard Python Lists

1. In-Place Mutation: arr[:id+1] in NumPy is a zero-copy view. When insertionSort1 mutates arr[i] = arr[i-1], it edits the exact memory space of the main data array directly.


2. No Re-Assignment Needed: You don't need arr[:id+1] = insertionSort1(...) because the view already alters the main array directly.

3. Identical HackerRank Output: It maintains the strict step-by-step printing required by competitive programming platforms while cleanly separating the sub-task function.

   # 💡 The Key NumPy Difference: Views vs. Copies
When you slice a regular Python list (arr[:id+1]), Python creates a copy in memory. Passing that slice into insertionSort1 modifies the copy, leaving arr untouched unless re-assigned.

In NumPy, slicing an array (arr[:id+1]) returns a view into the same memory buffer. Any mutation made inside insertionSort1 automatically reflects in the original array arr!
    """
    arr = np.array(arr) if not isinstance(arr, np.ndarray) else arr
    for id in range(1,n):
        insertionSort1(id+1,arr[:id+1])
    print(' '.join(list(map(str,arr))))
    # Write your code here

if False:#__name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    # insertionSort1(n, arr)
    insertionSort2(n,arr)
"""
1 + 1 + 
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
to_print = False
def quickSort1(arr, mode="In-place", l_ptr = 0, h_ptr = None):
    """SRP: partition logic"""
    if mode == "Copy":
    #global to_print
        if len(arr) <= 1:
            to_print = True
            return arr

        pivot = arr[0]
        # if to_print:
        #     print(arr)
        # vector = np.array(arr)
        left, right = quickSort([itm for itm in arr if itm < pivot]) , quickSort([itm for itm in arr if itm > pivot])
        merged = left + [itm for itm in arr if itm == pivot] + right
        print(*merged)
        return merged


    else:#In place mode 
        if h_ptr is None:
            h_ptr = len(arr) - 1
        
        if l_ptr < h_ptr:
            pivot_id = quick_IN_sort2(arr,l_ptr,h_ptr)
            print(*arr)

            #dealing with the RHS.
            quickSort1(arr,"",l_ptr,pivot_id - 1)
            quickSort1(arr,"",pivot_id + 1, h_ptr)
            #dealing with the RHS.
            

# return (sys.getsizeof([vector[vector < pivot], vector[vector == pivot], vector[vector > pivot]]), sys.getsizeof([itm for itm in arr if itm < pivot] + [itm for itm in arr if itm == pivot] + [itm for itm in arr if itm > pivot]) )

def quick_IN_sort2(arr,low,high):#_to_srt,original_arr=arr):
    """SRP: sorting logic"""
    # print(*arr)
    i = low - 1
    pivot = arr[high]    
    # for phase in ([len(arr)],[len(arr)//2],[len(arr)//2+1,len(arr)]):
    #     i= -1
    #     print("At some point: ",phase[-1],len(arr), *phase)
    #     pivot = arr[phase[-1] + i]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1;  
            arr[j], arr[i] = arr[i], arr[j]
    \
    arr[high], arr[i+1] = arr[i+1], arr[high]
    return i + 1
    # right, left = [], []
    # if m == n:
        # right = quick_IN_sort(arr[:n//2]);left = quick_IN_sort(arr[n//2:])
    # else:
        # return arr
    # yield from right + left

# def countingSort(arr):
    # return np.array([arr.count(i) for i in range(len(set(arr))) if 0 <= i < n])

if __name__ == '__main__':
    # import srchApp
    #TODO srchApp. _likewise_
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    # result = quickSort(arr)
    quickSort1(arr)