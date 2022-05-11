#This file implements shortest path from a specific node to all other nodes in the graph...
# ...given Huge Data set, using Heapq library
#Name: Phumuzile Moyo, Fatima R. Ortega
#Date: May 9, 2022
#Title: Project 1
#With Assistance: Most of our code comes from online sources, we added a few modifications... 
# ...to allow to enter all Nodes at once, and all edges at once.

from collections import defaultdict

#this file extracts data from txt file and stores in a dictionary, such that the key is the starting node...
#... value is a tuple with the end and weight respectively
def getAll(challengeDataSet):
    #tuple with weighted edges
    #edges list is a list of tuple with weighted edges
    edges_dict = defaultdict(list)
    #read each line and get all weighted edges from a particular vertex
    #{start : (end, weight)}
    counter = 1
    for i in challengeDataSet.readlines():
        random_list = i.split()
        #print(random_list)
        dict_entries = {}
        for j in range(1, len(random_list)):
            end, weight = random_list[j].split(",")
            dict_entries[int(end)] = int(weight)
        edges_dict[counter] = dict_entries
        counter += 1
    #print(edges_dict)
    return edges_dict

if __name__ == "__main__":
    challengeDataSet = open("ChallengeDataSet.txt")
    print(getAll(challengeDataSet))
    