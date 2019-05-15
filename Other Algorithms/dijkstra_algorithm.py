from structs import binheap

'''
dijkstra algorithm for minimal path
'''

#Args G s, dict int
#Ret dict: the edge for each vertex in the minimal path
def dijkstra_algorithm(G, s):

	ver = list(G.keys())
	dist = {}
	pred = {}

	for i in range(len(ver)):
		dist[ver[i]] = 9999
		pred[ver[i]] = None

	dist[s] = 0

	heap = binheap()

	for i in range(len(ver)):
		heap.insert(dist[ver[i]], ver[i])

	while(heap.heap != []):

		u = heap.delete()

		edges = G[u]

		for i in range(len(edges)):

			if(dist[ver[i]] > dist[u] + edges[i] and edges[i] != 0):
				heap.change_key(dist[u] + edges[i], ver[i])
				dist[ver[i]] = dist[u] + edges[i]
				pred[ver[i]] = [u, ver[i]]

	return pred
		


