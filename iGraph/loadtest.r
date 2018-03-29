library(igraph)
start_time <- Sys.time()
table <- read.table("twitter.txt")
gg<- graph.data.frame(table, directed=TRUE)

end_time <- Sys.time()
print("Time to read twitter")
end_time - start_time


print("number of vx:")
vcount(gg)
print("number of edge:")
ecount(gg)

