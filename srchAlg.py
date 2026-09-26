from srtAlg import improved_sel_srt

import numpy as np
import sys
#To disable this behaviour and force NumPy to print the entire array, you can change the printing options using set_printoptions.

np.set_printoptions(threshold=sys.maxsize) # sys module should be imported
#print(         )
np.arange(10000)

def NumSeqSrch(usr_lst, item):
    """"""
    vectorized_list = np.array( usr_lst.split(",")
                                )#end of array conversion
    print(vectorized_list)
    if item in vectorized_list:
        return True
    else:
        return False

def NumBinSrch(usr_lst, item):
    """
1. The Core Flaw: Array Slicing (O(N) Overhead)
When you write usr_lst[:mid_index] or usr_lst[mid_index:], Python creates a brand-new copy of that slice in memory.
Time Complexity: Copying K elements takes O(K) time. Because you copy half the list on every recursive step, your binary search time complexity degrades from O(log N) down to O(N).
Space Complexity: Creating array slices allocates new memory on every step, spiking space complexity from O(1) to O(N).

4. Recursive vs. Iterative Binary Search
Aspect,Recursive Binary Search,Iterative Binary Search (while loop)
Time Complexity,O(logN),O(logN)
Space Complexity,O(logN) (Call Stack frames),O(1) (Constant space)
Call Stack Risk,Minor risk of stack overflow on huge inputs,None
DSA Verdict,Great for teaching Divide & Conquer,Preferred in production/interviews
"""
    if type(usr_lst) is str:
        usr_lst = np.array(
                                improved_sel_srt(list(
                                    map(lambda x: int(x),usr_lst.split(",")
                                        )#end of map process
                                            )#end of list wrapping
                                    )#end of sorting
                            )
    print(f"dd: {usr_lst}")
    mid_index = usr_lst.size//2
    mid_itm = usr_lst[mid_index]
    print(f"mid: {mid_itm}")
    if item == mid_itm:
        return True
    elif len(usr_lst)-1:
        if item < mid_itm:
            return            NumBinSrch(usr_lst[:mid_index],item)
        else:
            return            NumBinSrch(usr_lst[mid_index:],item)
    return False

# try:
print(
    NumBinSrch("10,51,2,18,4,31,13,5,23,64,29",int(input("Enter your number: "))))
# except RecursionError:
    # print(False)
