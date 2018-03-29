#include <ctime>
#include <cstdlib>
#include <typeinfo>
#include "Snap.h"


int main(int argc, char* argv[]) {
  const clock_t begin_time = clock();
  PUNGraph Graph = TSnap::LoadEdgeList<PUNGraph>("soc-pokec-relationships.txt", 0, 1);
  printf("time for reading soc-pokec-relationships.txt:");
  printf("%g\n", float(clock() - begin_time) / CLOCKS_PER_SEC);
  TIntPrV count;
  printf("number of nodes: %i\n", Graph->GetNodes());
  printf("number of edges: %d\n", Graph->GetEdges());
  
  TSnap::DelSelfEdges(Graph);

  const clock_t begin_time2 = clock();
  TSnap::GetWccSzCnt(Graph, count);
  printf("time for WCC:");
  printf("%g\n", float(clock() - begin_time2) / CLOCKS_PER_SEC);

  const clock_t begin_time3 = clock();
  TIntFltH PRankH;
  TSnap::GetPageRank(Graph, PRankH, 0.85, 0.0001, 10);
  printf("time for PR:");
  printf("%g\n", float(clock() - begin_time3) / CLOCKS_PER_SEC);

  PUNGraph UGraph = TSnap::ConvertGraph<PUNGraph>(Graph);
  const clock_t begin_time4 = clock();
  TIntFltH CcfH;
  TSnap::GetNodeClustCf(UGraph, CcfH);
  printf("time for Clustering Coefficient:");
  printf("%g\n", float(clock() - begin_time4) / CLOCKS_PER_SEC);

  const clock_t begin_time5 = clock();
  TKCore<PUNGraph> KCore(UGraph);
  printf("3-core:");
  printf("%g\n", float(clock() - begin_time5) / CLOCKS_PER_SEC);



  const clock_t begin_time6 = clock();
  printf("Does the edge exist? ");
  printf(Graph->IsEdge(Graph->GetRndNId(), Graph->GetRndNId()) ? "true\n" : "false\n");
  printf("Time for test existence of edge");
  printf("%g\n", float(clock() - begin_time6) / CLOCKS_PER_SEC);








}
