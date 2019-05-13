#!/usr/bin/env python
# coding: utf-8

# In[4]:

import networkx
from networkx import Graph
import pandas as pd
import seaborn as sbn
from structs import unionfind

class pcluster:
    
    def __init__(self, edges, ver):
        self.cluster = make_clusters(edges)
        self.edges = edges
        self.ver = ver
    
    def show_clusters(self, name):
    
        df = pd.DataFrame()

        df['x'] = []
        df['y'] = []
        df['cluster'] = []
                
        for i in range(1, len(self.ver) + 1):
            for j in range(len(self.cluster)):
                if(i in self.cluster[j+1]):
                    df.loc[i] = [self.ver[i][0]] + [self.ver[i][1]] + [j+1]
                
        sbn.set()        
        sbn_plot = sbn.lmplot('x', 'y', data= df, fit_reg=False, hue="cluster")
        sbn_plot.savefig("out/" + name)
        
    def classes_list(self):
        
        classes = []
        
        for i in range(1, len(self.ver) + 1):
            for j in range(len(self.cluster)):
                if(i in self.cluster[j+1]):
                    classes.append(j+1)
                    
        return classes
    
    
def make_clusters(edges):
    
    edges1 = []
    edges2 = []
        
    for i in range(len(edges)):
        edges1.append(edges[i][1])
        edges2.append(edges[i][2])
                    
    undirected = Graph()
    undirected.add_edges_from(list(zip(edges1, edges2)))
    
    cluster = {}
    i = 1
    for component in networkx.connected_components(undirected):
        cluster[i] = component
        i = i + 1
        
            
    return cluster
    



