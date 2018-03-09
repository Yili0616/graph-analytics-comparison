import networkx as nx
import time as t


# Generating Watts_strogatz_graph using networkx. 
# Four parameters: 
# n (int) – The number of nodes
# k (int) – Each node is joined with its k nearest neighbors in a ring topology.
# p (float) – The probability of rewiring each edge
# seed (int, optional) – Seed for random number generator (default=None)


time1 = t.time()
G = nx.watts_strogatz_graph(100000,200,0.5)
time2 = t.time()

print "1st: watts_strogatz_graph 100000,200" 
print time2-time1


time1 = t.time()
G = nx.watts_strogatz_graph(100000,200,0.5)
time2 = t.time()

print "2nd: watts_strogatz_graph 100000,200" 
print time2-time1


time1 = t.time()
G = nx.watts_strogatz_graph(100000,200,0.5)
time2 = t.time()

print "3rd: watts_strogatz_graph 100000,200" 
print time2-time1


time1 = t.time()
G = nx.watts_strogatz_graph(100000,200,0.5)
time2 = t.time()

print "4th: watts_strogatz_graph 100000,200" 
print time2-time1


time1 = t.time()
G = nx.watts_strogatz_graph(100000,200,0.5)
time2 = t.time()

print "5th: watts_strogatz_graph 100000,200" 
print time2-time1




time1 = t.time()
G = nx.watts_strogatz_graph(1000000,200,0.5)
time2 = t.time()

print "1st: watts_strogatz_graph 1000000,200" 
print time2-time1


time1 = t.time()
G = nx.watts_strogatz_graph(1000000,200,0.5)
time2 = t.time()

print "2nd: watts_strogatz_graph 1000000,200" 
print time2-time1

time1 = t.time()
G = nx.watts_strogatz_graph(1000000,200,0.5)
time2 = t.time()

print "3rd: watts_strogatz_graph 1000000,200" 
print time2-time1

time1 = t.time()
G = nx.watts_strogatz_graph(1000000,200,0.5)
time2 = t.time()

print "4th: watts_strogatz_graph 1000000,200" 
print time2-time1

time1 = t.time()
G = nx.watts_strogatz_graph(1000000,200,0.5)
time2 = t.time()

print "5th: watts_strogatz_graph 1000000,200" 
print time2-time1