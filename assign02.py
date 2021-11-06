"""
Assign 02 - <INSERT YOUR NAME HERE>

Directions:
    * Complete the sorting algorithm functions that are given below. Note that
      it okay (and probably helpful) to define auxiliary/helper functions that
      are called from the functions below.  Refer to the README.md file for
      additional info.

    * NOTE: Remember to add a docstring for each function, and that a reasonable
      coding style is followed (e.g. blank lines between functions).
      Your program will not pass the tests if this is not done!

    * Be sure that you implement your own sorting functions since.
      No credit will be given if Python's built-in sort function is used.
"""

import time
import random
import sys
from math import ceil, log10

# Set recursion limit to be greater than the max size of any list you attempt to sort
sys.setrecursionlimit(10000)


def bubbleSort(list_of_items):
    """Bubble sort"""
    start_time = time.time()

    # INSERT YOUR BUBBLE SORT CODE HERE
    n = len(list_of_items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_of_items[j] > list_of_items[j + 1]:
                list_of_items[j], list_of_items[j + 1] = list_of_items[j + 1], list_of_items[j]

    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def merge_by_3(arr, start, mid1, mid2, end):
    """Merge by three"""
    left_array = arr[start - 1: mid1]
    mid_array = arr[mid1: mid2 + 1]
    right_array = arr[mid2 + 1: end]

    left_array.append(float('inf'))
    mid_array.append(float('inf'))
    right_array.append(float('inf'))
    ind_left = 0
    ind_mid = 0
    ind_right = 0
    for i in range(start - 1, end):
        minimum = min([left_array[ind_left], mid_array[ind_mid], right_array[ind_right]])
        if minimum == left_array[ind_left]:
            arr[i] = left_array[ind_left]
            ind_left += 1
        elif minimum == mid_array[ind_mid]:
            arr[i] = mid_array[ind_mid]
            ind_mid += 1
        else:
            arr[i] = right_array[ind_right]
            ind_right += 1


def merge_sort_3(arr, start, end):
    """Second merge sort"""
    if len(arr[start - 1: end]) < 2:
        return arr
    else:
        mid1 = start + ((end - start) // 3)
        mid2 = start + 2 * ((end - start) // 3)
        merge_sort_3(arr, start, mid1)
        merge_sort_3(arr, mid1 + 1, mid2 + 1)
        merge_sort_3(arr, mid2 + 2, end)
        merge_by_3(arr, start, mid1, mid2, end)
        return arr


def mergeSort(list_of_items, split_by_3=False):
    """Merge sort main"""
    start_time = time.time()
    # INSERT YOUR MERGE SORT CODE HERE...
    # * SPLITTING BY 2 WHEN split_by_3 = False
    # * SPLITTING BY 3 WHEN split_by_3 = True
    # * RETURNING A LIST OF LISTS WHEN split_by_3 = False
    if split_by_3:
        list_of_items = merge_sort_3(list_of_items, 1, len(list_of_items))
    else:
        if len(list_of_items) > 1:
            mid = len(list_of_items) // 2
            L = list_of_items[:mid]
            R = list_of_items[mid:]
            mergeSort(L, split_by_3)
            mergeSort(R, split_by_3)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    list_of_items[k] = L[i]
                    i += 1
                else:
                    list_of_items[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                list_of_items[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                list_of_items[k] = R[j]
                j += 1
                k += 1

    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def quickSort(list_of_items, pivot_to_use='first'):
    """Quick Sort"""
    start_time = time.time()
    # https://www.geeksforgeeks.org/quick-sort/
    # INSERT YOUR QUICK SORT CODE HERE...
    # * USING FIRST ITEM IN THE LIST AS THE PIVOT WHEN pivot_to_use = 'first'
    # * USING MIDDLE ITEM IN THE LIST AS THE PIVOT WHEN pivot_to_use != 'first'
    # AND BE SURE THAT CONTINUES FOR SUBSEQUENT/RECURSIVE CALLS AS WELL
    quick_sort(list_of_items, 0, len(list_of_items) - 1, pivot_to_use)
    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def partition(arr, start, end, pivot_mode):
    """Partition Sort"""
    if pivot_mode == 'first':
        pivot = arr[start]
    else:
        pivot_index = (start + end) // 2
        pivot = arr[pivot_index]
        arr[pivot_index], arr[start] = arr[start], arr[pivot_index]
    i = start + 1
    for j in range(start + 1, end + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[start], arr[i - 1] = arr[i - 1], arr[start]
    return i - 1


def quick_sort(arr, start, end, pivot_mode='middle'):
    """Middle Sort"""
    if start < end:
        split = partition(arr, start, end, pivot_mode)
        quick_sort(arr, start, split - 1, pivot_mode)
        quick_sort(arr, split + 1, end, pivot_mode)
        return arr


def radixSort(list_of_items, max_digits):
    """Radix Sort"""
    start_time = time.time()
    RADIX = 10
    placement = 1
    max_digit = max(list_of_items)
    # INSERT YOUR RADIX SORT CODE HERE
    # https://www.w3resource.com/
    while placement < max_digit:
      buckets = [list() for _ in range(RADIX)]
      for i in list_of_items:
        tmp = int((i / placement) % RADIX)
        buckets[tmp].append(i)
      a = 0
      for b in range(RADIX):
        buck = buckets[b]
        for i in buck:
          list_of_items[a] = i
          a += 1
      placement *= RADIX
    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def assign02_main():
    """ A 'main' function to be run when our program is run standalone """
    list1 = list(range(5000))
    random.seed(1)
    random.shuffle(list1)

    # list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20] # helpful for early testing

    # run sorting functions
    bubbleRes = bubbleSort(list(list1))
    mergeRes2 = mergeSort(list(list1), split_by_3=False)
    mergeRes3 = mergeSort(list(list1), split_by_3=True)
    quickResA = quickSort(list(list1), pivot_to_use='first')
    quickResB = quickSort(list(list1), pivot_to_use='middle')
    radixRes = radixSort(list(list1), ceil(log10(max(list1))))

    # Print results
    print(f"\nlist1 results (randomly shuffled w/ size = {len(list1)})")
    print(list1[:10])
    print(f"  bubbleSort time: {bubbleRes[1]:.4f} sec")
    print(bubbleRes[0][:10])
    print(f"  mergeSort2 time: {mergeRes2[1]:.4f} sec")
    print(mergeRes2[0][:10])
    print(f"  mergeSort3 time: {mergeRes3[1]:.4f} sec")
    print(mergeRes3[0][:10])
    print(f"  quickSortA time: {quickResA[1]:.4f} sec")
    print(quickResA[0][:10])
    print(f"  quickSortB time: {quickResB[1]:.4f} sec")
    print(quickResB[0][:10])
    print(f"  radixSort time: {radixRes[1]:.4f} sec")
    print(radixRes[0][:10])

    # Try with a list sorted in reverse order (worst case for quicksort)
    list2 = list(range(6000, 1000, -1))

    # run sorting functions
    bubbleRes = bubbleSort(list(list2))
    mergeRes2 = mergeSort(list(list2), split_by_3=False)
    mergeRes3 = mergeSort(list(list2), split_by_3=True)
    quickResA = quickSort(list(list2), pivot_to_use='first')
    quickResB = quickSort(list(list2), pivot_to_use='middle')
    radixRes = radixSort(list(list2), ceil(log10(max(list2))))

    # Print results
    print(f"\nlist2 results (sorted in reverse w/ size = {len(list2)})")
    print(list2[:10])
    print(f"  bubbleSort time: {bubbleRes[1]:.4f} sec")
    print(bubbleRes[0][:10])
    print(f"  mergeSort2 time: {mergeRes2[1]:.4f} sec")
    print(mergeRes2[0][:10])
    print(f"  mergeSort3 time: {mergeRes3[1]:.4f} sec")
    print(mergeRes3[0][:10])
    print(f"  quickSortA time: {quickResA[1]:.4f} sec")
    print(quickResA[0][:10])
    print(f"  quickSortB time: {quickResB[1]:.4f} sec")
    print(quickResB[0][:10])
    print(f"  radixSort time: {radixRes[1]:.4f} sec")
    print(radixRes[0][:10])


# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    assign02_main()
