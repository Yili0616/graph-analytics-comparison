from networkx import *
import sys
import time
import pickle

def networkxtest():
    start1 = time.time()
    Graph1 = read_edgelist("wiki-talk-temporal.txt",create_using = nx.DiGraph())
    end1 = time.time()
    print "Time for reading the graph Wiki-talk temporal:"
    print end1 - start1

    print "number of edges:"
    Graph1.number_of_edges()

    print "number of nodes:"
    Graph1.number_of_nodes()

    # start2  = time.time()
    # Graph2 = read_edgelist("testgraph.txt")
    # end2 = time.time()
    # print "Time for generating undirect ER:"
    # print end2 - start2

    # Graph1.remove_edges_from(Graph1.selfloop_edges())
    # Graph2.remove_edges_from(Graph2.selfloop_edges())


    # start2 = time.time()
    # networkx.write_gpickle(Graph1,"test.gpickle")
    # end2 = time.time()
    # print "Time for saving a 1m, 10m graph"
    # print end2-start2

    # start3 = time.time()
    # networkx.read_gpickle("test.gpickle")
    # end3 = time.time()
    # print "Time for loading 1m, 10m graph"
    # print end3 - start3

    start4 = time.time()
    k_core = networkx.k_core(Graph1)
    end4 = time.time()
    print "k-core:"
    print end4 - start4

    start5 = time.time()
    page_rank = networkx.pagerank(Graph1)
    end5 = time.time()
    print "page rank"
    print end5 - start5

    start6 = time.time()
    scc_number = networkx.number_strongly_connected_components(Graph1) # return number of SCC
    end6 = time.time()
    print "SCC"
    print end6 - start6

    start7 = time.time()
    wcc_number = networkx.number_weakly_connected_components(Graph1)
    end7 = time.time()
    print "WCC"
    print end7 - start7

    start8 = time.time()
    triangle_number = networkx.triangles(Graph2)
    end8 = time.time()
    print "triangle"
    print end8 - start8


    # eigenvector centrality
    start9 = time.time()
    eigenvector_centrality = networkx.eigenvector_centrality(Graph1)
    end9 = time.time()
    print "eigenvector centrality"
    print end9 - start9


    # in-degree distribution
    start10 = time.time()
    in_degree = networkx.in_degree_centrality(Graph1)
    end10 = time.time()
    print "indegree centrality"
    print end10-start10

    # out-degree distribution
    start11 = time.time()
    out_degree = networkx.out_degree_centrality(Graph1)
    end11 = time.time()
    print "outdegree centrality"
    print end11 - start11



if __name__ == '__main__':
    networkxtest()

