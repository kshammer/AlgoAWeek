package main

import (
    "bufio"
    "errors"
    "fmt"
    "log"
    "os"
    "strings"
)

// nothing special happening in here, just reading the input
// and calling the BFS function
func main() {
    if len(os.Args) < 2 {
        os.Exit(1)
    }
    file, err := os.Open(os.Args[1])
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    scanner.Split(bufio.ScanLines)
    var source string
    if scanner.Scan() {
        firstLine := scanner.Text()
        wordSlice := strings.Fields(firstLine)
        source = wordSlice[0]
    }
    adjList := make(map[string][]string)
    for scanner.Scan() {
        line := scanner.Text()
        wordArr := strings.Fields(line)
        var node string
        if len(wordArr) > 0 {
            node = wordArr[0]
            adjList[node] = []string{}
        }
        for i := 1; i < len(wordArr); i++ {
            neighbor := wordArr[i]
            adjList[node] = append(adjList[node], neighbor)
        }
    }

    fmt.Println(BreadthFirstSearchAdj(adjList,source))
}

// BreadthFirstSearchAdj performs BFS on an adjacency list from a
// given starting node.
// Input:
//   adjList (map[string][]string): Adjacency list of the graph being traversed.
//   source (string): Key of the desired start node.
// Output: Slice of all nodes found in the order they were visited and an
//         error message if there is one
// TODO: Have this return each level of traversal instead
func BreadthFirstSearchAdj(adjList map[string][]string, source string) ([]string, error) {
    if val, exist := adjList[source]; !exist {
        return val, errors.New("Source node not found in graph");
    }
    var queue, nodes []string
    queue = append(queue, source)
    visited := make(map[string]bool)
    visited[source] = true
    for len(queue) != 0 {
        node := queue[0]
        // pop from queue
        queue = queue[1:]
        nodes = append(nodes, node)
        for _, neighbor := range adjList[node] {
            if !visited[neighbor] {
                queue = append(queue, neighbor)
                visited[neighbor] = true
            }
        }
    }
    return nodes, nil
}
