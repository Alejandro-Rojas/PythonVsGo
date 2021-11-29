import time
import random
import sys
from math import ceil, log10

from matplotlib import pyplot as plt

# Set recursion limit to be greter than the max size of any list you attempt to sort
sys.setrecursionlimit(10000)


def bubbleSort(list_of_items):
    """Bubble sort"""
    start_time = time.time()
    n = len(list_of_items)
    for i in range(n):
        for j in range(n - i - 1):
            if list_of_items[j] > list_of_items[j + 1]:
                list_of_items[j], list_of_items[j + 1] = list_of_items[j + 1], list_of_items[j]
    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def radixSort(list_of_items, max_digits):
    """Radix Sort"""
    start_time = time.time()
    RADIX = 10
    placement = 1
    max_digit = max(list_of_items)
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
    # Try with a list sorted in reverse order (worst case for quicksort)
    list2 = list(range(0, 50000, 10))

    # run sorting functions
    bubbleRes = bubbleSort(list(list2))
    radixRes = radixSort(list(list2), ceil(log10(max(list2))))

    # Print results
    print(f"\nlist2 results (sorted in reverse w/ size = {len(list2)})")
    print(list2[:10])
    print(f"  bubbleSort time: {bubbleRes[1]:.4f} sec")
    print(bubbleRes[0][:10])
    print(f"  radixSort time: {radixRes[1]:.4f} sec")
    print(radixRes[0][:10])




# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    assign02_main()
