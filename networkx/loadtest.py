from networkx import *
import sys
import time
import pickle

def networkxtest():
    start1 = time.time()
    fh = open("WikiTalk.txt","r")
    Graph1=nx.read_weighted_edgelist(fh,create_using=networkx.DiGraph(), nodetype=int)
    end1 = time.time()
    fh.close()  
    print "edges:"
    print Graph1.number_of_edges()
    print "nodes:"
    print Graph1.number_of_nodes()
    print "Time for reading the graph Wiki-talk temporal:"
    print end1 - start1


if __name__ == '__main__':
    networkxtest()