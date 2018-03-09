library(igraph)
start_time <- Sys.time()
table <- read.table("wiki-talk-temporal.txt")
gg<- graph.data.frame(table, directed=TRUE)

end_time <- Sys.time()
end_time - start_time


print("number of vx:")
vcount(gg)
print("number of edge:")
ecount(gg)

newg <- simplify(g, remove.loops=TRUE)

# k-core
start_time <- Sys.time()
coreness(newg, mode = "all")
end_time <- Sys.time()
end_time - start_time

# page rank
start_time <- Sys.time()
page_rank(newg)
end_time <- Sys.time()
end_time - start_time

# SCC
start_time <- Sys.time()
components(newg, mode = "strong")
end_time <- Sys.time()
end_time - start_time

# WCC
start_time <- Sys.time()
components(newg, mode = "weak")
end_time <- Sys.time()
end_time - start_time

# Eigenvalue centrality 
start_time <- Sys.time()
eigen_centrality(newg, directed = TRUE)
end_time <- Sys.time()
end_time - start_time

# In-degree
start_time <- Sys.time()
degree(newg, mode = "in")
end_time <- Sys.time()
end_time - start_time

# Out-degree 
start_time <- Sys.time()
degree(newg, mode = "out")
end_time <- Sys.time()
end_time - start_time

