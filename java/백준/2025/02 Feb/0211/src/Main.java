import java.util.*;
import java.io.*;

public class Main {
    static int k;
    static List<List<Integer>> list;
    static int[] colors;
    static boolean check;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
        while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
           list = new ArrayList<>();
            for (int i = 0; i <= v; i++) {
                list.add(new ArrayList<>());
            }
            for (int i = 0; i < e; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                list.get(a).add(b);
                list.get(b).add(a);
            }
//            System.out.println(list);
            colors = new int[v+1];
            // 이분그래프 판별
            check = true;

            for (int i = 1; i <= v; i++) {
                if (!check) {
                    break;
                }
                if (colors[i] == 0) {
                    bfs(i, 1);
                }
            }
            System.out.println(check ? "YES" : "NO");
        }

    }

    static void bfs(int start, int color) {
        colors[start] = color;
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        while (!q.isEmpty()) {
            int cur = q.poll();

            for (int next : list.get(cur)) {
                if (colors[next] == 0) {
                    q.offer(next);
                    colors[next] = colors[cur] * -1;
                }
                else if (colors[next] == colors[cur]) {
                    check = false;
                    return;
                }
            }
        }
    }
}