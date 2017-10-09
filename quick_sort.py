#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:48:44 2017

@author: admin-ygb
"""

def quick_sort(lists, left, right):
    if left >= right:
        return lists
    low = left
    high = right
    key = lists[left]
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left-1)
    quick_sort(lists, left+1, high)
    return lists

if __name__ == '__main__':
    lists = [3,2,4,5,6,1,3,4,6,4]
    print(quick_sort(lists,0,9))


