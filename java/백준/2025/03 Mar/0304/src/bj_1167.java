import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class bj_1167 {
    static int n;
    static List<Node>[] graph;
    static int start;
    static boolean[] visited;
    static int cost = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new List[n+1];
        for (int i = 0; i <= n; i++) {
            graph[i] =  new ArrayList<>();
        }
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            while (true) {
                int b = Integer.parseInt(st.nextToken());
                if (b == -1) {
                    break;
                }
                int c = Integer.parseInt(st.nextToken());
                graph[a].add(new Node(b, c));
            }
        }
//        System.out.println(Arrays.toString(graph));

        visited = new boolean[n+1];
        dfs(1, 0);
        cost = 0;
        visited = new boolean[n+1];
        dfs(start, 0);
        System.out.println(cost);

    }
    static class Node {
        int point, weight;
        Node(int point, int weight) {
            this.point = point;
            this.weight = weight;
        }

        @Override
        public String toString() {
            return "point=" + point + ", weight=" + weight;
        }
    }

    static void dfs(int node, int W) {
        visited[node] = true;

        if (cost < W) {
            start = node;
            cost = W;
        }

        for (Node neighbor : graph[node]) {
            if (!visited[neighbor.point]) {
                visited[neighbor.point] = true;
                dfs(neighbor.point, W + neighbor.weight);
            }
        }

    }
}
