import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;
    static int p1;
    static int p2;
    static List<Integer>[] graph;
    static class Pair {
        int person;
        int degree;

        Pair(int person, int degree) {
            this.person = person;
            this.degree = degree;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        p1 = Integer.parseInt(st.nextToken());
        p2 = Integer.parseInt(st.nextToken());

        int m = Integer.parseInt(br.readLine());

        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        int ans = bfs();
        System.out.println(ans);

    }

    public static int bfs() {
        boolean[] visited = new boolean[n + 1];
        visited[p1] = true;
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(p1, 0));

        while (!q.isEmpty()) {
            Pair cur = q.poll();
            int person = cur.person;
            int degree = cur.degree;

            if (person == p2) {
                return degree;
            }

            for (int neighbor : graph[person]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.add(new Pair(neighbor, degree + 1));
                }
            }
        }
        return -1;
    }
}