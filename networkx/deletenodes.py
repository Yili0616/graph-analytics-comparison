import networkx as nx
import random

G = erdos_renyi_graph(1000000,0.00002)

ListOfNodes = G.nodes()
NumberofNodes = G.number_of_nodes()

sample = 100000
RandomSample = random.sample(ListOfNodes, sample)

time1 = time.time()
G.remove_nodes_from(RandomSample)
time2 = time.time()
print "Time for deleting 10 percent of nodes:"
time2 - time1
