import java.util.ArrayList;

public class GraphNode {
	int val;
	ArrayList<GraphNode> connectedNodes;
	
	public GraphNode(int val) {
		this.val = val;
		connectedNodes = new ArrayList<GraphNode>();
	}
}
