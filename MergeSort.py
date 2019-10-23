#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:17:57 2019

@author: WillCase
"""
def mergeSort(alist):#invoking merge sort function
    print("Splitting ",alist)
    if len(alist)>1: #splits list into first half
        mid = len(alist)//2 #splits list inot second half
        lefthalf = alist[:mid] #assign new list name for left half
        righthalf = alist[mid:] #assign new list name for right half

        mergeSort(lefthalf) 
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20] #unsorted list 
mergeSort(alist) #merge sort list alist
print(alist) #print sorted list

