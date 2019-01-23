# -*- coding: utf-8 -*-

""" 快速排序算法实现
思想： 取一个数作为分割线，将比该数小的数放到前面，把比该数大的数放到后面，然后再对分割后的数组进行递归快排
"""

def quicksort(arr):
    """ 非原地算法 """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

def quick_sort_classic(arr):
    """ 经典随机快排 """


def partition_classic(arr, low, high):
    """ 划分数组 """
            


if __name__== "__main__":
    print(quicksort([10, 4, 6, 7, 96, 8,23]))