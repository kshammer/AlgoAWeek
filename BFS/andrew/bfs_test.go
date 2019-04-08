package main

import "testing"

func TestNormalGraph(t *testing.T) {
    adjList := map[string][]string{
        "1": []string{ "3", "4" },
        "2": []string{ "5" },
        "3": []string{ "1", "5" },
        "4": []string{ "1" },
        "5": []string{ "2", "3" },
    }
    nodes := []string{"1", "3", "4", "5", "2"}
    output, err := BreadthFirstSearchAdj(adjList, "1")
    if !equal(output, nodes) || err != nil {
	t.Errorf("Should be %v, actual %v", nodes, output)
    }
}

func TestSingleNode(t *testing.T) {
    adjList := map[string][]string{
        "1": []string{},
    }
    nodes := []string{"1"}
    output, err := BreadthFirstSearchAdj(adjList, "1")
    if !equal(output, nodes) || err != nil {
	t.Errorf("Should be %v, actual %v", nodes, output)
    }
}

func TestEmptyGraph(t *testing.T) {
    adjList := map[string][]string{}
    output, err := BreadthFirstSearchAdj(adjList, "1")
    if err == nil {
	t.Errorf("Should have failed, output is %v", output)
    }
}

func TestSourceNotInGraph(t *testing.T) {
    adjList := map[string][]string{
        "1": []string{ "3", "4" },
        "2": []string{ "5" },
        "3": []string{ "1", "5" },
        "4": []string{ "1" },
        "5": []string{ "2", "3" },
    }
    output, err := BreadthFirstSearchAdj(adjList, "6")
    if err == nil {
	t.Errorf("Should have failed, output is %v", output)
    }
}

func TestForest(t *testing.T) {
    adjList := map[string][]string{
        "1": []string{ "2", "3" },
        "2": []string{ "1", "3" },
        "3": []string{ "1", "2" },
        "4": []string{ "5" },
        "5": []string{ "4" },
        "6": []string{ },
    }
    nodes := []string{"1", "2", "3"}
    output, err := BreadthFirstSearchAdj(adjList, "1")
    if !equal(output, nodes) || err != nil {
	t.Errorf("Should be %v, actual %v", nodes, output)
    }
}

func TestDirectedGraph(t *testing.T) {
    adjList := map[string][]string{
        "1": []string{ "2", "3" },
        "2": []string{ "3" },
        "3": []string{ "1", "4", "5" },
        "4": []string{ "2", "3", "4" },
        "5": []string{ "1" },
    }
    nodes := []string{"5", "1", "2", "3", "4"}
    output, err := BreadthFirstSearchAdj(adjList, "5")
    if !equal(output, nodes) || err != nil {
	t.Errorf("Should be %v, actual %v", nodes, output)
    }
}

func TestTree(t *testing.T) {
    adjList := map[string][]string{
        "1": []string{ "2", "3" },
        "2": []string{ "4", "5", "6" },
        "3": []string{ "7" },
        "4": []string{ },
        "5": []string{ },
        "6": []string{ "8" },
        "7": []string{ },
        "8": []string{ },
    }
    nodes := []string{"1", "2", "3", "4", "5", "6", "7", "8"}
    output, err := BreadthFirstSearchAdj(adjList, "1")
    if !equal(output, nodes) || err != nil {
	t.Errorf("Should be %v, actual %v", nodes, output)
    }
}

func equal(a, b []string) bool {
    if (a == nil) != (b == nil) {
        return false;
    }

    if len(a) != len(b) {
        return false
    }

    for i := range a {
        if a[i] != b[i] {
            return false
        }
    }

    return true
}
