#This file constructs and prints a directed graph with 8 vertices...
# ...which are obtained from a txt file. This file mainly extracts data from a txt file document..
#... such that each extracted set contains source node, destination node and the weight of an edge between the two nodes.

#Name: Phumuzile Moyo, Fatima R. Ortega
#Date: May 9, 2022
#Title: Project 1
#With Assistance: Most of our code comes from online sources, we added a few modifications to allow the program to get data from a txt file.

# A class to represent a graph object
class Graph:
    # Constructor to construct a graph
    def __init__(self, list_edges, n):
        # A list of lists to represent an adjacency list
        self.adjList = [None] * (n+1)
 
        # allocate memory for the adjacency list
        for i in range(n+1):
            self.adjList[i] = []
 
        # add edges to the directed graph
        for (src, dest, weight) in list_edges:
            # allocate node in adjacency list from src to dest
            self.adjList[src].append((dest, weight))
            
        #***** We could implement this if we wanted to an undirected graph
        #for (src, dest, weight) in list_edges:
            # allocate node in adjacency list from src to dest
            #self.adjList[dest].append((src, weight))
    
#Function to build the adjacency list with edges    
def edges(myFile):
    #tuple with weighted edges
    tuple_set = ()
    #edges list is a list of tuple with weighted edges
    edges_list = []
    #read each line and get all weighted edges from a particular vertex
    for i in myFile.readlines():
        random_list = []
        for j in i:
            if j.isdigit():
                random_list.append(int(j))
    
        for j in range(2,len(random_list),3):
            tuple_set = (random_list[j-2], random_list[j-1], random_list[j])
            tuple_set2 = (random_list[j-2], random_list[j+1], random_list[j+2])
            edges_list.append(tuple_set)
            edges_list.append(tuple_set2)
    return edges_list                
                    
# Function to print adjacency list representation of a graph
def printGraph(graph):
    for src in range(len(graph.adjList)):
        # print current vertex and all its neighboring vertices
        for (dest, weight) in graph.adjList[src]:
            print(f'({src} ???> {dest}, {weight}) ', end='')
        print()
 
if __name__ == '__main__':
    # Input: Edges in a weighted digraph (as per the above diagram)
    myFile = open("SimpleTest.txt")
   
    #n represents the number nodes
    list_edges = (edges(myFile))
    print(list_edges)
    n = 8
    # construct a graph from a given list of edges
    graph = Graph(list_edges, n)
    printGraph(graph)