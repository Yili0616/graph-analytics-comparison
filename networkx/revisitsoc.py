from networkx import *
import time
from random import sample

def networkxtest():
    start1 = time.time()
    fh = open("soc-LiveJournal1.txt","r")
    Graph1=nx.read_weighted_edgelist(fh,create_using=networkx.DiGraph(), nodetype=int)
    end1 = time.time()
    fh.close()  
    print "edges:"
    print Graph1.number_of_edges()
    print "nodes:"
    print Graph1.number_of_nodes()
    print "Time for reading the graph cit-Patents temporal:"
    print end1 - start1

    start9 = time.time()

    print "Test edge existence"
    print G.has_edge(*(sample(G.nodes(),2)))
    end9 = time.time()
    print end9-start9

    