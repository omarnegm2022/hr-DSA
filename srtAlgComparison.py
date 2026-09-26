#!/bin/python3
QS_time, IS_time = 0, 0


import math
import os
import random
import re
import sys

def insertionSort1(n, arr1):
    global IS_time
    outlier = arr1[-1]
    id = n-1
    while id+1 and arr1[id-1] > outlier:
            arr1[id] = arr1[id-1]
            IS_time += 1; id -= 1
    else:#SyntaxError: 'break' outside loop
        arr1[id] = outlier
        # IS_time += 1
        #TODO: Why not replacing it to while of the comparison? preventing falling with the outer case about 1st itm*
        
        # print(' '.join(list(map(str,arr))))
    
    # if arr[0] == arr[1]:
    #     #in case the outlier occurs only once!
    #     arr[0] = outlier 
    #     IS_time += 1

    # print(' '.join(list(map(str,arr))))
    return arr1

def insertionSort2(n, arr1):
    
    # arr = np.array(arr) if not isinstance(arr, np.ndarray) else arr
    for id in range(1,n):
        arr1[:id+1] = insertionSort1(id+1,arr1[:id+1])
    # print(' '.join(list(map(str,arr))))
    # Write your code here
    
"""
1 + 1 + 
"""

to_print = False
def quickSort1(arr2, mode="In-place", l_ptr = 0, h_ptr = None):
    """SRP: partition logic"""
    if mode == "Copy":
    #global to_print
        if len(arr2) <= 1:
            to_print = True
            return arr2

        pivot = arr2[0]
        # if to_print:
        #     print(arr)
        # vector = np.array(arr)
        left, right = quickSort1([itm for itm in arr2 if itm < pivot]) , quickSort1([itm for itm in arr if itm > pivot])
        merged = left + [itm for itm in arr2 if itm == pivot] + right
        # print(*merged)
        return merged


    else:#In place mode 
        if h_ptr is None:
            h_ptr = len(arr2) - 1
        
        if l_ptr < h_ptr:
            pivot_id = quick_IN_sort2(arr2,l_ptr,h_ptr)
            # print(*arr)

            #dealing with the RHS.
            quickSort1(arr2,"",l_ptr,pivot_id - 1)
            quickSort1(arr2,"",pivot_id + 1, h_ptr)
            #dealing with the RHS.
            

# return (sys.getsizeof([vector[vector < pivot], vector[vector == pivot], vector[vector > pivot]]), sys.getsizeof([itm for itm in arr if itm < pivot] + [itm for itm in arr if itm == pivot] + [itm for itm in arr if itm > pivot]) )

def quick_IN_sort2(arr2,low,high):#_to_srt,original_arr=arr):
    """SRP: sorting logic"""
    global QS_time
    # print(*arr)
    i = low - 1
    pivot = arr2[high]    
    # for phase in ([len(arr)],[len(arr)//2],[len(arr)//2+1,len(arr)]):
    #     i= -1
    #     print("At some point: ",phase[-1],len(arr), *phase)
    #     pivot = arr[phase[-1] + i]
    for j in range(low, high):
        if arr2[j] < pivot:
            i += 1;  QS_time += 1
            arr2[j], arr2[i] = arr2[i], arr2[j]
    \
    arr2[high], arr2[i+1] = arr2[i+1], arr2[high]
    QS_time += 1
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
    n1 = int(input().strip())
    n2 = n1
    arr1 = list(map(int, input().rstrip().split()))
    arr2 = arr1.copy()
    insertionSort2(n1,arr1)
    # result = quickSort(arr)
    quickSort1(arr2)
print(IS_time - QS_time)
