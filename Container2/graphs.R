
library(lattice)

read.table("output-throughput-latency/stats.csv", header=TRUE) -> csvDataFrameSource
csvDataFrame <- csvDataFrameSource

trellis.device("pdf", file="graph1.pdf", color=T, width=6.5, height=5.0)
xyplot(requests ~ rate, data=csvDataFrame,
   xlab = "No of requests",
   ylab = "Throughput (req/s)",
   type = "b",
   col = "red")

dev.off() -> null

trellis.device("pdf", file="graph2.pdf", color=T, width=6.5, height=5.0)
xyplot(latency ~ requests, data=csvDataFrame,
   ylab = "Latency (ms)",
   xlab = "Throughput (req/s)",
   type = "b",
   col = "red")

dev.off() -> null
