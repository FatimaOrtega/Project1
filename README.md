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

- One of the basic operations in the algorith: Check if node has been visited and compares the distances between one node and other nodes to see which one is the shortest distance.

### Predicted Time Complexity
All the other functions used act as helper functions, our goal was to understand the efficiency of Dijkstra's Algorithm. This algorithm processes vertices one by one, always searching for the nodes that have not been visited, and then choosing the closest to the starting vertex. The straightforward implementation runs in **O(mn)** time, where m in the number of edges and n is the number of vertices of the input graph.