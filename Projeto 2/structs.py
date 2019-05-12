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
            if (self.heap[i-1][0] < self.heap[(i//2)-1][0]):
                tmp = self.heap[(i//2)-1]
                self.heap[(i//2)-1] = self.heap[i-1]
                self.heap[i-1] = tmp
            i = i//2
    
    #Args key item, int object
    #Ret None; adds the new element in the heap
    def insert(self, key, item):
        
        key = [key, item]
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
            if self.heap[i][0] > self.heap[min_ind][0]:
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
            if self.heap[i*2 + 1][0] < self.heap[(i*2)+2][0]:
                return i * 2 + 1
            else:
                return i * 2 + 2
    
    #Args None
    #Ret int; the removed item from the heap
    def delete(self):
        remov = self.heap[0][1]
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
        return self.heap[mt.ceil(i/2) - 1][0] if i > 0 else 'root'
    
    #Args i; int
    #Ret: int, int; two positions from the heap
    def get_sons(self, i):
        return [self.heap[i*2 + 1][0], self.heap[i*2 + 2][0]]

    def change_key(self, cost, item):
        
        i = self.locin_heap(item)
        
        if(cost < self.heap[i][0]):
            self.heap[i][0] = cost
            self.ck_botup(i)
            
    def ck_botup(self, i):
                
        while (i/2 > 0):
            if (self.heap[i][0] < self.heap[i//2][0]):
                tmp = self.heap[i//2]
                self.heap[i//2] = self.heap[i]
                self.heap[i] = tmp
            i = i//2
    
    def locin_heap(self, item):
        for i in range(len(self.heap)):
            if(self.heap[i][1] == item):
                return i
     
    
    
class unionfind:
    
    def __init__(self, sets):
        self.sets = sets
        self.size = []
        for i in range(len(self.sets) + 1):
            self.size.append(1)

    def find(self, i):
        
        while(i != self.sets[i]):
            self.sets[i] = self.sets[self.sets[i]]
            i = self.sets[i]
      
        return i
    
    def union(self, i, j):
        
        i = self.find(i)
        j = self.find(j)
        
        if(i != j):
            
            if(self.size[i] < self.size[j]):
                self.size[j] = self.size[j] + self.size[i]
                self.sets[i] = j
                
            else:
                self.size[i] = self.size[i] + self.size[j]
                self.sets[j] = i
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    



