# Project1
# Name: Phumuzile Moyo, Fatima R. Ortega
# Date: May 9, 2022
# Title: Project 1

# **Introduction**
The goal of this project is to implement Dijkstra's Algorithms using two different techniques. First, we will use Adjacency List. Secondly, we will use Heap. We will use this algorithm to solve the single-source shortest path problem in different directed graphs. This program is implemented using Python

# **Program Analysis**
## **Straightforward Implementation**
### Algorithm Development
- Implemented a graph that was given by link: <https://pythonwife.com/dijkstras-algorithm-in-python/>. We found an adjacency graph that implements weight on the edge. The main method, *VisualDirGraph*, allows the user to manually input the edge and weight, modified code to be able to create variables that will identify the vertex and weight from a text file in which the format **must remain static**. 

- One major modification made in the program and code from online sources is how the program gets all of its edges and nodes from the txt file instead of manually adding each single node at a time. This modification is in function called **edges()** which takes the txt file as a parameter. The result from this function is used as an input in three other functions, i.e in the constructor for *VisualDirGraph*, in *addNodes*, and in *addEdges.*

- One of the basic operations in the algorithm: Check if node has been visited and compares the distances between one node and other nodes to see which one is the shortest distance.

### Predicted Time Complexity
All the other functions used act as helper functions, our goal was to understand the efficiency of Dijkstra's Algorithm. This algorithm processes vertices one by one, always searching for the nodes that have not been visited, and then choosing the closest to the starting vertex. The straightforward implementation runs in **O(mn)** time, where m in the number of edges and n is the number of vertices of the input graph.

## **Heap Implementation**
### Algorithm Development
- Implemented heap algorithm with help from given link: <https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/#:~:text=Dijkstra's%20algorithm%20uses%20a%20priority,of%20vertices%20sorted%20by%20distance.> and given advice on how the algorithm gives the entries given go through the priority queue. The main method, *shortesPathToAll* ensures that as we explore one vertex, and checks to see which one is in the shortest distance.

- One major modification that we made in the program and code from online sources was extracting all the nodes in the txt file and sending it into the dictionary, this would allow us to implement even more nodes in a file. This modification can be seen in **getAll** which takes the txt file as the parameter. This function is used when trying to print out to find specific nodes in the data set.

- One of the basic operations in the algorithm: A distance dictionary in which it adds every vertex in the graph and creating a while loop that check every entry that gets added to the priority queue. 

### Predicted Time Complexity
- Building the distances dictionary takes O(V) time because we have to add all the vertices to the dictionary. 

- The while loop is executed once for every entry that gets added to the queue. An entry can only be added when we explore an edge, so there are at most O(E) iterations of the while loop since we have to explore all the edges.

- The for loop goes through every vertex, and we ensure that we process a vertex only once; checking all outgoing edges, this is O(E).

- The operations in the priority queue involve adding or deleting an entry, this takes O(log E) run-time. So the overall running time for the Dijkstra Algorithm will be O(V + E log E).

- The other functions we constructed also take some time. To extract data from our text file, we have to go through all lines,N, in the file. For each line, we have to go through each the entire length, L, of the line and do some operations. So extracting our data from text file will take O(NL) where N is the number of lines we have to read and L is the size of each line.

- Another helper file that we constructed for someone that wants to seach for specific distances from one node to other. We used **findShortestPathToSm** function to do that. In this function, the user would iterate through an entire array that has all vertices they want to get to, and get the value of that key from dictionary with all shortest paths. iterating through array of size V takes O(V) run-time. Extracting the value of a key in a dictionary is constant. So this function takes O(V) time to find specific vertices from **distances** dictionary