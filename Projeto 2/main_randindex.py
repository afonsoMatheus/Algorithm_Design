import sys
from graph_builder import bgraph
from MST import mst
from plot_clusters import pcluster
import plot_clusters
from sklearn.metrics.cluster import adjusted_rand_score

def kruskal_clustering(G, edges, k):
    
    edges = mst.kruskal_algorithm(G, edges)
        
    tam = len(edges) - 1
    aux = []
                
    for i in range(k - 1):
        
        edges[tam - i] = [0, edges[tam - i][1], edges[tam - i][1]]
        
    for i in range(len(edges)):
        aux.append(edges[tam - i][1])
        
    aux = set(sorted(aux))
        
    for i in range(1, len(G.keys())+1):
        if i not in aux:
            edges.append([0, i, i])
        
    return edges

def prim_clustering(G, k):
    
    pred = mst.prim_algorithm(G)
    
    k = k - 1
        
    keys = list(pred.keys())
    edges = []
            
    for i in range(len(keys)):
        edges.append([G[keys[i]][pred[i+1]-1], i+1, pred[i+1]])
                                
    edges = sorted(edges, reverse=True)
    
    for j in range(k):
        edges[j] = [0, edges[j][1], edges[j][1]] 
    
    return edges

def k_clustering(arq, k, mstree):
    
    G, ver, edges = bgraph.build_graph("in/" + arq)
    
    if(mstree == "prim"):
        edges = prim_clustering(G, k)
        
    elif(mstree == "kruskal"):
        edges = kruskal_clustering(G, edges, k)
        
    else:
        
        return print("Choose a valid algorithm (prim or kruskal)!")
    
    plot = pcluster(edges, ver)

    pclasses = plot.classes_list()
    tclasses = bgraph.read_classes('in/classes.txt')
    
    return adjusted_rand_score(tclasses, pclasses)


if __name__ == "__main__":
    arq = sys.argv[1]
    mstree = sys.argv[2]

    ri = []    
    for i in range(1, 10):
    	value = k_clustering(arq, i, mstree)
    	ri.append([value, i])

    plot_clusters.plot_randindex(ri, "Randindex_" + str(mstree))