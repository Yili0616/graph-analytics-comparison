from networkx import *
import time
from random import sample

def networkxtest():
    start1 = time.time()
    fh = open("soc-pokec-relationships.txt","r")
    Graph1=nx.read_weighted_edgelist(fh,create_using=networkx.DiGraph(), nodetype=int)
    end1 = time.time()
    fh.close()  
    print "edges:"
    print Graph1.number_of_edges()
    print "nodes:"
    print Graph1.number_of_nodes()
    print "Time for reading the graph soc-pokec-relationships:"
    print end1 - start1


    # start2  = time.time()
    # Graph2 = read_edgelist("testgraph.txt")
    # end2 = time.time()
    # print "Time for generating undirect ER:"
    # print end2 - start2

    Graph1.remove_edges_from(Graph1.selfloop_edges())
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
    k_core = networkx.k_core(Graph1, k=3)
    end4 = time.time()
    print "3-core:"
    print end4 - start4

    start5 = time.time()
    page_rank = networkx.pagerank(Graph1, max_iter=10, tol=1e-04)
    end5 = time.time()
    print "page rank"
    print end5 - start5

    # start6 = time.time()
    # scc_number = networkx.number_strongly_connected_components(Graph1) # return number of SCC
    # end6 = time.time()
    # print "SCC"
    # print end6 - start6

    start7 = time.time()
    wcc_number = networkx.number_weakly_connected_components(Graph1)
    end7 = time.time()
    print "WCC"
    print end7 - start7

    # start8 = time.time()
    # triangle_number = networkx.triangles(Graph2)
    # end8 = time.time()
    # print "triangle"
    # print end8 - start8


    # eigenvector centrality
    # start9 = time.time()
    # eigenvector_centrality = networkx.eigenvector_centrality(Graph1)
    # end9 = time.time()
    # print "eigenvector centrality"
    # print end9 - start9


    # # in-degree distribution
    # start10 = time.time()
    # in_degree = networkx.in_degree_centrality(Graph1)
    # end10 = time.time()
    # print "indegree centrality"
    # print end10-start10

    # out-degree distribution
    # start11 = time.time()
    # out_degree = networkx.out_degree_centrality(Graph1)
    # end11 = time.time()
    # print "outdegree centrality"
    # print end11 - start11

    # average clustering -- convert to undirected graph first
    start8 = time.time()
    G = Graph1.to_undirected()
    clustering(G) 
    end8 = time.time()
    print "Clustering Coefficient:"
    print end8 - start8

    # test edge existence

    start9 = time.time()

    print "Test edge existence"
    print G.has_edge(*(sample(G.nodes(),2)))
    end9 = time.time()
    print end9-start9



if __name__ == '__main__':
    networkxtest()

