#include <ctime>
#include <cstdlib>
#include <typeinfo>
#include "Snap.h"

int main(int argc, char* argv[]) {
  const clock_t begin_time = clock();
  PNGraph Graph = TSnap::LoadEdgeList<PNGraph>("soc-LiveJournal1.txt", 0, 1);
  printf("time for reading soc-LiveJournal1.txt:");
  printf("%g\n", float(clock() - begin_time) / CLOCKS_PER_SEC);
  TIntPrV count;
  printf("number of nodes: %i\n", Graph->GetNodes());
  printf("number of edges: %d\n", Graph->GetEdges());
 
	TSnap::DelSelfEdges(Graph);
	
	const clock_t begin_time2 = clock();
	TSnap::GetWccSzCnt(Graph, count);
	printf("time for WCC:");
	printf("%g\n", float(clock() - begin_time2) / CLOCKS_PER_SEC);

}