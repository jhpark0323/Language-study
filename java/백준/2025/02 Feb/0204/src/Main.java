import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// bj_13424
public class Main {
    static int n, m, k;
    static int[] arr, realDist;
    static PriorityQueue<Node> pq;
    static ArrayList<Node>[] graph;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
        while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            graph = new ArrayList[n+1];
            for (int i = 0; i < n+1; i++) {
                graph[i] = new ArrayList<>();
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                graph[a].add(new Node(b, c));
                graph[b].add(new Node(a, c));
            }
            k = Integer.parseInt(br.readLine());
            arr = new int[k];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < k; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            realDist = new int[n+1];
            for (int i = 0; i < k; i++) {
                dijkstra(arr[i]);
            }
//            System.out.println(Arrays.toString(realDist));

            int ans = Integer.MAX_VALUE;
            int ansIdx = 0;
            for (int i = 1; i < n+1; i++) {
                if (ans > realDist[i]) {
                    ans = realDist[i];
                    ansIdx = i;
                }
            }
            System.out.println(ansIdx);

        }
    }
    static class Node implements Comparable<Node> {
        int end, length;
        Node(int end, int length) {
            this.end = end;
            this.length = length;
        }
        @Override
        public int compareTo(Node o) {
            return Integer.compare(length, o.length);
        }
    }
    static void dijkstra(int start) {
        int[] dist = new int[n+1];
        for (int i = 0; i < n+1; i++) {
            dist[i] = Integer.MAX_VALUE;
        }
        dist[start] = 0;
        pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            int curEnd = cur.end;
            int curLength = cur.length;

            if (dist[curEnd] < curLength) {
                continue;
            }

            for (Node node : graph[curEnd]) {
                int nextEnd = node.end;
                int nextLength = curLength + node.length;

                if (dist[nextEnd] < nextLength) {
                    continue;
                }

                dist[nextEnd] = nextLength;
                pq.offer(new Node(nextEnd, nextLength));

            }
        }
//        System.out.println(start);
//        System.out.println(Arrays.toString(dist));
        for (int i = 1; i < n+1; i++) {
            realDist[i] += dist[i];
        }
    }
}