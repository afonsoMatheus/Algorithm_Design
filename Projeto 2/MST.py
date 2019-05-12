#!/usr/bin/env python
# coding: utf-8
import structs as bh

class mst:
    
    def prim_algorithm(G):
    
        ver = list(G.keys())

        min_path = {}
        pred = {}
        exp = []

        start = ver[0]

        min_path[start] = 0
        exp.append(start)
        pred[start] = start

        for i in range(1, len(ver)):

            min_path[ver[i]] = 9999
            pred[ver[i]] = start

        heap = bh.binheap()

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

