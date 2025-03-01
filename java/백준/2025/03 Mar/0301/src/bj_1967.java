import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class bj_1967 {
    static int n;
    static List<Node>[] graph;
    static int ans = 0;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new List[n+1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        StringTokenizer st;
        for (int i = 0; i < n-1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[a].add(new Node(b,c));
            graph[b].add(new Node(a,c));
        }
//        System.out.println(Arrays.toString(graph[1].toArray()));
//        System.out.println(Arrays.toString(graph[2].toArray()));
        for (int i = 1; i <= n; i++) {
            visited = new boolean[n+1];
            dfs(i, 0);
        }
        System.out.println(ans);

    }

    static void dfs(int start, int W) {
        if (ans < W) {
            ans = W;
        }
        visited[start] = true;
        for (Node node : graph[start]) {
            int nxt = node.child;
            int nxtWeight = node.weight + W;
            if (visited[nxt]) {
                continue;
            }
            visited[nxt] = true;
            dfs(nxt, nxtWeight);
        }
    }

    static class Node {
        int child, weight;
        Node(int child, int weight) {
            this.child = child;
            this.weight = weight;
        }

        @Override
        public String toString() {
            return "child : " + child + " weight : " + weight;
        }
    }
}
