#include <ctime>
#include <cstdlib>
#include <typeinfo>
#include "Snap.h"

int main(int argc, char* argv[]) {
  const clock_t begin_time = clock();
  PUNGraph Graph = TSnap::LoadEdgeList<PUNGraph>("/nv/hmart1/yhui30/data/R/out.twitter", 0, 1); //change it to your file location
  printf("time for reading cit-Patents.txt:");
  printf("%g\n", float(clock() - begin_time) / CLOCKS_PER_SEC);
  TIntPrV count;
  printf("number of nodes: %i\n", Graph->GetNodes());
  printf("number of edges: %d\n", Graph->GetEdges());
	  


}