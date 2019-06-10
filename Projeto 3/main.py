#!/usr/bin/env python
# coding: utf-8

import math
import heapq as hp
import time
import sys

''' 
DTW (Dynamic Time Warping) is a dynamic programing algorithm thats compares two temporal series,
using a bottom-up approach. It's uses the distance function to calculate the distance between two poits
from the series, with a simple function of (v1-v2)^2. More information on the report.

'''

#Args v1 v2, int int
#Ret int; the distance betwen two points
def distance(v1, v2):
    
    dist = 0
    dist = math.pow(float(v1) - float(v2), 2)

    return dist

#Args ts1 ts2, list list
#Ret int; the final position in the matrix 
def DTW(ts1, ts2):
    
    n = len(ts1) + 1
    m = len(ts2) + 1
    
    mat = [[0 for i in range(m)] for i in range(n)]
    
    for i in range(1, n):
        mat[i][0] = 9999
         
    for i in range(1, m):
        mat[0][i] = 9999
        
    for i in range(1, n):
        for j in range(1, m):
            cost = distance(ts1[i-1], ts2[j-1])
            mat[i][j] = cost + min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1])
    
    return mat[n-1][m-1]

''' 
KNN (K-Nearest Neighboors) algorithm with k = 1

'''

#Args train test target, list list list 
#Ret list; the classification of the test
def knn(train, test, target):
    
    results = []
    
    print("Making classification...")
    print("Series from test classified:")

    
    for j in range(len(test)):
        
        heap = []

        for i in range(len(train)):
            
            hp.heappush(heap, [DTW(train[i], test[j]), target[i]])
        
        near = heap[0:1]
                
        results.append(near[0][1])

        sys.stdout.write("\r{0}".format(j))
        sys.stdout.flush()
        time.sleep(0.5)
                        
    return results

'''
Function to calculate the accuracy of the classification
'''

#Args pred_label real_label, list list
#Ret float; the accuracy of the classification
def evaluation(pred_label, real_label):
    
    count = 0
    
    for i in range(len(pred_label)):
        if(pred_label[i] == real_label[i]):
            count += 1
            
    return count/len(pred_label)

'''
Function thats reads the training and the test files
'''

#Args arq, String
#Ret list list; the list of classes and the temporal series
def read_txt(arq):

    arq = open(arq, 'r')
    lines = arq.readlines()

    ts = []
    target = []

    for line in lines:
        l = line.split()
        target.append(l[0])
        ts.append(l[1:])

    arq.close()
    
    return target, ts

if __name__ == "__main__":

    target_train, ts_train = read_txt("treino.txt")
    real_label, ts_test = read_txt("teste.txt")

    start = time.time()

    pred_label = knn(ts_train, ts_test, target_train)

    end = time.time()
    print("Time: ", end - start)
    
    print("Accuracy: ", evaluation(pred_label, real_label))


