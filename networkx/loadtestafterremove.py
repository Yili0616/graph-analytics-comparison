from networkx import *
import sys
import time
import pickle

def networkxtest():
    start1 = time.time()
    fh = open("wiki-talk-temporal.txt","r")
    Graph1=nx.read_weighted_edgelist(fh,create_using=networkx.DiGraph(), nodetype=int)
    end1 = time.time()
    fh.close()  
    print "edges:"
    print Graph1.number_of_edges()
    print "nodes:"
    print Graph1.number_of_nodes()
    print "Time for reading the graph Wiki-talk temporal:"
    print end1 - start1


    # start2  = time.time()
    # Graph2 = read_edgelist("testgraph.txt")
    # end2 = time.time()
    # print "Time for generating undirect ER:"
    # print end2 - start2


    Graph1.remove_edges_from(Graph1.selfloop_edges())
    print "after removing self loops:"
    Graph1.number_of_edges()

    