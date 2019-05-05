#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math as mt


# In[4]:


'''
Class that implements a binary heap
Functions are: insert, delete.
'''

class binheap:
    
    def __init__(self):
        self.heap = []
        self.size = 0
        
    '''
    insert and bot_up are functions that adds an element and sort the list 
    with a botton up approach that maintains the heap priority feature.
    ''' 
    
    
    #Args i, int
    #Ret None; rearrange the heap with a botton up approach
    def bot_up(self, i):
                
        while (i//2 > 0):
            if (self.heap[i-1] < self.heap[(i//2)-1]):
                tmp = self.heap[(i//2)-1]
                self.heap[(i//2)-1] = self.heap[i-1]
                self.heap[i-1] = tmp
            i = i//2
    
    #Args key, int
    #Ret None; adds the new element in the heap
    def insert(self, key):
        
        self.heap.append(key)
        self.size = self.size + 1
        self.bot_up(self.size)
        
    '''
    delete, top_down and get_min are functions that removes and 
    returns the first element of the heap and replace it with the 
    final item of the heap, maintaining the heap priority feature with a 
    top down approach.
    '''    
    #Args i, int
    #Ret None; rearrange the heap with a top down approach
    def top_down(self, i):
        while (i * 2 < self.size - 1):
            min_ind = self.get_min(i)
            if self.heap[i] > self.heap[min_ind]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[min_ind]
                self.heap[min_ind] = tmp
            i = min_ind
            
    #Args i, int
    #Ret int; an index of the minimal key value in the heap        
    def get_min(self,i):
        if (i * 2 + 2 > self.size - 1):
            return i*2 + 1
        else:
            if self.heap[i*2 + 1] < self.heap[(i*2)+2]:
                return i * 2 + 1
            else:
                return i * 2 + 2
    
    #Args None
    #Ret int; the removed item from the heap
    def delete(self):
        remov = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size = self.size - 1
        self.heap.pop()
        self.top_down(0)
        return remov
    
    '''
    get_fat and get_sons are auxiliary function to see the father and the sons of a determined
    index in the heap.
    '''
    
    #Args i; int
    #Ret int; a position from the heap
    def get_fat(self, i):
        return self.heap[mt.ceil(i/2) - 1] if i > 0 else 'root'
    
    #Args i; int
    #Ret: int, int; two positions from the heap
    def get_sons(self, i):
        return [self.heap[i*2 + 1], self.heap[i*2 + 2]]


# In[ ]:





# In[ ]:




