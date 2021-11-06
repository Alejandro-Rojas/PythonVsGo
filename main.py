import time
import random
import sys


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


def main():
    array = array(range(5000))    
    random.seed(1)
    random.shuffle(list1)




    if __name__ == '__main__':
        main()
