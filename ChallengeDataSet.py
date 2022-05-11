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
    