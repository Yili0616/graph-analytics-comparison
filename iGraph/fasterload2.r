ggg<- read.table("C:/Users/yilih/OneDrive/My stuff/Spring18/Research/data/cit-Patents.txt", header=FALSE)

g <- make_empty_graph(n = max(ggg))
for (num in c(1:16518948)) {

	g<-add.edges(g,c(ggg[num,"V1"], ggg[num,"V2"]))
}
delete_isolates(g)
vcount(g)
ecount(g)