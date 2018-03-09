import networkx as nx
from networkx import *

fh = open("wiki-talk-temporal.txt","r")
G=nx.read_weighted_edgelist(fh,create_using=DiGraph nodetype=int)
fh.close()
print "edges:"
print G.number_of_edges()
print "nodes:"
print G.number_of_nodes()