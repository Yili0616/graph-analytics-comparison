import time
from igraph import *
# dim,size, nei, p, loops, multiple

time1 = time.time()
G = Graph.Watts_Strogatz(2,100000,6,0.5)
time2 = time.time()
print "1st: Watts_Strogatz for 100000 vxs in 2 dimension with 0.5 prob rewritten, connected in 6 degree"
print time2-time1

time1 = time.time()
G = Graph.Watts_Strogatz(2,100000,6,0.5)
time2 = time.time()
print "2nd: Watts_Strogatz for 100000 vxs in 2 dimension with 0.5 prob rewritten, connected in 6 degree"
print time2-time1

time1 = time.time()
G = Graph.Watts_Strogatz(2,100000,6,0.5)
time2 = time.time()
print "3rd: Watts_Strogatz for 100000 vxs in 2 dimension with 0.5 prob rewritten, connected in 6 degree"
print time2-time1

time1 = time.time()
G = Graph.Watts_Strogatz(2,100000,6,0.5)
time2 = time.time()
print "4th: Watts_Strogatz for 100000 vxs in 2 dimension with 0.5 prob rewritten, connected in 6 degree"
print time2-time1

time1 = time.time()
G = Graph.Watts_Strogatz(2,100000,6,0.5)
time2 = time.time()
print "5th: Watts_Strogatz for 100000 vxs in 2 dimension with 0.5 prob rewritten, connected in 6 degree"
print time2-time1

time1 = time.time()
G = Graph.Watts_Strogatz(2,1000000,6,0.5)
time2 = time.time()
print "1st: Watts_Strogatz for 1000000 vxs in 2 dimension with 0.5 prob rewritten, connected in 6 degree"
print time2-time1

time1 = time.time()
G = Graph.Watts_Strogatz(2,1000000,6,0.5)
time2 = time.time()
print "2nd: Watts_Strogatz for 1000000 vxs in 2 dimension with 0.5 prob rewritten, connected in 6 degree"
print time2-time1

time1 = time.time()
G = Graph.Watts_Strogatz(2,1000000,6,0.5)
time2 = time.time()
print "3rd: Watts_Strogatz for 1000000 vxs in 2 dimension with 0.5 prob rewritten, connected in 6 degree"
print time2-time1

time1 = time.time()
G = Graph.Watts_Strogatz(2,1000000,6,0.5)
time2 = time.time()
print "4th: Watts_Strogatz for 1000000 vxs in 2 dimension with 0.5 prob rewritten, connected in 6 degree"
print time2-time1

time1 = time.time()
G = Graph.Watts_Strogatz(2,1000000,6,0.5)
time2 = time.time()
print "5th: Watts_Strogatz for 1000000 vxs in 2 dimension with 0.5 prob rewritten, connected in 6 degree"
print time2-time1