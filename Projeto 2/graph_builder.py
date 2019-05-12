#!/usr/bin/env python
# coding: utf-8

import math

class bgraph:
    
    def build_graph(file):

        ver = read_data(file)
        edges = []

        G = {}

        p = 1
        for i in range(1, len(ver) + 1):
            G[p] = []
            for j in range(1, len(ver) + 1):
                dist = dist_euclidiana(ver[i][:2],ver[j][:2])
                if(dist != 0):
                    edges.append([dist, i, j])
                G[p].append(dist)
                
            p = p + 1

        return G, ver, edges     
    
    def read_classes(file):
        
        arq = open(file, 'r')

        v = arq.readlines()

        tclasses = []

        for lin in v:
            tclasses.append(lin.rstrip())
            

        arq.close()

        return tclasses      
    
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

def dist_euclidiana(v1, v2):

    dim, soma = len(v1), 0
    for i in range(dim):
        soma += math.pow(v1[i] - v2[i], 2)

    return math.sqrt(soma)

