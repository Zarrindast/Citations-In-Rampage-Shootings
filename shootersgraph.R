library("igraph")
edges=read_excel(file.choose()) #choose edgelist
g=graph.data.frame(edges,directed=TRUE)
E(g)$weight <- 1
plot.igraph(g,vertex.size=5,vertex.color="orange",vertex.frame.color=NA,vertex.label.cex=.7,vertex.label.degree=90,edge.arrow.size=.5,edge.arrow.width=.5,edge.color="grey",edge.curved=0,margin=0)
