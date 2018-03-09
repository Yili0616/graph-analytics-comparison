library(igraph)
start_time <- Sys.time()
table <- fread("out.twitter", header = False)
end_time <- Sys.time()
end_time - start_time

print ("number of vx:")
start_time <- Sys.time()
vcount(table)
end_time <- Sys.time()
end_time - start_time

print("number of edges")
start_time <- Sys.time()
ecount(table)
end_time <- Sys.time()
end_time - start_time
