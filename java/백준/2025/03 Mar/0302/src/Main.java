import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static List<Integer>[] graph;
    static boolean visited[];
    static boolean tf;
    static int answer = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        StringTokenizer st = new StringTokenizer(br.readLine());
        int root = 0;
        for (int i = 0; i < n; i++) {
            int a = Integer.parseInt(st.nextToken());
            if (a == -1) {
                root = i;
                continue;
            }
            graph[a].add(i);
        }
//        System.out.println(Arrays.deepToString(graph));

        visited = new boolean[n];
        tf = false;
        dfs(Integer.parseInt(br.readLine()));
        tf = true;
        if (!visited[root]) {
            dfs(root);
        }
        System.out.println(answer);

    }

    static void dfs(int start) {
        visited[start] = true;

        if (tf) {
            if (graph[start].size() == 0) {
                answer++;
            } else {
                boolean found = false;
                for (int neighbor : graph[start]) {
                    if (!visited[neighbor]) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    answer++;
                }
            }
        }

        for (int neighbor : graph[start]) {
            if (visited[neighbor]) {
                continue;
            }
            dfs(neighbor);
        }
    }
}