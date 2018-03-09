# Comparison among Graph Analytics Tools

This is code repo for testing 3 different graph vizualization tools: SNAP(C++), NetworkX(python) and iGraph(C++)

Following functions are tested: 

Random Graph Generators: 
1) Erdos-Renyi
2) Watts–Strogatz small-world graph 
3) Preferential Attachment

Save/Load Time for 4 different datasets. All of them are from SNAP website(http://snap.stanford.edu/data/index.html) 
1) Wikitalk (https://snap.stanford.edu/data/wiki-Talk.html)
2) US Patent (https://snap.stanford.edu/data/cit-Patents.html)
3) Pokec Social Network (https://snap.stanford.edu/data/soc-pokec.html)
4) LiveJournal Social Network (https://snap.stanford.edu/data/soc-LiveJournal1.html)

Graph Analytics: 
1) Page Rank
2) Weakly-Connected Component(WCC)
3) 3-cores
4) Clustering Coefficient
5) Edge Existence

* Graph generator code are copied from SNAP C++ examples
* All of the code are run in a folder called graphgen.
