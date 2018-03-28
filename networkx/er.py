import networkx as nx
import time as time

# Generating ER graph using NetwortX
# Return a random graph G_{n,p} (ER graph, binomial graph).
# Chooses each of the possible edges with probability p.
# This is also called binomial_graph and erdos_renyi_graph.

# 10M edges
time1 = time.time()
G = nx.fast_gnp_random_graph(1000000,0.00002)
# count edges 
time2 = time.time()
print "1st: ER 1M, 10M"
print "number of edges"
print G.number_of_edges()
print time2-time1

time1 = time.time()
G = nx.fast_gnp_random_graph(1000000,0.00002)
# count edges 
time2 = time.time()
print "2ND: ER 1M, 10M"
print "number of edges"
print G.number_of_edges()
print time2-time1

time1 = time.time()
G = nx.fast_gnp_random_graph(1000000,0.00002)
# count edges 
time2 = time.time()
print "3RD: ER 1M, 10M"
print "number of edges"
print G.number_of_edges()
print time2-time1

time1 = time.time()
G = nx.fast_gnp_random_graph(1000000,0.00002)
# count edges 
time2 = time.time()
print "4th: ER 1M, 10M"
print "number of edges"
print G.number_of_edges()
print time2-time1

time1 = time.time()
G = nx.fast_gnp_random_graph(1000000,0.00002)
# count edges 
time2 = time.time()
print "5th: ER 1M, 10M"
print "number of edges"
print G.number_of_edges()
print time2-time1

# 100M edges
time1 = time.time()
G = nx.fast_gnp_random_graph(1000000,0.0002)
# count edges 
time2 = time.time()
print "1st: ER 1M, 100M"
print "number of edges"
print G.number_of_edges()
print time2-time1

time1 = time.time()
G = nx.fast_gnp_random_graph(1000000,0.0002)
# count edges 
time2 = time.time()
print "2nd: ER 1M, 100M"
print "number of edges"
print G.number_of_edges()
print time2-time1

time1 = time.time()
G = nx.fast_gnp_random_graph(1000000,0.0002)
# count edges 
time2 = time.time()
print "3rd: ER 1M, 100M"
print "number of edges"
print G.number_of_edges()
print time2-time1

time1 = time.time()
G = nx.fast_gnp_random_graph(1000000,0.0002)
# count edges 
time2 = time.time()
print "4th: ER 1M, 100M"
print "number of edges"
print G.number_of_edges()
print time2-time1

time1 = time.time()
G = nx.fast_gnp_random_graph(1000000,0.0002)
# count edges 
time2 = time.time()
print "5th: ER 1M, 100M"
print "number of edges"
print G.number_of_edges()
print time2-time1

## 10M, 100M
time1 = time.time()
G = nx.fast_gnp_random_graph(10000000,0.000002)
# count edges 
time2 = time.time()
print "1th: ER 10M, 100M"
print "number of edges"
print G.number_of_edges()
print time2-time1

time1 = time.time()
G = nx.fast_gnp_random_graph(10000000,0.000002)
# count edges 
time2 = time.time()
print "2nd: ER 10M, 100M"
print "number of edges"
print G.number_of_edges()
print time2-time1

time1 = time.time()
G = nx.fast_gnp_random_graph(10000000,0.000002)
# count edges 
time2 = time.time()
print "3rd: ER 10M, 100M"
print "number of edges"
print G.number_of_edges()
print time2-time1

time1 = time.time()
G = nx.fast_gnp_random_graph(10000000,0.000002)
# count edges 
time2 = time.time()
print "4th: ER 10M, 100M"
print "number of edges"
print G.number_of_edges()
print time2-time1

time1 = time.time()
G = nx.fast_gnp_random_graph(10000000,0.000002)
time2 = time.time()
print "5th: ER 10M, 100M"
print "number of edges"
print G.number_of_edges()
print time2-time1



