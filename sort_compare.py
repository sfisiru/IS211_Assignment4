import random
import time


def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value


def shellSort(alist):
    sublistcount = len(alist) // 2

    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


def python_sort(a_list):
    return sorted(a_list)


if __name__ == "__main__":

    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:

        total_insertion = 0
        total_shell = 0
        total_python = 0

        for i in range(100):

            mylist = get_me_random_list(the_size)

            list_copy = mylist.copy()
            start = time.time()
            insertion_sort(list_copy)
            total_insertion += time.time() - start

            list_copy = mylist.copy()
            start = time.time()
            shellSort(list_copy)
            total_shell += time.time() - start

            list_copy = mylist.copy()
            start = time.time()
            python_sort(list_copy)
            total_python += time.time() - start

        print(f"\nList Size: {the_size}")
        print(f"Insertion Sort took {total_insertion/100:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Shell Sort took {total_shell/100:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Python Sort took {total_python/100:10.7f} seconds to run, on average for a list of {the_size} elements")