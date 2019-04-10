import java.util.ArrayList;
import java.util.HashMap;

public class Solution {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		GraphNode start = new GraphNode(0);
		GraphNode mid1 = new GraphNode(1);
		GraphNode mid2 = new GraphNode(2);
		GraphNode mid3 = new GraphNode(3);
		GraphNode finish = new GraphNode(4);
		
		start.connectedNodes.add(mid1);
		mid1.connectedNodes.add(mid2);
		mid2.connectedNodes.add(mid3);
		mid3.connectedNodes.add(finish);
		
		ArrayList<GraphNode> path = shortestPath(start, finish);
		
		for(GraphNode node : path) {
			System.out.print(node.val);
			
			if(node != finish)
				System.out.print(" -> ");
		}
		
		System.out.println();
	}

	//Shortest Path between nodes using BFS
	private static ArrayList<GraphNode> shortestPath(GraphNode start, GraphNode finish){
		if(start == null || finish == null)
			return null;
		
		HashMap<GraphNode,GraphNode> map = new HashMap<GraphNode, GraphNode>();
		ArrayList<GraphNode> queue = new ArrayList<GraphNode>();
		map.put(start, null); 
		queue.add(start);
		
		if(start == finish)
			return queue;
		
		while(!queue.isEmpty()) {
			GraphNode node = queue.remove(0);
			
			for(GraphNode nextNode : node.connectedNodes) {
				if(map.containsKey(nextNode))
					continue;
				
				map.put(nextNode, node);
				
				if(nextNode == finish)
					break;
				
				queue.add(nextNode);
			}
		}
		
		if(!map.containsKey(finish))
			return null;
		
		ArrayList<GraphNode> path = new ArrayList<GraphNode>();
		GraphNode node = finish;
		
		while(node != null) {
			path.add(0, node);
			node = map.get(node);
		}
		
		return path;
	}
}

