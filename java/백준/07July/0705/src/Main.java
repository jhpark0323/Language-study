import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    static int m;
    static int n;
    static int k;
    static int[][] arr;
    static int[] di = new int[]{1, -1, 0, 0};
    static int[] dj = new int[]{0, 0, 1, -1};
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        arr = new int[m][n];

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            for (int x = x1; x < x2; x++) {
                for (int y = y1; y < y2; y++) {
                    arr[y][x] = 1;
                }
            }
        }
//        printArr();

        ArrayList<Integer> ansArea = new ArrayList<>();

        visited = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] == 0 && !visited[i][j]) {
                    int area = bfs(i, j);
                    ansArea.add(area);
                }
            }
        }

        Collections.sort(ansArea);

        System.out.println(ansArea.size());
        for (int each : ansArea) {
            System.out.print(each + " ");
        }

    }

    public static int bfs(int r, int c) {
        visited[r][c] = true;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{r, c});
        int area = 1;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int cur_r = cur[0];
            int cur_c = cur[1];

            for (int dij = 0; dij < 4; dij++) {
                int next_r = cur_r + di[dij];
                int next_c = cur_c + dj[dij];

                if (0 <= next_r && next_r < m && 0 <= next_c && next_c < n) {
                    if (arr[next_r][next_c] == 0 && !visited[next_r][next_c]) {
                        q.add(new int[]{next_r, next_c});
                        visited[next_r][next_c] = true;
                        area++;
                    }
                }
            }
        }
        return area;
    }

    static void printArr() {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}