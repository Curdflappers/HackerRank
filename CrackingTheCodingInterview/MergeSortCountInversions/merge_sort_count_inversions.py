#!/bin/python3

import sys

def countInversions(a):
    return merge_sort(a, a[:], 0, len(a) - 1)
    
def merge_sort(a, temp, left_start, right_end):
    if left_start >= right_end:
        return 0
    
    mid = int((left_start + right_end) / 2)
    
    return merge_sort(a, temp, left_start, mid) \
    + merge_sort(a, temp, mid + 1, right_end) \
    + merge_halves(a, temp, left_start, right_end)
    
def merge_halves(a, temp, left_start, right_end):
    left_end = int((left_start + right_end) / 2)
    right_start = left_end + 1
    swaps = 0
    size = right_end - left_start + 1
    
    # sort the halves into temp
    left = left_start
    right = right_start
    i = left_start
    
    while left <= left_end and right <= right_end:
        if a[left] <= a[right]:
            temp[i] = a[left]
            left += 1
        else:
            temp[i] = a[right]
            swaps += right - i
            right += 1
        i += 1
        
    if left > left_end:
        for index in range(right, right_end + 1):
            temp[i] = a[index]
            i += 1
    else:
        for index in range(left, left_end + 1):
            temp[i] = a[index]
            i += 1
            
    # copy sorted temp into array
    for index in range(left_start, left_start + size):
        a[index] = temp[index]
        
    #print(swaps)
    return swaps

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)
