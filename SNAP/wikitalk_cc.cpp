#include <ctime>
#include <cstdlib>
#include <typeinfo>
#include "Snap.h"

int main(int argc, char* argv[]) {
	const clock_t begin_time = clock();
	PNGraph Graph = TSnap::LoadEdgeList<PNGraph>("WikiTalk.txt", 0, 1);
	printf("time for reading wiki-talk.txt:");
	printf("%g\n", float(clock() - begin_time) / CLOCKS_PER_SEC);
	TIntPrV count;
	printf("number of nodes: %i\n", Graph->GetNodes());
	printf("number of edges: %d\n", Graph->GetEdges());
	
	TSnap::DelSelfEdges(Graph);

	PUNGraph UGraph = TSnap::ConvertGraph<PUNGraph>(Graph);
	const clock_t begin_time4 = clock();
	TIntFltH CcfH;
	TSnap::GetNodeClustCf(UGraph, CcfH);
	printf("time for Clustering Coefficient:");
	printf("%g\n", float(clock() - begin_time4) / CLOCKS_PER_SEC);
	

}