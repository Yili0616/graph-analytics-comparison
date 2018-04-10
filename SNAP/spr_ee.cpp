#include <ctime>
#include <cstdlib>
#include <typeinfo>
#include "Snap.h"

int main(int argc, char* argv[]) {
  	const clock_t begin_time = clock();
  	PNGraph Graph = TSnap::LoadEdgeList<PNGraph>("soc-pokec-relationships.txt", 0, 1);
  	printf("time for reading soc-pokec-relationships.txt:");
  	printf("%g\n", float(clock() - begin_time) / CLOCKS_PER_SEC);
  	TIntPrV count;
  	printf("number of nodes: %i\n", Graph->GetNodes());
  	printf("number of edges: %d\n", Graph->GetEdges());
  
    TSnap::DelSelfEdges(Graph);
	const clock_t begin_time6 = clock();
	printf("Does the edge exist? ");
		// printf("i:%i\n", i);
		// printf("%i\n",Graph->GetRndNId());
	for (int i = 0; i < 10000; i++) {
		Graph->IsEdge(Graph->GetRndNId(), Graph->GetRndNId());
    }
    
	printf("Time for test existence of edge for 100000 times\n");
	printf("%g\n", float(clock() - begin_time6) / CLOCKS_PER_SEC);

}