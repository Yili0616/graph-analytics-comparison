import networkx as nx
import time as time

# Generating PA graph using NetworkX
# n (int) – Number of nodes
# m (int) – Number of edges to attach from a new node to existing nodes
# seed (int, optional) – Seed for random number generator (default=None).

# 1m, 10 
time1 = time.time()
G = nx.barabasi_albert_graph(1000000, 10)
time2 = time.time()
print "1M nodes, 10 edges to attach from a new node to existing nodes"
print "number of edges"
G.number_of_edges()
print "1st: time: "
print time2 - time1

time1 = time.time()
G = nx.barabasi_albert_graph(1000000, 10)
time2 = time.time()
print "1M nodes, 10 edges to attach from a new node to existing nodes"
print "number of edges"
G.number_of_edges()
print "2nd: time: "
print time2 - time1

time1 = time.time()
G = nx.barabasi_albert_graph(1000000, 10)
time2 = time.time()
print "1M nodes, 10 edges to attach from a new node to existing nodes"
print "number of edges"
G.number_of_edges()
print "3rd: time: "
print time2 - time1

time1 = time.time()
G = nx.barabasi_albert_graph(1000000, 10)
time2 = time.time()
print "1M nodes, 10 edges to attach from a new node to existing nodes"
print "number of edges"
G.number_of_edges()
print "4th: time: "
print time2 - time1

time1 = time.time()
G = nx.barabasi_albert_graph(1000000, 10)
time2 = time.time()
print "1M nodes, 10 edges to attach from a new node to existing nodes"
print "number of edges"
G.number_of_edges()
print "5th: time: "
print time2 - time1

# 10m, 10
time1 = time.time()
G = nx.barabasi_albert_graph(10000000, 10)
time2 = time.time()
print "10M nodes, 10 edges to attach from a new node to existing nodes"
print "number of edges"
G.number_of_edges()
print "1st: time: "
print time2 - time1

time1 = time.time()
G = nx.barabasi_albert_graph(10000000, 10)
time2 = time.time()
print "10M nodes, 10 edges to attach from a new node to existing nodes"
print "number of edges"
G.number_of_edges()
print "2nd: time: "
print time2 - time1

time1 = time.time()
G = nx.barabasi_albert_graph(10000000, 10)
time2 = time.time()
print "10M nodes, 10 edges to attach from a new node to existing nodes"
print "number of edges"
G.number_of_edges()
print "3rd: time: "
print time2 - time1

time1 = time.time()
G = nx.barabasi_albert_graph(10000000, 10)
time2 = time.time()
print "10M nodes, 10 edges to attach from a new node to existing nodes"
print "number of edges"
G.number_of_edges()
print "4th: time: "
print time2 - time1

time1 = time.time()
G = nx.barabasi_albert_graph(10000000, 10)
time2 = time.time()
print "10M nodes, 10 edges to attach from a new node to existing nodes"
print "number of edges"
G.number_of_edges()
print "5th: time: "
print time2 - time1

