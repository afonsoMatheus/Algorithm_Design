#!/usr/bin/env python
# coding: utf-8

def merge_sort(array, start, end):
    
    mid = 0
    
    if(start < end):
        
        mid = (start + end)//2
        merge_sort(array, start, mid)
        merge_sort(array, mid+1, end)
        intercalate(array, start, mid, end)

def intercalate(array, start, mid, end):
        
    L = []
    R = []
    
    n1 = mid - start + 1
    n2 = end - mid
    
    for i in range(n1):
        L.append(array[start+i])
    L.append(9999)
        
    for i in range(n2):
        R.append(array[mid+i+1])
    R.append(9999)
        
    i = 0
    j = 0
    for k in range(start, end + 1):
        
        if(L[i] <= R[j]):
            array[k] = L[i]
            i = i + 1
        else:
            array[k] = R[j]
            j = j + 1           





