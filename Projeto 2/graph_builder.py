#!/usr/bin/env python
# coding: utf-8

import math

'''
class tha read the input file and generates the variables that will be
needed to do the clustering activity. Also, it reads the classes.txt file
to future comparations
Functions are: build_graph, read_classes
'''

class bgraph:
    
    '''
    build the graph structure using a dictionary, using the euclidian distance to add
    value to the edges. Also, returns the vertices and edges from the graph separately
    for the MST algorithms
    '''
    
    #Args file, String
    #Ret dict dict list; the graph dictionary, the vertices dictionary and the edge list
    def build_graph(file):

        ver = read_data(file)
        edges = []

        G = {}

        p = 1
        for i in range(1, len(ver) + 1):
            G[p] = []
            for j in range(1, len(ver) + 1):
                dist = dist_euclidian(ver[i][:2],ver[j][:2])
                if(dist != 0):
                    edges.append([dist, i, j])
                G[p].append(dist)
                
            p = p + 1

        return G, ver, edges
    
    '''
    open and read the classes.txt file, returning the true class value
    '''
    
    #Args file, String
    #Ret list; the classes from each vertex in data.txt
    def read_classes(file):
        
        arq = open(file, 'r')

        v = arq.readlines()

        tclasses = []

        for lin in v:
            tclasses.append(lin.rstrip())
            

        arq.close()

        return tclasses
    
    
'''
read the input file and labels each pair of values 
'''

#Args file, String
#Ret dict; the vertex dictionary
def read_data(file):

    arq = open(file, 'r')

    v = arq.readlines()

    ver = {}

    i = 1
    for lin in v:
        x, y = lin.split("\t")
        y = y.rstrip()
        ver[i] = [float(x),float(y)]
        i = i + 1

    arq.close()

    return ver

'''
euclidian distance to make the edges
'''

#Args v1 v2, float float
#Return float; the euclidian distance between v1 and v2 
def dist_euclidian(v1, v2):

    dim, soma = len(v1), 0
    for i in range(dim):
        soma += math.pow(v1[i] - v2[i], 2)

    return math.sqrt(soma)

