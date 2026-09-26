import numpy #as np

def mod_BubbleSort(usr_lst):
    """Uses modulo with one loop of O(n**2) iterations."""
    # vectorized_lst = np.array(usr_lst*2).reshape(2,len(usr_lst))
    # empty_arr = np.zeros(vectorized_lst.size)
    vectorized_lst = np.array(usr_lst)

    iters = len(vectorized_lst)-1
    no_exchange = True
    for j in range(iters**2):
        real_j = j%iters
        if vectorized_lst[(real_j)] > vectorized_lst[(real_j)+1]:
            no_exchange = False
            vectorized_lst[(real_j)], vectorized_lst[(real_j)+1] = vectorized_lst[(real_j)+1], vectorized_lst[(real_j)]
        if j:
            if j%iters == 0 and no_exchange:
                print("Sorted at position: {0}, iteration: {1}.".format(j%iters,j))
                break
            # else:
            #     no_exchange = True
        else:
            no_exchange = True

        # if not any_exhcange:

    print(vectorized_lst)

# print(np.array([1,2,3,4]*2).reshape(2,4))
mod_BubbleSort([1,5,3,2,4])

def ExchangeSort(usr_lst):
    """out of CCE tanta scope."""
    vectorized_lst = np.array(usr_lst)
    N = len(vectorized_lst)
    n_of_is = 0
    for outer_id in range(N):
        for inner_id in range(outer_id, N):
            n_of_is += 1
            if vectorized_lst[inner_id] > vectorized_lst[outer_id]:
                vectorized_lst[inner_id], vectorized_lst[outer_id] = vectorized_lst[outer_id], vectorized_lst[inner_id]
    print(vectorized_lst)

ExchangeSort([1,2,5,3,4])

def SelectionSort(usr_lst):
    """
Feedback on min() and expected_min_value
min() is redundant and slow here: Finding the minimum value using Python's min(), and then searching the array again to find its index using np.where(), performs two separate passes over the data.

expected_min_value comparison: Checking if expected_min_value != min_value is a good effort to avoid unnecessary self-swaps. However, in sorting algorithms, it is better practice to compare indices (if min_id != outer_id:) rather than values, as index comparisons are faster and immune to duplicate-value logic errors.
"""
    vectorized_lst = np.array(usr_lst)
    N = len(vectorized_lst)
    n_of_is = 0
    for outer_id in range(N):
        expected_min_value = vectorized_lst[outer_id]
        min_value = min(vectorized_lst[outer_id:N])
        min_id = np.where(vectorized_lst == min_value)[0][0]
        if expected_min_value != min_value:
            n_of_is += 1
            vectorized_lst[outer_id], vectorized_lst[min_id] = vectorized_lst[min_id], vectorized_lst[outer_id]


    print(vectorized_lst);print(n_of_is)

def improved_sel_srt(usr_lst):
    """# Key Improvements
Bug-free: Slicing inside np.argmin ensures you only search the unsorted right side of the array.
Speed: np.argmin finds the index in a single $O(K)$ pass rather than doing $O(K)$ for min() plus $O(N)$ for np.where().
Index Comparison: min_id != outer_id cleanly skips self-swaps without checking value equality."""
    vectorized_lst = np.array(usr_lst)
    N = len(vectorized_lst)
    n_of_is = 0
    for outer_id in range(N-1):
        # expected_min_value = vectorized_lst[outer_id]
        # min_value = min(vectorized_lst[outer_id:N])
        min_id = vectorized_lst[outer_id:N].argmin() + outer_id
        if outer_id != min_id:
            n_of_is += 1
            vectorized_lst[outer_id], vectorized_lst[min_id] = vectorized_lst[min_id], vectorized_lst[outer_id]


    print(vectorized_lst, n_of_is)
    return vectorized_lst

improved_sel_srt([2,5,4,2])


result = 0

def listsum(aList):
    return aList[0]

aList = [1,3,5,7,9]
while len(aList):
    result += listsum(aList)

    aList = aList[1:]
print(result)

def MergeSort(usr_lst: list(int)):
    ls_len= len(usr_lst); #pivot_item = None
    #if ls_len % 2:
    pivot_item = usr_lst.pop(ls_len//2) if ls_len % 2 else None

    usr_lst = np.array(usr_lst).reshape(len(usr_lst)//2,2)
    # ls_len = usr_lst.size
    # enumerate([(i,j) from i,j in usr_lst])
    # if usr_lst.size:
        # MergeSort(usr_lst[:])
    LHS, RHS = [], []
    for pair in usr_lst:
        if pair[0] > pair[1]:
            pair[0], pair[1] = pair[1], pair[0]
        LHS.append(int(pair[0])); RHS.append(int(pair[1]))

    semi_sorted_list = [pivot_item] + LHS + RHS if pivot_item < LHS[-1] else LHS + RHS + [pivot_item] if pivot_item > RHS[0] else LHS + [pivot_item] + RHS

    print(semi_sorted_list)

# print(np.array([[1,2],[3,4]]).reshape(1,4))
MergeSort([3,4,6,7,2,5,1])

def InsSort(usr_lst):

    for p_id in range(1,len(usr_lst)):
        position, current_val = p_id, usr_lst[p_id];
        try:
            while (usr_lst[position-1] > current_val):# and position > 0:
                usr_lst[position] = usr_lst[position-1]; position -= 1
            print((usr_lst[position-1] > current_val), position > 0)
            usr_lst[position] = current_val
        except IndexError:
            break

        print(usr_lst)


InsSort([54,26,93,17,77,31,44,55,20])
