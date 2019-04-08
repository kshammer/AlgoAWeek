Andrew's Submission
=======

## Input

This algo accepts graphs with keys represented as adjacency lists. The keys are assumed to be unique. Input to the binary should be a text file with an adjacency list, e.g.:
`1`
`1 2 3`
`2 1`
`3 1 4`
`4 3`
`5`
where the first line is the key of the starting node and subsequent lines are entries in the adjacency list, with each line indicating a node and its neighbors separated by spaces. In the example above, the starting node is `1`. `1`'s neighbors are `2` and `3`. `5` has no neighbors.

## Output

An array of the graph traversal and an error message if an error was encountered during traversal. For the example above, the output would be `[1 2 3 4] <nil>`. If the source node was given as `6`, the output would be `[] Source node not found in graph`.

## How to run

Install Go if you don't have it. Place `bfs.go` somewhere in your `GOPATH` and run `go install $GOPATH/bfs.go`. Run the newly constructed binary from `GOBIN` with your input file like so: `$GOBIN/bfs input.txt`.
