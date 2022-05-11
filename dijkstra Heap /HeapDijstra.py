#This file implements shortest path from a specific node to all other nodes in the graph...
# ...given Huge Data set, using Heapq library
#Name: Phumuzile Moyo, Fatima R. Ortega
#Date: May 9, 2022
#Title: Project 1
#With Assistance: Most of our code comes from online sources, we added a few modifications... 
# ...to allow to enter all Nodes at once, and all edges at once.

import heapq
from ChallengeDataSet import getAll

#Priority queues ensure that as we explore one vertex, we always explore one with the smallest distance.
def shortesPathToAll(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0

    pq = [(0, start)]
    while len(pq) > 0:
        #We want to only process a vertex the first time we remove it from the priority queue.
        CurrDistance, CurrVertex = heapq.heappop(pq)
        if CurrDistance > distances[CurrVertex]:
            continue

        for Node, weight in graph[CurrVertex].items():
            distance = CurrDistance + weight

            # Only consider this new path if it is shorter
            if distance < distances[Node]:
                distances[Node] = distance
                heapq.heappush(pq, (distance, Node))
    return distances

#This is just a function to find specific nodes from huge data sets after all shortest paths have been found.
def findShortestPathToSm(allShortest_Dict, arr):
    findShortestPathToSmArr = []
    for key in arr:
        findShortestPathToSmArr.append(allShortest_Dict[key])
    return findShortestPathToSmArr

if __name__ == "__main__":
    challengeDataSet = open("ChallengeDataSet.txt")
    my_Graph = getAll(challengeDataSet)
    print(shortesPathToAll(my_Graph, 1))
    allShortest_Dict = shortesPathToAll(my_Graph, 1)
    
    #What are the shortest-path distances from vertex 1 to the following ten vertices?: 7,37,59,82,99,115,133,165,188,197.
    findShortestPathToSmArr = findShortestPathToSm(allShortest_Dict, [7,37,59,82,99,115,133,165,188,197])
    print(findShortestPathToSmArr)