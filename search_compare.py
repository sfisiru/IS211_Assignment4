import time
import random


def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


if __name__ == "__main__":

    list_sizes = [500, 1000, 5000]
    target = 99999999

    for the_size in list_sizes:

        total_seq = 0
        total_ord = 0
        total_bin_iter = 0
        total_bin_rec = 0

        for i in range(100):

            mylist = get_me_random_list(the_size)

            start = time.time()
            sequential_search(mylist, target)
            total_seq += time.time() - start

            mylist_sorted = sorted(mylist)

            start = time.time()
            ordered_sequential_search(mylist_sorted, target)
            total_ord += time.time() - start

            start = time.time()
            binary_search_iterative(mylist_sorted, target)
            total_bin_iter += time.time() - start

            start = time.time()
            binary_search_recursive(mylist_sorted, target)
            total_bin_rec += time.time() - start

        print(f"\nList Size: {the_size}")
        print(f"Sequential Search took {total_seq/100:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Ordered Sequential Search took {total_ord/100:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Binary Search Iterative took {total_bin_iter/100:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Binary Search Recursive took {total_bin_rec/100:10.7f} seconds to run, on average for a list of {the_size} elements")