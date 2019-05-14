#!/usr/bin/env python
# coding: utf-8
from structs import binheap as bh
from structs import unionfind as uf

'''
class that implements two mst algorithms: Kruskal and Prim
Functions are: prim_algorithm, kruskal_algorithm
'''

class mst:
    
    '''
    prim algorithm makes a mst using a heap structure, which for each
    vertex v of G will have an edge associated, with are v and the father
    of v
    '''
    
    #Args G, dict
    #Ret dict; the father of each vertex of G 
    def prim_algorithm(G):
    
        ver = list(G.keys())

        min_path = {}
        pred = {}
        exp = []

        start = ver[0]

        min_path[start] = 0
        exp.append(start)
        pred[start] = start

        heap = bh()

        for i in range(1,len(ver)):

            heap.insert(G[ver[i]][start-1] , ver[i])
            pred[ver[i]] = start
            min_path[ver[i]] = G[ver[i]][start-1]

        while(heap.heap != []):

            minimun = heap.delete()
            exp.append(minimun)

            for i in range(len(G[minimun])):

                if(ver[i] not in exp):

                    if(G[minimun][ver[i]-1] < min_path[ver[i]] and G[minimun][ver[i]-1] != 0):

                        heap.change_key(G[minimun][ver[i]-1], ver[i])
                        min_path[ver[i]] = G[minimun][ver[i]-1]
                        pred[ver[i]] = minimun

        return pred
    
    
    '''
    kruskal algorithm makes a mst using an union find structure, using the sets
    to add edges that wont form a cycle
    '''
    
    #Args G edges, dict list
    #Ret list; the edges that forms the mst
    def kruskal_algorithm(G, edges):
    
        ver = G.keys()
        edges = sorted(edges)
        sets = {}

        nedges = []

        for i in range(1, len(ver) + 1):
            sets[i] = i

        unionf = uf(sets)

        for i in range(len(edges)):

            ver1, ver2 = edges[i][1], edges[i][2]

            if(unionf.find(ver1) != unionf.find(ver2)):
                nedges.append(edges[i])
                unionf.union(ver1,ver2)

        return nedges
    

