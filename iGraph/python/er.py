import time
from igraph import *

time1 = time.time()
g = Graph.Erdos_Renyi(1000000, m=10000000)
time2 = time.time()
print "1st: igraph 1M, 10M"
print time2-time1

time1 = time.time()
g = Graph.Erdos_Renyi(1000000, m=10000000)
time2 = time.time()
print "2nd: igraph 1M, 10M"
print time2-time1

time1 = time.time()
g = Graph.Erdos_Renyi(1000000, m=10000000)
time2 = time.time()
print "3rd: igraph 1M, 10M"
print time2-time1

time1 = time.time()
g = Graph.Erdos_Renyi(1000000, m=10000000)
time2 = time.time()
print "4th: igraph 1M, 10M"
print time2-time1

time1 = time.time()
g = Graph.Erdos_Renyi(1000000, m=10000000)
time2 = time.time()
print "5th: igraph 1M, 10M"
print time2-time1

time1 = time.time()
g = Graph.Erdos_Renyi(10000000, m=100000000)
time2 = time.time()
print "1st: igraph 10M, 100M"
print time2-time1

time1 = time.time()
g = Graph.Erdos_Renyi(10000000, m=100000000)
time2 = time.time()
print "2nd: igraph 10M, 100M"
print time2-time1

time1 = time.time()
g = Graph.Erdos_Renyi(10000000, m=100000000)
time2 = time.time()
print "3rd: igraph 10M, 100M"
print time2-time1

time1 = time.time()
g = Graph.Erdos_Renyi(10000000, m=100000000)
time2 = time.time()
print "4th: igraph 10M, 100M"
print time2-time1

time1 = time.time()
g = Graph.Erdos_Renyi(10000000, m=100000000)
time2 = time.time()
print "5th: igraph 10M, 100M"
print time2-time1

time1 = time.time()
g = Graph.Erdos_Renyi(1000000, m=100000000)
time2 = time.time()
print "1st: igraph 1M, 100M"
print time2-time1

time1 = time.time()
g = Graph.Erdos_Renyi(1000000, m=100000000)
time2 = time.time()
print "2nd: igraph 1M, 100M"
print time2-time1


time1 = time.time()
g = Graph.Erdos_Renyi(1000000, m=100000000)
time2 = time.time()
print "3rd: igraph 1M, 100M"
print time2-time1


time1 = time.time()
g = Graph.Erdos_Renyi(1000000, m=100000000)
time2 = time.time()
print "4th: igraph 1M, 100M"
print time2-time1

time1 = time.time()
g = Graph.Erdos_Renyi(1000000, m=100000000)
time2 = time.time()
print "5th: igraph 1M, 100M"
print time2-time1