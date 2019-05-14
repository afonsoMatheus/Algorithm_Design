#!/usr/bin/env python
# coding: utf-8

import networkx
from networkx import Graph
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt

'''
class that returns and plots the results of the clustering algorithms
Functions are: show_clusters, classes_list
'''

class pcluster:
    
    def __init__(self, edges, ver):
        self.cluster = make_clusters(edges)
        self.edges = edges
        self.ver = ver
        
    '''
    plots the clustering graphic
    '''
    
    #Args name, String
    #Ret None, plots the graphic and save it as a figure
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
        plt.title(name)
        sbn_plot.savefig("out/" + name)
        
    '''
    make the list of classes obtained with the clustering algorithm to make comparisons
    '''
    
    #Args None
    #Ret list; the classes list of the clustering algorithm
    def classes_list(self):
        
        classes = []
        
        for i in range(1, len(self.ver) + 1):
            for j in range(len(self.cluster)):
                if(i in self.cluster[j+1]):
                    classes.append(j+1)
                    
        return classes

'''
plots the rand index graphic
'''

#Args ri name, list String
#Ret None; plot a rand index graphic
def plot_randindex(ri, name):
    
    df = pd.DataFrame()

    df['k'] = []
    df['Rand index'] = []
            
    for i in range(len(ri)):
        df.loc[i] = [ri[i][1]] + [ri[i][0]]
            
    sbn.set()        
    sbn_plot = sbn.lineplot('k', 'Rand index', data= df)
    plt.title(name)
    fig = sbn_plot.get_figure()
    fig.savefig("out/" + name)
    

'''
using the connected components, make the clusters
'''

#Args edges, dict
#Ret dict; the clusters with its vertex
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
    



