import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static class Bridge {
        int to, weight;
        Bridge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    static int n;
    static int start;
    static int end;
    static List<List<Bridge>> graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            graph.get(from).add(new Bridge(to, weight));
            graph.get(to).add(new Bridge(from, weight));
        }

        st = new StringTokenizer(br.readLine());

        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());

//         그래프 출력 (디버깅용)
//         for (int i = 1; i <= n; i++) {
//             System.out.print(i + ": ");
//             for (Bridge bridge : graph.get(i)) {
//                 System.out.print("[" + bridge.to + ", " + bridge.weight + "] ");
//             }
//             System.out.println();
//         }

        int ans = BinarySearch();
        System.out.println(ans);
    }

    public static boolean bfs(int weightLimit) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        boolean[] visited = new boolean[n + 1];
        visited[start] = true;

        while (!queue.isEmpty()) {
            int current = queue.poll();
            if (current == end) {
                return true;
            }

            for (Bridge bridge : graph.get(current)) {
                if (!visited[bridge.to] && bridge.weight >= weightLimit) {
                    queue.add(bridge.to);
                    visited[bridge.to] = true;
                }
            }
        }
        return false;
    }
    public static int BinarySearch() {
        int left = 0;
        int right = 1000000000;
        int result = 0;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (bfs(mid)) {
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return result;
    }

}