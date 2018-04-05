library(igraph)
start_time <- Sys.time()
table <- read.table("out.twitter")
gg<- graph.data.frame(table, directed=TRUE)

end_time <- Sys.time()
print("Time to read twitter")
end_time - start_time


print("number of vx:")
vcount(gg)
print("number of edge:")
ecount(gg)

library(igraph)
start_time <- Sys.time()
table <- read.table("out.friendster")
gg<- graph.data.frame(table, directed=TRUE)

end_time <- Sys.time()
print("Time to read friendster")
end_time - start_time


print("number of vx:")
vcount(gg)
print("number of edge:")
ecount(gg)
