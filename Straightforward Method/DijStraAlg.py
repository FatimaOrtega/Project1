from VisualDirGraph import edges
from collections import defaultdict
#This file implements shortest path from a specific node to all other nodes in the graph
#Name: Phumuzile Moyo, Fatima R. Ortega
#Date: May 9, 2022
#Title: Project 1
#With Assistance: Most of our code comes from online sources, we added a few modifications to allow to enter all Nodes at once, and all edges at once.

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    #adding all nodes
    def addNodes(self,list_edges):
        for (src, dest, weight) in list_edges: 
            self.nodes.add(src)
    #adding all edges
    def addEdges(self, list_edges):
        for (src, dest, weight) in list_edges: 
            self.edges[src].append(dest)
            self.distances[(src, dest)] = weight

#Finding the shortest path
# https://pythonwife.com/dijkstras-algorithm-in-python/

def dijkstra(graph, initial):
    visited = {initial : 0}
    #path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                #path[edge].append(minNode) //if we wanted to see the path to get to destination node.
    
    return visited


if __name__ == '__main__':
    myFile = open("SimpleTest.txt")
    list_edges = (edges(myFile))
    #print(list_edges)
    my_graph = Graph()
    my_graph.addNodes(list_edges)
    my_graph.addEdges(list_edges)
    print(dijkstra(my_graph, 1))