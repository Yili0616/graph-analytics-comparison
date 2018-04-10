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
	
	const clock_t begin_time3 = clock();
	TIntFltH PRankH;
	TSnap::GetPageRank(Graph, PRankH, 0.85, 0.0001, 10);
	printf("time for PR:");
	printf("%g\n", float(clock() - begin_time3) / CLOCKS_PER_SEC);

}